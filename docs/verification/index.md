---
layout: default
title: "Verification"
description: "Analysis, validation, and change-control references — risk assessment, safety requirements spec, safety architecture, safety wiring, maintenance, management of change, and the full lifecycle journey."
breadcrumb:
  - name: "Verification"
---

<div class="page-header">
  <span class="page-header__label">Verification</span>
  <h1>Verification</h1>
  <p>References for the analysis, validation, and change-control half of the machine lifecycle. Everything that confirms the design is correct before build, and that it stays correct after handover.</p>
</div>

<blockquote>
<strong>Scope:</strong> Analysis-side activities (risk assessment, safety requirements, safety architecture) and post-handover activities (maintenance, management of change). Design work lives under <a href="{{ '/design/' | relative_url }}">Design</a>; build and commissioning under <a href="{{ '/implementation/' | relative_url }}">Implementation</a>.
</blockquote>

## Verification Gates

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/verification/risk-assessment/' | relative_url }}">Risk Assessment</a></h3>
    <p>ISO 12100 risk estimation and reduction process, hazard identification, harm probability and severity scoring, and the boundary conditions for moving to a Safety Requirements Specification.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/verification/safety-requirements-spec/' | relative_url }}">Safety Requirements Specification</a></h3>
    <p>SRS content rules, safety function enumeration, PL/SIL target assignment, reaction time budgets, and the traceability requirements that carry into design and V&amp;V.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/verification/safety-architecture/' | relative_url }}">Safety Architecture</a></h3>
    <p>Category-based and SIL-based safety architecture templates, E-stop chain design, dual-channel input patterns, safe output driving, and diagnostic coverage expectations.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/verification/safety-wiring/' | relative_url }}">Safety Wiring Practices</a></h3>
    <p>Practical safety wiring baseline: 24 VDC rationale, NC contact logic, wire gauge, color coding, termination, discrepancy time, dual-channel input specification.</p>
  </div>
</div>

## Post-Handover

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/verification/maintenance/' | relative_url }}">Maintenance</a></h3>
    <p>Ongoing verification activities — proof-test intervals, calibration management, spare-parts strategy, failure logging, and the path back into risk assessment when behavior drifts.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/verification/management-of-change/' | relative_url }}">Management of Change</a></h3>
    <p>MOC workflow for controlled modifications — impact assessment, approval chain, SRS update, V&amp;V re-run, and change-set documentation.</p>
  </div>
</div>

## Full Lifecycle Journey

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/verification/lifecycle/' | relative_url }}">Lifecycle Overview</a></h3>
    <p>The 13-stage machine lifecycle, from concept and standards selection through detailed design, draft documentation, and into the Implementation section for build / install / commissioning.</p>
  </div>
</div>

## Related Sections

- [Fundamentals]({{ '/fundamentals/' | relative_url }}) — prerequisite electrical and control concepts
- [Design]({{ '/design/' | relative_url }}) — architecture models, motor selection, design workflows
- [Implementation]({{ '/implementation/' | relative_url }}) — commissioning templates and scenarios
- [Standards]({{ '/standards/' | relative_url }}) — ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511, IEC 62443
