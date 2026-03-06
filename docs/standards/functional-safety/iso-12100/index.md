---
layout: default
title: "ISO 12100 — Risk Assessment and Risk Reduction"
description: "ISO 12100:2010 — the foundation risk assessment standard for machinery, CE marking, and safety function design."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "ISO 12100"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
lifecycle_stage:
  - name: "Concept"
    slug: "concept/"
  - name: "Risk Assessment"
    slug: "risk-assessment/"
  - name: "Safety Architecture"
    slug: "safety-architecture/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · ISO 12100</span>
  <h1>ISO 12100:2010 — Risk Assessment and Risk Reduction</h1>
  <span class="badge badge--verify">PLANNED — TO VERIFY local detail coverage</span>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | ISO 12100 |
| **Edition** | 2010 |
| **Publisher** | International Organization for Standardization (ISO) |
| **Jurisdiction** | Global; Type A standard under EU Machinery Directive |
| **Scope** | Risk assessment and risk reduction for machinery |
| **Repository** | `rag/international/functional_safety/iso_12100/` — planned |
| **Status in Corpus** | Planned <span class="badge badge--verify">TO VERIFY</span> |

**Purpose:** ISO 12100 is the foundation standard for machinery safety. It provides the principles and methodology for risk assessment and risk reduction. All other machinery safety standards (ISO 13849-1, IEC 62061, IEC 60204-1) assume ISO 12100 has been applied first.

---

## Lifecycle Application

ISO 12100 applies earliest in the design process:

| Stage | ISO 12100 Application |
|-------|----------------------|
| **Concept** | Define machine limits and intended use |
| **Risk Assessment** | Systematic hazard identification and risk evaluation |
| **Safety Architecture** | Risk reduction strategy selection |

---

## Risk Assessment Process

ISO 12100 defines a three-step risk reduction strategy (in order of preference):

1. **Inherently safe design** — Eliminate or reduce hazards by design
2. **Safeguarding and protective measures** — Guards, interlocks, safety functions
3. **Information for use** — Warning labels, instructions, training

This iterative process continues until residual risk is acceptable.

---

## Key Inputs to ISO 13849-1 / IEC 62061

ISO 12100 provides the required risk assessment inputs for PL and SIL determination:

- **Hazard identification** — list of hazards requiring safety functions
- **Risk parameters** — severity of harm (S), frequency/duration of exposure (F), probability of avoidance (P)
- **Required risk reduction** — determines PLr or SIL target for each safety function

**PL determination path:** ISO 12100 risk assessment → PLr target → ISO 13849-1 architecture design

---

## Type A / B / C Standard Classification

ISO 12100 is a **Type A** (basic safety) standard. The hierarchy:

| Type | Description | Examples |
|------|-------------|---------|
| A | Basic safety concepts | ISO 12100 |
| B | Generic safety aspects | ISO 13849-1, IEC 60204-1, ISO 13850 |
| C | Machine-specific | Robot safety, press safety |

Type A applies broadly; Type C takes precedence for specific machine types when it exists.

---

## Related Standards

- [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — uses ISO 12100 risk assessment outputs
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — alternative path, also uses ISO 12100 inputs
- [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) — electrical implementation after risk assessment
