---
layout: default
title: "Electrical Fundamentals — Training"
description: "9 modules covering electrical quantities, circuit analysis methods, passive components, switching devices, conductor sizing, and IEC earthing systems."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Electrical Fundamentals"
redirect_from:
  - /training/fundamentals/
  - /training/fundamentals/index.html

---

<div class="page-header">
  <span class="page-header__label">Training / Electrical Fundamentals</span>
  <h1>Electrical Fundamentals</h1>
  <p>For engineers and technicians building the circuit vocabulary and analysis skills required across all controls, panel design, and machine work. Includes circuit theory, passive components, conductor sizing, and IEC earthing systems.</p>
</div>

### Recommended entry modules

- [Electrical Quantities and Circuit Language]({{ '/fundamentals/electrical/electrical-quantities/' | relative_url }}) — vocabulary and circuit topology
- [Kirchhoff's Laws and Systematic Analysis]({{ '/fundamentals/electrical/kirchhoff-laws/' | relative_url }}) — systematic analysis for real circuits
- [Conductor Ampacity and Termination Temperature]({{ '/fundamentals/electrical/conductor-ampacity/' | relative_url }}) — NEC table reading and sizing rules

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
  {% assign fundamentals = site.data.training_catalog.modules | where: "group", "fundamentals" %}
  {% for mod in fundamentals %}
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
