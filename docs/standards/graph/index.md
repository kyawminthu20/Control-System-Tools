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

<p>Click any standard to open its reference page. Hover a node to highlight its connections. Hover an edge to see the relationship label. Dashed styling is reserved for planned coverage when present.</p>

{% include standards-graph.html mode="full" container_id="standards-graph-full" %}

---

<a href="{{ '/standards/' | relative_url }}" class="card__link">&larr; Standards explorer</a>
