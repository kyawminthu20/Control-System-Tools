#!/usr/bin/env python3
"""One-shot: update internal cross-links across docs/ for Batch 6.

Maps:
  /rag-browser/            -> /tools/rag-browser/
  /glossary/               -> /tools/glossary/
  /crosswalks/             -> /tools/crosswalks/  (covers index + 6 subpaths)
  /reference/              -> /tools/reference-hub/  (bare only — subpaths below)

Handled but already migrated by earlier batches; we still rewrite any stragglers:
  /reference/architecture/ -> /design/architecture/
  /reference/motor-systems/-> /design/motor-selection/

Rules:
- Do NOT modify `redirect_from:` entries (those must keep old URLs).
- Do NOT modify files under `docs/_data/phase26_migration_map.yml` (authoritative map).
- Skip binary assets. Act only on .md, .html, .yml, .yaml, .json.

Run:
    python3 tools/_phase26_batch6_update_links.py
"""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"

MAP_FILE = DOCS / "_data" / "phase26_migration_map.yml"
SKIP_FILES = {MAP_FILE.resolve()}

EXTS = {".md", ".html", ".yml", ".yaml", ".json"}

# Ordered replacements (longest/most-specific first so shorter prefixes don't gobble).
# Each entry: (old_prefix, new_prefix)
REPLACEMENTS = [
    # subpaths of /reference/ that moved to /design/ (already migrated in batch 3;
    # here only as safety net for stragglers)
    ("/reference/architecture/", "/design/architecture/"),
    ("/reference/motor-systems/motor-selection-matrix/",
     "/design/motor-selection/motor-selection-matrix/"),
    ("/reference/motor-systems/", "/design/motor-selection/"),
    # batch-6 core
    ("/rag-browser/", "/tools/rag-browser/"),
    ("/glossary/", "/tools/glossary/"),
    ("/crosswalks/", "/tools/crosswalks/"),
    ("/reference/", "/tools/reference-hub/"),
]


def update_text(text: str) -> tuple[str, int]:
    """Return (new_text, num_replacements). Skips lines inside redirect_from blocks."""
    lines = text.splitlines(keepends=True)
    out = []
    in_redirect_block = False
    in_frontmatter = False
    frontmatter_closes = 0
    count = 0

    for idx, line in enumerate(lines):
        stripped = line.strip()
        # Track frontmatter to detect whether we're inside it
        if stripped == "---":
            frontmatter_closes += 1
            in_frontmatter = frontmatter_closes < 2
            out.append(line)
            continue

        # Detect redirect_from: start (within frontmatter only)
        if in_frontmatter and stripped.startswith("redirect_from:"):
            in_redirect_block = True
            out.append(line)
            continue

        if in_redirect_block:
            # redirect_from entries are continuation list items. Stop when indent drops.
            if stripped.startswith("-") or stripped == "" or line.startswith("  "):
                # still inside list (or blank)
                if stripped == "" or stripped.startswith("-"):
                    out.append(line)
                    continue
            # otherwise, end of list
            in_redirect_block = False

        new_line = line
        for old, new in REPLACEMENTS:
            if old in new_line:
                # Do not rewrite if line already contains new path version (idempotent).
                new_line = new_line.replace(old, new)
                count += 1
        out.append(new_line)

    return "".join(out), count


def walk():
    total_files_touched = 0
    total_replacements = 0
    for path in DOCS.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in EXTS:
            continue
        if path.resolve() in SKIP_FILES:
            continue
        # skip vendor bundle + _site
        parts = path.parts
        if "vendor" in parts or "_site" in parts:
            continue
        # skip the moved tools files' redirect_from lines handled by update_text
        text = path.read_text()
        new_text, n = update_text(text)
        if n > 0 and new_text != text:
            path.write_text(new_text)
            total_files_touched += 1
            total_replacements += n
            print(f"  {n:4d}  {path.relative_to(REPO)}")
    print(f"Total: {total_replacements} replacements across {total_files_touched} files")


if __name__ == "__main__":
    walk()
