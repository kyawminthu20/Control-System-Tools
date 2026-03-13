---
layout: default
title: "Control Systems — Training"
description: "Modules covering control theory, PID intuition, industrial PLC implementation, loop architectures, and applied examples."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
---

<div class="page-header">
  <span class="page-header__label">Training / Control Systems</span>
  <h1>Control Systems</h1>
  <p>For engineers who work with feedback control loops, PLC PID blocks, VFDs, servo drives, or any process that must follow a setpoint. Covers control theory concepts through industrial implementation and applied design examples.</p>
</div>

### Recommended entry modules

- [Control Theory Overview]({{ '/training/control-systems/control-theory-overview/' | relative_url }}) — the full control-engineering workflow before going deep on PID
- [PID Control — Intuitive Foundation]({{ '/training/control-systems/pid-foundation/' | relative_url }}) — PID as a reading guide and concept map
- [PID Intuition — P, I, and D in Practice]({{ '/training/control-systems/pid-intuition/' | relative_url }}) — build intuition for each term without heavy math

---

<div class="training-table-wrap">
<table>
  <thead>
    <tr>
      <th>Module</th>
      <th class="hide-mobile">Level</th>
      <th class="hide-mobile">Time</th>
      <th class="hide-mobile">Type</th>
    </tr>
  </thead>
  <tbody>
  {% assign cs_modules = site.data.training_catalog.modules | where: "group", "control-systems" %}
  {% for mod in cs_modules %}
    <tr{% if mod.featured %} class="featured-row"{% endif %}>
      <td>
        <a href="{{ mod.url | relative_url }}">{{ mod.title }}</a>
        {% if mod.featured %}<span class="training-chip chip-featured">Core</span>{% endif %}
        <br><small style="color:var(--color-text-muted)">{{ mod.summary }}</small>
      </td>
      <td class="td-chips hide-mobile">
        {% if mod.level == "Beginner" %}<span class="training-chip chip-beginner">{{ mod.level }}</span>
        {% elsif mod.level == "Intermediate" %}<span class="training-chip chip-intermediate">{{ mod.level }}</span>
        {% elsif mod.level == "Advanced" %}<span class="training-chip chip-advanced">{{ mod.level }}</span>
        {% else %}<span class="training-chip">{{ mod.level }}</span>{% endif %}
      </td>
      <td class="hide-mobile">{{ mod.time }}</td>
      <td class="hide-mobile">{{ mod.type }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

---

<a href="{{ '/training/' | relative_url }}">&larr; All Training Modules</a>
