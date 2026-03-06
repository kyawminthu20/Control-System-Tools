<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "240"
  article_title: "Overcurrent Protection"

INDEX_TAGS:
  topics: ["overcurrent", "short_circuit", "breakers", "fuses"]
  systems: ["industrial_control_panel"]
-->


# NEC 2023 — Article 240 — Overcurrent Protection

## 0. Scope for control panels

Article 240 provides the general requirements for overcurrent protection (OCP) and the overcurrent protective devices (OCPDs) used to protect conductors and equipment. In the context of industrial control panels, this article ensures that internal wiring and downstream loads are protected against overloads, short circuits, and ground faults. It must be used in conjunction with **Article 409** (for panel specifics) and **Article 430** (for motor loads).

## 1. Overcurrent device selection

* **120.4 Protection of Conductors:** Conductors must be protected at the point where they receive their supply. The OCPD rating is generally determined by the ampacity of the conductor as calculated in **Article 310**.
* **Standard Ratings (240.6):** Lists standard ampere ratings for fuses and inverse time circuit breakers. Designers must select the next standard size up only when the conductor ampacity does not correspond to a standard rating (the "Next Size Up Rule," subject to 240.4(B) limitations).
* **Supplementary vs. Branch Circuit Protection:**
* **Branch Circuit OCPDs:** Must be used for the primary protection of the panel's supply and outgoing branches (e.g., UL 489 breakers or UL 248 fuses).
* **Supplementary OCPDs (UL 1077):** These are only permitted for use *inside* the panel to protect specific components. They **cannot** be used as a substitute for branch circuit protection.



## 2. Coordination with SCCR (Short-Circuit Current Rating)

* **240.86 Series Ratings:** If the panel relies on series-rated combinations to achieve a high SCCR, the specific combinations of devices must be tested and documented.
* **Interrupting Rating (240.1):** OCPDs must have an interrupting rating sufficient for the nominal circuit voltage and the current that is available at the line terminals of the equipment.
* **Integration with Article 409:** The SCCR of the entire control panel (required by 409.110) is heavily dictated by the current-limiting characteristics of the OCPDs selected in Article 240.

## 3. Common violations

1. **Using Supplementary Protectors for Branch Circuits:** Using UL 1077 "mini-breakers" to protect outgoing field wiring.
2. **Improper Tap Rule Application (240.21):** Misapplying the "10-foot" or "25-foot" tap rules for conductors inside or leaving the panel without meeting the specific termination and enclosure requirements.
3. **Ignoring Transformer Protection (450.3 via 240.21(C)):** Failing to provide primary and/or secondary protection for control power transformers (CPTs) based on their specific kVA rating.
4. **Inadequate Interrupting Rating:** Installing breakers with a 10kA AIC rating in a facility where the available fault current (AFC) is 42kA.

## 4. Change log

* 2026-01-15 — Initial draft created; integrated supplementary vs. branch circuit distinctions.

