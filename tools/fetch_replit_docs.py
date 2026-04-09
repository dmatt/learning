#!/usr/bin/env python3
"""
Download all Replit documentation into raw/replit-docs/.

Fetches llms-full.txt (every doc page concatenated) and splits it into
individual markdown files, one per doc page.

Usage:
    python3 tools/fetch_replit_docs.py

Requires: requests (pip install requests)
"""

import os
import re
import sys
import requests
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RAW_DIR = REPO_ROOT / "raw" / "replit-docs"
LLMS_FULL_URL = "https://docs.replit.com/llms-full.txt"
LLMS_INDEX_URL = "https://docs.replit.com/llms.txt"


def fetch(url: str) -> str:
    print(f"Fetching {url} ...")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    print(f"  -> {len(resp.text):,} chars")
    return resp.text


def slug_from_heading(heading: str) -> str:
    """Convert a heading like 'Introduction to Replit' to 'introduction-to-replit'."""
    slug = re.sub(r"[^\w\s-]", "", heading.lower())
    slug = re.sub(r"[\s]+", "-", slug.strip())
    return slug[:80]


def split_into_pages(full_text: str) -> list[tuple[str, str]]:
    """
    Split llms-full.txt into (filename, content) pairs.

    The file uses patterns like:
      Source: https://docs.replit.com/path/to/page
      # Page Title
    """
    pages = []
    # Split on "Source: https://docs.replit.com/..." lines
    chunks = re.split(r"(?=^Source:\s*https://docs\.replit\.com/)", full_text, flags=re.MULTILINE)

    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        # Extract source URL for filename
        source_match = re.match(r"Source:\s*https://docs\.replit\.com/(.+?)(?:\n|$)", chunk)
        if source_match:
            path = source_match.group(1).strip()
            filename = path.replace("/", "--") + ".md"
        else:
            # First chunk might be preamble
            title_match = re.match(r"#\s+(.+)", chunk)
            if title_match:
                filename = slug_from_heading(title_match.group(1)) + ".md"
            else:
                filename = "00-preamble.md"

        # Clean filename
        filename = re.sub(r"[^\w\-.]", "-", filename)
        pages.append((filename, chunk))

    return pages


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Download the full docs file
    full_text = fetch(LLMS_FULL_URL)

    # Also save the full file as-is
    full_path = RAW_DIR / "llms-full.txt"
    full_path.write_text(full_text, encoding="utf-8")
    print(f"Saved complete file: {full_path}")

    # Download the index file
    try:
        index_text = fetch(LLMS_INDEX_URL)
        index_path = RAW_DIR / "llms-index.txt"
        index_path.write_text(index_text, encoding="utf-8")
        print(f"Saved index: {index_path}")
    except Exception as e:
        print(f"Could not fetch index: {e}")

    # Split into individual pages
    pages = split_into_pages(full_text)
    print(f"\nSplitting into {len(pages)} individual doc pages...")

    for filename, content in pages:
        filepath = RAW_DIR / filename
        filepath.write_text(content, encoding="utf-8")

    print(f"\nDone! {len(pages)} files written to {RAW_DIR}/")
    print(f"Total size: {sum(f.stat().st_size for f in RAW_DIR.iterdir()):,} bytes")
    print(f"\nNext: open this repo in Claude Code and run:")
    print(f"  /wiki-ingest raw/replit-docs/llms-full.txt")


if __name__ == "__main__":
    main()
