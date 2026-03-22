---
layout: default
title: "Lifecycle Stage 2 — Standards Selection"
description: "Identify all applicable standards, resolve type-A/B/C hierarchy, and determine the PL or SIL pathway before detailed design begins."
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "2. Standards Selection"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 02</span>
  <h1>Standards Selection</h1>
</div>

## 1. Purpose of This Stage

This stage translates the concept-stage outputs — system description, boundary definition, market identification, and machine type — into a **definitive, project-specific register of applicable standards** that will govern all subsequent design, build, verification, and documentation activities.

Standards selection is not administrative. It is an engineering decision with direct consequences:

- Selecting the wrong standards means designing to requirements that do not satisfy the applicable regulatory framework — resulting in non-compliance discovered at commissioning, shipment, or audit
- Missing a type-C standard means designing to generic type-B requirements when more specific (and often more stringent or more permissive) requirements exist for that machine type
- Failing to identify conflicts between standards (e.g., NFPA 79 vs IEC 60204-1 wire color conventions) means discovering them during detailed design when changes are expensive
- Not deciding the PL vs SIL pathway at this stage means the risk assessment in Stage 3 cannot assign targets using the correct methodology

> **This stage answers: What rules are we designing to, and where those rules conflict, which takes precedence?**

---

## 2. Entry Criteria

This stage begins when **Stage 1 (Concept) exit criteria are met**.

### Required Inputs

| Input | Source (Stage) | Why It Matters |
|-------|---------------|----------------|
| System description | Stage 1 | Determines which type-C standards apply based on machine function |
| Machine / system boundary definition | Stage 1 | Determines what is inside the scope of standards compliance |
| Market and regulatory identification | Stage 1 | Determines which national/regional codes and directives apply |
| Operating mode definitions | Stage 1 | Some standards have specific requirements per operating mode (e.g., ISO 10218 for collaborative robot modes) |
| Type-C standard preliminary identification | Stage 1 | Starting point — to be confirmed and expanded here |
| Customer specification / contract | Sales / customer | May mandate specific standards, editions, or certifications |
| Assumptions register | Stage 1 | Any unresolved assumptions that affect standards applicability |

**If market identification is not confirmed from Stage 1, this stage cannot produce a reliable standards register. Resolve before proceeding.**

---

## 3. Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 12100:2010** | Defines the type-A / type-B / type-C hierarchy that governs how standards interact and which takes precedence |
| **`_standards_map.md`** | Internal routing document — primary tool for mapping project characteristics to applicable standards |
| **Decision workflow crosswalk** | Internal tool for resolving PL vs SIL pathway selection |
| **EU Machinery Directive 2006/42/EC / Machinery Regulation (EU) 2023/1230** | If CE marking is required, the list of harmonized standards determines which standards provide presumption of conformity |
| **EU Official Journal (OJ)** | Current list of harmonized standards under the Machinery Directive — must verify that the edition you are using is the one currently listed |
| **OSHA standards (29 CFR 1910)** | If US market, OSHA references specific consensus standards — these are not optional if cited in the contract or if OSHA jurisdiction applies |
| **Customer specification** | May mandate specific standards, editions, or deviations — these override default routing in some cases |

---

## 4. Standards Hierarchy — How Standards Interact

Before selecting standards, understand how they relate to each other:

```
┌─────────────────────────────────────────────────────────────┐
│  TYPE-A: Basic safety standards (fundamental concepts)       │
│  ISO 12100                                                   │
│  Applies to ALL machinery                                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  TYPE-B: Generic safety standards                            │
│                                                              │
│  B1 — Safety aspects:          B2 — Safeguarding devices:   │
│  • ISO 13849-1 (PL)           • ISO 13850 (e-stop)         │
│  • IEC 62061 (SIL)            • ISO 14119 (interlocking)   │
│  • IEC 60204-1 (electrical)   • ISO 13855 (safety distance)│
│  • ISO 13857 (reach distances)• IEC 61496 (light curtains) │
│  • IEC 61508 (functional      • ISO 14120 (guards)         │
│    safety umbrella)                                          │
│  Applies to wide range of machinery                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  TYPE-C: Machine-specific safety standards                   │
│                                                              │
│  • ISO 10218-1/2 (robots)                                   │
│  • ISO/TS 15066 (collaborative robots)                      │
│  • ISO 16092 (presses)                                      │
│  • ISO 11161 (integrated manufacturing systems)             │
│  • ISO 11553 (laser processing machines)                    │
│  • ISO 13732 (packaging machinery)                          │
│  • EN 415 (packaging machinery)                             │
│  • EN 619 (conveyors)                                       │
│  Applies to specific machine type                           │
│                                                              │
│  ★ TYPE-C OVERRIDES TYPE-B where they conflict ★            │
└─────────────────────────────────────────────────────────────┘
```

### The Override Rule

Per ISO 12100 Introduction:

> When a type-C standard deviates from one or more provisions dealt with by a type-A or type-B standard, the type-C standard takes precedence.

**This means:** If ISO 10218-2 specifies a particular safety distance calculation method for robotic cells, that method takes precedence over the generic ISO 13855 method — even if ISO 13855 would give a different result. You must identify type-C applicability before finalizing your type-B standards selections.

---

## 5. Engineering Activities

### 5.1 Confirm Market and Regulatory Requirements

Validate and expand the market identification from Stage 1:

| Question | Answer Needed | Impact |
|----------|--------------|--------|
| Is CE marking required? | Yes / No | If yes: Machinery Directive/Regulation applies, harmonized standards provide presumption of conformity |
| Is NRTL listing required (UL, CSA)? | Yes / No / Specific NRTL | If yes: UL 508A (panels), UL 61010 (test equipment), etc. |
| Is the machine installed in the US? | Yes / No | If yes: NEC (NFPA 70) governs field wiring, NFPA 79 governs machine electrical |
| Is the machine installed in Canada? | Yes / No | If yes: CEC (CSA C22.1), CSA standards may apply |
| Does the customer specification mandate specific standards? | List them | Customer mandates may add to or override default selections |
| Are there site-specific requirements? | List them | Some facilities (pharmaceutical, automotive, semiconductor) have internal standards that exceed published standards |
| Is the machine subject to process safety regulation? | Yes / No | If yes: IEC 61511 / IEC 61508 pathway, potentially OSHA PSM (29 CFR 1910.119) |

### 5.2 Identify All Applicable Type-C Standards

This is the most commonly missed activity at this stage. Use the machine type identified in Stage 1 to search for applicable type-C standards:

| Machine Type | Potentially Applicable Type-C Standards |
|-------------|---------------------------------------|
| Robotic system / robotic cell | ISO 10218-1, ISO 10218-2, ISO/TS 15066, ANSI/RIA 15.06 |
| Press / stamping system | ISO 16092 series, ANSI B11.1 through B11.19 |
| Integrated manufacturing system | ISO 11161 |
| Packaging machinery | EN 415 series |
| Conveyor system | EN 619, ANSI/ASME B20.1 |
| Laser processing machine | ISO 11553, IEC 60825-1 |
| Woodworking machinery | EN 691 (general), machine-specific EN standards |
| Printing machinery | EN 1010 series |
| Machine tools | ISO 16090 series |
| Food processing machinery | EN 1672-2 |
| Rubber and plastics machinery | EN 289, EN 201 (injection molding) |
| Lifting equipment / cranes | EN 13001, EN 15011 |

**If no type-C standard exists for your machine type**, document that determination explicitly. The project will then rely entirely on type-A and type-B standards.

**If the machine is a combination of types** (e.g., a robotic press tending cell), identify all applicable type-C standards and note where they overlap or conflict.

### 5.3 Apply the Routing Logic

The `_standards_map.md` routing document provides the primary decision logic. The expanded routing is:

```
START
  │
  ├─► Is the machine / system for the US market?
  │     │
  │     ├─ YES ──► NEC (NFPA 70) — field installation
  │     │          NFPA 79 — machine electrical safety
  │     │          UL 508A — if control panel NRTL listing required
  │     │          ANSI B11 series — if applicable machine type
  │     │          ANSI/RIA 15.06 — if robotic system (US version of ISO 10218)
  │     │          OSHA 29 CFR 1910 Subpart O — general machine guarding
  │     │          OSHA 29 CFR 1910.147 — lockout/tagout (LOTO)
  │     │
  │     └─ NO ───► Skip US-specific codes
  │
  ├─► Is the machine / system for the EU market (CE marking)?
  │     │
  │     ├─ YES ──► ISO 12100 — risk assessment (type-A)
  │     │          IEC 60204-1 — electrical safety of machinery
  │     │          ISO 13849-1 OR IEC 62061 — functional safety (see 5.4)
  │     │          ISO 13857 — safety distances (reach over, through, around)
  │     │          ISO 13855 — safety device positioning (approach speed)
  │     │          ISO 13850 — emergency stop design
  │     │          ISO 14119 — interlocking devices (if guards with interlocks)
  │     │          ISO 14120 — guards (fixed, movable)
  │     │          IEC 61496 — light curtains (if used)
  │     │          Applicable type-C standard(s) from 5.2
  │     │
  │     └─ NO ───► Skip EU harmonized standards (unless customer requires)
  │
  ├─► Is the machine for BOTH US and EU (global)?
  │     │
  │     └─ YES ──► Apply BOTH sets above
  │                Identify conflicts (see 5.5)
  │                Default to MOST RESTRICTIVE requirement from each
  │                Document conflict resolution in standards register
  │
  ├─► Are safety functions present or anticipated?
  │     │
  │     ├─ YES ──► Select PL or SIL pathway (see 5.4)
  │     │          ISO 13849-1 → Performance Level (PL a through e)
  │     │          IEC 62061 → Safety Integrity Level (SIL 1 through 3)
  │     │          IEC 61508 → if umbrella / complex / novel system
  │     │
  │     └─ NO ───► Document why no safety functions exist
  │                (rare — most machines have at least e-stop)
  │
  └─► Is this a process safety application (SIS/SIF)?
        │
        ├─ YES ──► IEC 61511-1/2/3 — process sector functional safety
        │          IEC 61508 — foundation standard
        │          ISA 84.00.01 — US adoption of IEC 61511
        │          OSHA PSM 29 CFR 1910.119 — if applicable process
        │
        └─ NO ───► Skip process safety standards
```

### 5.4 PL vs SIL Pathway Selection

This is a **preliminary decision** made here and **confirmed at Stage 3** after risk assessment. The decision determines which methodology is used to assign safety integrity targets.

| Factor | Favors ISO 13849-1 (PL) | Favors IEC 62061 (SIL) |
|--------|------------------------|------------------------|
| Machine type | Standard machinery, discrete manufacturing | Complex machinery with extensive safety PLC logic |
| Customer requirement | Customer specifies PL | Customer specifies SIL |
| Industry norm | Most machinery OEMs in EU use PL | Process industry, some automotive OEMs prefer SIL |
| Subsystem complexity | Simple to moderate (relay-based, hardwired, small safety PLC programs) | Complex (multiple safety PLCs, networked safety, extensive diagnostics) |
| Existing company practice | Team is experienced with SISTEMA and PL calculations | Team is experienced with SIL calculations and IEC 62061 methodology |
| Type-C standard requirement | Type-C standard references ISO 13849-1 | Type-C standard references IEC 62061 |
| Regulatory context | CE marking, Machinery Directive | Process safety, IEC 61511 (always SIL) |

**Important notes:**
- ISO 13849-1:2023 and IEC 62061:2021 have been significantly harmonized — either can be used for machinery applications
- You **cannot mix** PL and SIL within a single safety function — one function, one methodology
- You **can** use different methodologies for different safety functions on the same machine (though this adds complexity and is generally discouraged)
- For process safety (SIS/SIF), the pathway is always SIL via IEC 61511 — there is no PL option
- Document the rationale for the pathway selection — auditors will ask why

### 5.5 Identify and Resolve Standards Conflicts

For global projects (US + EU, or multi-market), conflicts **will** exist. Identify them now, not during detailed design.

| Topic | NFPA 79 (US) | IEC 60204-1 (EU) | Resolution Approach |
|-------|-------------|-------------------|-------------------|
| Wire color — protective earth | Green or green/yellow | Green/yellow only | Use green/yellow (satisfies both) |
| Wire color — neutral | White or gray | Light blue | Must decide per market OR use dual-labeled |
| Wire color — ungrounded conductors | Any color except green, white, gray | Any color except green/yellow, light blue | Use black (satisfies both) |
| Control circuit voltage | 120V common | 24VDC or 230V common | Specify per project — document basis |
| Overcurrent protection | Per NEC Article 430 | Per IEC 60204-1 §7 | Apply most restrictive |
| Disconnect requirements | NFPA 79 §5.3 | IEC 60204-1 §5.3 | Generally aligned — verify specific requirements |
| Grounding / earthing | NEC Article 250 | IEC 60204-1 §8 | Apply both — document compliance to each |
| Panel enclosure rating | NEMA types | IP ratings per IEC 60529 | Provide NEMA-to-IP cross-reference, design to most restrictive |
| Emergency stop color | Red on yellow background | Red on yellow background | Aligned (ISO 13850 governs both) |

**Document every conflict resolution decision in the standards register with rationale.**

### 5.6 Identify Applicable Type-B2 Standards (Safeguarding Device Standards)

Based on the preliminary hazard scan from Stage 1 and the anticipated safeguarding approach, identify which device-specific standards will apply:

| If You Anticipate Using... | Applicable Standard |
|---------------------------|-------------------|
| Emergency stop devices | ISO 13850 |
| Guard interlocking devices | ISO 14119 |
| Fixed and movable guards | ISO 14120 |
| Light curtains / AOPDs | IEC 61496-1 and applicable part (e.g., -2 for type 4) |
| Two-hand control devices | ISO 13851 |
| Pressure-sensitive mats / edges | ISO 13856-1, -2, -3 |
| Enabling devices (hold-to-run) | ISO 11161 Annex A, IEC 60204-1 §9.2.6 |
| Safety distances (reaching over/through/around) | ISO 13857 |
| Safety device positioning (approach speed) | ISO 13855 |
| Trapped key interlocks | ISO 14119 |

### 5.7 Verify Standard Editions

Standards are revised. Using an outdated edition can mean non-compliance:

| Check | Action |
|-------|--------|
| Is the edition you are referencing the current published edition? | Verify against ISO, IEC, ANSI, or NFPA catalog |
| If CE marking: is the edition listed in the EU Official Journal as a harmonized standard? | Verify against the current OJ listing — a standard can be current but not yet harmonized, or harmonized but withdrawn |
| Does the customer specification require a specific edition? | If yes, use that edition (even if not the latest) and document |
| Has a new edition been published since project start that changes requirements? | If yes, assess impact and decide whether to adopt — document decision |
| What is the transition period (if a new edition was recently published)? | Some standards have a transition date after which the old edition is withdrawn |

---

## 6. Key Deliverables

| # | Deliverable | Description |
|---|------------|-------------|
| 1 | **Standards register** | Formal list of all applicable standards with applicability basis, scope, edition, and conflict resolution notes (see expanded template below) |
| 2 | **PL vs SIL pathway selection record** | Documented decision with rationale for which functional safety methodology will be used, per safety function or for the project as a whole |
| 3 | **Type-C standard applicability determination** | Documented search and conclusion — either the applicable type-C standard(s) or a statement that none applies, with basis |
| 4 | **Standards conflict resolution log** | For multi-market projects: list of identified conflicts between standards with resolution and rationale for each |
| 5 | **Updated assumptions register** | Any new assumptions identified during standards selection, added to the register from Stage 1 |

### Expanded Standards Register Template

| # | Standard | Edition | Applicable? | Basis for Applicability | Scope / Applicable Sections | Harmonized (EU OJ)? | Conflict Notes | Verified By | Date |
|---|----------|---------|-------------|------------------------|---------------------------|---------------------|---------------|------------|------|
| 1 | NEC (NFPA 70) | 2023 | Yes | US installation, per contract | Articles 409, 430, 670 | N/A (US code) | — | [Name] | [Date] |
| 2 | NFPA 79 | 2024 | Yes | US machinery electrical, per contract | All chapters | N/A (US standard) | Wire color conflicts with IEC 60204-1 — see conflict log | [Name] | [Date] |
| 3 | UL 508A | 4th Ed. | Yes | NRTL listing required per customer | All sections | N/A (US listing) | — | [Name] | [Date] |
| 4 | ISO 12100 | 2010 | Yes | CE marking, type-A | Full standard | Yes | — | [Name] | [Date] |
| 5 | ISO 13849-1 | 2023 | Yes | CE marking, PL pathway selected | All clauses | Verify OJ listing for 2023 edition | — | [Name] | [Date] |
| 6 | IEC 60204-1 | 2016 | Yes | CE marking, EU electrical | All clauses | Yes | Wire color conflicts with NFPA 79 — see conflict log | [Name] | [Date] |
| 7 | ISO 10218-2 | 2011 | Yes | Robotic cell — type-C applies | All clauses | Yes | Overrides ISO 13855 safety distance calculation per type-C precedence | [Name] | [Date] |
| 8 | ISO 13857 | 2019 | Yes | Safety distances for guards | Tables 1–4 | Yes | ISO 10218-2 may override for robot-specific scenarios | [Name] | [Date] |
| 9 | ISO 14119 | 2013 | Yes | Interlocked guards present | All clauses | Yes | — | [Name] | [Date] |
| 10 | ISO 13850 | 2015 | Yes | E-stop devices present | All clauses | Yes | — | [Name] | [Date] |
| 11 | IEC 62061 | 2021 | No | PL pathway selected instead | — | — | Retained as reference for subsystem SIL data if needed | [Name] | [Date] |
| 12 | IEC 61511 | 2016+A1 | No | Not a process safety application | — | — | — | [Name] | [Date] |

**Every "No" entry must have a documented basis for exclusion, not just a blank.**

---

## 7. Exit Criteria — Gate Review

This stage is complete when **all** of the following are true:

| # | Criterion | Evidence |
|---|-----------|----------|
| 1 | Standards register is complete with all applicable type-A, type-B, type-B2, and type-C standards identified | Completed register with all columns filled |
| 2 | Every standard in the register has a confirmed edition and applicability basis | Edition column and basis column complete for all entries |
| 3 | Type-C standard applicability is confirmed or explicitly ruled out with documented rationale | Type-C determination record |
| 4 | PL vs SIL pathway is selected with documented rationale | Pathway selection record |
| 5 | For multi-market projects: all known conflicts between standards are identified and resolution is documented | Conflict resolution log |
| 6 | Harmonized standard status is verified against current EU OJ listing (if CE marking applies) | OJ verification date recorded |
| 7 | Customer-mandated standards are included and any deviations from default routing are documented | Customer requirements cross-referenced in register |
| 8 | Standards register is reviewed by at least one person other than the author | Review signature, date, comments resolved |
| 9 | Stage 1 assumptions affecting standards selection are resolved or explicitly carried forward | Updated assumptions register |

**If the PL vs SIL pathway is not decided, Stage 3 cannot proceed — the risk assessment methodology depends on this decision.**

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Safety / Controls Engineer** | Owns this stage — authors the standards register, performs the routing logic, selects PL vs SIL pathway, identifies type-C standards, identifies conflicts |
| **Project Manager** | Ensures this stage is completed before detailed engineering begins; confirms market and contract requirements are communicated to the safety engineer |
| **Mechanical / Process Engineer** | Confirms machine type classification for type-C standard identification; identifies any process-specific standards (e.g., food safety, pharmaceutical GMP) |
| **Sales / Application Engineer** | Confirms customer-mandated standards, certifications, and market destinations; resolves ambiguities in customer specification |
| **Quality / Compliance** | Verifies harmonized standard status against EU OJ (if CE marking); confirms NRTL listing requirements (if US market) |

---

## 9. Common Mistakes

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Type-C standard is not identified | Design proceeds under generic type-B requirements; late discovery causes rework or non-compliance | Systematically search for type-C standards by machine type — use the table in 5.2 as a starting checklist |
| Using an outdated edition of a standard | Design may comply with withdrawn requirements but not current ones; CE presumption of conformity may not apply | Verify editions against current catalogs and EU OJ at the start of the project |
| PL vs SIL pathway not decided | Risk assessment in Stage 3 cannot assign targets; engineers use ad hoc methods; calculations are inconsistent | Make the decision here, document rationale, confirm at Stage 3 |
| Standards conflicts not identified for global projects | Discovered during detailed design or build — causes wire re-pulling, label changes, panel rework | Run the conflict check in 5.5 for every multi-market project |
| "We always use these standards" without project-specific verification | Prior project may have been a different machine type, different market, or different customer — standards applicability is project-specific | Start from the routing logic every time, even if the result is the same |
| Customer specification references standards without edition | Ambiguous — which edition did they mean? | Clarify with customer in writing before finalizing register |
| Standards register is created but never updated | New standards or editions published during a long project; scope changes add new machine types | Assign an owner and a review trigger (scope change, phase gate, or quarterly for long projects) |
| Non-applicable standards are simply left blank instead of explicitly excluded | Auditors cannot tell whether the standard was considered and excluded or simply overlooked | Every standard considered must have a "Yes" or "No" with a documented basis |

---

## 10. Relationship to Adjacent Stages

```
┌──────────────────────────────┐
│  STAGE 1: CONCEPT             │
│                              │
│  Provides:                   │
│  • System description        │
│  • Machine type              │
│  • Market identification     │
│  • Type-C preliminary ID     │
│  • Operating modes           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  STAGE 2: STANDARDS           │  ◄── You are here
│  SELECTION                    │
│                              │
│  Produces:                   │
│  • Standards register        │
│  • PL vs SIL pathway         │
│  • Type-C confirmation       │
│  • Conflict resolution log   │
└──────────────┬───────────────┘
               │
               │  All outputs feed directly into
               ▼
┌──────────────────────────────┐
│  STAGE 3: RISK ASSESSMENT     │
│                              │
│  Uses:                       │
│  • Standards register to     │
│    determine which risk      │
│    assessment methodology    │
│    applies                   │
│  • PL vs SIL pathway to     │
│    determine how targets     │
│    are assigned              │
│  • Type-C standards for      │
│    machine-specific hazard   │
│    requirements and pre-     │
│    defined safety measures   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  STAGE 4: SAFETY ARCHITECTURE │
│                              │
│  Uses:                       │
│  • Standards register to     │
│    determine architecture    │
│    requirements (categories  │
│    per ISO 13849-1 or HFT   │
│    per IEC 62061)            │
│                              │
│  STAGE 5: DETAILED DESIGN    │
│                              │
│  Uses:                       │
│  • NFPA 79 / IEC 60204-1    │
│    for electrical design     │
│  • UL 508A for panel design  │
│  • Conflict resolution log   │
│    for multi-market wiring   │
│    decisions                 │
└──────────────────────────────┘
```

---

## 11. Reference: PL ↔ SIL Approximate Equivalence

For reference only — these are **approximate** equivalences, not exact conversions:

| Performance Level (ISO 13849-1) | SIL (IEC 62061) | PFH range |
|-------------------------------|-----------------|-----------|
| PL a | — | ≥ 10⁻⁵ to < 10⁻⁴ |
| PL b | SIL 1 | ≥ 3 × 10⁻⁶ to < 10⁻⁵ |
| PL c | SIL 1 | ≥ 10⁻⁶ to < 3 × 10⁻⁶ |
| PL d | SIL 2 | ≥ 10⁻⁷ to < 10⁻⁶ |
| PL e | SIL 3 | ≥ 10⁻⁸ to < 10⁻⁷ |

**Do not use this table to convert between PL and SIL after the fact. Choose one methodology and apply it consistently.**

---

## 12. Templates and Tools

| Resource | Purpose |
|----------|---------|
| `_standards_map.md` | Primary routing logic document |
| Decision workflow crosswalk | PL vs SIL pathway selection tool |
| Standards register template | Spreadsheet with all columns per Section 6 |
| Type-C standards lookup table | Reference list of machine types and corresponding type-C standards |
| Conflict resolution log template | Table for documenting multi-market standards conflicts and resolutions |
| EU Official Journal harmonized standards list | External reference — verify at [EU harmonized standards database](https://single-market-economy.ec.europa.eu/single-market/european-standards/harmonised-standards_en) |

---

<nav class="lifecycle-nav">
  <a href="{{ '/lifecycle/concept/' | relative_url }}" class="lifecycle-nav__prev">← Previous: Stage 1 — Concept</a>
  <a href="{{ '/lifecycle/risk-assessment/' | relative_url }}" class="lifecycle-nav__next">Next: Stage 3 — Risk Assessment →</a>
</nav>
