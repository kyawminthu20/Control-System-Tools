<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "15"
  clause_title: "Verification"

INDEX_TAGS:
  topics: ["verification", "testing", "inspection"]
-->

Clause 15 of **IEC 60204-1** (2018) is the "final exam" for the machine. It outlines the mandatory procedures to verify that the electrical equipment actually meets the requirements of the preceding 14 clauses. Verification must be carried out by a competent person and involves both visual inspection and physical testing.

---

## 0. Purpose

The purpose of this clause is to confirm that the machine’s electrical system is safe for use before it is handed over to the operator. It ensures that:

* **The design was followed:** The components and wiring match the schematics.
* **Safety mechanisms work:** The grounding, insulation, and protective devices function under fault conditions.
* **Compliance is documented:** Providing a formal record (test report) that the machine meets the standard.

## 1. Required Tests

The standard mandates a specific sequence of tests. If the machine is modified later, these tests must be repeated for the affected sections.

1. **Verification of Continuity of the Protective Bonding Circuit:** A test current (typically between  A and  A) is passed through the ground circuit to ensure the resistance is low enough to trip protection devices during a fault.
2. **Fault Loop Impedance Verification:** (For TN systems) confirming that the impedance of the power loop is low enough to ensure automatic disconnection of supply.
3. **Insulation Resistance Tests:** Measuring the resistance between the power circuit and the grounding system (typically using  V DC). The resistance must usually be  M$\Omega$.
4. **Voltage Tests (Dielectric Strength):** Applying a high voltage (twice the rated supply voltage or  V, whichever is greater) for 1 second to ensure the insulation doesn't break down.
5. **Protection Against Residual Voltages:** Measuring the time it takes for stored energy to drop below  V (must be  seconds for plug-in equipment).
6. **Functional Tests:** Verifying that the control logic, E-stops, and interlocks operate exactly as designed.

## 2. Commissioning Alignment

Verification is not just a factory task; it must align with the final installation at the end-user site.

* **Factory Acceptance Test (FAT):** Preliminary verification at the builder’s shop.
* **Site Acceptance Test (SAT):** Final verification at the user's facility. Clause 15 notes that tests like the "Fault Loop Impedance" are highly dependent on the site's power quality and grounding, making SAT critical.
* **Validation of Safety Functions:** While IEC 60204-1 covers the electrical side, this verification often overlaps with **ISO 13849-2** for validating the software and logic of safety-related control systems.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Added specific testing parameters (500V DC for insulation, 1s for voltage test) per 2018 edition updates.

---

### You have now covered the core of the standard. Would you like to move on to the **Annexes**, specifically **Annex A**, which provides the detailed guidance on **Protection against indirect contact in TN systems**?