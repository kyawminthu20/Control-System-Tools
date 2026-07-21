---
layout: default
title: "Marine Industry Standards Overlay"
description: "Standards path for marine vessels and ship control systems: IEC 60092, class society rules (DNV, ABS, Lloyd's), flag-state authority."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Marine"
related_standards:
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
review:
  standard: "IEC 60092 · class society rules (DNV, ABS, Lloyd's)"
  edition: "exact governing revisions not yet recorded — verify on the linked standards pages"
  status: "Review pending"
  coverage: "Overlay routing for marine vessels; class-rule and flag-state specifics summarized at overview level."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Marine</span>
  <h1>Marine Industry Standards</h1>
  <span class="badge badge--verify">IEC 60092 not in corpus — class rules summary only</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Commercial vessels, cargo ships, tankers, passenger ships, offshore support vessels |
| **Typical systems** | Propulsion control, machinery automation, cargo management, fire detection |
| **Markets** | International (IMO flag-state system) |
| **Special concerns** | Class society approval, flag-state authority, IMO regulations, marine environment rating |

> **Corpus note:** IEC 60092 (Electrical Installations in Ships) is not yet in the reference library. This page covers the framework and key concepts. For detailed IEC 60092 requirements, consult the standard directly.

---

## Regulatory Framework

Marine vessels operate under a layered regulatory system unlike any onshore industry:

| Layer | Body | Instrument |
|-------|------|-----------|
| **International law** | IMO (International Maritime Organization) | SOLAS, MARPOL conventions |
| **Class rules** | Classification society (DNV, ABS, Lloyd's Register, Bureau Veritas) | Class rules for construction and machinery |
| **Flag state** | Country of vessel registration | Adopts and enforces IMO conventions; may add national requirements |
| **Port state** | Country where vessel calls | Port State Control (PSC) — inspects foreign vessels for compliance |

**Key principle:** The classification society issues the class certificate. The flag state issues the statutory certificates (Safety Equipment Certificate, Safety Construction Certificate). Both are required to operate. Loss of class = loss of flag state certificates = vessel cannot trade.

---

## Standards Applicability

| Category | Standard | Status |
|----------|----------|--------|
| Electrical installations on ships | IEC 60092 series | Not in corpus — consult directly |
| Machinery control automation | IEC 60092-504 | Not in corpus |
| Process safety (SIS on tankers) | IEC 61511 | <span class="badge badge--reviewed">Reviewed</span> |
| Hazardous area (tankers, gas carriers) | IEC 60079 series | <span class="badge badge--reviewed">Reviewed</span> |
| Functional safety (machinery) | IEC 62061 / ISO 13849-1 | <span class="badge badge--reviewed">Reviewed</span> |
| IMO fire safety | SOLAS Chapter II-2 | Not in corpus |

---

## Key IEC 60092 Series Structure

| Part | Title | Relevance |
|------|-------|-----------|
| 60092-101 | Definitions and general requirements | Foundational |
| 60092-201 | System design — general | Power system architecture |
| 60092-301 | Equipment — generators and motors | Marine grade rotating machines |
| 60092-401 | Switchgear and controlgear | Marine switchboard requirements |
| 60092-504 | Special features — control and instrumentation | Process automation on ships |
| 60092-507 | Small vessels | Applies to OSVs and small offshore support |

---

## Marine vs. Offshore Control Systems: Key Differences

| Aspect | Marine vessel | Offshore platform |
|--------|--------------|-------------------|
| **Standards body** | IMO + class society | Class society (DNV/ABS) |
| **Earthing system** | IT (insulated neutral) — same as offshore | IT |
| **Key standard** | IEC 60092 series | DNV-OS-D201 / ABS Part 4 |
| **Primary hazard** | Flooding, fire, propulsion loss | Hydrocarbon release, blowout |
| **Safety system** | Fire detection, flooding alarm, stability control | ESD, F&G, HIPPS |
| **Typical lifecycle** | 25–30 years between major refits | 20–30 years |

---

## When IEC 61511 Applies to Marine

For chemical tankers, gas carriers (LNG, LPG), and offshore supply vessels with chemical cargo:
- SOLAS requires gas detection and emergency shutdown for cargo areas
- The SIS lifecycle approach of IEC 61511 is applicable and increasingly expected
- Class societies (DNV, ABS) reference IEC 61508/61511 for functional safety assessments on these vessel types

---

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
