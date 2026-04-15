---
layout: default
title: "15-Standard Minimum Compliance Stack"
description: "Minimum compliance baseline for semiconductor equipment targeting US, EU, and Asian fab installations — five technical domains, 15 standards."
breadcrumb:
  - name: "Reference Models"
    url: "/reference/"
  - name: "Architecture"
    url: "/design/architecture/"
  - name: "Compliance Stack"
redirect_from:
  - /reference/architecture/compliance-stack/
  - /reference/architecture/compliance-stack/index.html
---

<div class="page-header">
  <span class="page-header__label">Reference — Architecture</span>
  <h1>15-Standard Minimum Compliance Stack</h1>
  <p>Minimum compliance baseline used for semiconductor equipment that must install in US, EU, and Asian fabs without redesign. Five technical domains, 15 standards.</p>
</div>

## Overview

Large semiconductor equipment builders maintain an internal minimum compliance stack. The goal: a tool can be installed in US, EU, and Asian fabs without redesign.

The stack covers five technical domains:

1. Machine safety
2. Electrical systems
3. Functional safety
4. Hazardous materials & gases
5. Cybersecurity and factory integration

---

## Domain 1 — Core Machinery Safety

Applied first when designing a machine.

| Standard | Purpose |
|---|---|
| ISO 12100 | Formal hazard analysis process |
| ISO 13849-1 | Performance Level safety design |
| IEC 60204-1 | Electrical machine design (international) |

```
ISO 12100 → identify hazards
ISO 13849 → design safety functions
IEC 60204 → implement electrical system
```

These three form the **core of CE compliance**.

---

## Domain 2 — US Electrical Compliance

Mandatory for tools installed in US fabs.

| Standard | Purpose |
|---|---|
| NFPA 79 | US machine electrical requirements |
| NFPA 70 (NEC) | Installation code |
| UL 508A | Control panel construction |

NEC Article 670 references NFPA 79, so the tool must follow NFPA 79 to be NEC compliant.

---

## Domain 3 — Functional Safety

For complex tools with robotics, motion systems, or vacuum systems.

| Standard | Purpose |
|---|---|
| IEC 62061 | SIL-based machinery safety |
| IEC 61508 | Foundation standard |
| ISO 13850 | E-stop design requirements |

Typical semiconductor tool safety level: PL d or PL e.

---

## Domain 4 — Hazardous Materials & Gas Systems

Semiconductor tools use toxic gases, corrosive chemicals, and high-pressure gas cylinders.

| Standard | Purpose |
|---|---|
| SEMI S2 | Semiconductor equipment safety |
| SEMI S8 | Operator safety |
| SEMI S14 | Fire hazards in tools |
| NFPA 318 | Fab safety requirements |

These are unique to semiconductor fabs.

---

## Domain 5 — Industrial Cybersecurity

Modern semiconductor tools are fully networked.

| Standard | Purpose |
|---|---|
| IEC 62443 | Industrial automation security |
| NIST SP 800-82 | US ICS security guidance |

Typical fab rule: tools cannot connect directly to the internet. All communication goes through factory network gateways.

---

## Complete Stack

```
 1  ISO 12100
 2  ISO 13849-1
 3  ISO 13850
 4  IEC 60204-1
 5  IEC 62061
 6  IEC 61508
 7  NFPA 79
 8  NFPA 70 (NEC)
 9  UL 508A
10  SEMI S2
11  SEMI S8
12  SEMI S14
13  NFPA 318
14  IEC 62443
15  NIST SP 800-82
```

Ensures compliance with US regulations, European CE marking, and semiconductor fab safety rules.

---

## Why Semiconductor Tools Use Such a Large Stack

Semiconductor equipment combines: high voltages, hazardous gases, robotics, vacuum systems, chemical processing, and automated wafer handling. Multiple risk domains overlap, requiring a multi-standard compliance model.

---

<div style="margin-top:2rem; font-size:0.9rem; color:var(--color-text-muted);">
Source: <code>control-standards/rag/standards_intelligence/reference_models/15-Standard Minimum Compliance Stack.md</code>. This is a design aid derived from the canonical RAG. Verify against applicable standards before use.
</div>
