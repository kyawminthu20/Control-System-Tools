---
layout: default
title: "IEC 61511 — Functional Safety, Process Industry SIS"
description: "IEC 61511:2016 — safety instrumented systems for the process industry, SIL lifecycle, SIF design."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "IEC 61511"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/"
related_standards:
  - name: "IEC 61508 (foundation)"
    url: "/standards/functional-safety/iec-61508/"
  - name: "ISO 12100 (machinery risk assessment)"
    url: "/standards/functional-safety/iso-12100/"
lifecycle_stage:
  - name: "Risk Assessment"
    slug: "risk-assessment/"
  - name: "Safety Architecture"
    slug: "safety-architecture/"
  - name: "Commissioning"
    slug: "commissioning/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · IEC 61511</span>
  <h1>IEC 61511:2016 — Safety Instrumented Systems, Process Industry</h1>
  <span class="badge badge--verify">PLANNED — LIMITED LOCAL COVERAGE — TO VERIFY</span>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 61511 |
| **Edition** | 2016 (Edition 2) |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global; used in oil and gas, chemicals, power, etc. |
| **Scope** | Safety instrumented systems in the process industry |
| **Repository** | `rag/international/functional_safety/iec_61511/` — planned |
| **Status in Corpus** | Planned — **limited coverage** <span class="badge badge--verify">TO VERIFY</span> |

**Purpose:** IEC 61511 is the process industry application standard derived from IEC 61508. It covers the full lifecycle of Safety Instrumented Systems (SIS) / Safety Instrumented Functions (SIF) from concept through decommissioning.

---

## Parts of IEC 61511

| Part | Title |
|------|-------|
| Part 1 | Framework, definitions, system, hardware, and application requirements |
| Part 2 | Guidelines for application of IEC 61511-1 |
| Part 3 | Guidance for determining required SIL |

---

## Core Concepts

**Safety Instrumented System (SIS):** A system composed of sensors, logic solvers, and final elements implemented to bring a process to a safe state when predetermined conditions are violated.

**Safety Instrumented Function (SIF):** A single safety function implemented by the SIS with a specific SIL target. One SIS may implement multiple SIFs.

**Proof Test Interval (PTI):** The periodic test required to detect dangerous undetected failures. PTI significantly affects the achievable PFDavg.

---

## SIL Determination for Process

| Method | Description |
|--------|-------------|
| Risk graph | Simplified qualitative/semi-quantitative |
| LOPA (Layer of Protection Analysis) | Semi-quantitative; most common in practice |
| Fault tree analysis | Quantitative; used for complex SIFs |

**LOPA is the dominant method** in the oil and gas and chemical industries for SIL determination.

---

## Comparison with Machinery Safety

| Aspect | IEC 61511 (process) | ISO 13849-1 / IEC 62061 (machinery) |
|--------|--------------------|------------------------------------|
| Domain | Process industry SIS | Industrial machinery |
| Risk metric | SIL 1–4 (PFDavg) | PL a–e or SIL 1–3 (PFHd) |
| Proof testing | Central to lifecycle | Less prominent |
| Lifecycle standard | IEC 61511 | ISO 13849-1 / IEC 62061 |
| Foundation | IEC 61508 | IEC 61508 (IEC 62061) or standalone (ISO 13849-1) |

---

## When to Use IEC 61511 vs IEC 62061

| Situation | Standard |
|-----------|----------|
| Process plant shutdown system | IEC 61511 |
| Industrial machine safety function | ISO 13849-1 or IEC 62061 |
| Machinery on a process skid with SIS | IEC 61511 for SIS; ISO 13849-1/62061 for machinery guards |
| Gas detection and shutdown | IEC 61511 |

**Note:** For process skids with both process safety and machine safety requirements, both standards may apply to different functions.

<a href="{{ '/scenarios/process-skid/' | relative_url }}" class="card__link">See process skid scenario &rarr;</a>
