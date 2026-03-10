<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "14"
  clause_title: "Marking and Documentation"

INDEX_TAGS:
  topics: ["marking", "documentation"]
-->

Clause 14 of **IEC 60204-1** (2018) deals with the "informational safety" of the machine. Even a perfectly engineered electrical system is dangerous if a technician cannot identify which wire is live or if the schematics are missing. This clause ensures that the machine is self-describing and that all necessary technical data is available for its entire lifecycle.

---

## 0. Scope

This clause specifies the requirements for **marking, signs, and technical documentation**. It ensures that:

* The machine can be identified (manufacturer, model, ratings).
* Hazards are clearly communicated via warning labels.
* Conductors and components are uniquely identified to match technical drawings.
* A comprehensive documentation package is provided for installation, operation, and maintenance.

## 1. Identification and Labels

The machine and its components must be clearly and durably marked to prevent errors during servicing.

* **Nameplate Requirements:** The main control enclosure must have a permanent nameplate including the manufacturer's name, serial number, supply voltage, frequency, full-load current, and the **Short-Circuit Current Rating (SCCR)**.
* **Warning Signs:** Enclosures containing electrical hazards must be marked with the "Lightning Bolt" symbol (ISO 7010-W012). If residual voltage exists after power-off, a warning label specifying the discharge time is required.
* **Component Marking:** Every relay, PLC, and breaker must be marked with a reference designation (e.g., `-K1`, `-Q1`) that matches the electrical schematics.
* **Conductor Identification:** Wires must be identified at each termination by color, number, or alphanumeric code.

## 2. Documentation Set

The "Technical File" provided with the machine is a normative requirement. It must be provided in a medium agreed upon with the user (digital is standard in 2026, but hard copies are often required for the site).

* **Electrical Schematics:** Circuit diagrams showing the functional relationship of the electrical equipment. These must use standard IEC symbols (IEC 60617).
* **Instruction Manual:** Must include procedures for safe commissioning, operation, and a description of the safety functions and their maintenance/testing intervals.
* **Parts List:** A clear list of components, specifically identifying safety-related parts, to ensure correct replacement.
* **Installation Requirements:** Specifications for the external power supply, grounding requirements, and environmental conditions.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with 2018 requirements for SCCR marking on the nameplate and digital documentation standards.

---

### Would you like me to move on to **Clause 15**, which covers **Technical Documentation and Verification** (the actual testing and "checkout" procedures to prove the machine is safe)?