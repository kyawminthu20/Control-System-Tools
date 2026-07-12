<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "12"
  clause_title: "Conductors and cables"

INDEX_TAGS:
  topics: ["conductors", "cables", "cross_section", "insulation", "current_carrying_capacity"]
-->

Clause 12 of **IEC 60204-1** (2016+AMD1:2021) covers the **selection of conductors and cables** for the electrical equipment of the machine: what they are made of, how they are insulated, and how their cross-section is determined.

Clause 12 selects the conductor. **Clause 13 (Wiring practices)** governs how it is then installed and routed. The two are read together.

---

## 0. Scope

This clause specifies requirements for the conductors and cables used in the electrical equipment of the machine, including:

* conductor material and construction;
* insulation and sheath properties appropriate to the service conditions;
* the basis on which conductor **cross-section** is selected;
* current-carrying capacity and the conditions that derate it.

## 1. Selection Basis

Conductor cross-section is not chosen from load current alone. The selection must account for:

* the **current to be carried** in normal service, and the duty (continuous, intermittent, motor starting);
* the **method of installation** — conductors bunched in a duct or trunking run hotter than the same conductors in free air, so the permissible current is derated;
* the **ambient temperature** and the temperature rating of the insulation;
* the permissible **voltage drop** for correct operation of the connected equipment;
* the **mechanical strength** required — a minimum cross-section applies regardless of the calculated load, because a conductor thin enough to carry the current may still be too fragile to survive service;
* the **impedance required** for the protective device to operate within its required disconnection time on a fault (this couples Clause 12 to Clauses 6 and 7).

## 2. Insulation and Service Conditions

Insulation and any sheath must suit the voltage, the temperature, and the physical and chemical environment the cable actually sees — including flexing, abrasion, oil and coolant exposure, and, for cables on moving parts of the machine, continuous flexing life.

Conductors used for flexible connections (drag chains, moving axes, festoons) are a distinct selection problem from fixed wiring: they require cable constructions rated for the flexing regime, and a conductor chosen only on ampacity will fail mechanically long before it fails thermally.

## 3. Protective Conductors

The protective earthing (PE) conductor is sized by its own rules, related to the cross-section of the associated line conductors — not by the load current of the circuit it protects. See **Clause 8 (Equipotential bonding)**, which owns the protective bonding circuit requirements.

## 4. Cross-References

* **Clause 6** — protection against electric shock (disconnection times depend on circuit impedance).
* **Clause 7** — protection of equipment (overcurrent protection must be coordinated with the conductor's current-carrying capacity).
* **Clause 8** — equipotential bonding, protective conductor sizing.
* **Clause 13** — wiring practices: routing, segregation, terminations, identification.
* US equivalent — NFPA 79 conductor and wiring chapters; NEC Art. 310 for ampacity.
* Site guide — the wire-sizing walkthrough under `/design/wiring/wire-sizing/` works a full ampacity + voltage-drop selection end to end.

## 5. Change Log

* 2026-07-12 — **Created in the Phase 45 accuracy pass.** Clause 12 previously had **no file at all**: the corpus module skipped from Clause 11 straight to motors, and mis-numbered every clause after it. The clause structure has now been corrected against the official IEC 60204-1:2016+AMD1:2021 contents.

## 6. Coverage Note

**Gap — depth pass pending.** This file establishes the correct clause and states the selection principles at the level the rest of the module uses. It has **not** been verified against the purchased text of the standard, and it deliberately carries **no table values** (cross-sections, ampacities, derating factors) — those are licensed content and are not stored in this corpus. Consult the published standard for any numeric limit.
