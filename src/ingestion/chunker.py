"""
Structure-aware chunking with parent-child strategy.

- Parent chunks (~1024 tokens): used for generation context
- Child chunks (~128 tokens): used for retrieval precision
- Markdown structure is preserved (headers, code blocks)
- Token-based length function using the embedding model tokenizer
"""

import hashlib
import logging
import re
import uuid
from typing import Optional

from transformers import AutoTokenizer

from src.config import (
    EMBEDDING_MODEL_NAME,
    PARENT_CHUNK_SIZE,
    PARENT_CHUNK_OVERLAP,
    CHILD_CHUNK_SIZE,
    CHILD_CHUNK_OVERLAP,
)

logger = logging.getLogger(__name__)

# Tokenizer for length measurement (matches embedding model)
_tokenizer = None


def _get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL_NAME)
        logger.info(f"Chunker tokenizer loaded: {EMBEDDING_MODEL_NAME}")
    return _tokenizer


def token_len(text: str) -> int:
    """Count tokens using the embedding model tokenizer."""
    tok = _get_tokenizer()
    return len(tok.encode(text, add_special_tokens=False))


# --- Markdown splitting ---

HEADER_PATTERN = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)
CODE_BLOCK_PATTERN = re.compile(r"```[\s\S]*?```", re.MULTILINE)


def _split_by_headers(text: str) -> list[dict]:
    """
    Split Markdown by headers (h1, h2, h3).
    Returns sections with their heading path as metadata.
    """
    sections = []
    current_headers = {"h1": "", "h2": "", "h3": ""}
    current_text_parts = []
    current_start = 0

    lines = text.split("\n")
    for line in lines:
        match = HEADER_PATTERN.match(line)
        if match:
            # Save previous section
            if current_text_parts:
                section_text = "\n".join(current_text_parts).strip()
                if section_text:
                    sections.append({
                        "text": section_text,
                        "headers": dict(current_headers),
                        "section_path": [v for v in current_headers.values() if v],
                    })
                current_text_parts = []

            level = len(match.group(1))
            header_text = match.group(2).strip()

            if level == 1:
                current_headers = {"h1": header_text, "h2": "", "h3": ""}
            elif level == 2:
                current_headers["h2"] = header_text
                current_headers["h3"] = ""
            elif level == 3:
                current_headers["h3"] = header_text

            # Include the header line in the section
            current_text_parts.append(line)
        else:
            current_text_parts.append(line)

    # Final section
    if current_text_parts:
        section_text = "\n".join(current_text_parts).strip()
        if section_text:
            sections.append({
                "text": section_text,
                "headers": dict(current_headers),
                "section_path": [v for v in current_headers.values() if v],
            })

    return sections


def _split_text_preserving_code(
    text: str,
    max_tokens: int,
    overlap_tokens: int,
) -> list[str]:
    """
    Split text into chunks respecting token limits.
    Never splits inside code blocks.
    """
    # Identify code blocks to protect
    code_blocks = [(m.start(), m.end()) for m in CODE_BLOCK_PATTERN.finditer(text)]

    def _in_code_block(pos: int) -> bool:
        return any(start <= pos < end for start, end in code_blocks)

    # Preferred split points (in priority order)
    separators = ["\n\n", "\n", ". ", " "]

    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        # Estimate end position
        # Start with a generous char estimate (avg 4 chars/token)
        estimated_end = start + max_tokens * 4
        if estimated_end >= text_len:
            chunks.append(text[start:].strip())
            break

        # Shrink until within token budget
        end = min(estimated_end, text_len)
        segment = text[start:end]
        while token_len(segment) > max_tokens and end > start + 50:
            end -= max(50, (token_len(segment) - max_tokens) * 2)
            end = max(start + 50, end)
            segment = text[start:end]

        # Find best split point
        best_split = end
        for sep in separators:
            # Look for separator near the end, not inside code block
            search_start = max(start, end - 200)
            idx = text.rfind(sep, search_start, end)
            if idx > start and not _in_code_block(idx):
                best_split = idx + len(sep)
                break

        chunk = text[start:best_split].strip()
        if chunk:
            chunks.append(chunk)

        # Move start with overlap
        overlap_chars = overlap_tokens * 4  # rough estimate
        start = max(start + 1, best_split - overlap_chars)

    return chunks


def chunk_markdown(doc_text: str, base_metadata: dict) -> tuple[list[dict], list[dict]]:
    """
    Chunk a Markdown document into parent and child chunks.

    Returns:
        (parents, children) — each is a list of dicts with 'text' and 'metadata'.
    """
    parents = []
    children = []

    # Step 1: Split by headers into structural sections
    sections = _split_by_headers(doc_text)

    for section in sections:
        section_text = section["text"]
        section_path = section["section_path"]

        # Step 2: Split section into parent chunks
        parent_texts = _split_text_preserving_code(
            section_text, PARENT_CHUNK_SIZE, PARENT_CHUNK_OVERLAP
        )

        for p_idx, parent_text in enumerate(parent_texts):
            parent_id = f"{base_metadata.get('content_hash', 'unknown')[:12]}_{len(parents)}"

            parent_meta = {
                **base_metadata,
                "chunk_type": "parent",
                "parent_id": parent_id,
                "section_path": " > ".join(section_path) if section_path else "",
                "chunk_index": len(parents),
                "token_count": token_len(parent_text),
            }
            parents.append({"text": parent_text, "metadata": parent_meta})

            # Step 3: Split parent into child chunks for retrieval
            child_texts = _split_text_preserving_code(
                parent_text, CHILD_CHUNK_SIZE, CHILD_CHUNK_OVERLAP
            )

            for c_idx, child_text in enumerate(child_texts):
                child_meta = {
                    **base_metadata,
                    "chunk_type": "child",
                    "parent_id": parent_id,
                    "section_path": " > ".join(section_path) if section_path else "",
                    "chunk_index": len(children),
                    "token_count": token_len(child_text),
                }
                children.append({"text": child_text, "metadata": child_meta})

    logger.info(
        f"Chunked document: {len(parents)} parents, {len(children)} children "
        f"(source: {base_metadata.get('source_url', 'unknown')})"
    )
    return parents, children


def chunk_documents(documents: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Chunk a list of crawled documents into parents and children.
    Each document should have 'text' and 'metadata' keys.
    """
    all_parents = []
    all_children = []

    for doc in documents:
        parents, children = chunk_markdown(doc["text"], doc["metadata"])
        all_parents.extend(parents)
        all_children.extend(children)

    logger.info(
        f"Total chunking results: {len(all_parents)} parents, "
        f"{len(all_children)} children from {len(documents)} documents"
    )
    return all_parents, all_children
