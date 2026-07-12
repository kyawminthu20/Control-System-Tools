---
layout: default
title: "IEC 61508 — Functional Safety of E/E/PE Systems"
description: "IEC 61508:2010 — the foundational functional safety standard for electrical, electronic, and programmable electronic systems."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "IEC 61508"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/"
related_standards:
  - name: "IEC 62061 (machinery application)"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511 (process application)"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1 (machinery PL)"
    url: "/standards/functional-safety/iso-13849-1/"
lifecycle_stage:
  - name: "Safety Architecture"
    slug: "safety-architecture/"
review:
  standard: "IEC 61508"
  edition: "2010"
  status: "Reviewed"
  coverage: "Lifecycle overview and key concepts; worked example pending"
  last_reviewed: "April 2026"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · IEC 61508</span>
  <h1>IEC 61508:2010 — Functional Safety of E/E/PE Safety-Related Systems</h1>
</div>

## Quick Start

- IEC 61508 is the **parent/foundational standard** — use [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) (machinery) or [IEC 61511]({{ '/standards/functional-safety/iec-61511/' | relative_url }}) (process) instead for application work
- All SIL-rated applications ultimately trace back to IEC 61508 requirements; the sector standards are derived from it
- SIL 4 exists in the standard but is almost never used in industrial automation — it is designed for nuclear and aviation
- Understanding Part 2 (hardware) and Clause 7 (lifecycle) explains why IEC 62061 and IEC 61511 are structured the way they are
- Certified safety PLCs shift the Part 3 software burden to the manufacturer — this is why they dominate safety applications

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 61508 |
| **Edition** | 2010 (Parts 1–7) |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global |
| **Scope** | Generic E/E/PE safety-related systems across all industries |
| **Repository** | `rag/international/functional_safety/iec_61508/` |
**Purpose:** IEC 61508 is the umbrella standard for functional safety of electrical, electronic, and programmable electronic (E/E/PE) safety-related systems. It defines the SIL framework, hardware integrity concepts, software requirements, and 16-phase safety lifecycle that IEC 62061 and IEC 61511 both derive from.

---

## Seven-Part Structure

| Part | Scope | Who typically applies it |
|------|-------|--------------------------|
| **Part 1** — General requirements | Scope, definitions, safety lifecycle, functional safety management | All users; foundational concepts |
| **Part 2** — Hardware requirements | HFT, SFF, Type A/B classification, PFHd/PFDavg | Hardware designers, safety device manufacturers |
| **Part 3** — Software requirements | Software SIL, development lifecycle, techniques and measures | Safety PLC firmware developers; machine builders (application layer only) |
| **Part 4** — Definitions and abbreviations | Normative definitions for Parts 1–3 | Reference use |
| **Part 5** — Risk determination methods | Examples: risk graph, LOPA, hazard matrix | Risk assessment practitioners |
| **Part 6** — Guidelines on Parts 2 and 3 | Informative guidance for implementers | Implementers working from IEC 61508 directly |
| **Part 7** — Techniques and measures overview | Informative catalog of approaches | Reference use |

Parts 1–3 are normative. Parts 4–7 are informative or supporting.

---

## SIL Levels — Both Modes

| SIL | PFHd (high-demand mode) | PFDavg (low-demand mode) | Typical application |
|-----|-------------------------|--------------------------|---------------------|
| **SIL 1** | 10⁻⁶ to < 10⁻⁵ /hr | 10⁻² to < 10⁻¹ | Simple interlocks, basic process shutdowns |
| **SIL 2** | 10⁻⁷ to < 10⁻⁶ /hr | 10⁻³ to < 10⁻² | Most machinery safety functions, typical process SIS |
| **SIL 3** | 10⁻⁸ to < 10⁻⁷ /hr | 10⁻⁴ to < 10⁻³ | High-consequence process industry, critical machinery |
| **SIL 4** | 10⁻⁹ to < 10⁻⁸ /hr | 10⁻⁵ to < 10⁻⁴ | Nuclear reactor protection, aviation — not industrial automation |

**Mode selection:** Use **PFHd** for high-demand mode (safety function demanded at least once per year — machinery per IEC 62061). Use **PFDavg** for low-demand mode (safety function rarely demanded, tested periodically — process SIS per IEC 61511). Using the wrong metric is a serious calculation error.

---

## Hardware Concepts (Part 2)

These concepts from Part 2 underpin all modern functional safety hardware design and appear in the SILCL tables of IEC 62061 Annex A.

### Hardware Fault Tolerance (HFT)

The number of faults a subsystem can tolerate while maintaining its safety function:

| HFT | Architecture | Implication |
|-----|-------------|-------------|
| 0 | 1oo1 — single channel | One fault defeats the safety function |
| 1 | 1oo2 — dual channel | One fault tolerated |
| 2 | 2oo3 — voted triple | Two simultaneous faults tolerated |

### Safe Failure Fraction (SFF)

`SFF = (λS + λDD) / (λS + λD)` — proportion of failures that are safe or detected by diagnostics. Higher SFF enables a higher SIL claim at the same HFT.

### Type A vs Type B Subsystems

| Type | Criterion | Examples | SIL impact |
|------|-----------|---------|------------|
| **Type A** | All failure modes well defined and quantifiable | Relays, contactors, pressure switches | Can claim higher SIL at lower HFT |
| **Type B** | Not all failure modes known | PLCs, microprocessors, complex electronics | Requires higher HFT or SFF to claim same SIL |

**Combined effect:** A Type B subsystem (any PLC-based system) with SFF between 90–99% requires HFT 1 (dual channel) to claim SIL 3. This is why SIL 3 machinery systems almost always use redundant safety PLC architectures. The SILCL tables in [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) Annex A are the machinery-domain translation of these Part 2 concepts.

---

## The 16-Phase Safety Lifecycle (Clause 7)

Both IEC 62061 and IEC 61511 are structured as implementations of this lifecycle in their respective domains.

| Phase group | Phases | Description | Maps to in sector standards |
|-------------|--------|-------------|----------------------------|
| **Concept** | 1–3 | Concept, scope definition, hazard and risk analysis | ISO 12100 risk assessment; IEC 62061 Clause 5 scope; IEC 61511 Clause 8 |
| **Requirements** | 4–7 | Safety requirements, allocation, O&M planning, validation planning | IEC 62061 Clauses 5–6 (SIL determination, safety function spec); IEC 61511 Clauses 9–10 |
| **Realisation** | 8–13 | E/E/PE system design and build, other technology, installation, validation | IEC 62061 Clauses 6–8 (design, build, validate); IEC 61511 Clauses 11–12 |
| **Operation** | 14–16 | Operation, maintenance, modification, decommissioning | IEC 62061 Clause 8 + maintenance docs; IEC 61511 Clause 13 |

**Functional safety management** spans all phases: documentation, competency requirements, and independence requirements. Independence between design and validation teams is required from SIL 2 upward, and organizational separation is required at SIL 3+.

---

## When To Use IEC 61508 Directly

| Situation | Use IEC 61508 directly? | Preferred approach |
|-----------|------------------------|-------------------|
| Machine builder deploying safety functions on machinery | No | [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) |
| Process plant implementing a safety instrumented system | No | [IEC 61511]({{ '/standards/functional-safety/iec-61511/' | relative_url }}) / ISA 84 |
| Safety PLC or safety relay manufacturer seeking product certification | Yes | IEC 61508 Parts 1–3 (TÜV or UL certification) |
| System spanning machinery and process domains | Consider | IEC 61508 as baseline; sector standards for each domain layer |
| No applicable sector standard for the application domain | Yes | IEC 61508 directly |
| Custom safety system on non-certified hardware | Yes | IEC 61508 Parts 2 and 3 in full |

---

## Common Mistakes

1. **Applying IEC 61508 directly to machinery** when IEC 62061 is available and simpler — IEC 62061 is the correct standard for machinery; IEC 61508 adds scope and complexity that is not needed

2. **Treating SIL 4 as a realistic target** for industrial automation — SIL 4 is designed for nuclear reactor protection and aviation instrumentation; achieving SIL 4 requires diverse redundancy, formal verification, and organizational independence that industrial projects cannot sustain

3. **Confusing PFHd with PFDavg** — using the wrong metric entirely; a system in high-demand mode evaluated against PFDavg thresholds may appear to meet requirements while actually having a dangerous failure rate that exceeds the tolerable risk by orders of magnitude

4. **Applying full Part 3 software requirements to application code on a certified safety PLC** — the PLC manufacturer's certification already addresses the firmware-level Part 3 requirements; applying them again to ladder logic is unnecessary and not what the standard requires

5. **Equating the SIL of a component with the SIL of the system** — a component rated SIL 3 does not automatically produce a SIL 3 system; the system SIL depends on the complete architectural analysis including HFT, SFF, CCF (common cause failures), and PFHd/PFDavg calculations

6. **Not maintaining independence between E/E/PE realisation and safety validation teams at SIL 3+** — at SIL 3 and SIL 4, the standard requires organizational separation between the design team and the validation team; functional independence within the same team is insufficient

---

## Practical Checklist

- [ ] Confirm which mode applies (high-demand → PFHd; low-demand → PFDavg) before starting calculations
- [ ] Determine whether a sector standard applies before deciding to use IEC 61508 directly
- [ ] Identify all hazardous events and their associated required SIL targets through risk assessment
- [ ] Classify each subsystem as Type A or Type B for HFT/SFF analysis
- [ ] Verify that the safety PLC certificate states the SIL level and any restrictions on application programming
- [ ] Confirm that the architectural constraints (HFT × SFF × Type) support the target SIL for each subsystem
- [ ] Establish competency documentation for all persons performing safety lifecycle activities
- [ ] Plan independence between design and validation at the level required for the target SIL
- [ ] Establish proof test intervals for all safety functions (low-demand mode) or diagnostic coverage targets (high-demand mode)
- [ ] Ensure all lifecycle phases are represented in the safety plan, from hazard analysis through decommissioning

---

## Lifecycle Application Table

| IEC 61508 lifecycle phase | Typical deliverable | SIL-dependent rigor |
|--------------------------|--------------------|--------------------|
| Hazard and risk analysis (Phase 3) | Hazard log, SIL targets per safety function | Higher SIL → more conservative tolerable risk targets |
| Safety requirements allocation (Phase 5) | Safety requirements specification per protection layer | Higher SIL → greater allocation scrutiny |
| E/E/PE system realisation (Phase 9) | Hardware architecture, PFHd/PFDavg calculations, software validation records | Higher SIL → more redundancy, coverage, independence |
| Safety validation (Phase 13) | Safety validation report | Higher SIL → independent validation team |
| Operation and maintenance (Phase 14) | Proof test procedure and records | Higher SIL → shorter proof test intervals |
| Modification (Phase 15) | Change impact analysis, revalidation records | All SIL levels — any change to safety function must be revalidated |

---

## Related Standards

- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — applies IEC 61508 to machinery safety control systems; the correct standard for machine builders
- [IEC 61511]({{ '/standards/functional-safety/iec-61511/' | relative_url }}) — applies IEC 61508 to process industry safety instrumented systems
- [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — alternative machinery safety standard using Performance Level (PL) rather than SIL

---

<a href="{{ '/standards/functional-safety/' | relative_url }}" class="card__link">&larr; Functional Safety family</a>
