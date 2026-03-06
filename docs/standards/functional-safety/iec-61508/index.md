---
layout: default
title: "IEC 61508 — Functional Safety of E/E/PE Systems"
description: "IEC 61508:2010 — the foundational functional safety standard for electrical, electronic, and programmable electronic systems."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "IEC 61508"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/"
related_standards:
  - name: "IEC 62061 (machinery application)"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511 (process application)"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1 (machinery PL)"
    url: "/standards/functional-safety/iso-13849-1/"
lifecycle_stage:
  - name: "Safety Architecture"
    slug: "safety-architecture/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · IEC 61508</span>
  <h1>IEC 61508:2010 — Functional Safety of E/E/PE Safety-Related Systems</h1>
  <span class="badge badge--verify">PLANNED — TO VERIFY local detail coverage</span>
</div>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 61508 |
| **Edition** | 2010 (parts 1–7) |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global |
| **Scope** | Generic E/E/PE safety-related systems, all industries |
| **Repository** | `rag/international/functional_safety/iec_61508/` — planned |
| **Status in Corpus** | Planned <span class="badge badge--verify">TO VERIFY</span> |

**Purpose:** IEC 61508 is the umbrella standard for functional safety of electrical/electronic/programmable electronic (E/E/PE) safety-related systems. It defines the SIL framework and safety lifecycle that IEC 62061 and IEC 61511 both derive from.

---

## Parts of IEC 61508

| Part | Title | Notes |
|------|-------|-------|
| Part 1 | General requirements | Scope, definitions, safety management |
| Part 2 | E/E/PE hardware requirements | Hardware architectural constraints, SFF |
| Part 3 | Software requirements | Safety-related software, V-model |
| Part 4 | Definitions and abbreviations | Normative definitions |
| Part 5 | Examples of methods for SIL determination | Informative |
| Part 6 | Guidelines on Part 2 and 3 | Informative |
| Part 7 | Overview of techniques and measures | Informative |

**Part 3 (software)** is most frequently referenced by IEC 62061 and IEC 61511 for safety PLC software requirements.

---

## When IEC 61508 Is Applied Directly

IEC 61508 is typically applied directly when:
- Developing a safety device or system for general use (manufacturer)
- No application-specific sector standard exists
- System combines machinery, process, and other domains

Most application engineers will work with **IEC 62061** (machinery) or **IEC 61511** (process) rather than IEC 61508 directly.

---

## Hierarchy

```
IEC 61508 (generic foundation)
    ├── IEC 62061 (machinery application)
    └── IEC 61511 (process industry application)
```

<a href="{{ '/standards/functional-safety/' | relative_url }}" class="card__link">&larr; Functional Safety family</a>
