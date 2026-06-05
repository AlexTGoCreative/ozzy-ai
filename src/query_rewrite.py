"""
Query rewriting: contextualizes conversational follow-ups into standalone queries.
Uses a cheap LLM call to rewrite ambiguous/follow-up questions.
"""

import logging
from typing import Optional

from openai import OpenAI

from src.config import QUERY_REWRITE_MODEL

logger = logging.getLogger(__name__)

_client: Optional[OpenAI] = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI()
    return _client


REWRITE_SYSTEM_PROMPT = """You are a query rewriting assistant for a cybersecurity documentation search system (OPSWAT MetaDefender products).

Your job: Given the user's latest question and recent chat history, rewrite the question into a standalone, self-contained search query that would retrieve the most relevant documentation.

Rules:
- If the question is already standalone and clear, return it unchanged.
- Resolve pronouns and references ("it", "that", "the second one") using chat history.
- Expand acronyms when helpful (MD → MetaDefender, CDR → Content Disarm and Reconstruction).
- Keep the rewritten query concise (1-2 sentences max).
- Do NOT answer the question. Only rewrite it.
- Output ONLY the rewritten query, nothing else."""


def rewrite_query(
    question: str,
    chat_history: Optional[list] = None,
) -> str:
    """
    Rewrite a conversational follow-up into a standalone search query.

    Args:
        question: The user's latest question
        chat_history: Recent chat messages [{"role": ..., "content": ...}, ...]

    Returns:
        Rewritten standalone query string
    """
    # Skip rewriting for simple/standalone queries
    if not chat_history or len(chat_history) < 2:
        return question

    # Check if the question likely needs rewriting
    # (contains pronouns, is very short, or references previous context)
    needs_rewrite = _likely_needs_rewrite(question)
    if not needs_rewrite:
        return question

    try:
        client = _get_client()

        # Format recent history (last 4 turns max)
        recent = chat_history[-4:] if len(chat_history) > 4 else chat_history
        history_text = "\n".join(
            f"{msg['role'].upper()}: {msg['content']}" for msg in recent
        )

        user_prompt = f"""Chat history:
{history_text}

Latest question to rewrite:
{question}

Rewritten standalone query:"""

        response = client.responses.create(
            model=QUERY_REWRITE_MODEL,
            input=[
                {"role": "developer", "content": REWRITE_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
        )

        rewritten = response.output_text.strip()

        if rewritten and len(rewritten) > 5:
            logger.info(f"Query rewritten: '{question}' → '{rewritten}'")
            return rewritten
        return question

    except Exception as e:
        logger.warning(f"Query rewriting failed, using original: {e}")
        return question


def _likely_needs_rewrite(question: str) -> bool:
    """Heuristic check if a question likely needs rewriting."""
    question_lower = question.lower().strip()

    # Short questions often need context
    if len(question_lower.split()) <= 3:
        return True

    # Contains pronouns that reference prior context
    context_words = [
        "it", "this", "that", "these", "those", "them",
        "the same", "previous", "above", "mentioned",
        "what about", "how about", "and the", "also",
        "the first", "the second", "the last",
    ]
    if any(word in question_lower for word in context_words):
        return True

    return False
