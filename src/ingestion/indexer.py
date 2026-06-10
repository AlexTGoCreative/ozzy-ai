"""
Qdrant indexer: embeds documents and upserts to Qdrant with dense + sparse vectors.
Supports incremental indexing via content-hash deduplication.
"""

import logging
from typing import Optional

from qdrant_client import QdrantClient, models
from FlagEmbedding import BGEM3FlagModel

from src.config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    QDRANT_COLLECTION,
    EMBEDDING_MODEL_NAME,
)

logger = logging.getLogger(__name__)

# Module-level singletons (lazy-loaded)
_embed_model: Optional[BGEM3FlagModel] = None
_qdrant_client: Optional[QdrantClient] = None


def get_embed_model() -> BGEM3FlagModel:
    global _embed_model
    if _embed_model is None:
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL_NAME}")
        _embed_model = BGEM3FlagModel(EMBEDDING_MODEL_NAME, use_fp16=False)
        logger.info("Embedding model loaded")
    return _embed_model


def get_qdrant_client() -> QdrantClient:
    global _qdrant_client
    if _qdrant_client is None:
        _qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        logger.info(f"Qdrant client connected: {QDRANT_URL}")
    return _qdrant_client


def ensure_collection():
    """Create collection if it doesn't exist, with dense + sparse named vectors."""
    client = get_qdrant_client()

    collections = [c.name for c in client.get_collections().collections]
    if QDRANT_COLLECTION in collections:
        logger.info(f"Collection '{QDRANT_COLLECTION}' already exists")
        return

    client.create_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config={
            "dense": models.VectorParams(
                size=1024,  # bge-m3 dense output dimension
                distance=models.Distance.COSINE,
                on_disk=True,
            ),
        },
        sparse_vectors_config={
            "sparse": models.SparseVectorParams(
                index=models.SparseIndexParams(on_disk=False),
            ),
        },
    )

    # Create payload indexes for metadata filtering
    for field in ["product", "doc_type", "section_path", "chunk_type", "parent_id"]:
        client.create_payload_index(
            collection_name=QDRANT_COLLECTION,
            field_name=field,
            field_schema=models.PayloadSchemaType.KEYWORD,
        )

    client.create_payload_index(
        collection_name=QDRANT_COLLECTION,
        field_name="token_count",
        field_schema=models.PayloadSchemaType.INTEGER,
    )

    logger.info(f"Collection '{QDRANT_COLLECTION}' created with dense + sparse vectors")


def _get_existing_hashes() -> set[str]:
    """Get content hashes already in the collection for dedup."""
    client = get_qdrant_client()
    try:
        # Scroll through all points to get content_hash
        hashes = set()
        offset = None
        while True:
            results, offset = client.scroll(
                collection_name=QDRANT_COLLECTION,
                limit=1000,
                offset=offset,
                with_payload=["content_hash"],
            )
            for point in results:
                h = point.payload.get("content_hash")
                if h:
                    hashes.add(h)
            if offset is None:
                break
        return hashes
    except Exception:
        return set()


def index_documents(
    children: list[dict],
    parents: list[dict],
    batch_size: int = 32,
    skip_existing: bool = True,
):
    """
    Embed child chunks and upsert to Qdrant.
    Parents are stored as payload (fetched at generation time).

    Args:
        children: List of child chunk dicts with 'text' and 'metadata'
        parents: List of parent chunk dicts (stored for lookup by parent_id)
        batch_size: Embedding batch size
        skip_existing: Skip chunks with content_hash already in collection
    """
    client = get_qdrant_client()
    embed_model = get_embed_model()
    ensure_collection()

    # Build parent lookup
    parent_lookup = {}
    for p in parents:
        pid = p["metadata"].get("parent_id")
        if pid:
            parent_lookup[pid] = p["text"]

    # Dedup
    if skip_existing:
        existing_hashes = _get_existing_hashes()
        original_count = len(children)
        children = [
            c for c in children
            if c["metadata"].get("content_hash") not in existing_hashes
        ]
        skipped = original_count - len(children)
        if skipped > 0:
            logger.info(f"Skipped {skipped} already-indexed chunks")

    if not children:
        logger.info("No new chunks to index")
        return

    # Batch embed and upsert
    total_indexed = 0
    for i in range(0, len(children), batch_size):
        batch = children[i : i + batch_size]
        texts = [c["text"] for c in batch]

        # Encode with bge-m3 (dense + sparse)
        encoded = embed_model.encode(
            texts,
            return_dense=True,
            return_sparse=True,
            batch_size=batch_size,
        )

        points = []
        for j, chunk in enumerate(batch):
            dense_vec = encoded["dense_vecs"][j].tolist()
            sparse_weights = encoded["lexical_weights"][j]
            sparse_vec = models.SparseVector(
                indices=list(map(int, sparse_weights.keys())),
                values=list(map(float, sparse_weights.values())),
            )

            # Store parent text in payload for retrieval at generation time
            parent_id = chunk["metadata"].get("parent_id", "")
            parent_text = parent_lookup.get(parent_id, chunk["text"])

            payload = {
                **chunk["metadata"],
                "text": chunk["text"],
                "parent_text": parent_text,
            }

            point = models.PointStruct(
                id=total_indexed + j,
                vector={
                    "dense": dense_vec,
                    "sparse": sparse_vec,
                },
                payload=payload,
            )
            points.append(point)

        client.upsert(collection_name=QDRANT_COLLECTION, points=points)
        total_indexed += len(batch)
        logger.info(f"Indexed batch {i // batch_size + 1}: {len(batch)} chunks")

    logger.info(f"Indexing complete: {total_indexed} chunks upserted to '{QDRANT_COLLECTION}'")


def rebuild_index(documents: list[dict], batch_size: int = 32):
    """
    Full rebuild: drop collection, re-chunk, re-embed, re-index.
    Use for embedding model changes or major schema updates.
    """
    from src.ingestion.chunker import chunk_documents

    client = get_qdrant_client()

    # Drop existing collection
    collections = [c.name for c in client.get_collections().collections]
    if QDRANT_COLLECTION in collections:
        client.delete_collection(QDRANT_COLLECTION)
        logger.info(f"Dropped collection '{QDRANT_COLLECTION}'")

    # Re-chunk and index
    parents, children = chunk_documents(documents)
    index_documents(children, parents, batch_size=batch_size, skip_existing=False)
