---
layout: default
title: "Engineering Workflow"
description: "Workflow-first navigation for machine and panel design: lifecycle stages, engineering workflows, commissioning templates, and scenarios."
breadcrumb:
  - name: "Engineering Workflow"
redirect_from:
  - /design/
  - /design/index.html
---

<div class="page-header">
  <span class="page-header__label">Engineering Workflow</span>
  <h1>Engineering Workflow</h1>
  <p>Navigate from concept through commissioning by engineering task. Lifecycle stages provide structured progression; workflows guide decision points; commissioning templates support field verification.</p>
</div>

## Design &amp; Architecture

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/' | relative_url }}">Machine Lifecycle</a></h3>
    <p>11-stage structured progression from concept through maintenance, with standards and decision gates at each step.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/safety-architecture/' | relative_url }}">Safety Architecture</a></h3>
    <p>Functional layer separation, E-stop chain design, SIL/PL selection, and safety architecture constraints.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/lifecycle/detailed-design/' | relative_url }}">Detailed Design</a></h3>
    <p>Electrical design stage: schematics, IO lists, panel layout, conductor sizing, and protection coordination.</p>
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
    <h3><a href="{{ '/commissioning-templates/' | relative_url }}">Commissioning Templates</a></h3>
    <p>Printable field checklists for panel energization, motor commissioning, drive startup, and circuit verification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/workflows/vfd-commissioning/' | relative_url }}">VFD Commissioning</a></h3>
    <p>Step-by-step VFD startup: parameter entry, motor data, rotation check, and protection verification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/workflows/servo-commissioning/' | relative_url }}">Servo Commissioning</a></h3>
    <p>Servo drive startup: feedback configuration, homing, tuning, and safety function verification.</p>
  </div>
</div>

## Troubleshoot

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/workflows/motor-troubleshooting/' | relative_url }}">Motor Troubleshooting</a></h3>
    <p>Decision tree for motor faults: thermal, mechanical, electrical, and drive-related fault branches.</p>
  </div>
</div>

## Scenarios

Industry and application scenarios showing how standards, lifecycle stages, and workflows combine for specific machine types.

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/scenarios/' | relative_url }}">All Scenarios</a></h3>
    <p>9 machine and industry scenarios — from US control panels and global machinery to semiconductor fab tools and offshore platforms.</p>
  </div>
</div>
