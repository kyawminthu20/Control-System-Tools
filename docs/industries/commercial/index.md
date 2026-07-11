---
layout: default
title: "Commercial Industry Standards Overlay"
description: "Standards path for commercial buildings, light industrial equipment, and BAS-connected panels: NEC, UL 508A, NFPA 79 scope boundaries, IBC, and building automation gaps."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Commercial"
related_standards:
  - name: "NEC"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/commercial.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Commercial</span>
  <h1>Commercial Industry Standards</h1>
  <span class="badge badge--verify">IBC and building automation standards are not in corpus</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Commercial building, light industrial, HVAC, building automation |
| **Markets** | US primary |
| **Special concern** | Building codes, AHJ requirements, lighter safety burden than heavy industry |

> **Corpus note:** Commercial projects often sit at the boundary between facility electrical work and industrial machinery. The corpus is strongest on NEC, NFPA 79, and UL 508A. IBC, local building-code adoption, BAS protocols, and HVAC standards must be added outside the corpus.

---

## Standards Applicability by Project Phase

| Phase | Standards | Purpose |
|-------|-----------|---------|
| **Concept / code path** | NEC, IBC, local building codes | Decide whether the package is facility equipment, a listed panel, or industrial machinery inside a commercial building |
| **Panel design** | NEC, UL 508A | Establish SCCR, labeling, construction, and installation evidence for commercial AHJ review |
| **Field wiring / controls** | NEC Art. 110, 300, 725 | Control routing, Class 2 and Class 3 separation, and installer-facing wiring methods |
| **Machinery scope check** | NFPA 79, IEC 60204-1 | Apply machinery electrical rules only when the package truly behaves as industrial machinery |
| **Turnover / integration** | NEC plus external BAS and building-code documents | Deliver one-lines, schedules, point lists, sequences, and AHJ submittals |

---

## Standards Selection Flow

Evaluate all applicable questions below. Multiple standards paths may apply to a single project.

```text
Is the package general building or facility equipment with no machine hazard?
  YES -> Use NEC plus IBC and local building-code requirements
       -> NFPA 79 usually does not apply

Is a listed panel required by the owner, insurer, or AHJ?
  YES -> Add UL 508A for the panel construction route

Does the package include moving machinery, interlocked access, or machine-specific hazards?
  YES -> Add NFPA 79 and, for international machinery, IEC 60204-1

Does the system connect to BAS or low-voltage building controls?
  YES -> Apply NEC Art. 725 for Class 2 and Class 3 circuit separation
       -> Verify BAS protocol, sequence-of-operations, and controls standards directly
```

---

## Standards Path Summary

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC | <span class="badge badge--complete">Reviewed</span> |
| Building electrical | NEC commercial installation route | <span class="badge badge--complete">Reviewed</span> |
| Panel construction | UL 508A | <span class="badge badge--complete">Reviewed</span> |
| Machinery electrical | NFPA 79 (if machinery present) | <span class="badge badge--complete">Reviewed</span> |
| Building codes | IBC, local building codes | Not in corpus |
| HVAC | ASHRAE, NFPA 90A | Not in corpus |
| Building automation | BACnet, LON | Not in corpus |

---

## Key Engineering Decisions for Commercial Projects

**Facility equipment vs. industrial machinery:**
This boundary decides almost everything. A rooftop unit controller, pump panel, or BAS outstation is usually a commercial facility system governed mainly by NEC and building-code adoption. A packaging line or automated process skid installed inside a commercial building may still need NFPA 79. Make the scope call early and record it.

**Class 2 and Class 3 control wiring:**
Commercial projects often carry a heavier mix of BAS points, thermostats, VAV boxes, and low-voltage signaling than industrial machinery. NEC Article 725 becomes more important here than PL or SIL topics. Keep power-limited circuits segregated from power wiring and define who owns the field terminations, network drops, and controls conduit.

**AHJ and turnover package expectations:**
Commercial review often includes electrical inspectors, building departments, and sometimes fire or mechanical reviewers. Clear submittals matter: one-line, load schedule, panel label set, point list, sequence of operations, and installation instructions. The design is only as good as the package the AHJ can approve.

---

## Commercial Project Kickoff Checklist

- [ ] Record whether the package is facility equipment, a listed control panel, or industrial machinery
- [ ] Confirm the adopted NEC and IBC editions for the jurisdiction before design freeze
- [ ] Decide if UL 508A listing or a field evaluation mark is required
- [ ] Identify every BAS or low-voltage interface and route it under NEC Article 725
- [ ] Build the AHJ submittal set early: one-line, load schedule, panel label, point list, and sequence of operations
- [ ] Add local building, mechanical, and fire-code requirements directly to the project standards register

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/commercial.md`

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
