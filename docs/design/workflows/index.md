---
layout: default
title: Engineering Workflows
description: Structured workflows for motor selection, drive commissioning, troubleshooting, and electrical review.
redirect_from:
  - /workflows/
  - /workflows/index.html
review:
  standard: "Workflow index"
  edition: "n/a — routing page; governing editions are recorded on the child pages"
  status: "Review pending"
  coverage: "Section hub for design workflows."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <h1>Engineering Workflows</h1>
  <p class="page-subtitle">Task-oriented guides for motor selection, drive commissioning, troubleshooting, and electrical design review. Each workflow is a structured first-pass tool — not a substitute for OEM procedures or the applicable standard.</p>
</div>

<div class="content-note" style="margin-bottom: 2rem;">
  <strong>Source:</strong> All workflows are derived from the canonical RAG design framework layer. They reflect engineering practice patterns, not code requirements. For code compliance, use the linked standards references.
</div>

## Motor Systems

<div class="workflow-card-grid">

  <div class="workflow-card">
    <div class="workflow-card-header">
      <span class="workflow-badge motor">Motor Systems</span>
      <h3><a href="{{ '/design/workflows/motor-selection/' | relative_url }}">Motor Selection Workflow</a></h3>
    </div>
    <p>First-pass motor selection from load definition through protection and integration review. Covers supply architecture, environment, nameplate, and drive compatibility.</p>
    <div class="workflow-meta">
      <span class="wf-tag">Selection</span>
      <span class="wf-tag">Design</span>
    </div>
  </div>

  <div class="workflow-card">
    <div class="workflow-card-header">
      <span class="workflow-badge motor">Motor Systems</span>
      <h3><a href="{{ '/tools/troubleshooting/motors/' | relative_url }}">Motor Troubleshooting Decision Tree</a></h3>
    </div>
    <p>Systematic first-pass routing for motor and drive faults: no-start, overcurrent, overheating, wrong speed, and servo instability. Routes the review before OEM diagnostics.</p>
    <div class="workflow-meta">
      <span class="wf-tag">Troubleshooting</span>
      <span class="wf-tag">Field</span>
    </div>
  </div>

  <div class="workflow-card">
    <div class="workflow-card-header">
      <span class="workflow-badge drive">Drive Systems</span>
      <h3><a href="{{ '/lifecycle/guides/vfd-commissioning/' | relative_url }}">VFD Commissioning Workflow</a></h3>
    </div>
    <p>Structured first energization and functional check sequence for VFD-driven motor systems. Covers pre-power electrical verification through load review and evidence retention.</p>
    <div class="workflow-meta">
      <span class="wf-tag">Commissioning</span>
      <span class="wf-tag">VFD</span>
    </div>
  </div>

  <div class="workflow-card">
    <div class="workflow-card-header">
      <span class="workflow-badge drive">Drive Systems</span>
      <h3><a href="{{ '/lifecycle/guides/servo-commissioning/' | relative_url }}">Servo Commissioning Workflow</a></h3>
    </div>
    <p>Staged commissioning sequence for servo axes — from axis readiness and feedback verification through controlled enable, tuning, and functional motion review.</p>
    <div class="workflow-meta">
      <span class="wf-tag">Commissioning</span>
      <span class="wf-tag">Servo</span>
    </div>
  </div>

</div>

## Electrical Review

<div class="workflow-card-grid">

  <div class="workflow-card">
    <div class="workflow-card-header">
      <span class="workflow-badge electrical">Electrical</span>
      <h3><a href="{{ '/design/workflows/electrical-review/' | relative_url }}">Electrical Review Workflow</a></h3>
    </div>
    <p>Fast design-review and bench-troubleshooting workflows for resistive circuits: Ohm's law checks, network topology, voltage divider loading, power margin, and component sanity.</p>
    <div class="workflow-meta">
      <span class="wf-tag">Design Review</span>
      <span class="wf-tag">Calculations</span>
    </div>
  </div>

</div>

---

## Related site sections

| Section | Relationship |
|---|---|
| [Training](/fundamentals/) | Concept-level background for these workflows |
| [Standards](/standards/) | Code requirements that govern workflow outcomes |
| [Lifecycle](/lifecycle/) | Stage-oriented engineering process context |
| [Scenarios](/tools/scenarios/) | Applied project examples using these workflows |
