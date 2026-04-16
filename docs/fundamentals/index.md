---
layout: default
title: "Fundamentals"
description: "Foundational modules on electrical theory, control theory, and motor/drive systems — the prerequisite layer before design, implementation, and verification references."
breadcrumb:
  - name: "Fundamentals"
---

<div class="page-header">
  <span class="page-header__label">Fundamentals</span>
  <h1>Fundamentals</h1>
  <p>Foundational modules across electrical theory, control theory, and motor and drive systems. Each sub-group is independently navigable and the modules are short, outcome-focused, and cross-linked into design, implementation, and verification references.</p>
</div>

<blockquote>
<strong>Scope:</strong> Prerequisite concepts before doing design work or field engineering. For applied workflows see <a href="{{ '/design/' | relative_url }}">Design</a>, <a href="{{ '/implementation/scenarios/' | relative_url }}">Implementation</a>, and <a href="{{ '/verification/lifecycle/' | relative_url }}">Verification</a>.
</blockquote>

## Sub-groups

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/electrical/' | relative_url }}">Electrical Fundamentals</a></h3>
    <p>Electrical quantities, Kirchhoff's laws, series/parallel circuits, equivalent-circuit methods, passive components, diodes and transistors, conductor ampacity, IEC earthing systems.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/control/' | relative_url }}">Control Systems</a></h3>
    <p>Control theory overview, PID foundation/intuition/industrial, control loop architectures, machine state model, interlocks and permissives, multi-axis coordination, async faults in distributed systems, servo tuning, vibration and resonance, deterministic vs non-deterministic control.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/fundamentals/motors/' | relative_url }}">Motors and Drives</a></h3>
    <p>AC vs DC motors, induction motor basics, DC motor basics, BLDC/EV/drone motors, motor nameplates/slip/torque, motor control methods, motor-VFD equations, motor family comparison, VFD fundamentals, servo drive fundamentals, servo feedback/inertia, VFD/servo architecture, motor efficiency and losses.</p>
  </div>
</div>

## Related Sections

- [Design]({{ '/design/' | relative_url }}) — apply fundamentals to architecture, motor selection, and design workflows
- [Implementation]({{ '/implementation/' | relative_url }}) — commissioning templates and scenario references that use these concepts during build and install
- [Verification]({{ '/verification/' | relative_url }}) — lifecycle stages, risk assessment, and safety architecture that build on safety-relevant fundamentals
- [Tools]({{ '/tools/reference-hub/' | relative_url }}) — glossary, crosswalks, RAG browser
