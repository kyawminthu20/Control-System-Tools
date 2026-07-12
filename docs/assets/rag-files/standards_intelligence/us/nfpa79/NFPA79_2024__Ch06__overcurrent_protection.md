<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "6"
  chapter_title: "Overcurrent Protection"

INDEX_TAGS:
  topics: ["overcurrent", "short_circuit", "protection"]
-->

## 0. Intent

The intent of Chapter 7 is to define the requirements for protecting machine conductors and equipment against the effects of excessive current. It aims to:

* **Prevent Fire:** By ensuring wires do not reach temperatures that could ignite insulation.
* **Minimize Damage:** By interrupting short circuits before they cause catastrophic failure of components like contactors or PLCs.
* **Maintain Integrity:** Ensuring that a fault in one part of the machine does not necessarily compromise the safety systems of the entire machine.

## 1. Branch Circuit Protection

Branch circuit overcurrent protective devices (OCPDs) are the "first line of defense" for the machine's internal wiring.

* **Location:** Protective devices must be provided at the point where the conductor to be protected is connected to the supply.
* **Sizing:** Conductors must be protected in accordance with their ampacity. NFPA 79 provides specific tables (similar to NEC Table 310.16) for sizing wires and their corresponding fuses or circuit breakers.
* **Device Types:** Only "listed" branch-circuit-rated breakers or fuses can be used for branch circuit protection. Supplemental protectors (like "mini" breakers) are not permitted to replace branch circuit protection.

## 2. Coordination with NEC / UL

A major requirement in the 2024 edition is the calculation and labeling of the **Short-Circuit Current Rating (SCCR)**.

* **SCCR Alignment:** The SCCR of the machine must be equal to or greater than the "available fault current" at the installation site. This requires coordination with the facility engineer (governed by **NEC Art. 670**).
* **Component Interaction:** Designers must use UL-listed combinations of motor starters and OCPDs. If a component (like a VFD) has a 100kA SCCR only when used with Class J fuses, using a thermal-magnetic breaker instead would invalidate the machine's safety rating.

## 3. Control-System Impact

Overcurrent protection directly influences how the control system is wired and how it behaves during a fault:

* **Common Control Feed:** If a single OCPD protects multiple control circuits, a minor fault in one sensor could take down the entire safety system. Chapter 7 encourages (and in some cases requires) "selective coordination" or individual circuit protection to maintain machine uptime and safety monitoring.
* **Transformers and Power Supplies:** Specific rules apply to the protection of the primary and secondary sides of control transformers and DC power supplies to prevent "nuisance tripping" during the high inrush current of firing up the machine.
* **Grounded Circuits:** Overcurrent devices must **not** be placed in the grounded conductor (the neutral or common), as opening that circuit could leave the rest of the system "hot" even though it appears dead.
