<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "8"
  clause_title: "Equipotential bonding"

INDEX_TAGS:
  topics: ["bonding", "protective_earth"]
-->

Clause 8 of **IEC 60204-1** defines the electrical "backbone" of the machine. It ensures that all accessible conductive parts are connected to a common reference point. This prevents dangerous voltage differences between different parts of the machine and provides a reliable path for fault currents to trigger protection devices.

---

## 0. Purpose

The primary purpose of equipotential bonding is to ensure **personnel safety** and **system reliability**. It achieves this by:

* **Reducing Shock Risk:** Ensuring that no two simultaneously accessible conductive parts (e.g., a conveyor frame and a control panel) have a significant voltage difference between them.
* **Enabling Fault Protection:** Providing a low-impedance path to allow high fault currents to flow, which quickly trips the overcurrent protection devices (circuit breakers/fuses).
* **Functional Reliability:** Providing a stable reference for electronic signals and dissipating electromagnetic interference (EMI).

## 1. Bonding Strategy

IEC 60204-1 requires a hierarchical approach to the **Protective Bonding Circuit**:

* **The Protective Extra-Low Voltage (PE) Terminal:** Every machine must have a single main protective earthing terminal for connection to the external protective earthing system.
* **Continuity of the Circuit:** All structural metal parts (frames, ducts, motor housings) must be bonded. If a part is removed for maintenance (like a hinged door), a flexible "bonding jumper" (braided strap or green-and-yellow wire) must maintain the connection.
* **Connection Type:** Connections must be secured with mechanical fasteners (bolts/washers) that penetrate paint or coatings to ensure metal-to-metal contact. Moving parts must use conductors specifically designed for flexing.
* **Exclusions:** Small parts (screws, rivets, nameplates) that are unlikely to become energized or are too small to be gripped do not typically require individual bonding.

## 2. Noise vs. Safety Bonding

One of the most common challenges for control engineers is balancing **Safety Earthing** with **Functional Earthing (FE)**:

* **Protective Bonding (Safety):** Focuses on high-current capacity to prevent shock. These conductors are always **Green-and-Yellow**.
* **Functional Bonding (Noise):** Focuses on high-frequency performance to protect sensitive data (like Ethernet or encoder signals) from noise. This is often achieved using shielded cables and "Functional Earth" terminals, sometimes marked with a specific symbol (a circle with a "broken" ground).
* **The "One-Point" Rule:** To avoid "ground loops" (which cause electrical noise), the IEC standard generally recommends that the functional and protective systems meet at a single, central point (the main PE busbar).
* **Equipotentiality:** In systems with Variable Frequency Drives (VFDs), flat braided straps are preferred over round wires for bonding because they have lower impedance at high frequencies, better suppressing EMI.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Clarified requirements for bonding hinged doors and the distinction between safety and functional earthing.
