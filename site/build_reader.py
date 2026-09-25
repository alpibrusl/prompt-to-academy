#!/usr/bin/env python3
"""Render chapters/*.md into a web-native reader page.

bookkit's own HTML renderer emits a paginated, print-emulating document (fixed
6x9in @page rules, running headers, a table of contents whose page numbers
only resolve under paged media) meant to preview the EPUB/PDF layout. That is
the right tool for proofing the book, and the wrong one for reading it in a
browser. This script renders the same chapter Markdown into an actual web
page instead: a sticky chapter sidebar, dark-mode support and a reading
column sized for a screen rather than a 6x9in page.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "reader_template.html"
BASE_URL = "https://alpibrusl.github.io/prompt-to-academy/"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_chapters(config: dict) -> list[dict]:
    converter = markdown.Markdown(extensions=["extra", "smarty"])
    chapters = []
    for number, entry in enumerate(config["chapters"], start=1):
        text = (ROOT / entry["file"]).read_text()
        converter.reset()
        body = converter.convert(text)

        heading = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = re.sub(r"<[^>]+>", "", heading.group(1)).strip() if heading else entry["file"]
        body = re.sub(r"^\s*<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.S)

        chapters.append(
            {
                "number": number,
                "title": title,
                "part": entry.get("part", ""),
                "slug": f"ch{number:02d}",
                "body": body,
            }
        )
    return chapters


def render_sidebar(chapters: list[dict]) -> str:
    items = []
    last_part = None
    for chapter in chapters:
        if chapter["part"] != last_part:
            items.append(f'<li class="toc-part">{html.escape(chapter["part"])}</li>')
            last_part = chapter["part"]
        items.append(
            f'<li><a href="#{chapter["slug"]}" data-slug="{chapter["slug"]}">'
            f'<span class="toc-num">{chapter["number"]:02d}</span>'
            f'{html.escape(chapter["title"])}</a></li>'
        )
    return "\n".join(items)


def render_chapters(chapters: list[dict]) -> str:
    sections = []
    for i, chapter in enumerate(chapters):
        prev_link = (
            f'<a class="chapter-nav-link prev" href="#{chapters[i - 1]["slug"]}">'
            f'&larr; {html.escape(chapters[i - 1]["title"])}</a>'
            if i > 0
            else '<span></span>'
        )
        next_link = (
            f'<a class="chapter-nav-link next" href="#{chapters[i + 1]["slug"]}">'
            f'{html.escape(chapters[i + 1]["title"])} &rarr;</a>'
            if i + 1 < len(chapters)
            else '<span></span>'
        )
        sections.append(
            f'<section class="chapter" id="{chapter["slug"]}" data-slug="{chapter["slug"]}">\n'
            f'<p class="chapter-eyebrow">{html.escape(chapter["part"])} &middot; '
            f'Chapter {chapter["number"]}</p>\n'
            f'<h1>{html.escape(chapter["title"])}</h1>\n'
            f'{chapter["body"]}\n'
            f'<nav class="chapter-nav">{prev_link}{next_link}</nav>\n'
            f"</section>"
        )
    return "\n".join(sections)


def render_jsonld(config: dict, url: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": config["title"],
        "description": config.get("subtitle", ""),
        "author": {"@type": "Person", "name": (config.get("author") or {}).get("name") or ""},
        "inLanguage": "en",
        "license": config["copyright"]["license_url"],
        "url": url,
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2)}\n</script>'


def main() -> None:
    config = yaml.safe_load((ROOT / "book.yaml").read_text())
    chapters = load_chapters(config)

    out_dir = ROOT / "_site"
    out_dir.mkdir(parents=True, exist_ok=True)

    url = BASE_URL + "book.html"
    page = TEMPLATE.read_text()
    page = page.replace("{{TITLE}}", html.escape(config["title"]))
    page = page.replace("{{SUBTITLE}}", html.escape(config.get("subtitle", "")))
    page = page.replace("{{AUTHOR}}", html.escape((config.get("author") or {}).get("name") or ""))
    page = page.replace("{{LICENSE}}", html.escape(config["copyright"]["license"]))
    page = page.replace("{{LICENSE_URL}}", html.escape(config["copyright"]["license_url"]))
    page = page.replace("{{SIDEBAR}}", render_sidebar(chapters))
    page = page.replace("{{CHAPTERS}}", render_chapters(chapters))
    page = page.replace("{{URL}}", url)
    page = page.replace("{{JSONLD}}", render_jsonld(config, url))

    (out_dir / "book.html").write_text(page)
    print(f"wrote _site/book.html ({len(chapters)} chapters)")


if __name__ == "__main__":
    main()
