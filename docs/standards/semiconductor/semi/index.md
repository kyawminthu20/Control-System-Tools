---
layout: default
title: "SEMI S2 / S8 / S14 — Semiconductor Equipment Safety"
description: "SEMI S2 (equipment safety), S8 (ergonomics), S14 (fire risk assessment) for semiconductor manufacturing equipment."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Semiconductor"
    url: "/standards/semiconductor/"
  - name: "SEMI S2/S8/S14"
related_standards:
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
last_reviewed: "2026-03-08"
---

<div class="page-header">
  <span class="page-header__label">International · Semiconductor</span>
  <h1>SEMI S2 / S8 / S14 — Semiconductor Equipment Safety</h1>
</div>

<span class="badge badge--complete">Phase 10 Complete</span>

## Standard Overview

| Standard | Scope |
|----------|-------|
| **SEMI S2** | Environmental, Health, and Safety Guideline for Semiconductor Manufacturing Equipment |
| **SEMI S8** | Ergonomics Engineering of Semiconductor Manufacturing Equipment |
| **SEMI S14** | Fire Risk Assessment and Fire Safety for Semiconductor Manufacturing Equipment |

These guidelines apply to equipment used in semiconductor manufacturing fabs. Compliance is required by most fab operators as a condition of equipment purchase and installation.

---

## SEMI S2 — Equipment Safety Highlights

### Electrical safety (control engineering relevance)

- All conductive surfaces accessible during operation must be grounded
- Interlocks must de-energize high-voltage circuits before panels open — not defeatable without deliberate action
- Interlocks must fail to a safe state; failures must be detected
- Stored energy (capacitors): discharge to <50 V within 5 seconds of isolation, or provide discharge indicator + access interlock
- Manual reset required after safety interlock actuation — no automatic restart

### Lockout/Tagout

- Every energy isolation point must accept a padlock
- Tagout-only is not acceptable for primary energy isolation
- Stored energy procedures required (pneumatic, hydraulic, capacitive)

### Gas and chemical control systems

- Normally-closed automatic shutoff valves on all toxic/flammable gas lines
- Exhaust flow monitoring before permitting process gas flow
- Gas detector integration with automatic shutoff and exhaust increase

---

## SEMI S8 — Ergonomics Key Points

| Requirement | Limit |
|-------------|-------|
| E-stop height | 600–1,400 mm from floor |
| Pushbutton actuation force | ≤22 N |
| E-stop actuation force | ≤40 N |
| Maintenance panel opening force | ≤222 N |
| Single-person lift limit | ≤16 kg |

---

## SEMI S14 — Fire Risk Assessment Key Points

- Risk assessment required for all equipment with flammable/pyrophoric gases or chemicals
- Automatic shutoff of all flammable gas supplies on fire detection
- Over-temperature protection for heater circuits independent of process controller
- Water suppression prohibited in cleanrooms — clean agent systems required
- Local suppression must interface with facility-wide fire alarm system

---

## Relationship to Other Standards

| Standard | Relationship |
|----------|-------------|
| IEC 60204-1 | International machine electrical safety — often required alongside S2 |
| NFPA 79 | US equivalent — required for US-market semiconductor equipment |
| ISO 12100 | Risk assessment methodology referenced by S2 and S14 |
| IEC 62443 | Cybersecurity — applicable to networked semiconductor equipment |

---

<a href="{{ '/standards/semiconductor/' | relative_url }}" class="card__link">&larr; Semiconductor family</a>
