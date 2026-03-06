---
layout: default
title: "Lifecycle Stage 11 — Maintenance and Lifecycle Support"
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "11. Maintenance"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 11</span>
  <h1>Maintenance and Lifecycle Support</h1>
</div>

## Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 13849-1 §10** | Requirements for maintenance; proof test of safety functions |
| **IEC 61511** | Proof test interval, functional test procedures for SIS |

## Key Activities

**Proof Testing:**
- Periodic testing of safety functions to detect dangerous undetected failures
- Test interval is determined during design phase (ISO 13849-1 / IEC 61511)
- All safety functions must be tested — bypass procedures required

**Preventive Maintenance:**
- PM checklists aligned with safety function proof test requirements
- Calibration of instruments per calibration intervals

**Management of Change (MOC):**
- Any change to the safety-related control system requires formal MOC
- MOC triggers re-evaluation of PL/SIL if safety function is affected
- Document all changes, test after change

## Key Deliverables

| Deliverable | Notes |
|-------------|-------|
| Proof test procedures | One per safety function |
| PM checklist | Aligned with proof test intervals |
| Calibration records | Per calibration plan |
| MOC records | All changes documented |
| Revision history | As-built documentation updated |

## Lifecycle End

When the machine or system is decommissioned, the safety case and validation records should be retained per applicable regulations and internal retention policies.

<a href="{{ '/lifecycle/' | relative_url }}" class="card__link">&larr; Back to Lifecycle Overview</a>
