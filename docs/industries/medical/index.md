---
layout: default
title: "Medical Industry Standards Overlay"
description: "Standards path for medical and regulated equipment: NEC and IEC 60204-1 baseline with explicit corpus gaps for IEC 60601-1, ISO 14971, and regulated validation controls."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Medical"
related_standards:
  - name: "NEC"
    url: "/standards/us-electrical/nec/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/medical.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Medical</span>
  <h1>Medical Industry Standards</h1>
  <span class="badge badge--verify">IEC 60601-1 and ISO 14971 are not in corpus</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Medical devices and medical equipment |
| **Typical systems** | Diagnostic equipment, treatment devices, medical manufacturing |
| **Markets** | US (FDA) and EU (MDR) |
| **Special concern** | Patient safety boundary, regulated validation, audit trail, risk management |

> **Corpus note:** NEC and IEC 60204-1 give a useful electrical baseline for support equipment and manufacturing skids, but they are not substitutes for medical-device standards. IEC 60601-1, ISO 14971, and most medical regulatory content must be verified outside the corpus.

---

## Standards Applicability by Project Phase

| Phase | Standards | Purpose |
|-------|-----------|---------|
| **Intended-use definition** | IEC 60601-1, ISO 14971 | Decide whether the equipment is patient-connected medical electrical equipment or industrial support equipment |
| **Electrical architecture** | NEC, IEC 60204-1 | Establish the baseline for power distribution, isolation, labeling, and control-panel construction where applicable |
| **Risk management** | ISO 14971, ISO 12100 | Build hazard analysis, risk controls, and traceability from hazard to verification |
| **Software / records** | IEC 62304, 21 CFR Part 11, FDA quality rules | Define validation, audit trail, user access, and electronic record controls |
| **Verification / release** | IEC 60601-1 test route, regulated validation plan, calibration controls | Confirm safety, usability, record integrity, and configuration control before release |

---

## Standards Selection Flow

```text
Is the equipment patient-connected or used in the patient environment?
  YES -> IEC 60601-1 becomes the primary electrical safety route
       -> Do not rely on IEC 60204-1 alone

Is the package manufacturing, laboratory support, or utility equipment with no patient connection?
  YES -> NEC and IEC 60204-1 may remain the electrical baseline
       -> Still verify whether medical-device quality and records rules apply

Does the system create device history, batch, treatment, or patient-linked records?
  YES -> Add audit-trail, electronic-record, and user-access controls directly

Does the project need formal risk management traceability?
  YES -> Build the file around ISO 14971, not only a general machine risk review
```

---

## Standards Path Summary

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical baseline | NEC | <span class="badge badge--complete">Reviewed</span> |
| International electrical baseline | IEC 60204-1 | <span class="badge badge--complete">Reviewed</span> |
| Medical electrical safety | IEC 60601-1 / 60601 series | Not in corpus |
| Risk management | ISO 14971 | Not in corpus |
| Software lifecycle | IEC 62304 | Not in corpus |
| US regulatory / quality | 21 CFR Part 11, 21 CFR Part 820, FDA guidance | Not in corpus |
| EU regulatory / quality | MDR, ISO 13485 | Not in corpus |

---

## Key Engineering Decisions for Medical Projects

**Patient-connected vs. industrial-support boundary:**
This is the first decision that matters. If the equipment touches the patient environment, monitors physiological signals, or forms part of a medical electrical system, IEC 60601-1 drives the electrical safety route. If it is manufacturing or lab support equipment, the machine-electrical baseline may still be appropriate, but regulated validation and records controls can still apply.

**Risk-management traceability:**
Medical projects usually need a hazard-to-control-to-verification chain that is tighter than a normal machine package. ISO 14971 is the missing anchor here. Use the local machine safety material for structure if it helps, but keep the official risk-management file, residual-risk decisions, and verification matrix under the medical standard set.

**Audit trail, access control, and calibration evidence:**
Once the system stores regulated data, supports dosing, or affects release decisions, event logging is no longer just a convenience feature. User roles, audit trails, record retention, software revision control, and calibration history become acceptance items, not optional documentation add-ons.

---

## Medical Project Kickoff Checklist

- [ ] Write an intended-use statement that clearly says whether the equipment is patient-connected, clinical support, or manufacturing support
- [ ] Decide whether IEC 60601-1 applies before freezing the electrical architecture
- [ ] Start the risk-management file under ISO 14971 if the project is medical-device scope
- [ ] Define software validation, audit trail, and user-account expectations early
- [ ] Identify which records are regulated: device history, treatment, batch, calibration, or service logs
- [ ] Build the turnover package to include schematics, IO list, interlock matrix, calibration status, and revision history

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/medical.md`

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
