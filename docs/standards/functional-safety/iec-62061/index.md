---
layout: default
title: "IEC 62061 — Functional Safety, Machinery SIL"
description: "IEC 62061:2021 — SIL approach for safety-related electrical control systems on machinery."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "IEC 62061"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/"
related_standards:
  - name: "ISO 13849-1 (PL alternative)"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 61508 (foundation)"
    url: "/standards/functional-safety/iec-61508/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
lifecycle_stage:
  - name: "Safety Architecture"
    slug: "safety-architecture/"
  - name: "Detailed Design"
    slug: "detailed-design/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · IEC 62061</span>
  <h1>IEC 62061:2021 — Functional Safety of Machinery (SIL)</h1>
  <span class="badge badge--verify">PLANNED — TO VERIFY local detail coverage</span>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 62061 |
| **Edition** | 2021 |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global; harmonized under EU Machinery Directive |
| **Scope** | Safety-related electrical control systems on machinery |
| **Repository** | `rag/international/functional_safety/iec_62061/` — planned |
| **Status in Corpus** | Planned <span class="badge badge--verify">TO VERIFY</span> |

**Purpose:** IEC 62061 provides requirements for design and implementation of safety-related electrical, electronic, and programmable electronic control systems (SRECS) on machinery. It derives from IEC 61508 but is scoped specifically to machinery applications.

---

## SIL Levels for Machinery

| SIL | PFHd range | Typical machinery application |
|-----|-----------|------------------------------|
| SIL 1 | 10⁻⁵ to < 10⁻⁴ /hr | Lower risk, supplementary functions |
| SIL 2 | 10⁻⁶ to < 10⁻⁵ /hr | Most industrial safety PLCs |
| SIL 3 | 10⁻⁷ to < 10⁻⁶ /hr | High-risk, process-like machinery |

**SIL 3 is rarely needed for typical industrial machinery.** SIL 2 corresponds approximately to PLd and is the most common target for industrial safety systems.

---

## IEC 62061 vs ISO 13849-1

| Aspect | IEC 62061 | ISO 13849-1 |
|--------|-----------|-------------|
| Metric | SIL (1–3) | PL (a–e) |
| Methodology | PFHD calculation from subsystems | Category + MTTFd + DC |
| Scope | Electrical/electronic safety functions | Includes mechanical/pneumatic |
| Complexity | Higher (more detailed calculation) | Simpler for common architectures |
| Standards alignment | IEC 61508-derived | Standalone machinery standard |

---

## Relationship to IEC 61508

IEC 62061 derives from IEC 61508 but simplifies the application for machinery:
- Scoped to SIL 1–3 (IEC 61508 covers SIL 1–4)
- Provides machinery-specific subsystem definitions
- Aligned with machinery lifecycle (ISO 12100 risk assessment as input)

For software on safety PLCs within machinery, IEC 62061 references IEC 61508-3 for software requirements.

---

## When to Choose IEC 62061 Over ISO 13849-1

Consider IEC 62061 when:
- Safety function involves complex logic not easily categorized
- SIL > PLd equivalent is required
- Design team is already working in IEC 61508 methodology
- Subsystem PFHD calculation is preferred over simplified MTTFd/DC approach

<a href="{{ '/standards/functional-safety/iso-13849-1/' | relative_url }}" class="card__link">Compare with ISO 13849-1 &rarr;</a>
