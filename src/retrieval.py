"""
Vector store initialization and document retrieval.
"""

import os
import json
import time
import logging

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.config import (
    CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL_NAME,
    DOC_PATH, DB_DIR, MMR_K, MMR_FETCH_K, MMR_LAMBDA_MULT,
)
from src.metrics import monitor

logger = logging.getLogger(__name__)

# --- Embedding model (loaded once) ---
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
logger.info(f"Embedding model loaded: {EMBEDDING_MODEL_NAME}")

# --- Document loading and chunking ---
loader = TextLoader(DOC_PATH, encoding="utf-8")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=len,
    separators=["\n\n", "\n", " ", ""],
)
chunks = splitter.split_documents(documents)
logger.info(f"Document chunked: {len(chunks)} chunks from {DOC_PATH}")


def _should_rebuild() -> bool:
    meta_path = os.path.join(DB_DIR, "meta.json")
    if not os.path.exists(meta_path):
        return True
    with open(meta_path) as f:
        meta = json.load(f)
    return meta.get("model_name") != EMBEDDING_MODEL_NAME


def initialize_vectorstore() -> Chroma:
    """Load or create the ChromaDB vector store."""
    start = time.time()
    try:
        if os.path.exists(DB_DIR) and not _should_rebuild():
            vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embedding_model)
            logger.info("VectorStore loaded from disk")
        else:
            vectordb = Chroma.from_documents(
                chunks, embedding=embedding_model, persist_directory=DB_DIR
            )
            # Save meta for future rebuild checks
            meta_path = os.path.join(DB_DIR, "meta.json")
            with open(meta_path, "w") as f:
                json.dump({"model_name": EMBEDDING_MODEL_NAME}, f)
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
