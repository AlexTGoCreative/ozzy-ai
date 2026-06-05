"""
CLI script to run the ingestion pipeline.

Usage:
    # Recursive crawl from seed URLs + index
    python -m scripts.ingest

    # Crawl specific URLs (non-recursive)
    python -m scripts.ingest --urls https://opswat.com/docs/mdcore/... https://...

    # Limit max pages or depth
    python -m scripts.ingest --max-pages 20 --max-depth 2

    # Rebuild index from already-crawled data in data/scraped/
    python -m scripts.ingest --from-disk

    # Full rebuild (drop Qdrant collection + reindex)
    python -m scripts.ingest --rebuild
"""

import argparse
import glob
import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import SCRAPED_DIR
from src.ingestion.crawler import crawl_recursive, crawl_urls
from src.ingestion.chunker import chunk_documents
from src.ingestion.indexer import index_documents, rebuild_index
from src.ingestion.cleaner import clean_content

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def _load_from_disk() -> list[dict]:
    """Load previously scraped .md files from data/scraped/ directory."""
    documents = []
    for filepath in glob.glob(os.path.join(SCRAPED_DIR, "*.md")):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse metadata from HTML comments at top
        metadata = {"source_url": "", "product": "", "doc_type": "concept"}
        for line in content.split("\n")[:5]:
            if line.startswith("<!-- source:"):
                metadata["source_url"] = line.replace("<!-- source:", "").replace("-->", "").strip()
            elif line.startswith("<!-- product:"):
                metadata["product"] = line.replace("<!-- product:", "").replace("-->", "").strip()
            elif line.startswith("<!-- doc_type:"):
                metadata["doc_type"] = line.replace("<!-- doc_type:", "").replace("-->", "").strip()

        # Strip metadata comments from text
        text_lines = [l for l in content.split("\n") if not l.startswith("<!--")]
        text = "\n".join(text_lines).strip()

        # Clean UI artifacts
        text = clean_content(text)

        if text:
            documents.append({"text": text, "metadata": metadata})

    logger.info(f"Loaded {len(documents)} documents from {SCRAPED_DIR}")
    return documents


def _clean_scraped_files():
    """Re-clean all scraped .md files on disk (in-place)."""
    files = glob.glob(os.path.join(SCRAPED_DIR, "*.md"))
    cleaned_count = 0
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Separate metadata header from text
        lines = content.split("\n")
        meta_lines = []
        text_start = 0
        for i, line in enumerate(lines):
            if line.startswith("<!--"):
                meta_lines.append(line)
                text_start = i + 1
            elif line.strip() == "" and meta_lines:
                text_start = i + 1
            else:
                break

        text = "\n".join(lines[text_start:])
        cleaned_text = clean_content(text)

        if cleaned_text != text:
            # Rewrite file with metadata + cleaned content
            with open(filepath, "w", encoding="utf-8") as f:
                for ml in meta_lines:
                    f.write(ml + "\n")
                f.write("\n")
                f.write(cleaned_text)
            cleaned_count += 1

    logger.info(f"Cleaned {cleaned_count}/{len(files)} files in {SCRAPED_DIR}")


def main():
    parser = argparse.ArgumentParser(description="Run the ozzy-ai ingestion pipeline")
    parser.add_argument("--urls", nargs="+", help="Specific URLs to crawl (non-recursive)")
    parser.add_argument("--max-pages", type=int, default=None, help="Max pages to crawl")
    parser.add_argument("--max-depth", type=int, default=3, help="Max recursion depth")
    parser.add_argument("--rebuild", action="store_true", help="Full rebuild (drop + reindex)")
    parser.add_argument("--from-disk", action="store_true", help="Index from existing scraped files")
    parser.add_argument("--clean-only", action="store_true", help="Clean scraped files on disk without indexing")
    parser.add_argument("--batch-size", type=int, default=32, help="Embedding batch size")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (sec)")
    args = parser.parse_args()

    # Step 1: Get documents
    if args.clean_only:
        logger.info("Cleaning scraped files on disk (no indexing)")
        _clean_scraped_files()
        logger.info("Done!")
        return

    if args.from_disk:
        logger.info("Loading from disk (data/scraped/)")
        documents = _load_from_disk()
    elif args.urls:
        logger.info(f"Crawling {len(args.urls)} specific URLs (non-recursive)")
        documents = crawl_urls(args.urls, delay=args.delay)
    else:
        logger.info("Recursive crawl from seed URLs")
        documents = crawl_recursive(
            max_pages=args.max_pages,
            max_depth=args.max_depth,
            delay=args.delay,
            save_to_disk=True,
        )

    if not documents:
        logger.error("No documents found. Exiting.")
        sys.exit(1)

    logger.info(f"Total documents: {len(documents)}")

    # Step 2: Chunk + Index
    if args.rebuild:
        logger.info("Rebuilding index from scratch")
        rebuild_index(documents, batch_size=args.batch_size)
    else:
        logger.info("Chunking documents")
        parents, children = chunk_documents(documents)
        logger.info(f"Chunked: {len(parents)} parents, {len(children)} children")

        logger.info("Indexing to Qdrant")
        index_documents(children, parents, batch_size=args.batch_size)

    logger.info("Ingestion complete!")


if __name__ == "__main__":
    main()
