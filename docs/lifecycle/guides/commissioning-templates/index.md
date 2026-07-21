---
layout: default
title: "Commissioning Templates"
description: "Printable commissioning checklists for control panels, motor branches, drives, and circuit verification — designed for field use."
breadcrumb:
  - name: "Commissioning Templates"
redirect_from:
  - /implementation/commissioning-templates/
  - /commissioning-templates/
  - /commissioning-templates/index.html
review:
  standard: "Field verification practice — OEM instructions and the site electrical safety program govern"
  edition: "n/a — procedure-agnostic checklists"
  status: "Review pending"
  coverage: "Printable reminder-layer checklists; not a substitute for equipment-specific procedures, site LOTO, or qualified-person requirements."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Commissioning Templates</span>
  <h1>Commissioning Templates</h1>
  <p>Structured checklists for commissioning, first energization, and field verification. Each checklist is printable and links back into relevant training and workflows.</p>
</div>

<div class="workflow-card-grid">
{% for cl in site.data.field_checklists %}
  <div class="workflow-card">
    <h3><a href="{{ cl.url | relative_url }}">{{ cl.title }}</a></h3>
    <p>{{ cl.use_context }}</p>
  </div>
{% endfor %}
</div>

<div style="margin-top:2rem; font-size:0.9rem; color:var(--color-text-muted);">
These checklists are derived from the canonical reference library. They complement, but do not replace, OEM commissioning instructions, site LOTO procedures, and applicable standards.
</div>
