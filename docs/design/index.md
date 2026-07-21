---
layout: default
title: "Engineering Workflow"
description: "Workflow-first navigation for machine and panel design: lifecycle stages, engineering workflows, commissioning templates, and scenarios."
breadcrumb:
  - name: "Engineering Workflow"
redirect_from:
  - /engineering-workflow/
  - /engineering-workflow/index.html
review:
  standard: "Design section index"
  edition: "n/a — routing page; governing editions are recorded on the child pages"
  status: "Review pending"
  coverage: "Section landing page; routes to wiring, architecture, motor selection, software stack, AI integration, and workflows."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Engineering Workflow</span>
  <h1>Engineering Workflow</h1>
  <p>Navigate from concept through commissioning by engineering task. Lifecycle stages provide structured progression; workflows guide decision points; commissioning templates support field verification.</p>
</div>

<div class="section-guide">
  <div class="section-guide__row">
    <span class="section-guide__label">Use this when</span>
    <p>You are designing or reviewing wiring, panel and machine architecture, motor selection, the software stack, or AI/ML integration.</p>
  </div>
  <div class="section-guide__row">
    <span class="section-guide__label">Start here</span>
    <p><a href="{{ '/design/wiring/' | relative_url }}">Wiring &amp; Installation</a> for point-to-point design work; <a href="{{ '/design/architecture/' | relative_url }}">Architecture</a> when you are structuring the whole system.</p>
  </div>
  <div class="section-guide__row">
    <span class="section-guide__label">Next step</span>
    <p>Run the <a href="{{ '/design/workflows/electrical-review/' | relative_url }}">Electrical Review workflow</a> before release to build, then continue at the <a href="{{ '/lifecycle/build/' | relative_url }}">Build lifecycle stage</a>.</p>
  </div>
</div>

## Design &amp; Architecture

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/' | relative_url }}">Machine Lifecycle</a></h3>
    <p>A structured progression from concept through operation and management of change, with standards and decision gates at each step.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/safety-architecture/' | relative_url }}">Safety Architecture</a></h3>
    <p>Functional layer separation, E-stop chain design, SIL/PL selection, and safety architecture constraints.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/detailed-design/' | relative_url }}">Detailed Design</a></h3>
    <p>Electrical design stage: schematics, IO lists, panel layout, conductor sizing, and protection coordination.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/ai-integration/' | relative_url }}">AI &amp; ML Integration</a></h3>
    <p>An authority-first register for deciding when classical, learned, interface, chemical, and biological methods are justified—and when to keep them offline.</p>
  </div>
</div>

## Select &amp; Size

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/design/workflows/motor-selection/' | relative_url }}">Motor Selection</a></h3>
    <p>Decision framework for motor-system family selection across induction, servo, BLDC, and stepper platforms.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/design/workflows/electrical-review/' | relative_url }}">Electrical Review</a></h3>
    <p>Systematic electrical design review: conductor sizing, protection coordination, grounding, and panel checklist.</p>
  </div>
</div>

## Commission &amp; Verify

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/guides/commissioning-templates/' | relative_url }}">Commissioning Templates</a></h3>
    <p>Printable field checklists for panel energization, motor commissioning, drive startup, and circuit verification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/guides/vfd-commissioning/' | relative_url }}">VFD Commissioning</a></h3>
    <p>Step-by-step VFD startup: parameter entry, motor data, rotation check, and protection verification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/guides/servo-commissioning/' | relative_url }}">Servo Commissioning</a></h3>
    <p>Servo drive startup: feedback configuration, homing, tuning, and safety function verification.</p>
  </div>
</div>

## Troubleshoot

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/tools/troubleshooting/motors/' | relative_url }}">Motor Troubleshooting</a></h3>
    <p>Decision tree for motor faults: thermal, mechanical, electrical, and drive-related fault branches.</p>
  </div>
</div>

## Scenarios

Industry and application scenarios showing how standards, lifecycle stages, and workflows combine for specific machine types.

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/tools/scenarios/' | relative_url }}">All Scenarios</a></h3>
    <p>9 machine and industry scenarios — from US control panels and global machinery to semiconductor fab tools and offshore platforms.</p>
  </div>
</div>
