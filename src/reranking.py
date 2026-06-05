"""
Cross-encoder reranking with bge-reranker-v2-m3.
Scores retrieval candidates and applies threshold filtering.
"""

import logging
from typing import Optional

from sentence_transformers import CrossEncoder

from src.config import RERANK_MODEL_NAME, RERANK_TOP_K, RERANK_THRESHOLD
from src.metrics import monitor

logger = logging.getLogger(__name__)

# Module-level singleton (lazy-loaded)
_model: Optional[CrossEncoder] = None


def _get_model() -> CrossEncoder:
    global _model
    if _model is None:
        logger.info(f"Loading reranker: {RERANK_MODEL_NAME}")
        _model = CrossEncoder(RERANK_MODEL_NAME, max_length=512)
        logger.info("Reranker loaded")
    return _model


def rerank(query: str, candidates: list[dict]) -> list[dict]:
    """
    Score and filter candidates using the cross-encoder.

    Args:
        query: The user's search query
        candidates: List of dicts from hybrid_search with 'text', 'parent_text', 'metadata', 'score'

    Returns:
        Filtered and re-scored candidates (top-k above threshold), with 'rerank_score' added.
    """
    if not candidates:
        return []

    import time
    start = time.time()

    model = _get_model()

    # Score pairs: (query, candidate_text)
    pairs = [[query, c["text"]] for c in candidates]
    scores = model.predict(pairs, batch_size=32, show_progress_bar=False)

    # Normalize scores to [0, 1] using sigmoid if raw logits
    import numpy as np
    normalized_scores = 1 / (1 + np.exp(-np.array(scores)))

    # Attach scores and sort
    for candidate, score in zip(candidates, normalized_scores):
        candidate["rerank_score"] = float(score)

    candidates.sort(key=lambda c: c["rerank_score"], reverse=True)

    # Threshold filter
    survivors = [c for c in candidates if c["rerank_score"] >= RERANK_THRESHOLD]

    # Top-K cut
    survivors = survivors[:RERANK_TOP_K]

    duration = time.time() - start
    monitor.record("reranking", duration)
    logger.info(
        f"Reranking: {len(candidates)} candidates → {len(survivors)} above threshold "
        f"(threshold={RERANK_THRESHOLD}, "
        f"top_score={survivors[0]['rerank_score']:.3f} if survivors else 'N/A', "
        f"duration={duration:.3f}s)"
    )
    return survivors
