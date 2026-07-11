# Phase 9: Interactive Standards Graph — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an interactive, navigable standards relationship graph using Cytoscape.js — a mini version on the homepage replacing the static Mermaid block, and a full dedicated page at `/standards/graph/`.

**Architecture:** Graph data stored in `docs/_data/standards_graph.yml` (Jekyll inlines as JSON). A reusable `_includes/standards-graph.html` renders the Cytoscape container, parameterized for `mini` vs `full` mode. Vanilla JS only — no build step.

**Tech Stack:** Jekyll 4.3, Cytoscape.js 3.28.1 (CDN), vanilla JS, CSS custom properties already in `main.css`.

---

### Task 1: Create graph data file

**Files:**
- Create: `docs/_data/standards_graph.yml`

**Step 1: Create the file**

Write the following to `docs/_data/standards_graph.yml`:

```yaml
# Standards relationship graph data
# nodes: id, label, family, url, x/y (for mini preset layout)
# edges: source, target, type (requires|pairs-with|enforces|aligns-with), label

nodes:
  - id: nec
    label: "NEC"
    family: us-electrical
    url: "/Control-System-Tools/standards/us-electrical/nec/"
    x: 400
    y: 320

  - id: nfpa79
    label: "NFPA 79"
    family: us-electrical
    url: "/Control-System-Tools/standards/us-electrical/nfpa-79/"
    x: 250
    y: 220

  - id: ul508a
    label: "UL 508A"
    family: us-electrical
    url: "/Control-System-Tools/standards/us-electrical/ul-508a/"
    x: 400
    y: 220

  - id: iec60204
    label: "IEC 60204-1"
    family: machinery
    url: "/Control-System-Tools/standards/machinery/iec-60204-1/"
    x: 250
    y: 120

  - id: iso12100
    label: "ISO 12100"
    family: functional-safety
    url: "/Control-System-Tools/standards/functional-safety/iso-12100/"
    x: 100
    y: 60

  - id: iso138491
    label: "ISO 13849-1"
    family: functional-safety
    url: "/Control-System-Tools/standards/functional-safety/iso-13849-1/"
    x: 100
    y: 180

  - id: iec62061
    label: "IEC 62061"
    family: functional-safety
    url: "/Control-System-Tools/standards/functional-safety/iec-62061/"
    x: 250
    y: 60

  - id: iec61508
    label: "IEC 61508"
    family: functional-safety
    url: "/Control-System-Tools/standards/functional-safety/iec-61508/"
    x: 100
    y: 300

  - id: iec61511
    label: "IEC 61511"
    family: functional-safety
    url: "/Control-System-Tools/standards/functional-safety/iec-61511/"
    x: 250
    y: 340

  - id: iec62443
    label: "IEC 62443"
    family: cybersecurity
    url: "/Control-System-Tools/standards/cybersecurity/iec-62443/"
    x: 550
    y: 120

  - id: iec60079
    label: "IEC 60079"
    family: hazardous-area
    url: "/Control-System-Tools/standards/hazardous-area/iec-60079/"
    planned: true
    x: 550
    y: 320

  - id: semi
    label: "SEMI S2/S8/S14"
    family: semiconductor
    url: "/Control-System-Tools/standards/semiconductor/semi/"
    planned: true
    x: 550
    y: 220

edges:
  - source: nfpa79
    target: nec
    type: enforces
    label: "enforced via Art. 670"

  - source: ul508a
    target: nec
    type: enforces
    label: "SCCR per Art. 409"

  - source: nfpa79
    target: iec60204
    type: aligns-with
    label: "US/international equivalent"

  - source: ul508a
    target: nfpa79
    type: pairs-with
    label: "panel + machine wiring"

  - source: iso138491
    target: iso12100
    type: requires
    label: "requires risk assessment"

  - source: iec62061
    target: iso12100
    type: requires
    label: "requires risk assessment"

  - source: iec60204
    target: iso12100
    type: requires
    label: "requires risk assessment"

  - source: iso138491
    target: iec62061
    type: pairs-with
    label: "machinery SRP/CS: choose one"

  - source: iec61511
    target: iec61508
    type: requires
    label: "derives from IEC 61508"

  - source: iec62061
    target: iec61508
    type: requires
    label: "derives from IEC 61508"

  - source: iec62443
    target: iec62061
    type: pairs-with
    label: "safety + security pairing"

  - source: iec62443
    target: iec61511
    type: pairs-with
    label: "SIS security coordination"

  - source: iec60079
    target: nec
    type: aligns-with
    label: "Zone system via Art. 505"

  - source: semi
    target: iec60204
    type: aligns-with
    label: "semiconductor equipment"
```

**Step 2: Verify**

```bash
cd "docs" && python3 -c "import yaml; yaml.safe_load(open('_data/standards_graph.yml'))" && echo "YAML valid"
```
Expected: `YAML valid`

**Step 3: Commit**

```bash
git add docs/_data/standards_graph.yml
git commit -m "feat(graph): add standards_graph.yml data file (12 nodes, 14 edges)"
```

---

### Task 2: Create the reusable Cytoscape include

**Files:**
- Create: `docs/_includes/standards-graph.html`

**Step 1: Create the include**

Write the following to `docs/_includes/standards-graph.html`:

```html
{% assign graph_mode = include.mode | default: "full" %}
{% assign container_id = include.container_id | default: "standards-graph" %}

<div class="standards-graph-wrap standards-graph-wrap--{{ graph_mode }}" id="{{ container_id }}-wrap">
  <div id="{{ container_id }}" class="standards-graph-canvas"></div>
  {% if graph_mode == "mini" %}
  <p class="standards-graph-link">
    <a href="{{ '/standards/graph/' | relative_url }}">View full interactive graph &rarr;</a>
  </p>
  {% else %}
  <div class="standards-graph-legend">
    <span class="legend-item legend-item--requires">requires</span>
    <span class="legend-item legend-item--pairs-with">pairs&nbsp;with</span>
    <span class="legend-item legend-item--enforces">enforces</span>
    <span class="legend-item legend-item--aligns-with">aligns&nbsp;with</span>
    <span class="legend-item legend-item--planned">planned</span>
  </div>
  {% endif %}
</div>

<script>
(function() {
  var GRAPH_DATA = {{ site.data.standards_graph | jsonify }};
  var MODE = "{{ graph_mode }}";
  var CONTAINER_ID = "{{ container_id }}";

  var FAMILY_COLORS = {
    "us-electrical": "#3b82f6",
    "machinery":     "#f97316",
    "functional-safety": "#10b981",
    "cybersecurity": "#ef4444",
    "hazardous-area": "#eab308",
    "semiconductor": "#a855f7"
  };

  var EDGE_COLORS = {
    "requires":    "#f59e0b",
    "pairs-with":  "#3b82f6",
    "enforces":    "#10b981",
    "aligns-with": "#9ca3af"
  };

  function buildElements() {
    var els = [];
    GRAPH_DATA.nodes.forEach(function(n) {
      var el = {
        data: {
          id: n.id,
          label: n.label,
          family: n.family,
          url: n.url,
          planned: n.planned || false
        }
      };
      if (MODE === "mini" && n.x !== undefined) {
        el.position = { x: n.x * 0.9, y: n.y * 0.9 };
      }
      els.push(el);
    });
    GRAPH_DATA.edges.forEach(function(e) {
      els.push({
        data: {
          source: e.source,
          target: e.target,
          type: e.type,
          label: e.label
        }
      });
    });
    return els;
  }

  function buildStyle() {
    return [
      {
        selector: "node",
        style: {
          "label": "data(label)",
          "font-size": MODE === "mini" ? 9 : 11,
          "font-family": "system-ui, sans-serif",
          "text-valign": "center",
          "text-halign": "center",
          "text-wrap": "wrap",
          "text-max-width": 70,
          "width": MODE === "mini" ? 60 : 80,
          "height": MODE === "mini" ? 28 : 34,
          "shape": "roundrectangle",
          "background-color": function(ele) {
            return FAMILY_COLORS[ele.data("family")] || "#6b7280";
          },
          "border-width": function(ele) { return ele.data("planned") ? 2 : 0; },
          "border-style": function(ele) { return ele.data("planned") ? "dashed" : "solid"; },
          "border-color": "#ffffff",
          "color": "#ffffff",
          "opacity": function(ele) { return ele.data("planned") ? 0.55 : 1; },
          "cursor": "pointer"
        }
      },
      {
        selector: "edge",
        style: {
          "line-color": function(ele) { return EDGE_COLORS[ele.data("type")] || "#9ca3af"; },
          "target-arrow-color": function(ele) { return EDGE_COLORS[ele.data("type")] || "#9ca3af"; },
          "target-arrow-shape": "triangle",
          "arrow-scale": 0.8,
          "curve-style": "bezier",
          "width": 1.5,
          "opacity": 0.7
        }
      },
      {
        selector: "node:selected, node.highlighted",
        style: { "border-width": 3, "border-color": "#ffffff", "opacity": 1 }
      },
      {
        selector: "edge.faded",
        style: { "opacity": 0.1 }
      }
    ];
  }

  function initGraph() {
    if (typeof cytoscape === "undefined") { return; }

    var cy = cytoscape({
      container: document.getElementById(CONTAINER_ID),
      elements: buildElements(),
      style: buildStyle(),
      layout: MODE === "mini"
        ? { name: "preset" }
        : { name: "cose", animate: false, padding: 40, nodeRepulsion: 8000, idealEdgeLength: 100 },
      userZoomingEnabled: MODE !== "mini",
      userPanningEnabled: MODE !== "mini",
      boxSelectionEnabled: false
    });

    // Click to navigate
    cy.on("tap", "node", function(evt) {
      var url = evt.target.data("url");
      if (url && !evt.target.data("planned")) {
        window.location.href = url;
      }
    });

    // Hover: highlight connected edges
    if (MODE === "full") {
      cy.on("mouseover", "node", function(evt) {
        var node = evt.target;
        cy.edges().addClass("faded");
        node.connectedEdges().removeClass("faded");
      });
      cy.on("mouseout", "node", function() {
        cy.edges().removeClass("faded");
      });

      // Edge tooltip
      var tooltip = document.createElement("div");
      tooltip.className = "graph-tooltip";
      tooltip.style.cssText = "display:none;position:fixed;background:var(--color-bg-card);border:1px solid var(--color-border);padding:4px 8px;border-radius:4px;font-size:0.75rem;pointer-events:none;z-index:9999;";
      document.body.appendChild(tooltip);

      cy.on("mouseover", "edge", function(evt) {
        tooltip.textContent = evt.target.data("label");
        tooltip.style.display = "block";
      });
      cy.on("mousemove", "edge", function(evt) {
        tooltip.style.left = (evt.originalEvent.clientX + 10) + "px";
        tooltip.style.top  = (evt.originalEvent.clientY + 10) + "px";
      });
      cy.on("mouseout", "edge", function() {
        tooltip.style.display = "none";
      });
    }
  }

  // Wait for Cytoscape to load
  if (typeof cytoscape !== "undefined") {
    initGraph();
  } else {
    document.addEventListener("DOMContentLoaded", initGraph);
  }
})();
</script>
```

**Step 2: Verify Jekyll builds**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
```
Expected: `done in X seconds.` with no errors.

**Step 3: Commit**

```bash
git add docs/_includes/standards-graph.html
git commit -m "feat(graph): add reusable standards-graph.html include (Cytoscape.js)"
```

---

### Task 3: Add CSS styles

**Files:**
- Modify: `docs/assets/css/main.css` (append at end)

**Step 1: Append to `docs/assets/css/main.css`**

```css
/* ============================================================
   Standards Relationship Graph
   ============================================================ */

.standards-graph-wrap {
  margin: 1.5rem 0;
}

.standards-graph-canvas {
  width: 100%;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 6px;
}

.standards-graph-wrap--full .standards-graph-canvas {
  height: 520px;
}

.standards-graph-wrap--mini .standards-graph-canvas {
  height: 280px;
  pointer-events: none; /* disable pan/zoom on mini */
}

.standards-graph-wrap--mini .standards-graph-canvas node {
  cursor: default;
}

.standards-graph-link {
  text-align: right;
  font-size: 0.8rem;
  margin: 0.4rem 0 0;
}

/* Legend */
.standards-graph-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.75rem;
  font-size: 0.75rem;
}

.legend-item {
  padding: 2px 8px;
  border-radius: 3px;
  color: #fff;
  font-weight: 500;
}

.legend-item--requires    { background: #f59e0b; }
.legend-item--pairs-with  { background: #3b82f6; }
.legend-item--enforces    { background: #10b981; }
.legend-item--aligns-with { background: #9ca3af; }
.legend-item--planned     { background: transparent; border: 2px dashed #9ca3af; color: var(--color-text-muted); }
```

**Step 2: Verify build**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
```

**Step 3: Commit**

```bash
git add docs/assets/css/main.css
git commit -m "feat(graph): add graph canvas, legend CSS"
```

---

### Task 4: Add Cytoscape.js CDN to default layout

**Files:**
- Modify: `docs/_layouts/default.html`

**Step 1: Read the file and find the closing `</body>` tag**

Open `docs/_layouts/default.html` and find the line with the lunr.js CDN script. Add the Cytoscape CDN **before** it:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.28.1/cytoscape.min.js" crossorigin="anonymous"></script>
```

It should appear before the existing `<script src=".../lunr.min.js"...>` line.

**Step 2: Verify build**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
```

**Step 3: Commit**

```bash
git add docs/_layouts/default.html
git commit -m "feat(graph): add Cytoscape.js 3.28.1 CDN to default layout"
```

---

### Task 5: Create the full graph page

**Files:**
- Create: `docs/standards/graph/index.md`

**Step 1: Create the file**

```markdown
---
layout: default
title: "Standards Relationship Graph"
description: "Interactive map of how industrial automation standards relate, depend on, and enforce each other."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Graph"
---

<div class="page-header">
  <span class="page-header__label">Standards Explorer</span>
  <h1>Standards Relationship Graph</h1>
</div>

<p>Click any standard to open its reference page. Hover a node to highlight its connections. Hover an edge to see the relationship label. Dashed nodes are planned (not yet in corpus).</p>

{% include standards-graph.html mode="full" container_id="standards-graph-full" %}

---

<a href="{{ '/standards/' | relative_url }}" class="card__link">&larr; Standards explorer</a>
```

**Step 2: Add graph page link to sidebar**

Open `docs/_includes/sidebar.html`. Find the Standards section and add a "Relationship Graph" link. Look for the `Standards Explorer` nav section and add:

```html
<li><a href="{{ '/standards/graph/' | relative_url }}" {% if page.url contains '/standards/graph/' %}class="active"{% endif %}>Relationship Graph</a></li>
```

**Step 3: Verify build — confirm page count increases by 1**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | grep "pages"
```

**Step 4: Commit**

```bash
git add docs/standards/graph/index.md docs/_includes/sidebar.html
git commit -m "feat(graph): add /standards/graph/ full interactive page"
```

---

### Task 6: Replace homepage Mermaid block with mini graph

**Files:**
- Modify: `docs/index.md`

**Step 1: Find and replace the Mermaid block**

In `docs/index.md`, find the entire `## Standards Relationship Graph` section (from the `## Standards Relationship Graph` heading through the closing `</div>` and the source `<p>` tag that follows). Replace it with:

```markdown
## Standards Relationship Graph

<span class="section-label">How standards reference and depend on each other</span>

{% include standards-graph.html mode="mini" container_id="standards-graph-home" %}
```

(Remove the old `<div class="mermaid-wrap">...</div>` block and both `<p style="...">Source:...</p>` lines around it.)

**Step 2: Verify build**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
```

**Step 3: Commit**

```bash
git add docs/index.md
git commit -m "feat(graph): replace homepage Mermaid block with mini Cytoscape graph"
```

---

### Task 7: Update project state and push

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

**Step 1: Update project_state.md**

Add Phase 9 as COMPLETE after Phase 8:

```markdown
## Phase 9 Scope — Interactive Standards Graph — COMPLETE

- [x] `docs/_data/standards_graph.yml` — 12 nodes, 14 edges
- [x] `docs/_includes/standards-graph.html` — Cytoscape.js include (mini + full modes)
- [x] `docs/standards/graph/index.md` — full interactive page
- [x] `docs/index.md` — mini graph replaces static Mermaid block
- [x] CSS legend and canvas styles
- [x] Cytoscape.js 3.28.1 CDN added to default layout
```

**Step 2: Add change_log.md entry**

```markdown
### 2026-03-08 — Phase 9 Complete: Interactive Standards Graph

- Added `docs/_data/standards_graph.yml` — 12 nodes (4 families), 14 edges (4 types)
- Added `docs/_includes/standards-graph.html` — Cytoscape.js, parameterized mini/full
- Added `/standards/graph/` full page with zoom, pan, hover highlights, edge tooltips
- Homepage Mermaid block replaced with mini Cytoscape graph (preset layout, click-navigable)
- Edge types: requires (amber), pairs-with (blue), enforces (green), aligns-with (gray)
- Planned nodes (IEC 60079, SEMI) shown as dashed/dimmed — auto-activate when corpus added
```

**Step 3: Final build + push**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
cd "." && git add project_state/ && git commit -m "chore(state): mark Phase 9 complete — interactive standards graph" && git push
```
