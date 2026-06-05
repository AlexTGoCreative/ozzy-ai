# ozzy-ai

RAG-powered cybersecurity assistant for OPSWAT MetaDefender. Provides contextual answers about scan results, hash lookups, and MetaDefender documentation using a production-grade Retrieval-Augmented Generation pipeline with hybrid search, cross-encoder reranking, and query rewriting.

## Architecture

```
User Query → Query Rewrite → Hybrid Search (Qdrant: dense + sparse RRF)
    → Cross-Encoder Reranking → Parent-Child Context Assembly
    → Cache Check (Redis) → Prompt Construction → Generation (OpenAI) → Response
```

| Stage | Technology | Purpose |
|-------|-----------|---------|
| Query Rewrite | GPT-4o-mini | Contextualizes follow-up questions |
| Embedding | BAAI/bge-m3 (1024-d dense + sparse) | Multi-vector document & query encoding |
| Vector Store | Qdrant (Cloud or self-hosted) | Hybrid search with HNSW + payload indexes |
| Retrieval | Dense + Sparse with RRF fusion | Best of semantic + keyword matching |
| Reranking | BAAI/bge-reranker-v2-m3 | Cross-encoder precision filtering (threshold 0.2) |
| Cache | Redis (L1) | 24h TTL, SHA-256 keyed |
| Generation | OpenAI Responses API | GPT-5.4-nano streaming |
| Metrics | Prometheus + custom | Per-stage timing & counters |

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full pipeline breakdown.

## Project Structure

```
ozzy-ai/
├── src/
│   ├── __init__.py        # Package marker
│   ├── config.py          # Constants, env loading, paths
│   ├── schemas.py         # Pydantic request models
│   ├── metrics.py         # Prometheus collectors + PerformanceMonitor
│   ├── cache.py           # Redis get/put with graceful degradation
│   ├── retrieval.py       # Qdrant hybrid search (dense + sparse + RRF)
│   ├── reranking.py       # bge-reranker-v2-m3 cross-encoder scoring
│   ├── query_rewrite.py   # Conversational follow-up rewriting via LLM
│   ├── context.py         # Scan context + system prompt assembly
│   ├── generation.py      # OpenAI client, token-budgeted history, streaming
│   ├── main.py            # FastAPI app, routes, CORS, orchestration
│   └── ingestion/         # Document ingestion pipeline
│       ├── __init__.py
│       ├── crawler.py     # Playwright recursive crawler (JS-rendered pages)
│       ├── chunker.py     # Structure-aware Markdown chunking (parent-child)
│       └── indexer.py     # bge-m3 embedding + Qdrant upsert
├── scripts/
│   ├── ingest.py          # CLI for crawling, chunking, and indexing
│   ├── scrape_docs.py     # Legacy scraper (single page)
│   └── evaluate.py        # RAG evaluation against golden set
├── data/
│   ├── scraped/           # Crawled documents (Markdown with metadata headers)
│   └── evaluation/        # Golden set for eval
├── docs/
│   ├── ARCHITECTURE.md    # Detailed pipeline documentation
│   └── EVALUATION.md      # Eval methodology & results
├── tests/                 # Test suite
├── .env.example           # Required environment variables
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.11+
- Redis (optional — degrades gracefully)
- Qdrant Cloud account (free tier available)
- OpenAI API key

### Setup

```bash
# Clone
git clone https://github.com/AlexTGoCreative/ozzy-ai.git
cd ozzy-ai

# Environment
cp .env.example .env
# Edit .env with your keys:
#   OPENAI_API_KEY=sk-...
#   QDRANT_URL=https://your-cluster.cloud.qdrant.io:6333
#   QDRANT_API_KEY=your-qdrant-api-key

# Install
python -m venv .venv
.venv/Scripts/activate   # Windows
pip install -r requirements.txt
python -m playwright install chromium  # For web crawling
```

### Ingest Documentation

```bash
# Crawl seed URLs recursively + chunk + index to Qdrant
python -u -m scripts.ingest --max-depth 2

# Or limit pages for testing
python -u -m scripts.ingest --max-pages 5 --max-depth 1

# Re-index from already-crawled files (no network needed)
python -u -m scripts.ingest --from-disk

# Full rebuild (drops Qdrant collection + re-indexes)
python -u -m scripts.ingest --rebuild
```

Scraped pages are saved to `data/scraped/` as Markdown files for inspection.

### Run the API

```bash
uvicorn src.main:app --port 7860
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/ask` | Synchronous Q&A (returns full answer) |
| POST | `/ask/stream` | Streaming Q&A (SSE deltas) |
| GET | `/metrics` | JSON performance metrics |
| GET | `/metrics/prometheus` | Prometheus exposition format |
| GET | `/health` | Health check |

### Request Format

```json
{
  "chat_history": [
    {"role": "user", "text": "What does verdict 1 mean?"}
  ],
  "scan_results": {},
  "file_info": {},
  "sandbox_data": {},
  "url_data": {}
}
```

### Response

```json
{"answer": "Based on the MetaDefender documentation [1]..."}
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key |
| `QDRANT_URL` | Yes | — | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Yes | — | Qdrant Cloud API key |
| `REDIS_URL` | No | `redis://localhost:6379/0` | Redis connection string |

## Ingestion Pipeline

The ingestion pipeline transforms web documentation into searchable vectors:

```
Seed URLs → Playwright (JS rendering) → Trafilatura (Markdown extraction)
    → Structure-aware chunking (parent 1024 tok / child 128 tok)
    → bge-m3 encoding (dense 1024-d + sparse) → Qdrant upsert
```

**Seed URLs** are configured in `src/config.py`:
```python
SEED_URLS = [
    "https://www.opswat.com/docs/mdcore/metascan-engines",
    "https://www.opswat.com/docs/mdcore/deep-cdr",
    "https://www.opswat.com/docs/mdcore/proactive-dlp",
    "https://www.opswat.com/docs/mdcore/sandbox",
    "https://www.opswat.com/docs/mdcore/metadefender-core",
]
```

The crawler follows internal links recursively (depth-limited) and only indexes pages matching `opswat.com/docs/mdcore`.

## Evaluation

Run the RAG evaluation suite against the golden set:

```bash
python scripts/evaluate.py
```

See [docs/EVALUATION.md](docs/EVALUATION.md) for methodology and metrics.

## Development

```bash
# Lint
ruff check src/

# Type check
mypy src/

# Test
pytest tests/
```
