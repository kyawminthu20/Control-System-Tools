<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "16"
  clause_title: "Marking, warning signs and reference designations"

INDEX_TAGS:
  topics: ["marking", "warning_signs", "reference_designations"]
-->

Clause 16 of **IEC 60204-1** (2016+AMD1:2021) covers the "informational safety" of the machine: even a perfectly engineered electrical system is dangerous if a technician cannot identify which conductor is live, or which physical device a schematic symbol refers to. This clause makes the machine self-describing.

**Technical documentation is a separate clause** — see Clause 17.

---

## 0. Scope

This clause specifies the requirements for **marking, warning signs, and reference designations**. It ensures that:

* The machine can be identified (manufacturer, model, ratings).
* Hazards are clearly communicated via warning signs.
* Conductors and components carry unique reference designations that match the technical drawings.

## 1. Identification and Labels

The machine and its components must be clearly and durably marked to prevent errors during servicing.

* **Nameplate requirements:** The main control enclosure carries a permanent nameplate including the manufacturer's name, serial number, supply voltage, frequency, and full-load current. (For the US market, NFPA 79 and NEC Art. 409 additionally require the panel's **Short-Circuit Current Rating (SCCR)** to be marked.)
* **Warning signs:** Enclosures containing electrical hazards must be marked with the electrical-hazard symbol. If residual voltage persists after power-off, a warning specifying the discharge time is required.
* **Component marking:** Every relay, PLC, and breaker must be marked with a reference designation (e.g., `-K1`, `-Q1`) that matches the electrical schematics.
* **Conductor identification:** Conductors must be identified at each termination by colour, number, or alphanumeric code.

## 2. Cross-References

* **Clause 17** — technical documentation (schematics, manuals, parts lists).
* **Clause 18** — verification, including that required markings are present.
* US equivalent — NFPA 79 marking and safety-sign requirements.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-07-12 — Phase 45 accuracy pass: renumbered from Clause 14 to **Clause 16** against the official IEC 60204-1:2016+AMD1:2021 contents; technical documentation split out into the new Clause 17; edition label corrected (the "2018" edition does not exist); AI drafting artifact removed.
