# ozzy-ai

RAG-powered cybersecurity assistant for OPSWAT MetaDefender. Provides contextual answers about scan results, hash lookups, and MetaDefender API documentation using a Retrieval-Augmented Generation pipeline.

## Architecture

```
User Query → Retrieval (ChromaDB + MMR) → Reranking (Cross-Encoder) → Cache Check (Redis)
    → Context Assembly → Generation (OpenAI GPT-5.4-nano) → Response
```

| Stage | Technology | Purpose |
|-------|-----------|---------|
| Embedding | all-mpnet-base-v2 (768-d) | Document & query encoding |
| Vector Store | ChromaDB (SQLite) | Persistent similarity search |
| Retrieval | MMR (k=10, fetch_k=30) | Diverse relevant chunks |
| Reranking | ms-marco-MiniLM-L-6-v2 | Precision filtering (threshold 0.1) |
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
│   ├── retrieval.py       # Embedding, chunking, ChromaDB, MMR search
│   ├── reranking.py       # Cross-encoder scoring & filtering
│   ├── context.py         # Scan context + system prompt assembly
│   ├── generation.py      # OpenAI client, token-budgeted history, streaming
│   └── main.py            # FastAPI app, routes, CORS, startup
├── scripts/
│   ├── scrape_docs.py     # Documentation scraper (hash lookup page)
│   └── evaluate.py        # RAG evaluation against golden set
├── data/
│   ├── scraped/           # Source documents (txt)
│   └── evaluation/        # Golden set for eval
├── docs/
│   ├── ARCHITECTURE.md    # Detailed pipeline documentation
│   └── EVALUATION.md      # Eval methodology & results
├── tests/                 # Test suite
├── chroma_db/             # Persisted vector store (gitignored)
├── .env.example           # Required environment variables
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.9+
- Redis (optional — degrades gracefully)
- OpenAI API key

### Setup

```bash
# Clone
git clone https://github.com/AlexTGoCreative/ozzy-ai.git
cd ozzy-ai

# Environment
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# Install
pip install -r requirements.txt

# Run
uvicorn src.main:app --port 7860
```

### Docker

```bash
docker build -t ozzy-ai .
docker run -p 7860:7860 --env-file .env ozzy-ai
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
{"answer": "Based on the MetaDefender documentation..."}
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key |
| `REDIS_URL` | No | `redis://localhost:6379/0` | Redis connection string |

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
