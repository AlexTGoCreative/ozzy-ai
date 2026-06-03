# Architecture

> Version 2.2 — Modular Package Structure

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     POST /ask  |  POST /ask/stream                           │
│                     (ChatPayload: history + scan context)                    │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 1. EXTRACT QUERY — Last user message from chat_history                       │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 2. RETRIEVAL — ChromaDB MMR search (k=10, fetch_k=30, λ=0.5)                │
│    Embedding: all-mpnet-base-v2 (768-d)                                      │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 3. RERANKING — cross-encoder/ms-marco-MiniLM-L-6-v2                          │
│    Filter: score ≥ 0.1, keep top 5                                           │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 4. CACHE LOOKUP — Redis L1, key=sha256(question+context_hash)                │
│    Hit → return immediately | Miss → continue                                │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 5. CONTEXT ASSEMBLY — Scan context + doc context + abstention path           │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 6. PROMPT CONSTRUCTION — developer msg + token-budgeted history (4000 tok)   │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 7. GENERATION — OpenAI GPT-5.4-nano (Responses API)                          │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 8. RESPONSE + CACHE STORE — TTL 24h (normal) / 30min (abstention)            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Module Responsibilities

| Module | Exports | Purpose |
|--------|---------|---------|
| `src/config.py` | Constants | All env vars, paths, model names, hyperparameters |
| `src/schemas.py` | `ChatMessage`, `ChatPayload` | Pydantic request validation |
| `src/metrics.py` | `monitor`, Prometheus collectors | Per-stage timing + exposition |
| `src/cache.py` | `get()`, `put()` | Redis L1 with graceful degradation |
| `src/retrieval.py` | `retrieve(query)`, `vectordb` | Embedding + ChromaDB + MMR |
| `src/reranking.py` | `rerank(query, docs)` | Cross-encoder scoring + filtering |
| `src/context.py` | `build_scan_context()`, `build_system_prompt()` | Context assembly |
| `src/generation.py` | `generate()`, `generate_stream()`, `truncate_history()` | OpenAI + tokenization |
| `src/main.py` | `app` | FastAPI routes, CORS, orchestration |

## Stage Details

### Retrieval

- **Vector Store:** ChromaDB with SQLite backend, persisted to `chroma_db/`
- **Embedding:** `sentence-transformers/all-mpnet-base-v2` (768 dimensions)
- **Strategy:** Maximal Marginal Relevance (balances relevance + diversity)
- **Document Source:** `data/scraped/hash_lookup.txt` + `data/scraped/explanations.txt`
- **Chunking:** `RecursiveCharacterTextSplitter` (1000 chars, 200 overlap)

### Reranking

The cross-encoder processes (query, document) pairs jointly — more accurate than the bi-encoder used for retrieval but too slow for the full corpus.

| Parameter | Value |
|-----------|-------|
| Model | `cross-encoder/ms-marco-MiniLM-L-6-v2` (22M params) |
| Threshold | 0.1 (below → discard) |
| Top-K | 5 documents max |

### Caching

- **Key:** `sha256(question + context_hash)` where `context_hash = sha256(doc_context | scan_context)[:16]`
- **TTL:** 24h for normal answers, 30min for abstentions (more likely to improve with new data)
- **Degradation:** If Redis unavailable, caching is skipped silently

### History Management

Chat history is trimmed to a **4000 token budget** (tiktoken `o200k_base`):
1. Iterate messages newest → oldest
2. Count tokens per message + 4 overhead
3. Stop when budget exhausted
4. Return in chronological order

### Prompt Roles

| Role | Purpose |
|------|---------|
| `developer` | System instructions + context (highest priority in OpenAI hierarchy) |
| `user` | End-user messages from chat history |
| `assistant` | Model's previous responses from chat history |

## Configuration

All constants live in `src/config.py`:

| Constant | Value | Description |
|----------|-------|-------------|
| `OPENAI_MODEL` | `gpt-5.4-nano` | LLM model |
| `RERANK_MODEL_NAME` | `cross-encoder/ms-marco-MiniLM-L-6-v2` | Reranker |
| `RERANK_TOP_K` | 5 | Max docs after reranking |
| `RERANK_THRESHOLD` | 0.1 | Min relevance score |
| `HISTORY_TOKEN_BUDGET` | 4000 | Chat history token cap |
| `CHUNK_SIZE` | 1000 | Characters per chunk |
| `CHUNK_OVERLAP` | 200 | Overlap between chunks |
| `CACHE_TTL_NORMAL` | 86400 | Normal cache TTL (24h) |
| `CACHE_TTL_ABSTENTION` | 1800 | Abstention cache TTL (30min) |

## Security

| Measure | Implementation |
|---------|---------------|
| Secret storage | `.env` (gitignored) via `python-dotenv` |
| Context isolation | `<<<CONTEXT_START>>>` / `<<<CONTEXT_END>>>` markers |
| Role separation | `developer` role for system prompt |
| Input validation | Pydantic models |
| CORS | Configurable origins (currently `*` for dev) |

## Startup Sequence

1. Load `.env` → environment variables
2. Initialize OpenAI client
3. Load tiktoken encoding (`o200k_base`)
4. Load cross-encoder reranker model
5. Connect to Redis (graceful degradation)
6. Initialize Prometheus collectors
7. Load embedding model (`all-mpnet-base-v2`)
8. Build/load ChromaDB from `data/scraped/`
9. Start FastAPI on port 7860
