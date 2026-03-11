---
layout: default
title: "NEC for Machines and Panels — Training"
description: "11 modules covering NEC code reading, table navigation, motor circuit sizing, grounding and bonding, SCCR, and article-level routing for Articles 409, 430, and 725."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
---

<div class="page-header">
  <span class="page-header__label">Training / NEC for Machines and Panels</span>
  <h1>NEC for Machines and Panels</h1>
  <p>For panel designers, machine builders, and engineers applying NEC to motor circuits and industrial control panels. 11 modules covering code structure, motor sizing, grounding and bonding, SCCR, Class 1/2/3 circuits, and practical Article 430 and 409 workflows.</p>
</div>

### Recommended entry modules

- [NEC Code Reading Fundamentals]({{ '/training/nec-application/nec-code-reading/' | relative_url }}) — start here for code structure and language rules
- [Branch Circuits vs. Feeders for Motor Loads]({{ '/training/nec-application/branch-circuits-vs-feeders/' | relative_url }}) — 125% conductor rule and feeder formula
- [Grounding and Bonding for Control Panels]({{ '/training/nec-application/grounding-bonding-panels/' | relative_url }}) — EGC sizing and neutral/ground separation
- [SCCR Workflow]({{ '/training/nec-application/sccr-workflow/' | relative_url }}) — component method and NEC 409.110 marking

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
