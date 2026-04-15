#!/usr/bin/env python3
"""
Internal link checker for the Jekyll-built static site.

Usage:
    python3 tools/check_internal_links.py docs/_site/

Walks every .html file in the given directory, extracts every <a href>, and
verifies that each internal link resolves to a real file on disk.

Exits 0 if zero broken links, 1 otherwise.
"""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

BASEURL = "/Control-System-Tools"


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value:
                self.links.append(value)


def is_external(href: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https", "mailto", "tel"):
        return True
    if href.startswith("//"):
        return True
    return False


def resolve(href: str, source: Path, site_root: Path) -> Path | None:
    # Strip fragment and query
    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href:
        return None
    href = unquote(href)

    # Site-root-relative (respects baseurl)
    if href.startswith(BASEURL):
        href = href[len(BASEURL):] or "/"
    if href.startswith("/"):
        target = site_root / href.lstrip("/")
    else:
        target = (source.parent / href).resolve()

    # Jekyll collapses directory URLs to index.html
    if target.is_dir():
        target = target / "index.html"
    if target.suffix == "":
        candidate = target.with_suffix(".html")
        if candidate.exists():
            return candidate
        candidate = target / "index.html"
        if candidate.exists():
            return candidate

    return target


def check_file(html_file: Path, site_root: Path) -> list[tuple[str, str]]:
    extractor = LinkExtractor()
    try:
        extractor.feed(html_file.read_text(encoding="utf-8", errors="ignore"))
    except Exception as exc:
        return [("<parse-error>", f"{exc}")]

    broken: list[tuple[str, str]] = []
    for href in extractor.links:
        if is_external(href) or not href or href.startswith("#"):
            continue
        target = resolve(href, html_file, site_root)
        if target is None:
            continue
        if not target.exists():
            broken.append((href, str(target)))
    return broken


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_internal_links.py <site-root>", file=sys.stderr)
        return 2

    site_root = Path(sys.argv[1]).resolve()
    if not site_root.is_dir():
        print(f"error: {site_root} is not a directory", file=sys.stderr)
        return 2

    total_broken = 0
    broken_by_source: dict[str, list[tuple[str, str]]] = {}
    for html_file in sorted(site_root.rglob("*.html")):
        broken = check_file(html_file, site_root)
        if broken:
            rel = html_file.relative_to(site_root)
            broken_by_source[str(rel)] = broken
            total_broken += len(broken)

    if total_broken == 0:
        print(f"OK: no broken internal links ({len(list(site_root.rglob('*.html')))} files scanned)")
        return 0

    for source, links in broken_by_source.items():
        for href, target in links:
            print(f"{source}: {href} -> {target}")

    print(f"\nFAIL: {total_broken} broken internal link(s) across {len(broken_by_source)} file(s)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
