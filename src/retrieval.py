"""
Vector store initialization and document retrieval.
"""

import os
import glob
import json
import time
import logging

# Suppress broken chromadb posthog telemetry errors
logging.getLogger("chromadb.telemetry.product.posthog").setLevel(logging.CRITICAL)

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from chromadb.config import Settings

from src.config import (
    CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL_NAME,
    SCRAPED_DIR, DB_DIR, MMR_K, MMR_FETCH_K, MMR_LAMBDA_MULT,
)
from src.metrics import monitor

logger = logging.getLogger(__name__)

# --- Embedding model (loaded once) ---
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
logger.info(f"Embedding model loaded: {EMBEDDING_MODEL_NAME}")

# --- Document loading and chunking ---
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=len,
    separators=["\n\n", "\n", " ", ""],
)


def _load_and_chunk():
    """Load all .txt files from scraped dir and chunk with overlap."""
    all_chunks = []
    for filepath in glob.glob(os.path.join(SCRAPED_DIR, "*.txt")):
        loader = TextLoader(filepath, encoding="utf-8")
        documents = loader.load()
        chunks = splitter.split_documents(documents)
        all_chunks.extend(chunks)
        logger.info(f"Chunked {os.path.basename(filepath)}: {len(chunks)} chunks")

    logger.info(f"Total chunks from scraped dir: {len(all_chunks)}")
    return all_chunks


chunks = _load_and_chunk()


# --- ChromaDB client with telemetry disabled ---
chroma_settings = Settings(anonymized_telemetry=False)
chroma_client = chromadb.PersistentClient(path=DB_DIR, settings=chroma_settings)


def _should_rebuild() -> bool:
    meta_path = os.path.join(DB_DIR, "meta.json")
    if not os.path.exists(meta_path):
        return True
    with open(meta_path) as f:
        meta = json.load(f)
    return (
        meta.get("model_name") != EMBEDDING_MODEL_NAME
        or meta.get("chunk_size") != CHUNK_SIZE
        or meta.get("chunk_overlap") != CHUNK_OVERLAP
    )


def initialize_vectorstore() -> Chroma:
    """Load or create the ChromaDB vector store."""
    start = time.time()
    try:
        if os.path.exists(DB_DIR) and not _should_rebuild():
            vectordb = Chroma(
                client=chroma_client,
                embedding_function=embedding_model,
            )
            logger.info("VectorStore loaded from disk")
        else:
            vectordb = Chroma.from_documents(
                chunks,
                embedding=embedding_model,
                client=chroma_client,
            )
            # Save meta for future rebuild checks
            meta_path = os.path.join(DB_DIR, "meta.json")
            with open(meta_path, "w") as f:
                json.dump({
                    "model_name": EMBEDDING_MODEL_NAME,
                    "chunk_size": CHUNK_SIZE,
                    "chunk_overlap": CHUNK_OVERLAP,
                }, f)
            logger.info("VectorStore created and persisted")

        monitor.record("vectorstore_init", time.time() - start)
        return vectordb
    except Exception as e:
        logger.error(f"Error initializing vector store: {e}")
        raise


# Module-level singleton
vectordb = initialize_vectorstore()


def retrieve(query: str):
    """Run MMR retrieval against the vector store."""
    retriever = vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": MMR_K,
            "fetch_k": MMR_FETCH_K,
            "lambda_mult": MMR_LAMBDA_MULT,
        },
    )
    return retriever.invoke(query)
