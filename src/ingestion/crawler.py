"""
Recursive crawler with Playwright for JS-rendered pages + trafilatura for extraction.
Crawls seed URLs, follows internal links recursively, and saves to disk.
Produces Markdown-formatted documents with metadata.
Uses async Playwright with persistent context to bypass CloudFront bot detection.
"""

import asyncio
import hashlib
import logging
import os
import re
import time
from datetime import datetime
from typing import Optional
from urllib.parse import urljoin, urlparse, urldefrag
from xml.etree import ElementTree

import requests
import trafilatura
from playwright.async_api import async_playwright, BrowserContext

from src.config import SEED_URLS, CRAWL_ALLOWED_PATTERNS, SCRAPED_DIR
from src.ingestion.cleaner import clean_content

logger = logging.getLogger(__name__)

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Browser-like headers
_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Browser data dir for persistent context (avoids CloudFront WAF)
_BROWSER_DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    ".browser_data"
)


async def _download_rendered(url: str, ctx: BrowserContext, wait_ms: int = 5000) -> Optional[str]:
    """
    Download a JS-rendered page using Playwright persistent context.
    Returns the rendered HTML string.
    """
    try:
        page = await ctx.new_page()
        await page.goto(url, timeout=60000, wait_until="networkidle")
        await page.wait_for_timeout(wait_ms)
        html = await page.content()
        await page.close()
        return html
    except Exception as e:
        logger.warning(f"Playwright download failed ({e}): {url}")
        return None


def _is_allowed(url: str) -> bool:
    """Check URL against allowed patterns."""
    return any(re.search(pattern, url) for pattern in CRAWL_ALLOWED_PATTERNS)


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _url_to_filename(url: str) -> str:
    """Convert URL to a safe filename for disk storage."""
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "_")
    if not path:
        path = "index"
    # Remove fragment
    path = path.split("#")[0]
    # Sanitize
    path = re.sub(r"[^\w\-.]", "_", path)
    return f"{path}.md"


def _save_to_disk(doc: dict):
    """Save extracted document to data/scraped/ as Markdown."""
    os.makedirs(SCRAPED_DIR, exist_ok=True)
    filename = _url_to_filename(doc["metadata"]["source_url"])
    filepath = os.path.join(SCRAPED_DIR, filename)

    # Write with metadata header
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"<!-- source: {doc['metadata']['source_url']} -->\n")
        f.write(f"<!-- product: {doc['metadata']['product']} -->\n")
        f.write(f"<!-- doc_type: {doc['metadata']['doc_type']} -->\n")
        f.write(f"<!-- crawled_at: {doc['metadata']['crawled_at']} -->\n\n")
        f.write(doc["text"])

    logger.info(f"Saved: {filepath}")


def _extract_links(html: str, base_url: str) -> list[str]:
    """Extract internal links from HTML that match allowed patterns."""
    links = set()
    # Find href attributes
    href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
    for match in href_pattern.finditer(html):
        href = match.group(1)
        # Resolve relative URLs
        full_url = urljoin(base_url, href)
        # Remove fragment
        full_url, _ = urldefrag(full_url)
        # Only keep allowed URLs
        if _is_allowed(full_url):
            links.add(full_url)
    return list(links)


def fetch_sitemap_urls(sitemap_url: str) -> list[str]:
    """Parse a sitemap XML and return all <loc> URLs."""
    try:
        resp = requests.get(sitemap_url, headers=_HEADERS, timeout=30)
        resp.raise_for_status()
        tree = ElementTree.fromstring(resp.content)

        # Handle sitemap index (nested sitemaps)
        sitemap_tags = tree.findall("sm:sitemap/sm:loc", SITEMAP_NS)
        if sitemap_tags:
            urls = []
            for tag in sitemap_tags:
                urls.extend(fetch_sitemap_urls(tag.text))
            return urls

        # Regular sitemap
        loc_tags = tree.findall("sm:url/sm:loc", SITEMAP_NS)
        urls = [tag.text for tag in loc_tags if tag.text]
        logger.info(f"Fetched {len(urls)} URLs from {sitemap_url}")
        return urls
    except Exception as e:
        logger.error(f"Error fetching sitemap {sitemap_url}: {e}")
        return []


def extract_page(url: str) -> Optional[dict]:
    """
    Sync wrapper for extracting a single page.
    Uses asyncio to run the async version.
    """
    return asyncio.run(_extract_page_async(url))


async def _extract_page_async(url: str, ctx: BrowserContext = None) -> Optional[dict]:
    """
    Download and extract content from a URL using Playwright + trafilatura.
    Returns a document dict with text (Markdown), metadata.
    """
    close_ctx = False
    try:
        if ctx is None:
            pw = await async_playwright().start()
            ctx = await pw.chromium.launch_persistent_context(
                user_data_dir=_BROWSER_DATA_DIR,
                headless=True,
                user_agent=_HEADERS["User-Agent"],
                viewport={"width": 1920, "height": 1080},
            )
            close_ctx = True

        downloaded = await _download_rendered(url, ctx)
        if not downloaded:
            return None

        # Extract as Markdown to preserve structure
        text = trafilatura.extract(
            downloaded,
            output_format="markdown",
            include_links=False,
            include_images=False,
            include_tables=True,
            favor_recall=True,
        )

        if not text or len(text) < 100:
            logger.warning(f"Insufficient content from {url} ({len(text) if text else 0} chars)")
            return None

        # Clean website UI artifacts
        text = clean_content(text)

        if len(text) < 50:
            logger.warning(f"Content too short after cleaning for {url}")
            return None

        # Detect 403/error pages
        if "403 ERROR" in text[:200] or "Request blocked" in text[:300]:
            logger.warning(f"CloudFront 403 block detected for {url}")
            return None

        doc_type = _infer_doc_type(url)
        product = _infer_product(url)

        return {
            "text": text,
            "metadata": {
                "source_url": url,
                "doc_type": doc_type,
                "product": product,
                "content_hash": _content_hash(text),
                "crawled_at": datetime.utcnow().isoformat(),
                "char_count": len(text),
            },
        }
    except Exception as e:
        logger.error(f"Error extracting {url}: {e}")
        return None
    finally:
        if close_ctx and ctx:
            await ctx.close()


def _infer_doc_type(url: str) -> str:
    """Infer document type from URL path."""
    url_lower = url.lower()
    if "/api" in url_lower or "api-v" in url_lower:
        return "api_reference"
    if "/tutorial" in url_lower or "/guide" in url_lower or "/getting-started" in url_lower:
        return "tutorial"
    if "/changelog" in url_lower or "/release" in url_lower:
        return "changelog"
    if "/faq" in url_lower:
        return "faq"
    return "concept"


def _infer_product(url: str) -> str:
    """Infer product name from URL path."""
    url_lower = url.lower()
    product_map = {
        "mdcloud": "metadefender_cloud",
        "metadefender-cloud": "metadefender_cloud",
        "metadefender-core": "metadefender_core",
        "mdcore": "metadefender_core",
        "metadefender-kiosk": "metadefender_kiosk",
        "filescan": "metadefender_cloud",
        "sandbox": "metadefender_sandbox",
        "metadefender-sandbox": "metadefender_sandbox",
        "cdr": "metadefender_cdr",
        "deep-cdr": "metadefender_cdr",
        "icap": "metadefender_icap",
        "metadefender-email": "metadefender_email",
    }
    for pattern, product in product_map.items():
        if pattern in url_lower:
            return product
    return "opswat_general"


def crawl_recursive(
    seed_urls: list[str] | None = None,
    max_pages: int | None = None,
    max_depth: int = 3,
    delay: float = 1.0,
    save_to_disk: bool = True,
) -> list[dict]:
    """
    Recursively crawl from seed URLs, following internal links.
    Sync wrapper around the async implementation.
    """
    return asyncio.run(_crawl_recursive_async(
        seed_urls=seed_urls,
        max_pages=max_pages,
        max_depth=max_depth,
        delay=delay,
        save_to_disk=save_to_disk,
    ))


async def _crawl_recursive_async(
    seed_urls: list[str] | None = None,
    max_pages: int | None = None,
    max_depth: int = 3,
    delay: float = 1.0,
    save_to_disk: bool = True,
) -> list[dict]:
    """
    Async recursive crawl using Playwright persistent context.
    """
    seed_urls = seed_urls or SEED_URLS
    visited: set[str] = set()
    documents: list[dict] = []

    # Queue: (url, depth)
    queue: list[tuple[str, int]] = [(url, 0) for url in seed_urls]

    os.makedirs(_BROWSER_DATA_DIR, exist_ok=True)

    async with async_playwright() as pw:
        ctx = await pw.chromium.launch_persistent_context(
            user_data_dir=_BROWSER_DATA_DIR,
            headless=True,
            user_agent=_HEADERS["User-Agent"],
            viewport={"width": 1920, "height": 1080},
        )
        logger.info("Playwright persistent context launched")

        try:
            while queue:
                if max_pages and len(documents) >= max_pages:
                    logger.info(f"Reached max_pages limit ({max_pages})")
                    break

                url, depth = queue.pop(0)
                url, _ = urldefrag(url)

                if url in visited:
                    continue
                if not _is_allowed(url):
                    continue

                visited.add(url)
                logger.info(f"Crawling [{len(documents)+1}] (depth={depth}): {url}")

                # Download rendered HTML
                raw_html = await _download_rendered(url, ctx)
                if not raw_html:
                    continue

                # Extract content as Markdown
                text = trafilatura.extract(
                    raw_html,
                    output_format="markdown",
                    include_links=False,
                    include_images=False,
                    include_tables=True,
                    favor_recall=True,
                )

                if not text or len(text) < 100:
                    logger.warning(f"Insufficient content from {url} ({len(text) if text else 0} chars)")
                else:
                    # Clean website UI artifacts
                    text = clean_content(text)

                    if not text or len(text) < 50:
                        logger.warning(f"Content too short after cleaning for {url}")
                    elif "403 ERROR" in text[:200] or "Request blocked" in text[:300]:
                        logger.warning(f"CloudFront 403 detected for {url}, skipping")
                    else:
                        doc_type = _infer_doc_type(url)
                        product = _infer_product(url)

                        doc = {
                            "text": text,
                            "metadata": {
                                "source_url": url,
                                "doc_type": doc_type,
                                "product": product,
                                "content_hash": _content_hash(text),
                                "crawled_at": datetime.utcnow().isoformat(),
                                "char_count": len(text),
                            },
                        }
                        documents.append(doc)

                        if save_to_disk:
                            _save_to_disk(doc)

                # Follow links if within depth limit
                if depth < max_depth and raw_html:
                    child_links = _extract_links(raw_html, url)
                    for link in child_links:
                        link_clean, _ = urldefrag(link)
                        if link_clean not in visited:
                            queue.append((link_clean, depth + 1))

                if delay > 0:
                    await asyncio.sleep(delay)

        finally:
            await ctx.close()

    logger.info(f"Recursive crawl complete: {len(documents)} documents from {len(visited)} URLs visited")
    return documents


def crawl_urls(urls: list[str], delay: float = 1.0, save_to_disk: bool = True) -> list[dict]:
    """Crawl a specific list of URLs (non-recursive). Sync wrapper."""
    return asyncio.run(_crawl_urls_async(urls, delay=delay, save_to_disk=save_to_disk))


async def _crawl_urls_async(urls: list[str], delay: float = 1.0, save_to_disk: bool = True) -> list[dict]:
    """Async crawl a specific list of URLs."""
    documents = []
    os.makedirs(_BROWSER_DATA_DIR, exist_ok=True)

    async with async_playwright() as pw:
        ctx = await pw.chromium.launch_persistent_context(
            user_data_dir=_BROWSER_DATA_DIR,
            headless=True,
            user_agent=_HEADERS["User-Agent"],
            viewport={"width": 1920, "height": 1080},
        )
        try:
            for i, url in enumerate(urls):
                logger.info(f"Crawling [{i+1}/{len(urls)}]: {url}")
                doc = await _extract_page_async(url, ctx)
                if doc:
                    documents.append(doc)
                    if save_to_disk:
                        _save_to_disk(doc)
                if delay > 0 and i < len(urls) - 1:
                    await asyncio.sleep(delay)
        finally:
            await ctx.close()
    return documents


# Keep for backward compat
def crawl_sitemap(
    sitemap_urls: list[str] | None = None,
    max_pages: int | None = None,
    delay: float = 1.0,
) -> list[dict]:
    """Crawl all pages from sitemaps (non-recursive)."""
    sitemap_urls = sitemap_urls or []
    all_urls = []
    for sitemap_url in sitemap_urls:
        all_urls.extend(fetch_sitemap_urls(sitemap_url))

    allowed_urls = [u for u in all_urls if _is_allowed(u)]
    if max_pages:
        allowed_urls = allowed_urls[:max_pages]

    return crawl_urls(allowed_urls, delay=delay)
