---
layout: default
title: "NEC for Machines and Panels — Training"
description: "3 modules covering NEC code reading method, table navigation discipline, and article routing for motors and industrial control panels."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
---

<div class="page-header">
  <span class="page-header__label">Training / NEC for Machines and Panels</span>
  <h1>NEC for Machines and Panels</h1>
  <p>For panel designers, machine builders, and engineers applying NEC to motor circuits and industrial control panels. Covers code structure, table navigation, and article-level routing for Articles 110, 409, 430, and 725. More NEC modules are planned for Phase 16.</p>
</div>

### Recommended entry modules

- [NEC Code Reading Fundamentals]({{ '/training/nec-application/nec-code-reading/' | relative_url }}) — start here for code structure and language rules
- [Motor and Panel Code Application]({{ '/training/nec-application/motor-panel-code-application/' | relative_url }}) — Art 430, Art 409 SCCR, Art 725 control circuits

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
  {% assign nec = site.data.training_catalog.modules | where: "group", "nec-application" %}
  {% for mod in nec %}
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
