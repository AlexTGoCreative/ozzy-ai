"""
OpenAI generation and token-aware history management.
"""

import logging
from typing import List, Dict

import tiktoken
from openai import OpenAI

from src.config import OPENAI_MODEL, TOKEN_ENCODING, HISTORY_TOKEN_BUDGET

logger = logging.getLogger(__name__)

# Module-level singletons
client = OpenAI()
logger.info(f"OpenAI client initialized (model: {OPENAI_MODEL})")

tokenizer = tiktoken.get_encoding(TOKEN_ENCODING)
logger.info(f"Tokenizer loaded: {TOKEN_ENCODING}")


def truncate_history(chat_history, budget: int = HISTORY_TOKEN_BUDGET) -> List[Dict[str, str]]:
    """
    Keep the most recent messages within the token budget.
    Returns messages in chronological order.
    """
    messages = []
    token_count = 0

    for msg in reversed(chat_history):
        role = "user" if msg.role == "user" else "assistant"
        msg_tokens = len(tokenizer.encode(msg.text)) + 4  # +4 overhead per message
        if token_count + msg_tokens > budget:
            logger.info(
                f"History truncated: {token_count} tokens kept, "
                f"{len(chat_history) - len(messages)} messages dropped"
            )
            break
        messages.append({"role": role, "content": msg.text})
        token_count += msg_tokens

    messages.reverse()
    return messages


def generate(input_messages: List[Dict[str, str]]) -> str:
    """Call OpenAI Responses API and return the output text."""
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=input_messages,
    )
    return response.output_text


def generate_stream(input_messages: List[Dict[str, str]]):
    """Yield streaming deltas from the OpenAI Responses API."""
    stream = client.responses.create(
        model=OPENAI_MODEL,
        input=input_messages,
        stream=True,
    )
    for event in stream:
        if event.type == "response.output_text.delta":
            yield event.delta
