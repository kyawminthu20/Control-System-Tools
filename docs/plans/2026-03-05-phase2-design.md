# Phase 2 Design — Control System Standards Atlas

**Date:** 2026-03-05
**Status:** Approved

## Overview

Phase 2 adds interactivity and discoverability to the Phase 1 Jekyll site. Split into two releases with a clean boundary between CSS/minimal-JS work and JS-heavy features.

---

## Release 1: Print Stylesheet + Diagram Lightbox

### Print Stylesheet

- `@media print` block added to `docs/assets/css/main.css`
- Hides: topnav, sidebar, context panel, mobile toggle, skip link, trust boundary footer
- Main content expands to full width
- Appends URL text after links: `a[href]:after { content: " (" attr(href) ")" }`
- Mermaid diagrams render as SVG and print natively — no special handling required
- No new files; purely additive to `main.css`

### Diagram Lightbox

- `docs/assets/js/main.js` wraps each `.mermaid` element in a clickable container after Mermaid renders
- On click: clones the rendered SVG into a full-screen overlay `<div class="lightbox-overlay">`
- Closes on: click outside the diagram, or `Escape` key
- Overlay styles added to `main.css`
- No library required — approximately 30 lines of JS total
- No new files

---

## Release 2: Search + Crosswalk Comparison Selector

### Search (lunr.js inline dropdown)

**Data layer:**
- New file: `docs/assets/data/search.json` — Liquid template rendered by Jekyll at build time
- Iterates all pages, outputs: `title`, `url`, `content` (truncated to ~200 chars), `tags` from front matter

**Client side:**
- lunr.js loaded from CDN — added to `docs/_layouts/default.html`
- On page load: fetch `search.json`, build lunr index
- Existing topnav `<input>` gets a `keyup` handler in `main.js`
- Queries lunr index on each keystroke, renders up to 8 results in a `<div class="search-dropdown">` below the input
- Each result shows: page title + section label (e.g., "Standards / NFPA 79")
- Keyboard navigation: arrow keys move selection, `Enter` follows link, `Escape` closes dropdown
- Click outside closes dropdown
- Styles added to `main.css`

### Crosswalk Comparison Selector

**New page:** `docs/tools/crosswalks/compare/index.md`

**UI:**
- Two `<select>` dropdowns listing all 9 standards (NEC, NFPA 79, UL 508A, IEC 60204-1, ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511)
- When both are selected, vanilla JS shows the matching overlap table
- If no comparison data exists for the selected pair: shows "No comparison data available for this pair" with links to individual standard pages
- When a match is found: shows the table and links to the full crosswalk page

**Data:**
- The 3 existing crosswalk tables (NFPA 79 / IEC 60204-1, UL 508A / NEC / NFPA 79, Standards Decision Workflow) embedded as hidden `<div data-pair="...">` blocks in the compare page
- No separate data files; no new dependencies beyond lunr.js (already added for search)

---

## Files Affected

| File | Release | Change |
|------|---------|--------|
| `docs/assets/css/main.css` | 1 + 2 | Add print styles, lightbox styles, search dropdown styles |
| `docs/assets/js/main.js` | 1 + 2 | Add lightbox logic, search logic |
| `docs/_layouts/default.html` | 2 | Add lunr.js CDN script tag |
| `docs/assets/data/search.json` | 2 | New — Jekyll Liquid search index |
| `docs/tools/crosswalks/compare/index.md` | 2 | New — comparison selector page |

---

## Constraints

- Vanilla JS only — no framework, no build step
- No new Jekyll plugins
- All new dependencies via CDN only (lunr.js)
- GitHub Pages compatible (custom Actions build already in place)
- Each release is independently shippable
