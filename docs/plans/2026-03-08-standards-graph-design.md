# Standards Graph — Design Document

**Date:** 2026-03-08
**Status:** Approved
**Phase:** Phase 9

## Overview

An interactive, navigable standards relationship graph built with Cytoscape.js (CDN). Data-driven from a single YAML file — adding a new standard requires one node entry, no JS changes. Deployed in two sizes: a mini version on the homepage replacing the static Mermaid block, and a full dedicated page at `/standards/graph/`.

## Goals

- Show how standards relate to each other with labeled, typed edges
- Allow click-to-navigate to any standard's site page
- Auto-include new standards as pages are added (data-driven)
- No build step, no framework — vanilla JS + CDN only

## Architecture

### Data source

`docs/_data/standards_graph.yml` — single source of truth for all nodes and edges.

```yaml
nodes:
  - id: nec
    label: "NEC (NFPA 70)"
    family: us-electrical
    url: /standards/us-electrical/nec/
  ...

edges:
  - source: nfpa79
    target: nec
    type: enforces
    label: "enforced via Art. 670"
  ...
```

Jekyll inlines this as JSON into `<script>` tags at build time using Liquid. No runtime data fetch required.

### Edge types

| Type | Color | Semantic meaning |
|------|-------|-----------------|
| `requires` | amber `#f59e0b` | Upstream dependency — must satisfy this standard first |
| `pairs-with` | blue `#3b82f6` | Same scope — use one or both together |
| `enforces` | green `#10b981` | Enforcement vehicle — one standard is enforced through another |
| `aligns-with` | gray `#6b7280` | Harmonized or equivalent international/US counterparts |

### Components

| File | Purpose |
|------|---------|
| `docs/_data/standards_graph.yml` | Graph node + edge data |
| `docs/_includes/standards-graph.html` | Cytoscape container + init script, parameterized (`mini` vs `full` mode) |
| `docs/standards/graph/index.md` | Full dedicated page |
| `docs/assets/js/main.js` | Graph init code (appended) |
| `docs/assets/css/main.css` | Graph container + legend styles (appended) |
| `docs/index.md` | Replace static Mermaid relationship block with mini graph |

### Full page (`/standards/graph/`)

- Cytoscape.js force-directed layout (cola or cose)
- Zoom and pan enabled
- Click node → navigate to standard page
- Hover node → highlight connected edges, dim others
- Hover edge → show tooltip with relationship label
- Legend: color key for 4 edge types
- Layout toggle button: force-directed ↔ breadthfirst (hierarchical)

### Mini version (homepage)

- Fixed preset layout (no force simulation — positions hard-coded in YAML)
- Smaller container (300px height)
- Zoom/pan disabled
- Click still navigates
- "View full graph →" link below

## Library

**Cytoscape.js** via CDN (`cdnjs.cloudflare.com`). No additional plugins required for core functionality. Optional: `cytoscape-cola` layout plugin for better force-directed layout on the full page.

## Initial Node Set (~15 standards)

NEC, NFPA 79, UL 508A, IEC 60204-1, ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511, IEC 62443, IEC 60079 (planned), SEMI S2 (planned). Nodes without site pages yet rendered as dimmed/dashed outline.

## Out of Scope

- Server-side graph processing
- Graph editing UI
- Export to image/PDF
- Filtering by family or lifecycle stage (future enhancement)
