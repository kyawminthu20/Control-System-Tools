---
layout: default
title: "Lifecycle Stage 1 — Concept"
description: "Define machine limits, intended use, foreseeable misuse, and applicable markets before risk assessment begins."
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "1. Concept"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 01</span>
  <h1>Concept</h1>
  <p class="page-header__description">Define machine limits, intended use, foreseeable misuse, and applicable markets before risk assessment begins.</p>
</div>

## 1. Purpose of This Stage

This is the foundation stage of the safety engineering lifecycle. Its purpose is to establish **what the machine or system is**, **what it does**, **where its boundaries are**, and **what context it operates in** — before any risk assessment, design, or standards compliance work begins.

Every decision made in later stages depends on the accuracy and completeness of what is defined here. A poorly defined concept stage leads to:

- Missed hazards in risk assessment (because the scope was unclear)
- Wrong standards selected (because the market or application was not identified)
- Scope creep during design (because boundaries were not agreed)
- Disputes during commissioning (because intended use was ambiguous)

> **The concept stage answers one question: What exactly are we making safe, and for whom?**

---

## 2. Entry Criteria

This stage begins when **any** of the following are true:

| Trigger | Source |
|---------|--------|
| New project kicked off with safety scope identified | Project manager / sales handoff |
| Customer specification received referencing safety requirements | Proposal or contract review |
| Internal decision to design a new machine or system | Engineering leadership |
| Significant modification to an existing machine requiring re-scoping | MOC process (Stage 12 routes back here) |

### Required Inputs to Begin

| Input | Source | Why It Matters |
|-------|--------|----------------|
| Customer specification or RFQ | Sales / customer | Defines what the customer expects the machine to do |
| Process description or P&ID (if applicable) | Process engineering | Defines what the machine interacts with |
| Site or facility information | Customer / site survey | Environmental conditions, existing infrastructure, local codes |
| Applicable contract or regulatory requirements | Legal / commercial | CE marking, OSHA, NRTL listing, customer-specific mandates |
| Prior machine documentation (if retrofit/modification) | Engineering records | Existing risk assessments, drawings, safety function register |

**If these inputs are not available, document what is missing and flag it as an assumption to be confirmed.**

---

## 3. Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 12100:2010 §5** | Defines the methodology for determining limits of the machine — use limits, space limits, time limits, and other limits |
| **ISO 12100:2010 §3.22–3.24** | Defines intended use, reasonably foreseeable misuse, and intended purpose — the language you use here must align with these definitions |
| **Machinery Directive 2006/42/EC** or **Machinery Regulation (EU) 2023/1230** | If CE marking is required, the essential health and safety requirements (EHSRs) apply from concept onward — EHSR 1.1.1 requires consideration of intended use and foreseeable misuse at the design stage |
| **Type-C standards (initial identification)** | If the machine type has a dedicated product standard (e.g., ISO 10218 for robots, ISO 16092 for presses, ISO 11161 for integrated manufacturing systems), it must be identified now — type-C standards override type-B defaults and may impose specific concept-stage requirements |
| **OSHA 29 CFR 1910 Subpart O** (if US market) | General requirements for machinery — establishes employer obligations that inform what "intended use" means in a US context |
| **ANSI/NFPA 79** (if US market) | Early identification that this will govern electrical design — influences concept decisions about voltage, power distribution, control architecture |
| **IEC 61511-1 §8** (if process safety) | Requires a clear definition of the process, its hazards, and the allocation of safety functions to protection layers — this allocation starts at concept |

### Note on Type-C Standards

At this stage you are not yet selecting all applicable standards (that is Stage 2). However, you **must** identify whether a type-C standard exists for your machine type, because type-C standards can impose requirements that fundamentally change the concept — for example:

- ISO 10218-2 requires specific definitions of collaborative workspace if a robot is involved
- ISO 11161 requires definition of inter-machine interfaces and zone boundaries for integrated systems
- ISO 16092 requires specific definitions of operating modes for press systems

If a type-C standard exists and you do not identify it here, you risk designing to generic requirements that are later overridden.

---

## 4. Engineering Activities

### 4.1 Define Machine / System Limits

Per ISO 12100 §5.2, determine:

| Limit Type | What to Define | Example |
|-----------|---------------|---------|
| **Use limits** | Intended use, operating modes, operator skill level, foreseeable misuse | "Machine is intended for continuous production of Part X by trained operators. Foreseeable misuse includes reaching into the die area during cycling." |
| **Space limits** | Physical boundary of the machine, range of motion, reach zones, operator access positions | "Machine boundary includes the press frame, conveyor infeed, and outfeed to point of transfer to downstream conveyor." |
| **Time limits** | Expected life of machine, recommended service intervals, life of safety-critical components | "Designed for 20-year service life, safety components rated for 10-year replacement cycle." |
| **Other limits** | Material properties, environmental conditions (temperature, humidity, dust, vibration, altitude), utility requirements | "Operating environment: 0–45°C, indoor, non-explosive atmosphere, 480V 3-phase supply." |

### 4.2 Document Intended Use and Foreseeable Misuse

This is not a one-sentence statement. It should be a structured narrative covering:

**Intended Use:**
- What does the machine do (process, function, output)?
- Who operates it (skill level, training assumptions)?
- What materials does it process?
- What are the defined operating modes (automatic, manual, setup, maintenance, cleaning, fault recovery)?
- What is the production context (standalone, part of a line, upstream/downstream interfaces)?

**Reasonably Foreseeable Misuse:**
- What could an operator do wrong that is predictable based on human behavior?
- What could maintenance personnel do that bypasses safety?
- What could happen if the machine is used beyond its rated capacity?
- What could happen if the machine is operated in an environment it was not designed for?

> **Important:** Foreseeable misuse is not "anything imaginable." Per ISO 12100 §3.24, it is use that is **not intended by the designer but can be readily anticipated based on human behavior.** Document both what is foreseeable misuse AND what is explicitly excluded from scope (abnormal use that is not foreseeable).

### 4.3 Identify Applicable Markets and Regulatory Context

| Market | Regulatory Framework | Implications at Concept Stage |
|--------|---------------------|-------------------------------|
| European Union | Machinery Directive / Regulation, CE marking | Must design to harmonized standards, must produce Declaration of Conformity, must include technical file |
| United States | OSHA, NRTL listing (UL/CSA), NEC, NFPA 79 | Must design to US national codes, panel may require UL 508A listing, field wiring per NEC |
| Canada | CSA standards, provincial regulations | May require CSA certification or field evaluation |
| Global / multiple markets | All of the above, potentially simultaneously | Must identify conflicts between standards early (e.g., NFPA 79 vs IEC 60204-1 differences in wire color, grounding) |

**This decision directly affects Stage 2 (Standards Selection) and Stage 5 (Detailed Design). It cannot be deferred.**

### 4.4 Identify Initial Stakeholders for Risk Assessment

At concept stage, identify **who must participate** in the Stage 3 risk assessment:

| Stakeholder | Why They Are Needed |
|------------|-------------------|
| Machine operator (or representative) | Knows actual use patterns and workarounds |
| Maintenance technician (or representative) | Knows access requirements and common failure modes |
| Process / mechanical engineer | Knows the physical hazards, forces, materials |
| Controls / safety engineer | Knows safety architecture options and standards |
| Customer safety representative (if applicable) | Knows site-specific requirements and risk tolerance |

**If the risk assessment team is not identified at concept, it will be assembled ad hoc at Stage 3 and will likely be missing critical perspectives.**

### 4.5 Establish Preliminary Safety Objectives

These are not PL/SIL targets (those come from Stage 3). These are project-level objectives such as:

- "All operator access points shall be safeguarded to prevent contact with hazardous motion"
- "The system shall achieve a safe state within [X] seconds of any safety demand"
- "The safety system shall comply with [specific customer safety specification reference]"
- "No single fault shall lead to loss of the safety function" (this is a preliminary architecture intent, to be confirmed at Stage 4)

### 4.6 Identify Known Hazard Categories (Preliminary)

Without conducting the full risk assessment (Stage 3), perform a **preliminary hazard scan** to identify the broad categories of hazards that will need to be assessed:

| Hazard Category (per ISO 12100 Annex B) | Present? | Notes |
|-----------------------------------------|----------|-------|
| Mechanical (crushing, shearing, cutting, entanglement, impact, stabbing/puncture, friction, high-pressure fluid) | | |
| Electrical (direct/indirect contact, arc flash, electrostatic) | | |
| Thermal (burns, scalds, frostbite) | | |
| Noise | | |
| Vibration | | |
| Radiation (ionizing, non-ionizing, laser) | | |
| Material/substance (chemical, biological, dust, fume) | | |
| Ergonomic (posture, repetitive motion, manual handling) | | |
| Environmental (slip, trip, fall, oxygen deficiency) | | |
| Combination / unexpected startup | | |

**This is not the risk assessment. It is a scoping exercise to ensure the risk assessment in Stage 3 covers all relevant hazard types and the right expertise is in the room.**

---

## 5. Key Deliverables

| # | Deliverable | Description | Format / Template |
|---|------------|-------------|-------------------|
| 1 | **System description** | Narrative of what the machine does, its function, its process context, its interfaces with upstream/downstream equipment and personnel | Document (1–3 pages typical) |
| 2 | **Intended use and foreseeable misuse statement** | Structured per ISO 12100 §5.2 — operating modes, user groups, materials processed, environmental conditions, and explicitly identified foreseeable misuse scenarios | Section within system description or standalone document |
| 3 | **Machine / system boundary definition** | What is inside and outside the scope of this safety engineering effort — physical boundary, control boundary, interface boundaries with adjacent equipment | Drawing or diagram with narrative |
| 4 | **Operating mode definitions** | List of all modes the machine will operate in (automatic, manual, setup, jog, maintenance, cleaning, fault recovery, emergency stop, restart after e-stop) with description of each | Table |
| 5 | **Market and regulatory identification** | Which markets the machine will be delivered to, which regulatory frameworks apply, whether CE marking or NRTL listing is required | Table |
| 6 | **Initial standards identification** | Preliminary list of type-A, type-B, and type-C standards that may apply (to be confirmed in Stage 2) | Standards register draft |
| 7 | **Operating assumptions** | Process parameters, environmental conditions, operator training assumptions, maintenance access assumptions, utility specifications | Table or document section |
| 8 | **Preliminary hazard category scan** | Checklist of ISO 12100 Annex B hazard categories with initial identification of which are present | Checklist table |
| 9 | **Risk assessment team identification** | Named individuals or roles who will participate in Stage 3 | List |
| 10 | **Concept-stage assumptions register** | Any assumptions made due to incomplete information, with owner and date for resolution | Table (living document) |

---

## 6. Exit Criteria — Gate Review

This stage is complete when **all** of the following are true:

| # | Criterion | Evidence |
|---|-----------|----------|
| 1 | Machine/system boundary is defined and agreed with stakeholders | Signed or approved boundary drawing/description |
| 2 | Intended use and foreseeable misuse are documented per ISO 12100 §5.2 | Documented in system description |
| 3 | All operating modes are identified and described | Operating mode table complete |
| 4 | Target markets and regulatory frameworks are identified | Market identification table complete |
| 5 | Type-C standard applicability is determined (exists or confirmed none applies) | Documented in initial standards identification |
| 6 | Preliminary hazard categories are scanned | Hazard category checklist complete |
| 7 | Risk assessment team is identified and scheduled | Names/roles listed, Stage 3 scheduled in project plan |
| 8 | All assumptions are documented with owners | Assumptions register created |
| 9 | Concept deliverables are reviewed by at least one person other than the author | Review record (signature, date, comments resolved) |

**If any criterion is not met, the stage does not close. Proceeding to Stage 2 without a defined boundary and intended use statement will result in an unfounded standards selection.**

---

## 7. Roles and Responsibilities at This Stage

| Role | Responsibility |
|------|---------------|
| **Project Manager** | Ensures this stage is scheduled, resourced, and completed before engineering proceeds; owns the project timeline gate |
| **Safety / Controls Engineer** | Authors the system description, boundary definition, and intended use/misuse statement; identifies preliminary standards and hazard categories |
| **Mechanical / Process Engineer** | Provides process description, machine function, material properties, environmental conditions; validates boundary definition |
| **Sales / Application Engineer** | Provides customer specification, market identification, contractual safety requirements; clarifies customer intent |
| **Customer (if accessible)** | Confirms intended use, operating modes, site conditions, user training assumptions |

---

## 8. Common Mistakes at This Stage

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Boundary is vague or undefined | Risk assessment in Stage 3 either misses hazards at interfaces or wastes time assessing things outside scope | Use a physical drawing with a clear line. If it's inside the line, it's in scope. If it's outside, it's not. Document interface responsibilities. |
| Foreseeable misuse is not documented | Auditors and risk assessment both suffer — if you didn't anticipate misuse at concept, you won't design against it | Use ISO 12100 §5.2 and Annex B as a structured prompt. Interview operators or experienced field engineers. |
| Operating modes are incomplete | Safety functions designed for automatic mode may not address manual/setup/maintenance modes, leading to gaps | Use a standard mode list as a starting checklist: automatic, manual, setup/jog, maintenance, cleaning, fault recovery, e-stop, restart, teach (if applicable). |
| Market is assumed rather than confirmed | Designing to IEC standards when the machine goes to a US facility that requires NFPA 79 and UL 508A, or vice versa | Confirm market in writing with sales/customer before proceeding. |
| Type-C standard is missed | Entire design proceeds under generic type-B standards, then a late-stage review reveals a type-C standard that imposes different/additional requirements, causing rework | Search for type-C standards by machine type at concept. Check ISO, IEC, and ANSI/NFPA catalogs. |
| Concept stage is skipped because "we've built this machine before" | Prior machine may have been non-compliant, or the new project has different scope, different market, or different customer requirements | Every project gets a concept stage, even if it is brief. Document what is the same and what is different from the prior machine. |

---

## 9. Relationship to Adjacent Stages

```
                    ┌──────────────────────────┐
                    │  PROJECT KICKOFF          │
                    │  (General Engineering)    │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │  STAGE 1: CONCEPT         │  ◄── You are here
                    │                          │
                    │  Outputs:                │
                    │  • System description    │
                    │  • Boundary definition   │
                    │  • Intended use/misuse   │
                    │  • Market identification │
                    │  • Operating modes       │
                    │  • Preliminary hazard    │
                    │    categories            │
                    └────────────┬─────────────┘
                                 │
                    All outputs feed directly into
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │  STAGE 2: STANDARDS       │
                    │  SELECTION                │
                    │                          │
                    │  Uses market ID and      │
                    │  type-C identification   │
                    │  to build full standards │
                    │  register                │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │  STAGE 3: RISK ASSESSMENT │
                    │                          │
                    │  Uses boundary, intended │
                    │  use/misuse, operating   │
                    │  modes, and hazard       │
                    │  categories as direct    │
                    │  inputs                  │
                    └──────────────────────────┘
```

---

## 10. Templates and Tools

| Resource | Purpose |
|----------|---------|
| System Description Template | Structured document with sections for all concept-stage deliverables |
| Boundary Definition Drawing Template | CAD or Visio template with scope boundary notation |
| Operating Mode Checklist | Standard list of modes to consider for every machine |
| Hazard Category Scan Checklist | ISO 12100 Annex B categories in checklist format |
| Assumptions Register Template | Table with columns: Assumption, Impact if Wrong, Owner, Resolution Date, Status |

*Link to your internal template repository here.*

---

← [Lifecycle Overview]({{ '/lifecycle/' | relative_url }}) | → [Stage 2: Standards Selection]({{ '/lifecycle/standards-selection/' | relative_url }})
