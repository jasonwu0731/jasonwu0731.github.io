#!/usr/bin/env python3
"""Fetches the latest post from a Medium RSS feed; writes _data/medium_latest.json.

The full feed is not always well‑formed XML (invalid tokens in old items), so we
parse only the first <item> block with targeted regex, then read title/link/etc.

For local runs: python3 script/fetch-latest-medium-post.py
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

DEFAULT_FEED_URL = "https://medium.com/feed/@jason-wu830731"


def clean_medium_url(href: str) -> str:
    if "?" in href:
        return href.split("?")[0]
    return href


def first_item_block(rss: str) -> str | None:
    m = re.search(r"<item>(.*?)</item>", rss, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else None


def field_cdata_or_plain(block: str, tag: str) -> str:
    c = re.search(
        rf"<{re.escape(tag)}><!\[CDATA\[(.*?)\]\]></{re.escape(tag)}>",
        block,
        re.DOTALL | re.IGNORECASE,
    )
    if c:
        return c.group(1).strip()
    p = re.search(
        rf"<{re.escape(tag)}>([^<]*)</{re.escape(tag)}>", block, re.IGNORECASE
    )
    return (p.group(1) if p else "").strip()


def excerpt_from_description(html: str) -> str | None:
    m = re.search(
        r'<p class="medium-feed-snippet"[^>]*>(.*?)</p>', html, re.IGNORECASE | re.DOTALL
    )
    if not m:
        return None
    raw = m.group(1)
    text = re.sub(r"<[^>]+>", " ", raw)
    text = unescape(text)
    return " ".join(text.split()) or None


def first_image_url(html: str) -> str | None:
    m = re.search(r'<img[^>]+src="([^"]+)"', html, re.IGNORECASE)
    return m.group(1) if m else None


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out = root / "_data" / "medium_latest.json"
    url = feed_url()

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "jasonwu0731.github.io/1.0 (medium preview; +https://jasonwu0731.github.io)"
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="replace")

    block = first_item_block(raw)
    if not block:
        print("No <item> in feed", file=sys.stderr)
        return 1

    title = field_cdata_or_plain(block, "title")
    link = field_cdata_or_plain(block, "link")
    pub_raw = field_cdata_or_plain(block, "pubDate")
    desc_html = field_cdata_or_plain(block, "description")

    if not title or not link:
        print("First item missing title or link", file=sys.stderr)
        return 1

    link = clean_medium_url(link)
    date_iso = ""
    try:
        dt = parsedate_to_datetime(pub_raw)
        date_display = dt.strftime("%B %d, %Y")
        date_iso = dt.isoformat()
    except (TypeError, ValueError, OverflowError):
        date_display = pub_raw

    data = {
        "title": title,
        "url": link,
        "date_display": date_display,
        "date_iso": date_iso,
        "excerpt": excerpt_from_description(desc_html) or "",
        "image": first_image_url(desc_html) or "",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {out}")
    return 0


def feed_url() -> str:
    import os

    u = (os.environ.get("MEDIUM_FEED_URL") or "").strip()
    return u or DEFAULT_FEED_URL


if __name__ == "__main__":
    raise SystemExit(main())
