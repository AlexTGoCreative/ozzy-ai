"""
Centralized configuration for the ozzy-ai RAG pipeline.
All constants and environment-driven settings live here.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# --- OpenAI ---
OPENAI_MODEL = "gpt-5.4-nano"

# --- Embedding ---
EMBEDDING_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"

# --- Chunking ---
CHUNK_SIZE = 4000
CHUNK_OVERLAP = 1000

# --- Reranker (disabled until better docs available) ---
# RERANK_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"
# RERANK_TOP_K = 5
# RERANK_THRESHOLD = -10.5  # Raw logit threshold (sentence-transformers v4)

# --- Token budgets ---
HISTORY_TOKEN_BUDGET = 4000
CONTEXT_TOKEN_BUDGET = 6000
ANSWER_HEADROOM = 2000
TOKEN_ENCODING = "o200k_base"

# --- Redis cache ---
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CACHE_TTL_NORMAL = 86400       # 24 hours
CACHE_TTL_ABSTENTION = 1800    # 30 minutes

# --- Retrieval ---
MMR_K = 5
MMR_FETCH_K = 20
MMR_LAMBDA_MULT = 0.5

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCRAPED_DIR = os.path.join(DATA_DIR, "scraped")
DB_DIR = os.path.join(BASE_DIR, "chroma_db")

# --- Misc ---
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["ANONYMIZED_TELEMETRY"] = "False"
