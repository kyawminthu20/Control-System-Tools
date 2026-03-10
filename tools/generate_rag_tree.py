#!/usr/bin/env python3
"""
Generate docs/_data/rag_tree.json and copy RAG markdown files into
docs/assets/rag-files/ so they are served by GitHub Pages (same origin).

Run from repo root:
    python3 tools/generate_rag_tree.py
"""

import json
import shutil
from pathlib import Path

RAG_ROOT    = Path("control-standards/rag")
OUT_FILE    = Path("docs/_data/rag_tree.json")
SERVE_ROOT  = Path("docs/assets/rag-files")   # served at /assets/rag-files/

SKIP_FILES  = {"README.md"}
SKIP_DIRS   = {"__pycache__", ".git"}


def walk(path: Path) -> list:
    entries = []
    for item in sorted(path.iterdir()):
        if item.name.startswith(".") or item.name in SKIP_DIRS:
            continue
        if item.is_dir():
            children = walk(item)
            if children:
                entries.append({
                    "name": item.name,
                    "type": "dir",
                    "children": children,
                })
        elif item.is_file() and item.suffix == ".md" and item.name not in SKIP_FILES:
            # serve_path is relative to docs/assets/rag-files/
            rel = item.relative_to(RAG_ROOT)
            entries.append({
                "name": item.name,
                "type": "file",
                "path": str(item),          # repo-relative path (display only)
                "serve_path": str(rel),     # path under /assets/rag-files/
            })
    return entries


def copy_files(path: Path) -> int:
    """Copy all .md files (except SKIP_FILES) into SERVE_ROOT, preserving structure."""
    count = 0
    for item in path.rglob("*.md"):
        if item.name in SKIP_FILES:
            continue
        dest = SERVE_ROOT / item.relative_to(RAG_ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, dest)
        count += 1
    return count


def main():
    if not RAG_ROOT.exists():
        raise SystemExit(f"RAG root not found: {RAG_ROOT}")

    # Clean and repopulate serve dir
    if SERVE_ROOT.exists():
        shutil.rmtree(SERVE_ROOT)
    SERVE_ROOT.mkdir(parents=True)

    copied = copy_files(RAG_ROOT)
    print(f"Copied:  {copied} .md files  →  {SERVE_ROOT}")

    tree = walk(RAG_ROOT)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(tree, indent=2))
    print(f"Written: {OUT_FILE}  ({len(tree)} top-level entries)")


if __name__ == "__main__":
    main()
