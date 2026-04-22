---
layout: default
title: "Motors, Drives, and Motion — Training"
description: "18 modules covering induction and DC motors, VFDs, servo drives, motor selection, efficiency, and equations reference."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Motors, Drives, and Motion"
redirect_from:
  - /training/electrical-machines/
  - /training/electrical-machines/index.html

---

<div class="page-header">
  <span class="page-header__label">Training / Motors, Drives, and Motion</span>
  <h1>Motors, Drives, and Motion</h1>
  <p>For controls engineers and field technicians working with motor selection, VFD commissioning, servo tuning, and drive troubleshooting. Covers induction and DC machines, drive topologies, motion control fundamentals, and deep BLDC/PMSM implementation reference.</p>
</div>

### Recommended entry modules

- [Induction Motor Basics]({{ '/fundamentals/motors/induction-motor-basics/' | relative_url }}) — rotating field, slip, and torque
- [Motor Nameplates, Slip, and Torque]({{ '/fundamentals/motors/motor-nameplates-slip-torque/' | relative_url }}) — reading nameplate data and NEMA codes
- [VFD Fundamentals]({{ '/fundamentals/motors/vfd-fundamentals/' | relative_url }}) — drive topology and commissioning parameters

---

{% assign group = site.data.training_catalog.topic_groups | where: "key", "electrical-machines" | first %}
{% assign group_modules = site.data.training_catalog.modules | where: "group", "electrical-machines" %}

{% for bucket in group.sidebar_buckets %}
  {% assign bucket_modules = group_modules | where: "sidebar_bucket", bucket %}
  {% if bucket_modules.size == 0 %}{% continue %}{% endif %}

## {{ bucket }}

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
  {% for mod in bucket_modules %}
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

{% endfor %}

---

<a href="{{ '/training/' | relative_url }}">&larr; All Training Modules</a>
