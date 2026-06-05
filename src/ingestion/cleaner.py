"""
Post-processing cleaner for scraped OPSWAT documentation.
Strips website UI artifacts (CMS modals, search widgets, page chrome)
that Playwright captures from the DOM but are not documentation content.
"""

import re


# --- Header noise: CMS editor UI rendered in the DOM ---
_HEADER_NOISE_BLOCK = re.compile(
    r"^("
    # Repeated page title lines (2-3x at the top, before first heading)
    r"(?:.*\n){0,4}"
    # Version string like "v5.19.0"
    r"(?:v\d+\.\d+\.\d+\s*\n)?"
    r"(?:Search this version\s*\n)?"
    # Title repeated again
    r"(?:.*\n){0,4}"
    # CMS modal blocks
    r"(?:####\s*Title\s*\n)?"
    r"(?:Message\s*\n)?"
    r"(?:####\s*Create new category\s*\n)?"
    r"(?:What is the title of your new category\?\s*\n)?"
    r"(?:####\s*Edit page index title\s*\n)?"
    r"(?:What is the title of the page index\?\s*\n)?"
    r"(?:####\s*Edit category\s*\n)?"
    r"(?:What is the new title of your category\?\s*\n)?"
    r"(?:####\s*Edit link\s*\n)?"
    r"(?:What is the new title and URL of your link\?\s*\n)?"
    r")",
    re.MULTILINE,
)

# Lines to remove anywhere in the document
_INLINE_NOISE_LINES = [
    "Copy Markdown",
    "Open in ChatGPT",
    "Open in Claude",
]

# Footer noise: search widgets, feedback prompts, CMS modals at the bottom
_FOOTER_NOISE_PATTERNS = [
    r"VariableType to search.*?ESC to discard",
    r"GlossaryType to search.*?ESC to discard",
    r"InsertType to search.*?ESC to discard",
    r"No matches",
    r"Last updated on.*",
    r"Was this page helpful\?",
    r"Next to read:.*",
    r"####\s*Discard Changes",
    r"Do you want to discard your current changes and overwrite with the template\?",
    r"####\s*Archive Synced Block",
    r"####\s*Create new Template",
    r"What is this template's title\?",
    r"####\s*Delete Template",
    # "Message" alone on a line (CMS placeholder) - only in footer section
    r"^Message$",
]

_FOOTER_RE = re.compile(
    r"|".join(f"({p})" for p in _FOOTER_NOISE_PATTERNS),
    re.MULTILINE,
)


def clean_content(text: str) -> str:
    """
    Remove OPSWAT docs site UI artifacts from extracted Markdown.
    Preserves metadata HTML comments and actual documentation content.
    """
    if not text:
        return text

    lines = text.split("\n")
    cleaned_lines = []
    in_footer = False

    for line in lines:
        stripped = line.strip()

        # Skip inline noise lines
        if stripped in _INLINE_NOISE_LINES:
            continue

        # Detect footer section start
        if not in_footer and _is_footer_start(stripped):
            in_footer = True

        if in_footer:
            # In footer, skip all noise lines
            if _FOOTER_RE.match(stripped) or stripped == "Message" or stripped == "":
                continue
            # If we hit real content after footer noise started, it's still noise
            # (e.g. "Supported File Types#### Discard Changes" merged line)
            if _has_footer_marker(stripped):
                continue
            # Non-empty non-noise line after footer started — likely a stray nav link
            # Keep only if it looks like substantial content (has punctuation or is long)
            if len(stripped) < 60 and not any(c in stripped for c in ".,:;!?"):
                continue
            # Otherwise, it's probably real content that somehow ended up here
            in_footer = False
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Remove header noise block (before the first # heading)
    text = _strip_header_noise(text)

    # Collapse multiple blank lines into max 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def _strip_header_noise(text: str) -> str:
    """Remove repeated title, version string, and CMS modal text before first real heading."""
    lines = text.split("\n")
    first_heading_idx = None

    for i, line in enumerate(lines):
        # Find first Markdown heading that's actual content (# or ##)
        if re.match(r"^#{1,3}\s+\S", line):
            first_heading_idx = i
            break

    if first_heading_idx is None:
        return text

    # Check if lines before the heading are noise
    header_lines = lines[:first_heading_idx]
    content_lines = lines[first_heading_idx:]

    # Filter header lines: keep only metadata comments and blank lines
    kept_header = []
    for line in header_lines:
        stripped = line.strip()
        # Keep HTML metadata comments
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            kept_header.append(line)
        # Keep blank lines between metadata and content
        elif stripped == "" and kept_header:
            kept_header.append(line)
        # Skip everything else (repeated titles, version, CMS modals)

    return "\n".join(kept_header + content_lines)


def _is_footer_start(line: str) -> bool:
    """Detect the beginning of footer noise."""
    footer_starters = [
        "VariableType to search",
        "GlossaryType to search",
        "InsertType to search",
        "Last updated on",
        "Was this page helpful",
    ]
    return any(line.startswith(s) for s in footer_starters)


def _has_footer_marker(line: str) -> bool:
    """Check if a line contains known footer/CMS markers."""
    markers = [
        "Discard Changes",
        "Archive Synced Block",
        "Create new Template",
        "Delete Template",
        "Was this page helpful",
        "Next to read:",
        "Type to search",
        "ESC to discard",
    ]
    return any(m in line for m in markers)
