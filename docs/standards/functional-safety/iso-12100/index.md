---
layout: default
title: "ISO 12100 — Risk Assessment and Risk Reduction"
description: "ISO 12100:2010 — the foundation risk assessment standard for machinery, CE marking, and safety function design."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "ISO 12100"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
lifecycle_stage:
  - name: "Concept"
    slug: "concept/"
  - name: "Risk Assessment"
    slug: "risk-assessment/"
  - name: "Safety Architecture"
    slug: "safety-architecture/"
review:
  standard: "ISO 12100"
  edition: "2010"
  status: "Review pending"
  coverage: "Risk-assessment methodology; worked example pending. PLr attribution and CE-marking wording corrected July 2026"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · ISO 12100</span>
  <h1>ISO 12100:2010 — Risk Assessment and Risk Reduction</h1>
</div>

## Quick Start

For practitioners new to ISO 12100:

- **Apply ISO 12100 first** — before ISO 13849-1, IEC 62061, or any other safety standard. Those standards require ISO 12100 risk assessment outputs as inputs.
- **ISO 12100 does not give you PLr** — it gives you the risk assessment. The required Performance Level is estimated from the risk graph in **ISO 13849-1 Annex A**; a required SIL is determined by the method in **IEC 62061**. Cite the design standard, not ISO 12100, as the normative source of PLr or SIL.
- **The three-step method is the harmonized route, not the legal text itself** — EU machinery law requires a documented risk assessment and compliance with the applicable essential health and safety requirements. Applying EN ISO 12100 is voluntary but confers presumption of conformity for the requirements it covers.
- **The process is iterative** — after any risk reduction measure is applied, return to hazard identification and verify no new hazards have been introduced.
- **Document everything** — a risk assessment without adequate written records is non-compliant, even if the engineering decisions were correct.

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | ISO 12100 |
| **Edition** | 2010 |
| **Publisher** | International Organization for Standardization (ISO) |
| **Jurisdiction** | Global; Type A standard under EU Machinery Directive and EU Machinery Regulation 2023/1230 |
| **Scope** | Risk assessment and risk reduction for machinery |
| **Repository** | `rag/international/functional_safety/iso_12100/` |
**Purpose:** ISO 12100 is the foundation standard for machinery safety. It provides the principles and methodology for risk assessment and risk reduction. All other machinery safety standards (ISO 13849-1, IEC 62061, IEC 60204-1) assume ISO 12100 has been applied first.

---

## The Iterative Risk Assessment Process

ISO 12100 defines a closed-loop, four-step process. The loop repeats until residual risk is judged acceptable.

| Step | Activity | Clause |
|------|----------|--------|
| 1 | **Hazard identification** — systematically identify all hazards, hazardous situations, and hazardous events across the full machine lifecycle | 4.2 / Annex A |
| 2 | **Risk estimation** — characterise each hazard using severity (S), frequency of exposure (F), and possibility of avoidance (P) | Clause 5 |
| 3 | **Risk evaluation** — judge whether the estimated risk is acceptable, considering state of the art, legal requirements, and known incidents | Clause 6 |
| 4 | **Risk reduction** — apply measures in the mandatory three-step sequence; return to Step 1 to verify no new hazards introduced | Clause 7 |

The loop is exited only when all identified hazards have been evaluated as acceptable after reduction measures have been applied and verified.

---

## Risk Estimation Elements (Clause 5)

ISO 12100 Clause 5 estimates risk from the **severity of harm** and the **probability of
its occurrence** (exposure, occurrence of a hazardous event, and the possibility of
avoiding or limiting harm). Clause 5 does not itself produce a PLr or a SIL.

The coded **S/F/P parameters and the risk graph** below belong to **ISO 13849-1 Annex A**,
which is the normative source of PLr. IEC 62061 has its own, differently parameterised
method for determining a required SIL. The ISO 12100 risk estimation is the engineering
judgement those methods encode — the table maps one to the other.

| Parameter | Symbol | Level | Definition |
|-----------|--------|-------|-----------|
| **Severity of harm** | S | S1 | Slight — normally reversible injury (bruising, minor laceration) |
| | | S2 | Serious — normally irreversible injury including death (amputation, permanent disability, fatality) |
| **Frequency and duration of exposure** | F | F1 | Seldom to infrequent, and/or short duration |
| | | F2 | Frequent to continuous, and/or long duration |
| **Possibility of avoiding or limiting harm** | P | P1 | Possible under specific conditions (hazard visible, sufficient reaction time) |
| | | P2 | Scarcely possible (sudden action, high speed, person constrained) |

**PLr lookup:** The combination of S, F, and P determines PLr via the **ISO 13849-1 Annex A** risk graph — that annex, not ISO 12100, is the normative source. S2/F2/P2 yields PLr e (the highest requirement); S1/F1/P1 yields PLr a (the lowest).

---

## The Three-Step Method (Clause 7)

The three-step method is mandatory in the order shown. A lower-priority step cannot substitute for a higher-priority step where the higher step is reasonably practicable.

| Step | Method | Examples | Notes |
|------|--------|---------|-------|
| **Step 1** | Inherently safe design (ISD) | Eliminate nip point by geometry change; use SELV voltage; reduce travel speed to non-injurious level; substitute less hazardous material | Preferred — eliminates or reduces hazard at source; not defeatable by user behaviour |
| **Step 2** | Safeguarding and protective measures | Fixed guards; interlocked movable guards (ISO 14119); light curtains / area scanners (IEC 61496); two-hand controls (ISO 13851); STO/SS1/SLS safety functions (IEC 61800-5-2) | Introduces safety functions — PL or SIL must be determined per ISO 13849-1 or IEC 62061 |
| **Step 3** | Information for use | Warning labels (ISO 11684); operator manual; PPE specification; lockout/tagout procedure; training requirements | Addresses residual risk only — effectiveness depends on human compliance; weakest protection |

---

## Key Clauses

| Clause | Topic | Key Output |
|--------|-------|-----------|
| 4 | Risk assessment principles | Iterative process definition; machine limits; documentation requirements |
| 5.3 | Severity of harm | S1/S2 classification |
| 5.4 | Frequency and duration of exposure | F1/F2 classification |
| 5.5 | Probability of occurrence of hazardous event | Reliability, human error factors |
| 5.6 | Possibility of avoiding or limiting harm | P1/P2 classification |
| 6 | Risk evaluation | Acceptability decision; state-of-the-art benchmark |
| Annex A | Normative hazard list | Checklist of 8 hazard categories with sub-categories |

---

## When To Use ISO 12100

| Situation | Use ISO 12100? |
|-----------|---------------|
| Starting a new machine design | Yes — required before any other safety standard |
| Determining PLr for a safety function | As an input — the PLr itself comes from the ISO 13849-1 Annex A risk graph |
| Determining SIL target for a safety function | As an input — the SIL target itself comes from the IEC 62061 SIL determination method |
| Modifying an existing machine | Yes — reassess affected hazards; verify no new hazards introduced |
| Preparing CE marking technical file | Yes — EU machinery law requires a documented risk assessment; EN ISO 12100 is the standard methodology used to produce it |
| Machine-type-specific standard exists (Type C) | Recommended — use ISO 12100 to fill gaps not addressed by Type C |
| Product already has full Type C standard coverage | Conditional — ISO 12100 still governs hazards not covered by the Type C standard |
| Electrical safety design (wiring, enclosures) | Indirect — ISO 12100 identifies electrical hazards; IEC 60204-1 implements protective measures |

---

## Common Mistakes

1. **Starting with ISO 13849-1 instead of ISO 12100.** The ISO 13849-1 Annex A risk graph cannot be applied meaningfully without a completed risk assessment behind it. Skipping ISO 12100 produces PLr values that are not grounded in a systematic hazard analysis.

2. **Incomplete lifecycle coverage.** Hazard identification limited to normal production operation misses maintenance, cleaning, setup, and decommissioning — where a disproportionate share of serious accidents occur.

3. **Accepting S1/F1/P1 without justification.** Each parameter must be supported by documented reasoning. Defaulting to the most favourable parameters without evidence is a common audit finding.

4. **Using Step 3 to address hazards that Step 1 or Step 2 could reduce.** A warning label on a machine that could have been guarded does not satisfy the three-step hierarchy and creates regulatory exposure.

5. **Not re-entering the loop after applying protective measures.** New hazards introduced by safeguards (e.g., a light curtain mounting bracket creating a new shear point) are missed if the iterative loop is not completed.

6. **Treating the risk assessment as a document-after-the-fact exercise.** ISO 12100 requires the assessment to drive design decisions. A risk assessment written after the machine is built cannot satisfy this requirement — it can only document decisions already made, not influence them.

---

## Practical Checklist

Work through these items for each machine project:

- [ ] Machine limits defined: spatial, time, power, and use limits documented
- [ ] Intended use and reasonably foreseeable misuse documented
- [ ] Hazard identification completed using Annex A as checklist for all lifecycle stages
- [ ] Risk estimation completed for each hazard: S, F, and P assigned with documented reasoning
- [ ] Risk evaluation completed for each hazard: acceptable or not acceptable, with reasoning
- [ ] Step 1 (ISD) applied first for each unacceptable risk; design changes documented
- [ ] Step 2 (safeguarding) applied where ISD insufficient; safety function identified
- [ ] PLr or SIL determined for each Step 2 safety function (ISO 13849-1 or IEC 62061)
- [ ] Step 3 (information for use) addresses remaining residual risk only
- [ ] Iterative loop completed: re-assessed after each measure applied; no new hazards unaddressed
- [ ] Residual risks documented and addressed in operating instructions

---

## Lifecycle Application

| Lifecycle Stage | ISO 12100 Activity |
|----------------|-------------------|
| **Concept** | Define machine limits; define intended use and foreseeable misuse |
| **Preliminary design** | Initial hazard identification (Annex A); first risk estimation pass |
| **Detailed design** | Apply three-step method; determine PLr/SIL for safety functions; update hazard list |
| **Prototype / commissioning** | Verify risk reduction measures are effective; complete iterative loop |
| **Production / normal use** | Information for use in place; residual risks communicated to users |
| **Maintenance and cleaning** | Hazards at these stages assessed and addressed (lockout/tagout, safe isolation) |
| **Modification** | Re-enter risk assessment for affected hazards; verify no new hazards introduced |
| **Decommissioning** | Hazardous energy isolation, hazardous material disposal addressed |

---

## Next Steps After ISO 12100

After completing the risk assessment, use the following standards to design and validate the safety functions identified in Step 2:

- [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — Performance Level methodology for safety-related parts of control systems; its Annex A risk graph determines PLr, informed by the ISO 12100 risk estimation
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — SIL methodology for electrical/electronic/programmable safety-related control systems; parallel path to ISO 13849-1
