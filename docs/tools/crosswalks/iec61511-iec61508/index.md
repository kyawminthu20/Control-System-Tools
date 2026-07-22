---
layout: default
title: "IEC 61511 ↔ IEC 61508 Crosswalk"
description: "Application vs. foundation: how IEC 61511 (process SIS) derives from and relates to IEC 61508 (functional safety foundation)."
breadcrumb:
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
  - name: "IEC 61511 ↔ IEC 61508"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
redirect_from:
  - /crosswalks/iec61511-iec61508/
  - /crosswalks/iec61511-iec61508/index.html
review:
  standard: "IEC 61511 ↔ IEC 61508"
  edition: "exact governing revisions not yet recorded — verify on the linked standards pages"
  status: "Review pending"
  coverage: "Application-vs-foundation relationship at topic level; lifecycle mapping summarized, no clause-level determinations."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Crosswalk</span>
  <h1>IEC 61511 ↔ IEC 61508</h1>
  <p>Application vs. foundation: how the process industry sector standard relates to and invokes the mother standard.</p>
</div>

## Purpose

IEC 61508 is the **foundation standard** for functional safety of electrical, electronic, and programmable electronic (E/E/PE) safety-related systems. It covers the full development lifecycle for any safety system across all industries.

IEC 61511 is the **sector application standard** for Safety Instrumented Systems (SIS) in the process industry. It was derived from IEC 61508 and references it extensively, but simplifies many requirements by allowing "proven in use" (prior use) justification for field-installed hardware.

**Key rule:** Engineers operating a SIS at a process plant primarily work under IEC 61511. IEC 61508 is invoked when custom or novel logic solver hardware is developed, or when a "proven in use" argument cannot be made.

---

## Relationship Overview

| Aspect | IEC 61508 | IEC 61511 |
|--------|-----------|-----------|
| **Scope** | All E/E/PE safety-related systems, all industries | Safety Instrumented Systems (SIS) in the process industry |
| **Primary audience** | Safety system developers, logic solver manufacturers | Process plant engineers, SIS integrators |
| **Technology assumption** | Covers novel and custom development from the ground up | Allows "proven in use" subsystems; invokes IEC 61508 for novel devices |
| **SIL range** | SIL 1–4 | SIL 1–4 (SIL 4 effectively excluded for most process applications) |
| **Key differentiator** | Full systematic capability assessment required | Prior use justification accepted per §11.5 |
| **Relationship** | Foundation / mother standard | Derived sector standard |

---

## Lifecycle Structure Comparison

| Phase | IEC 61508 (Part 1, §5–7) | IEC 61511 (Part 1) |
|-------|--------------------------|---------------------|
| **Hazard and risk assessment** | Overall safety lifecycle §7.4 | §8–9: Process hazard analysis, risk assessment |
| **Safety requirements** | Safety requirements allocation §7.5–7.6 | §10: SIL determination (LOPA or risk graph) |
| **SIS design** | Realization §7.7–7.9 (Part 2 hardware, Part 3 software) | §11: Safety requirements specification, SIS design |
| **Integration and commissioning** | Integration §7.10–7.12 | §12: Installation, commissioning, pre-startup |
| **Validation** | Safety validation §7.13 | §12: SIS validation and proof test |
| **Operation and maintenance** | Operation, maintenance §7.14 | §16: Operation, maintenance, proof testing |
| **Modification** | Modification §7.15 | §17: Management of functional safety during modifications |
| **Decommissioning** | Decommissioning §7.16 | §18: Decommissioning |

---

## SIL Framework

Both standards use the same SIL 1–4 scale — the SIL targets and PFDavg bands are fully compatible.

| SIL | PFDavg (demand mode) | Risk reduction factor | Typical process application |
|-----|---------------------|-----------------------|-----------------------------|
| SIL 1 | 0.1 – 0.01 | 10 – 100 | Single-effect shutdowns, low-consequence trips |
| SIL 2 | 0.01 – 0.001 | 100 – 1,000 | ESD, F&G, HIPPS on moderate-consequence hazards |
| SIL 3 | 0.001 – 0.0001 | 1,000 – 10,000 | High-consequence releases; requires rigorous architecture |
| SIL 4 | < 0.0001 | > 10,000 | Rarely used in process industry; nearly always nuclear or specialty |

**SIL determination methods:**
- IEC 61511 favors **LOPA** (Layer of Protection Analysis) — quantitative, with defined credit rules
- IEC 61508 describes risk graph and quantitative risk assessment — LOPA is consistent with IEC 61508 methods
- Both accept multiple methods; LOPA is the de facto process industry standard

---

## Architecture Constraints Comparison

| Constraint | IEC 61508 (Route 1H, Table 3) | IEC 61511 (Table 5) |
|------------|-------------------------------|----------------------|
| **Approach** | Safe Failure Fraction (SFF) + Hardware Fault Tolerance (HFT) matrix | Architectural constraints with prior use allowance |
| **SIL 1** | SFF ≥ 60% with HFT 0, or SFF ≥ 90% with HFT 0 (Type B) | 1oo1 sufficient if PFDavg target is met with prior-use devices |
| **SIL 2** | SFF ≥ 90% with HFT 0, or SFF ≥ 60% with HFT 1 | 1oo2 or 2oo3; prior-use justification can support lower HFT |
| **SIL 3** | SFF ≥ 99% with HFT 0, or SFF ≥ 90% with HFT 1 | Typically requires 2oo3 or 1oo2D with diagnostic coverage |
| **Prior use** | Not applicable — systematic capability assessment required | IEC 61511 §11.5 allows prior use in lieu of full development evidence |

---

## "Proven In Use" (Prior Use) — The Key Differentiator

IEC 61511 §11.5 allows hardware to be accepted into a SIS based on **demonstrated field history** (prior use), without requiring the full IEC 61508 development assessment. This is the most significant practical difference between the two standards.

**Prior use criteria (IEC 61511 §11.5.3):**
- Sufficient operational history in similar service conditions
- Field failure data reviewed and quantified
- No systematic failures attributed to the device design
- Change control maintained — same device revision as in service record

**Implication for field instruments and logic solvers:**
Most certified transmitters, final elements, and safety PLCs used in process plants are accepted under prior use. Vendors typically provide a Safety Manual and a failure rate data sheet (FMEDA report) that supports the prior use claim.

**When prior use is NOT available:**
- Novel sensor technology without field history
- Custom-developed or modified hardware
- First-generation product without a FMEDA or demonstrated service record

In these cases, compliance with IEC 61508 (Parts 2 and 3) is required — typically by the device manufacturer, not the plant engineer.

---

## When to Invoke IEC 61508 Directly

Engineers working under IEC 61511 need to invoke IEC 61508 in these situations:

1. **Custom logic solver development** — developing the safety PLC firmware or hardware from the ground up
2. **Novel field device** — using a transmitter or valve with no prior use history and no FMEDA
3. **SIL 3+ applications** — where the IEC 61511 architectural constraints cannot be satisfied without deeper systematic capability evidence
4. **Competent authority requirement** — when a regulator or certifying body specifically requires IEC 61508 functional safety assessment for the SIS
5. **IEC 61511 §1.5 clause** — explicitly requires that subsystems based on novel technology comply with IEC 61508

---

## Clause / Section Cross-Reference

| IEC 61511 Clause | Topic | IEC 61508 Reference |
|-----------------|-------|---------------------|
| §1 — Scope | SIS process industry application | IEC 61508-1 §1 |
| §5 — Competence | Functional safety management | IEC 61508-1 §6 |
| §8 — Overall safety lifecycle | Safety lifecycle structure | IEC 61508-1 §5 |
| §9 — Hazard and risk assessment | HAZOP, consequence analysis | IEC 61508-1 §7.4 |
| §10 — SIL determination | LOPA, risk graph | IEC 61508-1 §7.6 |
| §11 — Safety requirements specification | SRS and SIS design | IEC 61508-1 §7.5, Part 2 §7 |
| §11.5 — Prior use | Proven in use criteria | IEC 61508-2 §7.4.2 (systematic capability) |
| §11.9 — SIS software requirements | Application programming | IEC 61508-3 §7 |
| §12 — SIS installation and commissioning | Integration and validation | IEC 61508-1 §7.10–7.13 |
| §13 — SIS operation and maintenance | Operational safety | IEC 61508-1 §7.14 |
| §16 — Proof testing | Periodic testing strategy | IEC 61508-1 §7.14 |
| §17 — Modification management | Change control | IEC 61508-1 §7.15 |
| §18 — Decommissioning | End of life | IEC 61508-1 §7.16 |

---

## Certification and Assessment

| Aspect | IEC 61508 | IEC 61511 |
|--------|-----------|-----------|
| **Product certification** | Third-party functional safety assessment by TÜV, Exida, Bureau Veritas, etc. | No product certification — compliance demonstrated by plant FSM plan |
| **Who does the work** | Logic solver / device manufacturer | Plant owner, SIS integrator, competent engineer |
| **Evidence required** | Functional safety assessment report, FMEDA, systematic capability level (SCL) | FSM plan, safety requirements specification, HAZOP/SIL determination records, proof test procedures |
| **Third-party role** | Required for SIL-certified product claims | Optional; sometimes required by regulator or owner specification |

---

## Corpus Status

| Topic | Standards | Corpus Status |
|-------|-----------|---------------|
| Functional safety foundation | IEC 61508 (4 files) | <span class="badge badge--reviewed">Reviewed</span> |
| Process SIS lifecycle | IEC 61511 (4 files) | <span class="badge badge--reviewed">Reviewed</span> |
| Machinery functional safety | ISO 13849-1, IEC 62061 | <span class="badge badge--reviewed">Reviewed</span> |
| LOPA methodology | (within IEC 61511 corpus) | <span class="badge badge--reviewed">Reviewed</span> |
| Notified body assessment process | External to corpus | Out of scope for this corpus |

---

## Practical Summary

**If you are a process plant engineer, SIS integrator, or project team operating a safety system at a refinery, chemical plant, or similar facility:**
→ Work under **IEC 61511**. Use vendor-supplied FMEDA data and safety manuals to support prior use claims for field devices and logic solvers.

**If you are a logic solver manufacturer, safety PLC firmware developer, or developing novel safety hardware:**
→ Comply with **IEC 61508 Parts 2 and 3**. Obtain third-party functional safety assessment (SIL certification) for your product.

**If your IEC 61511 project reaches SIL 3 or uses non-prior-use devices:**
→ Invoke **IEC 61508** requirements explicitly, coordinate with the device manufacturer's safety documentation, and consider engaging a competent functional safety assessor.

<a href="{{ '/tools/crosswalks/' | relative_url }}" class="card__link">&larr; All Crosswalks</a>
