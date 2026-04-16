---
layout: default
title: "Petroleum / Oil and Gas Industry Standards Overlay"
description: "Standards path for oil and gas onshore facilities: IEC 61511 SIS, IEC 60079 hazardous area, NEC 500–505, IEC 60204-1."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Petroleum"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
  - name: "IEC 60079"
    url: "/standards/hazardous-area/iec-60079/"
  - name: "NEC (Art. 500–505)"
    url: "/standards/us-electrical/nec/"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Petroleum / Oil and Gas</span>
  <h1>Petroleum and Oil and Gas Standards</h1>
  <span class="badge badge--complete">Phase 11 — Corpus Complete</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Petroleum, oil and gas — onshore upstream / midstream / downstream |
| **Typical systems** | ESD, F&G, HIPPS, wellhead control, pipeline control, compressor control |
| **Markets** | US, international |
| **Special concerns** | Hazardous areas (Ex), Safety Instrumented Systems (SIS), process safety management |

---

## Standards Applicability by Project Phase

| Phase | Standards | Purpose |
|-------|-----------|---------|
| **Concept / HAZOP** | IEC 61511 §5–6, ISO 12100 | Hazard identification, consequence assessment |
| **SIL Determination** | IEC 61511 §9 (LOPA), IEC 61508 | Determine required SIL for each SIF |
| **SIS Design** | IEC 61511 §10–11, IEC 61508 Part 2/3 | Logic solver selection, SIF architecture, PFDavg calculation |
| **Ex Equipment Selection** | IEC 60079-0, IEC 60079-10-1, IEC 60079-11 | Zone classification, EPL/T-code selection, IS barrier sizing |
| **Electrical Design** | IEC 60204-1, NEC Art. 500/504/505 | Machine electrical, US hazardous location wiring |
| **Installation** | IEC 60079-14, NEC Art. 300/250 | Cable selection, IS segregation, equipotential bonding |
| **Commissioning** | IEC 61511 §12, IEC 60079-14 §6 | SIS FAT/SAT, Ex installation initial verification |
| **Maintenance** | IEC 61511 §16 (proof testing), IEC 60079-17 | Periodic SIF proof tests, Ex inspection regime |

---

## Standards Selection Flow

```
Is the installation in a hazardous area (flammable gas/vapor)?
  YES → Classify zones per IEC 60079-10-1
       → Select Ex equipment by EPL, gas group, T-code (IEC 60079-0)
       → US installation: NEC Art. 505 (Zone) or Art. 500 (Division)
       → IS field devices: IEC 60079-11 + entity parameter check

Does the process have a credible loss-of-containment hazard?
  YES → Perform HAZOP (IEC 61511 §5)
       → Determine if a Safety Instrumented Function (SIF) is required
       → Run LOPA to establish SIL target
       → Design SIF per IEC 61511 §10

Is the SIL target ≥ SIL 3, or is the logic solver a custom design?
  YES → Apply IEC 61508 directly for logic solver development
  NO  → IEC 61511 reference to IEC 61508 is sufficient
```

---

## Standards Path Summary

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical installation | NEC Art. 240, 250, 300, 500, 504, 505 | <span class="badge badge--complete">Complete</span> |
| Machine electrical design | IEC 60204-1 | <span class="badge badge--complete">Complete</span> |
| Process safety (SIS) | IEC 61511 | <span class="badge badge--complete">Complete</span> |
| SIS foundation | IEC 61508 | <span class="badge badge--complete">Complete</span> |
| Hazardous area equipment | IEC 60079 (6 parts) | <span class="badge badge--complete">Complete</span> |
| API standards | API 14C, API 670 | Not in corpus |

---

## Key Engineering Decisions for O&G

**Zone vs. Division classification:**
IEC Zone (Art. 505) is preferred when using ATEX/IECEx certified equipment. NEC Division (Art. 500) is used on legacy US installations. Both are legally valid in the US — verify with AHJ.

**Zener barrier vs. galvanic isolator:**
Use zener barriers where a dedicated IS earth ≤1 Ω is available and galvanic isolation is not needed. Use galvanic isolators where multiple ground loops cause measurement errors or where the field device is floating. See [IEC 60079-11]({{ '/standards/hazardous-area/iec-60079/' | relative_url }}).

**SIL 2 vs. SIL 3 architecture:**
SIL 2 SIFs can typically be achieved with 1oo2 or 2oo3 voted architectures using proven-in-use devices. SIL 3 generally requires 1oo2D or 2oo3 with hardware fault tolerance ≥2 and full IEC 61508 application for the logic solver.

---

## Pre-Commissioning Compliance Checklist

- [ ] Area classification drawing current, signed, and revision-controlled
- [ ] All Ex equipment certificates verified against IECEx/ATEX database (not just nameplate)
- [ ] EPL, gas group, and T-code verified for each Ex device
- [ ] IS entity parameters calculated and documented for every IS loop
- [ ] IS earth resistance measured and confirmed ≤1 Ω (zener barrier loops)
- [ ] Equipotential bonding verified on all metallic structures
- [ ] SIS FAT completed with witnessed proof tests for each SIF
- [ ] SIL verification report completed and accepted
- [ ] Proof test procedures written and approved (per IEC 61511 §16)
- [ ] Ex installation initial verification certificate issued (IEC 60079-14 §6)

---

<a href="{{ '/implementation/scenarios/oil-gas-process-skid/' | relative_url }}" class="card__link">See Oil &amp; Gas Process Skid scenario &rarr;</a>

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
