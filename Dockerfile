# ozzy-ai — FastAPI RAG service (OpenAI generation + BGE-M3 retrieval/rerank)
#
# Note: the BGE-M3 embedding and reranker models (~4 GB total) are downloaded
# from Hugging Face on first startup. Mount a volume at HF_HOME (see compose) so
# they persist across restarts instead of re-downloading every time.
FROM python:3.11-slim

# git is needed by some HF/model downloads; build-essential for any wheels that
# compile. curl is used by the container healthcheck.
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential git curl ca-certificates \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install CPU-only PyTorch first (avoids pulling multi-GB CUDA wheels), then the
# rest of the requirements.
COPY requirements.txt .
RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu torch \
  && pip install --no-cache-dir -r requirements.txt

# The ingestion entrypoint (scripts/ingest.py -> src.ingestion.crawler) imports
# playwright at module load. Install the package so `python -m scripts.ingest
# --from-disk` works in this image. Browsers are intentionally NOT installed
# (disk ingestion does no crawling).
RUN pip install --no-cache-dir playwright

COPY . .

ENV PYTHONUNBUFFERED=1 \
    HF_HOME=/hf_cache \
    TRANSFORMERS_VERBOSITY=error

EXPOSE 7860

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]
