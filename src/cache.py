"""
Redis L1 cache for RAG responses.
Gracefully degrades when Redis is unavailable.
"""

import hashlib
import logging
from typing import Optional

import redis

from src.config import REDIS_URL, CACHE_TTL_NORMAL, CACHE_TTL_ABSTENTION
from src.metrics import CACHE_HITS, CACHE_MISSES

logger = logging.getLogger(__name__)

# --- Connection ---
try:
    client = redis.from_url(REDIS_URL, decode_responses=True, socket_timeout=2)
    client.ping()
    logger.info(f"Redis connected: {REDIS_URL}")
except (redis.ConnectionError, redis.TimeoutError) as e:
    client = None
    logger.warning(f"Redis unavailable, caching disabled: {e}")


def _key(question: str, context_hash: str) -> str:
    raw = f"{question.strip().lower()}|{context_hash}"
    return f"rag:v1:{hashlib.sha256(raw.encode()).hexdigest()}"


def get(question: str, context_hash: str) -> Optional[str]:
    """Lookup cached response. Returns None on miss or Redis unavailability."""
    if not client:
        return None
    try:
        key = _key(question, context_hash)
        cached = client.get(key)
        if cached:
            CACHE_HITS.inc()
            logger.info(f"Cache HIT: {key[:20]}...")
            return cached
        CACHE_MISSES.inc()
        return None
    except (redis.ConnectionError, redis.TimeoutError):
        return None


def put(question: str, context_hash: str, answer: str, is_abstention: bool = False):
    """Store response in cache with appropriate TTL."""
    if not client:
        return
    try:
        key = _key(question, context_hash)
        ttl = CACHE_TTL_ABSTENTION if is_abstention else CACHE_TTL_NORMAL
        client.setex(key, ttl, answer)
    except (redis.ConnectionError, redis.TimeoutError):
        pass
