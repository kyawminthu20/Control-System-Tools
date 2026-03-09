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

* **240.4 Protection of Conductors:** The basic rule is that conductors must be protected in accordance with their allowable ampacity. In practical design work, that means the OCPD rating is selected only after the conductor ampacity has been established using the applicable Article 310 logic.
* **Standard Ratings (240.6):** Designers usually select from standard fuse and circuit-breaker sizes. If a calculated conductor ampacity falls between standard ratings, the "next-size-up" concept may apply in limited cases, but it is not a blanket permission.
* **Small Conductor Limits:** Designers should keep the familiar small-conductor protection limits in mind for common copper branch conductors. These rules often override the temptation to match an OCPD directly to a higher insulation-column ampacity.
* **Supplementary vs. Branch Circuit Protection:** Inside control panels, supplementary protectors can protect a component or subcircuit, but they do not replace required branch-circuit protection at the supply side.
* **Tap and Special Rules:** Article 240 includes special rules for taps, transformer secondary conductors, and other exceptions. These are narrow permissions that require the full set of conditions to be met, not shortcuts for general undersized wiring.



## 2. Coordination with SCCR (Short-Circuit Current Rating)

* **240.86 Series Ratings:** If the panel relies on series-rated combinations to achieve a high SCCR, the specific combinations of devices must be tested and documented.
* **Interrupting Rating (240.1):** OCPDs must have an interrupting rating sufficient for the nominal circuit voltage and the current that is available at the line terminals of the equipment.
* **Integration with Article 409:** The SCCR of the entire control panel (required by 409.110) is heavily dictated by the current-limiting characteristics of the OCPDs selected in Article 240.

## 3. Conductor-protection logic engineers actually use

The practical design sequence is usually:

1. determine conductor ampacity using Article 310
2. apply temperature, bundling, and installation-method limits
3. check terminal-temperature constraints from 110.14(C)
4. choose an OCPD that protects the corrected conductor ampacity
5. confirm that no small-conductor or special-rule limitation is violated

This is why overcurrent protection is not a standalone breaker-selection task. It is the final protection decision after conductor sizing has already been checked.

## 4. Common violations

1. **Using Supplementary Protectors for Branch Circuits:** Using UL 1077 "mini-breakers" to protect outgoing field wiring.
2. **Improper Tap Rule Application (240.21):** Misapplying the "10-foot" or "25-foot" tap rules for conductors inside or leaving the panel without meeting the specific termination and enclosure requirements.
3. **Ignoring Transformer Protection (450.3 via 240.21(C)):** Failing to provide primary and/or secondary protection for control power transformers (CPTs) based on their specific kVA rating.
4. **Inadequate Interrupting Rating:** Installing breakers with a 10kA AIC rating in a facility where the available fault current (AFC) is 42kA.
5. **Protecting to the Wrong Ampacity Column:** Selecting the OCPD from a conductor's higher insulation-column value without respecting terminal-temperature limitations.

## 5. Change log

* 2026-01-15 — Initial draft created; integrated supplementary vs. branch circuit distinctions.
* 2026-03-09 — Corrected Article 240.4 reference and expanded conductor-protection logic, small-conductor limits, and terminal-temperature coordination.
