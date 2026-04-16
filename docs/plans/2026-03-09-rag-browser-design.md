# RAG File Browser — Design

**Date:** 2026-03-09
**Status:** Approved

## Summary

Add a RAG file browser to the Jekyll site so users can navigate and read all markdown files in `control-standards/rag/` directly from the browser. The folder tree lives in the sidebar; clicking a file renders its content in the main panel via dynamic fetch.

## Architecture

### User flow

1. User clicks "RAG Files" in the global sidebar → navigates to `/tools/rag-browser/`
2. Left sidebar shows collapsible folder tree (nested `<details>`/`<summary>`)
3. User clicks a file → JS fetches raw markdown from GitHub → `marked.js` renders → main panel updates
4. Main panel starts with placeholder: "Select a file to read"

### Data flow

```
Jekyll build
  → tools/generate_rag_tree.py walks control-standards/rag/
  → outputs docs/_data/rag_tree.json (nested folder/file structure)
  → Jekyll bakes tree into rag-browser layout as JS variable

Runtime (browser)
  → user clicks file node in tree
  → JS fetches raw.githubusercontent.com/kyawminthu20/Control-System-Tools/master/<relative-path>
  → marked.js parses and renders markdown
  → content injected into main panel div
```

## Components

### 1. `tools/generate_rag_tree.py`

- Walks `control-standards/rag/` recursively
- Skips non-`.md` files and `README.md` entries (configurable)
- Outputs `docs/_data/rag_tree.json` with shape:

```json
[
  {
    "name": "design_framework",
    "type": "dir",
    "children": [
      {
        "name": "motor_systems",
        "type": "dir",
        "children": [
          {
            "name": "motor_selection_workflow.md",
            "type": "file",
            "path": "control-standards/rag/design_framework/motor_systems/motor_selection_workflow.md"
          }
        ]
      }
    ]
  }
]
```

### 2. `docs/_layouts/rag-browser.html`

- Extends the default layout structure
- Left sidebar: renders tree from `site.data.rag_tree` as nested `<details>`/`<summary>` (pure HTML, no JS for expand/collapse)
- Embeds `rag_tree` as a JS variable for the fetch handler
- Includes `marked.js` via CDN
- Includes `rag-browser.js`
- Right context panel: unchanged (kept for consistency)

### 3. `docs/rag-browser/index.md`

```yaml
---
layout: rag-browser
title: RAG Files
---
```

- No body content — layout handles everything
- Added to global sidebar as "RAG Files" link

### 4. `docs/assets/js/rag-browser.js`

- Attaches click handlers to all file nodes in the tree
- On click:
  - Highlights active file in tree
  - Shows loading state in main panel
  - Fetches `https://raw.githubusercontent.com/kyawminthu20/Control-System-Tools/master/<path>`
  - Renders with `marked.parse(text)` into main panel
- Error state: shows fetch error message in main panel

## Dependencies

- `marked.js` — CDN (same pattern as Mermaid.js already used on site)
- No new npm packages, no build changes

## Constraints

- Repo must be public (already is — GitHub Pages is live)
- Tree data is static: re-run `generate_rag_tree.py` and rebuild site when RAG files change
- `marked.js` renders GitHub-flavored markdown; tables and code blocks render correctly

## Files Changed

| File | Action |
|------|--------|
| `tools/generate_rag_tree.py` | Create |
| `docs/_data/rag_tree.json` | Generate (via script) |
| `docs/_layouts/rag-browser.html` | Create |
| `docs/rag-browser/index.md` | Create |
| `docs/assets/js/rag-browser.js` | Create |
| `docs/_includes/sidebar.html` (or equivalent) | Edit — add RAG Files link |
