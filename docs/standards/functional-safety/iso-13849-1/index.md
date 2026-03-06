---
layout: default
title: "ISO 13849-1 — Safety of Machinery, Control Systems (PL)"
description: "ISO 13849-1:2023 — Performance Level approach for safety-related control systems in machinery."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "ISO 13849-1"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "IEC 62061 (alternative SIL path)"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
lifecycle_stage:
  - name: "Risk Assessment"
    slug: "risk-assessment/"
  - name: "Safety Architecture"
    slug: "safety-architecture/"
  - name: "Commissioning"
    slug: "commissioning/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · ISO 13849-1</span>
  <h1>ISO 13849-1:2023 — Safety-Related Parts of Control Systems (PL)</h1>
  <span class="badge badge--verify">PLANNED — TO VERIFY local detail coverage</span>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | ISO 13849-1 |
| **Edition** | 2023 |
| **Publisher** | International Organization for Standardization (ISO) |
| **Jurisdiction** | Global; harmonized under EU Machinery Directive |
| **Scope** | Safety-related parts of control systems — PL determination |
| **Repository** | `rag/international/functional_safety/iso_13849_1/` — planned |
| **Status in Corpus** | Planned <span class="badge badge--verify">TO VERIFY</span> |

**Purpose:** ISO 13849-1 provides requirements for design and validation of safety-related parts of control systems (SRP/CS). The standard uses Performance Levels (PLa–PLe) to quantify the ability of a safety-related control system to perform a safety function.

---

## Performance Level Overview

| PL | Approximate PFHd range | Typical application |
|----|----------------------|---------------------|
| PLa | ≥ 10⁻⁵ /hr | Low risk, simple machine |
| PLb | < 10⁻⁵ /hr | Low–medium risk |
| PLc | < 3×10⁻⁶ /hr | Medium risk |
| PLd | < 10⁻⁶ /hr | High risk; most common industrial safety |
| PLe | < 10⁻⁷ /hr | Very high risk |

**PLd is the most commonly specified level** for industrial machine guarding, E-stop, and light curtain applications.

---

## Design Parameters

Three parameters determine the achievable PL:

| Parameter | Description |
|-----------|-------------|
| **Category** (B, 1–4) | Architectural structure of the safety function |
| **MTTFd** | Mean Time To dangerous Failure (per channel) |
| **DC** | Diagnostic Coverage (none / low / medium / high) |
| **CCF** | Common Cause Failure (score must meet minimum) |

Category 3 or 4 with high MTTFd and medium/high DC typically achieves PLd or PLe.

---

## Lifecycle Application

ISO 13849-1 applies after ISO 12100 risk assessment has determined the required PL (PLr):

| Stage | Activity |
|-------|---------|
| **Risk Assessment** | ISO 12100 outputs PLr for each safety function |
| **Safety Architecture** | Design SRP/CS to meet or exceed PLr |
| **Detailed Design** | Component selection (MTTFd, DC, CCF inputs) |
| **Validation** | Annex K verification checklist |
| **Commissioning** | Final validation documentation |

---

## ISO 13849-1 vs IEC 62061

Both standards are valid approaches for machinery safety functions:

| Aspect | ISO 13849-1 | IEC 62061 |
|--------|-------------|-----------|
| Metric | PL (a–e) | SIL (1–3) |
| Methodology | Category + MTTFd + DC | PFHD calculation |
| Scope | Includes mechanical/pneumatic | Electrical/electronic only |
| Complexity | Simpler for typical applications | More flexible for complex SIF |
| Common usage | Most industrial machinery | Complex, high-SIL applications |

**Can be used together:** ISO 13849-1 for mechanical and pneumatic elements; IEC 62061 for electrical/electronic safety functions. The combined result must meet the overall safety requirement.

---

## Related Standards

- [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) — required first step (risk assessment → PLr)
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — alternative/complementary SIL path
- [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) — electrical implementation of safety functions
- ISO 13849-2 — Validation methods for ISO 13849-1 designs
