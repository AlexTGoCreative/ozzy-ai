"""
ozzy-ai — FastAPI application entry point.

Run with:
    uvicorn src.main:app --port 7860
"""

import hashlib
import json
import logging
import time

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langdetect import detect
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

from src.schemas import ChatPayload
from src.config import OPENAI_MODEL, RERANK_MODEL_NAME, RERANK_THRESHOLD, RERANK_TOP_K
from src import cache
from src.context import build_scan_context, build_system_prompt
from src.generation import truncate_history, generate, generate_stream
from src.metrics import (
    monitor, REQUEST_COUNT, REQUEST_LATENCY,
    RETRIEVAL_LATENCY, RERANK_LATENCY, GENERATION_LATENCY,
)
from src.retrieval import retrieve
from src.reranking import rerank

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# --- App ---
app = FastAPI(
    title="ozzy-ai",
    description="OPSWAT cybersecurity RAG assistant",
    version="2.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Helpers ────────────────────────────────────────────────────────────────

def _context_hash(doc_context: str, scan_context: str) -> str:
    combined = f"{doc_context}|{scan_context}"
    return hashlib.sha256(combined.encode()).hexdigest()[:16]


# ─── Endpoints ──────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask")
async def ask(payload: ChatPayload):
    start_time = time.time()

    try:
        last_question = next(
            (msg.text for msg in reversed(payload.chat_history) if msg.role == "user"),
            None,
        )
        if not last_question:
            raise HTTPException(status_code=400, detail="No question found in chat history")

        # --- Retrieval ---
        retrieval_start = time.time()
        relevant_docs = retrieve(last_question)
        retrieval_duration = time.time() - retrieval_start
        monitor.record("retrieval", retrieval_duration)
        RETRIEVAL_LATENCY.observe(retrieval_duration)

        # --- Reranking ---
        rerank_start = time.time()
        reranked_docs, _ = rerank(last_question, relevant_docs)
        rerank_duration = time.time() - rerank_start
        monitor.record("reranking", rerank_duration)
        RERANK_LATENCY.observe(rerank_duration)

        has_relevant_context = len(reranked_docs) > 0

        # --- Context assembly ---
        scan_context = build_scan_context(payload)
        doc_context = "\n\n".join(doc.page_content for doc in reranked_docs)

        # --- Cache lookup ---
        ctx_hash = _context_hash(doc_context, scan_context)
        cached_answer = cache.get(last_question, ctx_hash)
        if cached_answer:
            duration = time.time() - start_time
            monitor.record("total_request", duration)
            REQUEST_COUNT.labels(endpoint="/ask", status="cache_hit").inc()
            REQUEST_LATENCY.labels(endpoint="/ask").observe(duration)
            logger.info(f"Cache hit, served in {duration:.3f}s")
            return {"answer": cached_answer}

        # --- Prompt construction ---
        system_prompt = build_system_prompt(doc_context, scan_context)
        input_messages = [{"role": "developer", "content": system_prompt}]

        if payload.chat_history:
            input_messages.extend(truncate_history(payload.chat_history))
        else:
            input_messages.append({"role": "user", "content": last_question})

        # --- Generation ---
        generation_start = time.time()
        answer_text = generate(input_messages)
        gen_duration = time.time() - generation_start
        monitor.record("generation", gen_duration)
        GENERATION_LATENCY.observe(gen_duration)

        # --- Cache store ---
        is_abstention = not has_relevant_context and not scan_context
        cache.put(last_question, ctx_hash, answer_text, is_abstention)

        # --- Metrics ---
        duration = time.time() - start_time
        monitor.record("total_request", duration)
        REQUEST_COUNT.labels(endpoint="/ask", status="success").inc()
        REQUEST_LATENCY.labels(endpoint="/ask").observe(duration)

        logger.info(
            f"Request completed in {duration:.2f}s "
            f"(retrieval={retrieval_duration:.2f}s, "
            f"rerank={rerank_duration:.2f}s, "
            f"generation={gen_duration:.2f}s)"
        )
        return {"answer": answer_text}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        REQUEST_COUNT.labels(endpoint="/ask", status="error").inc()
        duration = time.time() - start_time
        monitor.record("failed_request", duration)
        REQUEST_LATENCY.labels(endpoint="/ask").observe(duration)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask/stream")
async def ask_stream(payload: ChatPayload):
    """Streaming version of /ask — returns Server-Sent Events."""
    start_time = time.time()

    try:
        last_question = next(
            (msg.text for msg in reversed(payload.chat_history) if msg.role == "user"),
            None,
        )
        if not last_question:
            raise HTTPException(status_code=400, detail="No question found in chat history")

        # Retrieval + Reranking
        relevant_docs = retrieve(last_question)
        reranked_docs, _ = rerank(last_question, relevant_docs)
        has_relevant_context = len(reranked_docs) > 0

        # Context
        scan_context = build_scan_context(payload)
        doc_context = "\n\n".join(doc.page_content for doc in reranked_docs)

        # Cache check
        ctx_hash = _context_hash(doc_context, scan_context)
        cached_answer = cache.get(last_question, ctx_hash)
        if cached_answer:
            async def _cached():
                yield f"data: {json.dumps({'delta': cached_answer})}\n\n"
                yield "data: [DONE]\n\n"
            REQUEST_COUNT.labels(endpoint="/ask/stream", status="cache_hit").inc()
            return StreamingResponse(_cached(), media_type="text/event-stream")

        # Prompt
        system_prompt = build_system_prompt(doc_context, scan_context)
        input_messages = [{"role": "developer", "content": system_prompt}]

        if payload.chat_history:
            input_messages.extend(truncate_history(payload.chat_history))
        else:
            input_messages.append({"role": "user", "content": last_question})

        # Stream
        async def _stream():
            full_response = []
            try:
                for delta in generate_stream(input_messages):
                    full_response.append(delta)
                    yield f"data: {json.dumps({'delta': delta})}\n\n"

                answer_text = "".join(full_response)
                is_abstention = not has_relevant_context and not scan_context
                cache.put(last_question, ctx_hash, answer_text, is_abstention)

                yield "data: [DONE]\n\n"
                REQUEST_COUNT.labels(endpoint="/ask/stream", status="success").inc()
                REQUEST_LATENCY.labels(endpoint="/ask/stream").observe(time.time() - start_time)
            except Exception as e:
                logger.error(f"Streaming error: {e}")
                yield f"data: {json.dumps({'error': str(e)})}\n\n"
                yield "data: [DONE]\n\n"
                REQUEST_COUNT.labels(endpoint="/ask/stream", status="error").inc()

        return StreamingResponse(_stream(), media_type="text/event-stream")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Stream setup error: {e}")
        REQUEST_COUNT.labels(endpoint="/ask/stream", status="error").inc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/metrics")
async def get_metrics():
    return {
        "average_request_time": monitor.average("total_request"),
        "average_retrieval_time": monitor.average("retrieval"),
        "average_reranking_time": monitor.average("reranking"),
        "average_generation_time": monitor.average("generation"),
        "average_vectorstore_init_time": monitor.average("vectorstore_init"),
        "total_requests": monitor.count("total_request"),
        "failed_requests": monitor.count("failed_request"),
        "llm_model": OPENAI_MODEL,
        "reranker_model": RERANK_MODEL_NAME,
        "rerank_threshold": RERANK_THRESHOLD,
        "rerank_top_k": RERANK_TOP_K,
    }


@app.get("/metrics/prometheus")
async def prometheus_metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
