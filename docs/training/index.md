---
layout: default
title: "Training Modules"
description: "Curriculum for controls engineers, panel designers, and field service technicians — 24 modules covering electrical fundamentals, motors and drives, and NEC application."
breadcrumb:
  - name: "Training"
---

<div class="page-header">
  <span class="page-header__label">Training</span>
  <h1>Training Modules</h1>
  <p>A practical curriculum for controls engineers, panel designers, and field service technicians. 24 modules organized into three tracks — from circuit fundamentals to motor drives to NEC code application.</p>
</div>

<div class="training-verification">
  <strong>Before you start:</strong> {{ site.data.training_catalog.verification_note }}
</div>

---

## Start Here

Choose the entry point that fits your current work:

<div class="start-here-grid">
{% for entry in site.data.training_catalog.start_here %}
  <div class="start-here-card">
    <h4>{{ entry.audience }}</h4>
    <p>{{ entry.description }}</p>
    <ul>
    {% for mod in entry.entry_modules %}
      <li><a href="{{ mod.url | relative_url }}">{{ mod.title }}</a></li>
    {% endfor %}
    </ul>
  </div>
{% endfor %}
</div>

---

## Learning Paths

Structured sequences built from the existing module inventory:

<div class="learning-paths-grid">
{% for path in site.data.training_catalog.learning_paths %}
  <div class="learning-path-card">
    <h4>{{ path.name }}</h4>
    <p>{{ path.description }}</p>
  </div>
{% endfor %}
</div>

---

## Browse by Topic

<div class="card-grid">
{% for group in site.data.training_catalog.topic_groups %}
  <div class="card">
    <div class="topic-group-label">{{ group.module_count }} modules</div>
    <h3>{{ group.label }}</h3>
    <p>{{ group.description }}</p>
    <a href="{{ group.url | relative_url }}">Browse {{ group.label }} &rarr;</a>
  </div>
{% endfor %}
</div>

---

## All Modules

<div class="training-table-wrap">
<table>
  <thead>
    <tr>
      <th>Module</th>
      <th class="hide-mobile">Track</th>
      <th class="hide-mobile">Level</th>
      <th class="hide-mobile">Time</th>
      <th class="hide-mobile">Type</th>
    </tr>
  </thead>
  <tbody>
  {% for mod in site.data.training_catalog.modules %}
    <tr{% if mod.featured %} class="featured-row"{% endif %}>
      <td>
        <a href="{{ mod.url | relative_url }}">{{ mod.title }}</a>
        {% if mod.featured %}<span class="training-chip chip-featured">Core</span>{% endif %}
        <br><small style="color:var(--color-text-muted)">{{ mod.summary }}</small>
      </td>
      <td class="hide-mobile">{{ mod.group_label }}</td>
      <td class="td-chips hide-mobile">
        {% if mod.level == "Beginner" %}<span class="training-chip chip-beginner">{{ mod.level }}</span>
        {% elsif mod.level == "Intermediate" %}<span class="training-chip chip-intermediate">{{ mod.level }}</span>
        {% elsif mod.level == "Advanced" %}<span class="training-chip chip-advanced">{{ mod.level }}</span>
        {% else %}<span class="training-chip chip-concept">{{ mod.level }}</span>{% endif %}
      </td>
      <td class="hide-mobile">{{ mod.time }}</td>
      <td class="hide-mobile">{{ mod.type }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

---

## Related Standards

These modules connect directly to the following standards. Follow the links to read article-level detail, crosswalks, and lifecycle context.

<ul class="related-standards-list">
{% for std in site.data.training_catalog.related_standards %}
  <li>
    <a href="{{ std.url | relative_url }}">{{ std.title }}</a>
    <span>{{ std.relevance }}</span>
  </li>
{% endfor %}
</ul>

---

{% include trust-boundary.html %}
