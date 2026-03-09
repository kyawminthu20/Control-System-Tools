---
layout: default
title: "Offshore Industry Standards Overlay"
description: "Standards path for offshore platforms and FPSOs: DNV-OS-D201, ABS, IEC 61511 SIS, IEC 60079 hazardous area, LSOH cable, IT earthing."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Offshore"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 60079"
    url: "/standards/hazardous-area/iec-60079/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Offshore</span>
  <h1>Offshore Industry Standards</h1>
  <span class="badge badge--complete">Phase 12 — DNV + ABS Corpus Complete</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Offshore oil and gas platforms, FPSOs, MODUs, semi-submersibles |
| **Typical systems** | ESD, F&G, HIPPS, BPCS/DCS, dynamic positioning, emergency power |
| **Markets** | North Sea (DNV), US Gulf of Mexico (ABS), international |
| **Special concerns** | Class society approval, marine-grade equipment, IT earthing, LSOH cable, DP redundancy |

---

## Standards Applicability by Project Phase

| Phase | Standards | Purpose |
|-------|-----------|---------|
| **FEED / Concept** | DNV-OS-D201 / ABS Part 4, IEC 61511 §5 | Safety philosophy, ESD architecture, Approval in Principle |
| **SIL Determination** | IEC 61511 §9 (LOPA) | SIL targets for each SIF (ESD, HIPPS) |
| **Detailed Design** | DNV-OS-D201 §2/4/6/7, IEC 60204-1 | Electrical system design, drawing approval submission |
| **Ex Equipment Selection** | IEC 60079-0, IEC 60079-10-1 | Zone classification, EPL/T-code selection |
| **Procurement** | DNV / ABS type approval database | Verify all major equipment has class type approval |
| **FAT** | IEC 61511 §12, DNV / ABS witness | ESD FAT, F&G FAT — class surveyor attends |
| **Commissioning** | IEC 60079-14 §6, IEC 61511 §12 | Ex initial inspection, SIS SAT, class survey |
| **Annual Inspection** | IEC 60079-17, IEC 61511 §16 | Ex periodic inspection, SIF proof tests |

---

## Standards Selection Flow

```
Who is the classification society?
  DNV → DNV-OS-D201 is the primary electrical standard
  ABS → ABS Rules Part 4 is the primary electrical standard
  Dual class → apply the more stringent of each requirement

Is the platform in US waters or US-flagged?
  YES → NEC Art. 500/505 applies for hazardous area wiring (in addition to class rules)
  NO  → IEC 60079-14 applies for Ex installation

Does the process have loss-of-containment hazards?
  YES → IEC 61511 SIS lifecycle required
       → SIL determination via LOPA
       → ESD and HIPPS designed to the required SIL

Is the platform dynamically positioned (DP)?
  YES → Power system must meet DP-2 or DP-3 redundancy class
       → Control system power distributed across two independent buses
       → UPS autonomy per class requirement
```

---

## Standards Path Summary

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| Class society — DNV | DNV-OS-D201 | <span class="badge badge--complete">Complete</span> |
| Class society — ABS | ABS Offshore Electrical (Part 4) | <span class="badge badge--complete">Complete</span> |
| Process safety (SIS) | IEC 61511 | <span class="badge badge--complete">Complete</span> |
| Hazardous area equipment | IEC 60079 series | <span class="badge badge--complete">Complete</span> |
| Machine electrical design | IEC 60204-1 | <span class="badge badge--complete">Complete</span> |
| Marine electrical (ships) | IEC 60092 series | Not in corpus |
| Offshore fire code | NFPA 306 | Not in corpus |

---

## Key Engineering Decisions for Offshore

**IT earthing system vs. onshore TN-S:**
Offshore platforms use an insulated neutral (IT) earthing system. The first earth fault raises an alarm but does not trip. This is fundamentally different from onshore practice where earth faults cause immediate trip. Do not connect control circuit 0 V to earth — this creates a concealed first earth fault that will mask future faults. Specify earth fault monitoring on all isolated 24 VDC buses.

**LSOH cable selection:**
PVC cables are prohibited on offshore units. Specify LSOH (Low Smoke, Zero Halogen) cables throughout — IEC 60754-1 for halogen content, IEC 60332-3 for fire propagation. For ESD and F&G circuits, also specify fire-resistant (FR) rated cables maintaining circuit integrity at 750°C for 3 hours (IEC 60331). Budget for approximately 30–50% cost premium over standard industrial cable.

**Class type approval vs. project approval:**
Using type-approved equipment (listed in DNV or ABS database) avoids costly project-specific approval submissions. Check the relevant class type approval list before finalising the equipment list. For PLCs and safety systems, most major vendors (Siemens, Rockwell, Emerson, Honeywell) have type-approved products.

**DNV vs. ABS — which is more stringent?**
On most requirements the two societies are equivalent. Key difference: emergency generator auto-start — DNV requires 30 seconds, ABS allows 45 seconds. On dual-classed projects, always apply the more stringent requirement.

---

## Pre-Commissioning Compliance Checklist

- [ ] Class society (DNV / ABS) engaged at FEED — Approval in Principle obtained
- [ ] All major equipment on class type approval list — no unapproved substitutions
- [ ] LSOH and fire-resistant cable used throughout — cable schedule certified
- [ ] IT earthing system design documented — earth fault monitoring specified on all buses
- [ ] Area classification drawing approved by class society
- [ ] All Ex certificates current and verified against IECEx / ATEX database
- [ ] ESD cause-and-effect matrix reviewed and approved
- [ ] ESD FAT and F&G FAT completed — class surveyor witness report received
- [ ] SIL verification report accepted
- [ ] Ex initial inspection certificate issued (IEC 60079-14 §6)
- [ ] Class survey completed — class notation confirmed

---

<a href="{{ '/scenarios/offshore-platform-control/' | relative_url }}" class="card__link">See Offshore Platform Control scenario &rarr;</a>

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
