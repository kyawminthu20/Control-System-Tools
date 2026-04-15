---
layout: default
title: "Reference — Architecture"
description: "Architecture reference models: 7-layer machine architecture, universal safety architecture, and minimum compliance stack."
breadcrumb:
  - name: "Reference Models"
    url: "/reference/"
  - name: "Architecture"
redirect_from:
  - /reference/architecture/
  - /reference/architecture/index.html
---

<div class="page-header">
  <span class="page-header__label">Reference Models</span>
  <h1>Architecture Models</h1>
</div>

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
