#!/usr/bin/env python3
"""
Generate docs/_data/rag_tree.json from control-standards/rag/.

Run from repo root:
    python3 tools/generate_rag_tree.py
"""

import json
import os
from pathlib import Path

RAG_ROOT = Path("control-standards/rag")
OUT_FILE = Path("docs/_data/rag_tree.json")

SKIP_FILES = {"README.md"}
SKIP_DIRS  = {"__pycache__", ".git"}


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
            entries.append({
                "name": item.name,
                "type": "file",
                "path": str(item),
            })
    return entries


def main():
    if not RAG_ROOT.exists():
        raise SystemExit(f"RAG root not found: {RAG_ROOT}")

    tree = walk(RAG_ROOT)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(tree, indent=2))
    print(f"Written: {OUT_FILE}  ({len(tree)} top-level entries)")


if __name__ == "__main__":
    main()
