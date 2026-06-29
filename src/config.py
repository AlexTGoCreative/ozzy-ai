"""
Centralized configuration for the ozzy-ai RAG pipeline.
All constants and environment-driven settings live here.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# --- OpenAI ---
OPENAI_MODEL = "gpt-5.4-nano"
QUERY_REWRITE_MODEL = "gpt-4o-mini"  # Cheap model for query rewriting

# --- Embedding ---
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"

# --- Chunking (token-based) ---
PARENT_CHUNK_SIZE = 1024      # tokens — large chunks for generation context
PARENT_CHUNK_OVERLAP = 64
CHILD_CHUNK_SIZE = 128        # tokens — small chunks for retrieval precision
CHILD_CHUNK_OVERLAP = 16

# --- Reranker ---
RERANK_MODEL_NAME = "BAAI/bge-reranker-v2-m3"
RERANK_TOP_K = 8
RERANK_THRESHOLD = 0.2        # Normalized score threshold

# --- Token budgets ---
HISTORY_TOKEN_BUDGET = 4000
CONTEXT_TOKEN_BUDGET = 6000
ANSWER_HEADROOM = 2000
TOKEN_ENCODING = "o200k_base"

# --- Redis cache ---
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CACHE_TTL_NORMAL = 86400       # 24 hours
CACHE_TTL_ABSTENTION = 1800    # 30 minutes

# --- Qdrant ---
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
QDRANT_COLLECTION = "opswat_docs_v1"

# --- Hybrid Retrieval ---
# Candidates from hybrid search before reranking. The cross-encoder reranker
# scores every candidate on CPU, so this count is the dominant pre-LLM latency
# cost (≈ linear in top_n). 24 keeps recall effectively unchanged — the final 8
# reranked docs almost always come from the hybrid top ~20 — while roughly
# halving rerank time vs the old 50. Override via env without a code change.
RETRIEVAL_TOP_N = int(os.getenv("RETRIEVAL_TOP_N", "24"))  # was 50
RETRIEVAL_FINAL_K = 8          # Final docs after reranking
# NOTE: Hybrid fusion uses Qdrant's built-in Reciprocal Rank Fusion (RRF) with
# the server's default rank constant — see retrieval.py's FusionQuery. There is
# no client-side RRF k override, so no constant is defined here.

# --- Ingestion ---
SEED_URLS = [
    "https://www.opswat.com/docs/mdcore/metascan-engines",
    "https://www.opswat.com/docs/mdcore/deep-cdr",
    "https://www.opswat.com/docs/mdcore/proactive-dlp",
    "https://www.opswat.com/docs/mdcore/sandbox",
    "https://www.opswat.com/docs/mdcore/metadefender-core",
]
CRAWL_ALLOWED_PATTERNS = [
    r"opswat\.com/docs/mdcore",
]

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCRAPED_DIR = os.path.join(DATA_DIR, "scraped")
RAW_DOCS_DIR = os.path.join(DATA_DIR, "raw_docs")

# --- Misc ---
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["ANONYMIZED_TELEMETRY"] = "False"
