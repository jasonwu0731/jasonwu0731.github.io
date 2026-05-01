#!/usr/bin/env python3
"""Fetches the latest post from the Salesforce Blog author RSS; writes _data/salesforce_blog_latest.json.

WordPress author feed (stable URL): …/author/<slug>/feed/rss/

For local runs: python3 script/fetch-latest-salesforce-blog-post.py
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

DEFAULT_FEED_URL = "https://www.salesforce.com/blog/author/chien-sheng-wu/feed/rss/"


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


def field_content_encoded(block: str) -> str:
    c = re.search(
        r"<content:encoded><!\[CDATA\[(.*?)\]\]></content:encoded>",
        block,
        re.DOTALL | re.IGNORECASE,
    )
    return c.group(1).strip() if c else ""


def plain_excerpt(html: str) -> str | None:
    if not html:
        return None
    text = re.sub(r"<[^>]+>", " ", html)
    text = unescape(text)
    return " ".join(text.split()) or None


def first_image_url(html: str) -> str | None:
    if not html:
        return None
    m = re.search(r'<img[^>]+src="([^"]+)"', html, re.IGNORECASE)
    return m.group(1) if m else None


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out = root / "_data" / "salesforce_blog_latest.json"
    url = feed_url()

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "jasonwu0731.github.io/1.0 (salesforce blog preview; +https://jasonwu0731.github.io)"
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        raw = resp.read().decode("utf-8", errors="replace")

    block = first_item_block(raw)
    if not block:
        print("No <item> in feed", file=sys.stderr)
        return 1

    title = field_cdata_or_plain(block, "title")
    link = field_cdata_or_plain(block, "link")
    pub_raw = field_cdata_or_plain(block, "pubDate")
    desc_html = field_cdata_or_plain(block, "description")
    content_html = field_content_encoded(block)

    if not title or not link:
        print("First item missing title or link", file=sys.stderr)
        return 1

    date_iso = ""
    try:
        dt = parsedate_to_datetime(pub_raw)
        date_display = dt.strftime("%B %d, %Y")
        date_iso = dt.isoformat()
    except (TypeError, ValueError, OverflowError):
        date_display = pub_raw

    excerpt = plain_excerpt(desc_html) or plain_excerpt(content_html) or ""
    image = first_image_url(content_html) or first_image_url(desc_html) or ""
    if image:
        image = unescape(image)

    data = {
        "title": title,
        "url": link,
        "date_display": date_display,
        "date_iso": date_iso,
        "excerpt": excerpt,
        "image": image,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {out}")
    return 0


def feed_url() -> str:
    import os

    u = (os.environ.get("SALESFORCE_BLOG_FEED_URL") or "").strip()
    return u or DEFAULT_FEED_URL


if __name__ == "__main__":
    raise SystemExit(main())
