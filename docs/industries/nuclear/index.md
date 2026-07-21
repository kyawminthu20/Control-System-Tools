---
layout: default
title: "Nuclear Industry Standards Overlay"
description: "Standards path for nuclear and important-to-safety controls: NEC and IEC 60204-1 baseline with explicit corpus gaps for IEC 61513, IEEE 603, and nuclear QA requirements."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Nuclear"
related_standards:
  - name: "NEC"
    url: "/standards/us-electrical/nec/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/nuclear.md"
review:
  standard: "NEC · IEC 60204-1 baseline; IEC 61513 / IEEE 603 gaps flagged"
  edition: "exact governing revisions not yet recorded — verify on the linked standards pages"
  status: "Review pending"
  coverage: "Overlay routing for nuclear/important-to-safety controls; nuclear-specific standards are explicitly flagged as corpus gaps, not covered."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Nuclear</span>
  <h1>Nuclear Industry Standards</h1>
  <span class="badge badge--verify">IEC 61513 and IEEE 603 are not in corpus</span>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Nuclear power generation and fuel processing |
| **Typical systems** | Reactor protection, plant control, radiation monitoring |
| **Markets** | US (NRC) and international (IAEA) |
| **Special concern** | Nuclear QA (10 CFR 50 Appendix B), seismic qualification, strict traceability |

> **Corpus note:** The reference library helps with general electrical workmanship, panel construction, and verification structure. It does not contain the nuclear safety, QA, software, independence, or qualification standards needed for reactor or important-to-safety I&C decisions.

---

## Standards Applicability by Project Phase

| Phase | Standards | Purpose |
|-------|-----------|---------|
| **Safety classification** | IEEE 603, IEC 61513, site licensing basis | Determine whether the function is safety-related, important-to-safety, or balance-of-plant only |
| **Electrical architecture** | NEC, IEC 60204-1 | Apply general electrical and machinery practices to non-safety portions and supporting equipment |
| **QA and procurement** | 10 CFR 50 Appendix B, ASME NQA-1, project QA program | Control pedigree, supplier qualification, document retention, and configuration release |
| **Digital I&C / software** | IEEE 7-4.3.2, IEC 61513, site cyber and software procedures | Address independence, determinism, software lifecycle, and verification depth |
| **Qualification and turnover** | IEEE 603, IEC 61513, seismic and environmental qualification standards | Verify separation, redundancy, witnessed testing, and lifecycle traceability |

---

## Standards Selection Flow

```text
Is the function safety-related or important-to-safety?
  YES -> Route the design under IEEE 603 / IEC 61513 and the plant QA program
       -> Treat NEC and IEC 60204-1 as supporting electrical references only

Is the package balance-of-plant equipment with no nuclear safety claim?
  YES -> NEC and IEC 60204-1 may cover the general electrical baseline
       -> Still verify site QA, documentation, and procurement controls

Does the system include digital logic, software changes, or networked I&C?
  YES -> Add nuclear digital I&C governance, configuration control, and witness testing

Does the equipment need seismic or environmental qualification?
  YES -> Pull the qualification route into the design basis before procurement
```

---

## Standards Path Summary

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical baseline | NEC | <span class="badge badge--reviewed">Reviewed</span> |
| International electrical baseline | IEC 60204-1 | <span class="badge badge--reviewed">Reviewed</span> |
| Nuclear QA | 10 CFR 50 Appendix B | Not in corpus |
| Nuclear I&C | IEEE 603, IEEE 7-4.3.2 | Not in corpus |
| IEC nuclear I&C | IEC 61513, IEC 62138 | Not in corpus |
| Safety classification | RG 1.152, IEEE 279 | Not in corpus |

---

## Key Engineering Decisions for Nuclear Projects

**Safety-related boundary vs. balance-of-plant scope:**
The most important question is whether the package performs a nuclear safety claim or only supports non-safety plant operation. If it is safety-related or important-to-safety, IEEE 603 and IEC 61513 become primary and the local machine-electrical corpus is only supporting context. If it is strictly balance-of-plant, NEC and IEC 60204-1 may still be useful for the electrical baseline, but site QA and configuration rules usually still apply.

**Independence, separation, and redundancy:**
Nuclear projects usually need stricter physical and functional separation than normal machine control systems. Cable routing, power distribution, channel independence, and defeat or bypass management should be treated as architectural decisions with formal review points, not just panel-layout details.

**Pedigree and configuration control:**
Component pedigree, revision control, software baselines, and witness points are acceptance items. A technically correct design can still fail turnover if the supplier documentation trail is incomplete. Build the documentation structure at the same time as the hardware design.

---

## Nuclear Project Kickoff Checklist

- [ ] Classify the package as safety-related, important-to-safety, or balance-of-plant before detailed design
- [ ] Confirm which nuclear standards and site QA program govern the work: IEEE 603, IEC 61513, Appendix B, NQA-1, or plant-specific requirements
- [ ] Define separation, redundancy, and independence rules before cable and cabinet layouts are frozen
- [ ] Identify qualification needs early: seismic, environmental, EMI, software, and cyber controls
- [ ] Start the component pedigree and document-retention dossier at procurement kickoff
- [ ] Build a witnessed verification matrix covering FAT, SAT, hold points, and as-built configuration records

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/nuclear.md`

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
