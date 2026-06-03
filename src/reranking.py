"""
Cross-encoder reranking for retrieved documents.
"""

import logging
from typing import List, Tuple

from sentence_transformers import CrossEncoder

from src.config import RERANK_MODEL_NAME, RERANK_TOP_K, RERANK_THRESHOLD

logger = logging.getLogger(__name__)

# Module-level singleton
model = CrossEncoder(RERANK_MODEL_NAME)
logger.info(f"Cross-encoder reranker loaded: {RERANK_MODEL_NAME}")


def rerank(query: str, docs: list) -> Tuple[list, List[float]]:
    """
    Score and filter documents using the cross-encoder.

    Returns:
        (reranked_docs, scores) — filtered and sorted by relevance.
    """
    if not docs:
        return [], []

    pairs = [[query, doc.page_content] for doc in docs]
    scores = model.predict(pairs)

    scored_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    filtered = [(doc, float(s)) for doc, s in scored_docs if s >= RERANK_THRESHOLD]
    filtered = filtered[:RERANK_TOP_K]

    reranked_docs = [doc for doc, _ in filtered]
    top_scores = [s for _, s in filtered]

    logger.info(
        f"Reranking: {len(docs)} candidates -> {len(reranked_docs)} above threshold "
        f"(threshold={RERANK_THRESHOLD}, top_score={top_scores[0] if top_scores else 'N/A'})"
    )
    return reranked_docs, top_scores
