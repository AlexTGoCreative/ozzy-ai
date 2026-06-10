"""
Hybrid retrieval: dense + sparse search on Qdrant with RRF fusion.
Uses bge-m3 for encoding (produces both dense and sparse vectors).
"""

import logging
import time
from typing import Optional

from qdrant_client import QdrantClient, models
from FlagEmbedding import BGEM3FlagModel

from src.config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    QDRANT_COLLECTION,
    EMBEDDING_MODEL_NAME,
    RETRIEVAL_TOP_N,
    RETRIEVAL_FINAL_K,
    RRF_K,
)
from src.metrics import monitor, RETRIEVAL_LATENCY

logger = logging.getLogger(__name__)

# --- Module-level singletons (lazy init) ---
_embed_model: Optional[BGEM3FlagModel] = None
_qdrant_client: Optional[QdrantClient] = None


def _get_embed_model() -> BGEM3FlagModel:
    global _embed_model
    if _embed_model is None:
        logger.info(f"Loading embedding model for retrieval: {EMBEDDING_MODEL_NAME}")
        _embed_model = BGEM3FlagModel(EMBEDDING_MODEL_NAME, use_fp16=False)
        logger.info("Embedding model loaded")
    return _embed_model


def _get_qdrant() -> QdrantClient:
    global _qdrant_client
    if _qdrant_client is None:
        _qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        logger.info(f"Qdrant client connected: {QDRANT_URL}")
    return _qdrant_client


def _build_filter(filters: Optional[dict]) -> Optional[models.Filter]:
    """Build Qdrant filter from metadata dict."""
    if not filters:
        return None
    must = [
        models.FieldCondition(key=k, match=models.MatchValue(value=v))
        for k, v in filters.items()
    ]
    return models.Filter(must=must)


def hybrid_search(
    query: str,
    *,
    top_n: int = RETRIEVAL_TOP_N,
    filters: Optional[dict] = None,
) -> list[dict]:
    """
    Perform hybrid search (dense + sparse) with server-side RRF fusion.

    Args:
        query: The search query
        top_n: Number of candidates to retrieve before reranking
        filters: Optional metadata filters (e.g. {"product": "metadefender_cloud"})

    Returns:
        List of candidate dicts with keys: id, text, parent_text, metadata, score
    """
    embed_model = _get_embed_model()
    client = _get_qdrant()

    start = time.time()

    # Encode query (both dense and sparse)
    encoded = embed_model.encode(
        [query],
        return_dense=True,
        return_sparse=True,
    )
    dense_vec = encoded["dense_vecs"][0].tolist()
    sparse_weights = encoded["lexical_weights"][0]
    sparse_vec = models.SparseVector(
        indices=list(map(int, sparse_weights.keys())),
        values=list(map(float, sparse_weights.values())),
    )

    qfilter = _build_filter(filters)

    # Hybrid search with Qdrant's native RRF fusion
    results = client.query_points(
        collection_name=QDRANT_COLLECTION,
        prefetch=[
            models.Prefetch(
                query=dense_vec,
                using="dense",
                limit=top_n,
                filter=qfilter,
            ),
            models.Prefetch(
                query=sparse_vec,
                using="sparse",
                limit=top_n,
                filter=qfilter,
            ),
        ],
        query=models.FusionQuery(fusion=models.Fusion.RRF),
        limit=top_n,
        with_payload=True,
    )

    candidates = []
    for point in results.points:
        candidates.append({
            "id": point.id,
            "text": point.payload.get("text", ""),
            "parent_text": point.payload.get("parent_text", point.payload.get("text", "")),
            "metadata": {
                k: v for k, v in point.payload.items()
                if k not in ("text", "parent_text")
            },
            "score": point.score,
        })

    duration = time.time() - start
    monitor.record("retrieval", duration)
    logger.info(
        f"Hybrid search: {len(candidates)} candidates in {duration:.3f}s "
        f"(query: '{query[:50]}...')"
    )
    return candidates


def retrieve(query: str, filters: Optional[dict] = None) -> list[dict]:
    """
    Main retrieval entry point. Returns candidates ready for reranking.
    Falls back gracefully if Qdrant is unavailable.
    """
    try:
        return hybrid_search(query, filters=filters)
    except Exception as e:
        logger.error(f"Retrieval failed: {e}")
        return []
