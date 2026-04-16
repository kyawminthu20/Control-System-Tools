#!/usr/bin/env python3
"""One-shot: insert redirect_from OLD-URL stanzas into Batch 6 moved files.

Reads docs/_data/phase26_migration_map.yml, walks the 'tools' group, and for
each entry inserts a `redirect_from:` block (bare + /index.html variants)
into the moved file's frontmatter, skipping files that already have it.

Usage:
    python3 tools/_phase26_batch6_add_redirects.py
"""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"
MAP_FILE = DOCS / "_data" / "phase26_migration_map.yml"


def parse_tools_entries(text: str):
    """Parse the `tools:` group entries from the migration map YAML.

    Each line in the tools section is:
      - { old: /...,   new: /...,   from: ...,   to: ... }
    """
    entries = []
    in_tools = False
    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped.startswith("tools:"):
            in_tools = True
            continue
        if in_tools:
            if not raw.startswith(" ") and not raw.startswith("\t") and stripped and not stripped.startswith("#"):
                # next top-level key — stop
                break
            if stripped.startswith("- {"):
                # Extract the dict body
                body = stripped[3:].rstrip(" }")
                # body like: "old: /.../,   new: /.../,   from: ...,   to: ..."
                fields = {}
                for part in body.split(","):
                    if ":" not in part:
                        continue
                    k, v = part.split(":", 1)
                    fields[k.strip()] = v.strip()
                if "old" in fields and "to" in fields:
                    entries.append(fields)
    return entries


def insert_redirect_from(fpath: Path, old_url: str) -> bool:
    text = fpath.read_text()
    if not text.startswith("---\n"):
        print(f"  !! {fpath}: no frontmatter block", file=sys.stderr)
        return False
    # Find end of frontmatter
    end = text.find("\n---\n", 4)
    if end == -1:
        print(f"  !! {fpath}: unterminated frontmatter", file=sys.stderr)
        return False
    front = text[4:end]
    rest = text[end + 5:]

    bare = old_url.rstrip("/") + "/"
    index_variant = bare + "index.html"

    # Check if already present
    if "redirect_from:" in front:
        # Extract existing list and append if missing
        lines = front.splitlines()
        new_lines = []
        i = 0
        inserted = False
        while i < len(lines):
            line = lines[i]
            new_lines.append(line)
            if line.startswith("redirect_from:"):
                # collect existing entries
                existing = []
                j = i + 1
                while j < len(lines) and lines[j].startswith("  - "):
                    existing.append(lines[j][4:].strip())
                    j += 1
                # determine what to add
                to_add = []
                if bare not in existing:
                    to_add.append(bare)
                if index_variant not in existing:
                    to_add.append(index_variant)
                # copy existing lines
                for k in range(i + 1, j):
                    new_lines.append(lines[k])
                # append new
                for u in to_add:
                    new_lines.append(f"  - {u}")
                inserted = True
                i = j
                continue
            i += 1
        if not inserted:
            return False
        new_front = "\n".join(new_lines)
    else:
        # Insert redirect_from block right after the layout: line (or at top)
        new_front = front + f"\nredirect_from:\n  - {bare}\n  - {index_variant}"

    new_text = "---\n" + new_front + "\n---\n" + rest
    fpath.write_text(new_text)
    return True


def main():
    text = MAP_FILE.read_text()
    entries = parse_tools_entries(text)
    print(f"Found {len(entries)} tools-group entries")
    for e in entries:
        new_path = DOCS / e["to"] / "index.md"
        if not new_path.exists():
            print(f"  SKIP (missing): {new_path}")
            continue
        ok = insert_redirect_from(new_path, e["old"])
        flag = "OK" if ok else "FAIL"
        print(f"  [{flag}] {new_path.relative_to(REPO)}  <-  {e['old']}")


if __name__ == "__main__":
    main()
