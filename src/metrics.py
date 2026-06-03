"""
Performance monitoring and Prometheus metrics.
"""

import logging
from datetime import datetime
from prometheus_client import Counter, Histogram

logger = logging.getLogger(__name__)


class PerformanceMonitor:
    """In-memory metrics collector for the /metrics JSON endpoint."""

    def __init__(self, max_entries: int = 1000):
        self.metrics: list = []
        self._max_entries = max_entries

    def record(self, operation: str, duration: float):
        try:
            self.metrics.append({
                "timestamp": datetime.now().isoformat(),
                "operation": operation,
                "duration": float(duration) if duration is not None else 0.0,
            })
            if len(self.metrics) > self._max_entries:
                self.metrics = self.metrics[-self._max_entries:]
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid duration for {operation}: {duration} ({e})")

    def average(self, operation: str) -> float:
        relevant = [m["duration"] for m in self.metrics if m["operation"] == operation]
        return sum(relevant) / len(relevant) if relevant else 0.0

    def count(self, operation: str) -> int:
        return sum(1 for m in self.metrics if m["operation"] == operation)


# Singleton
monitor = PerformanceMonitor()

# --- Prometheus collectors ---
REQUEST_COUNT = Counter(
    "chatbot_requests_total", "Total requests", ["endpoint", "status"]
)
REQUEST_LATENCY = Histogram(
    "chatbot_request_duration_seconds", "Request latency", ["endpoint"]
)
RETRIEVAL_LATENCY = Histogram(
    "chatbot_retrieval_duration_seconds", "Retrieval latency"
)
RERANK_LATENCY = Histogram(
    "chatbot_rerank_duration_seconds", "Reranking latency"
)
GENERATION_LATENCY = Histogram(
    "chatbot_generation_duration_seconds", "LLM generation latency"
)
CACHE_HITS = Counter("chatbot_cache_hits_total", "Cache hits")
CACHE_MISSES = Counter("chatbot_cache_misses_total", "Cache misses")
