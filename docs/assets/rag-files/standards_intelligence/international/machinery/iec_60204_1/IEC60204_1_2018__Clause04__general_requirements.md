<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "4"
  clause_title: "General Requirements"

INDEX_TAGS:
  topics: ["general_requirements", "safety_principles"]
-->

Clause 4 of **IEC 60204-1** serves as the "constitution" for the entire standard. It establishes the foundational safety objectives and the environmental conditions that the machine must be designed to withstand. Before diving into specific wire colors or component ratings, Clause 4 requires the designer to consider the big picture of the machine's lifecycle and its operating environment.

---

## 0. Safety Philosophy

The core philosophy is based on the **reduction of risk** through design. It mandates that the electrical equipment shall be suitable for its intended use and that any failure of the electrical equipment shall not lead to a hazardous situation.

* **Hazard Identification:** Design begins with identifying electrical hazards, including shock, fire, and unintended motion.
* **Operating Conditions:** The equipment must be capable of operating correctly in the specified environment. Clause 4 defines "Standard" conditions (e.g., ambient temperature between °C and °C, humidity up to  percent at °C) unless otherwise specified.
* **Transportation and Storage:** The design must account for the physical stresses and temperatures the machine will face before it is even powered on at the end-user site.

## 1. General Electrical Design Principles

Clause 4 outlines several "golden rules" for the electrical architecture:

* **Electromagnetic Compatibility (EMC):** The equipment must not generate electromagnetic disturbances that interfere with other devices, and it must have a level of immunity to disturbances in its environment.
* **Supply Voltage Variations:** The machine must be designed to operate correctly despite standard fluctuations in the utility power (typically  percent of nominal voltage).
* **Protection against Ingress:** The selection of enclosures must be based on the environmental conditions (dust, liquids, etc.), referencing the IP ratings established in IEC 60529.

## 2. Control-System Interpretation

From a control-engineering perspective, Clause 4 dictates the "predictability" of the system:

* **Failsafe Principles:** The control system must be designed so that a fault in the control circuit (e.g., a short to ground or an open circuit) does not result in the machine starting unexpectedly or failing to stop when requested.
* **Logical Coordination:** When a machine has multiple control stations (e.g., a main HMI and a local pendant), Clause 4 requires that the system be designed so that only one station can exercise control at a time, preventing conflicting commands.
* **Selection of Components:** All electrical components must comply with their respective IEC standards and be applied within their specified ratings (voltage, current, and duty cycle).

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with specific references to EMC requirements and supply voltage variation limits for the 2018 edition.

---

### Would you like me to proceed to **Clause 5**, which details the **Incoming Supply Line Link and Disconnecting Devices** (the requirements for the main power switch and isolation)?