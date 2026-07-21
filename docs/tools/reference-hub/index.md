---
layout: default
title: "Reference Models"
description: "Quick-reference architecture models and matrices derived from the canonical RAG. Use during design, selection, and review."
breadcrumb:
  - name: "Reference Models"
redirect_from:
  - /reference/
  - /reference/index.html
review:
  standard: "Reference model index"
  edition: "n/a — routing page; governing editions are recorded on the child pages"
  status: "Review pending"
  coverage: "Hub for the cross-cutting reference models; model caveats live on the model pages."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Reference Models</span>
  <h1>Reference Models</h1>
  <p>Quick-reference models and matrices derived from the canonical RAG. Not a substitute for the applicable standard.</p>
</div>

<h2>Architecture Models</h2>
<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/design/architecture/machine-architecture-model/' | relative_url }}">7-Layer Machine Architecture Model</a></h3>
    <p>Separates machine responsibilities by layer — physical process, sensors, control, safety, HMI, network, and enterprise — with applicable standards per layer.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/architecture/machine-safety-architecture/' | relative_url }}">Universal Machine Safety Architecture</a></h3>
    <p>Reusable safety system template covering E-stop chains, energy isolation, safety function design, and V&amp;V for industrial machines across industries.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/architecture/compliance-stack/' | relative_url }}">15-Standard Minimum Compliance Stack</a></h3>
    <p>Minimum compliance baseline for semiconductor equipment targeting US, EU, and Asian fab installations — five technical domains, 15 standards.</p>
  </div>
</div>

<h2>Motor Systems</h2>
<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/design/motor-selection/motor-selection-matrix/' | relative_url }}">Motor Selection Comparison Matrix</a></h3>
    <p>Decision flowchart and comparison matrix for motor-system family selection: induction, servo, BLDC, stepper, and traction platforms with application mapping.</p>
  </div>
</div>

<h2>Quick Reference</h2>
<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/tools/glossary/' | relative_url }}">Glossary</a></h3>
    <p>45 cross-linked terms across Safety, Electrical, Standards Bodies, and Regulatory domains.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/crosswalks/' | relative_url }}">Crosswalks</a></h3>
    <p>Side-by-side standard comparisons: NFPA 79 ↔ IEC 60204-1, IEC 61511 ↔ IEC 61508, IEC 60079 ↔ NEC 500/505, and more.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/software-stack/' | relative_url }}">Software Stack</a></h3>
    <p>Site technology stack, Jekyll configuration, and deployment notes.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/tools/rag-browser/' | relative_url }}">RAG File Browser</a></h3>
    <p>Browse all canonical RAG source files directly — standards, training modules, design frameworks, and commissioning checklists.</p>
  </div>
</div>

<div style="margin-top:2rem; font-size:0.9rem; color:var(--color-text-muted);">
These reference models are derived from the canonical reference library at <code>control-standards/rag/</code>. They are design aids, not authoritative standards documents. Always verify against the applicable standard and OEM documentation.
</div>
