<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "7"
  clause_title: "Protection of equipment"

INDEX_TAGS:
  topics: ["equipment_protection", "overcurrent"]
-->

Clause 7 of **IEC 60204-1** focuses on the "self-preservation" of the machine's electrical system. While Clause 6 focuses on protecting humans from the machine, Clause 7 focuses on protecting the machine from internal and external electrical faults that could lead to fire, mechanical damage, or total system failure.

---

## 0. Purpose

The purpose of this clause is to ensure that the electrical equipment is protected against the effects of:

* **Overcurrents** (resulting from short-circuits or overloads).
* **Earth faults** (insulation breakdown to the machine frame).
* **Abnormal temperatures** (overheating of motors or enclosures).
* **Supply interruptions** or voltage drops.

By implementing these protections, the machine remains within its "Safe Operating Area," preventing hardware destruction that could lead to safety hazards.

## 1. Overcurrent and Overload Protection

IEC 60204-1 distinguishes between protecting wires from burning up (overcurrent) and protecting motors from wearing out (overload).

* **Overcurrent Protection:** Must be provided for all "live" conductors. This is typically achieved using fuses or circuit breakers. The device must be sized to protect the smallest conductor in the circuit.
* **Short-Circuit Current Rating (SCCR):** The protection devices must be capable of breaking the maximum prospective fault current at the point of installation without exploding or failing to clear the arc.
* **Motor Overload Protection:** Motors rated over **0.5 kW** must have protection against overheating. This is usually done with thermal relays or electronic "e-overloads" that monitor the current over time.
* **Location of Devices:** Protection devices should be placed at the point where a reduction in the cross-sectional area of the conductors occurs (unless the upstream device already protects the smaller wire).

## 2. Environmental Protection

Electrical equipment must be shielded from the specific rigors of its factory environment to prevent premature failure.

* **Ingress Protection (IP Rating):** As referenced in Clause 4, the equipment must be housed in enclosures that prevent the entry of dust, oil, and water. For example, a machine in a wash-down area typically requires **IP65** or higher.
* **Thermal Management:** If the control panel contains heat-generating components (like VFDs or large power supplies), Clause 7 requires the use of cooling fans, heat exchangers, or air conditioners to prevent the internal temperature from exceeding the components' ratings.
* **Vibration and Shock:** Equipment must be mounted to withstand the mechanical vibrations of the machine. This may require the use of DIN-rail end-anchors, spring-terminal connections, or anti-vibration mounts for sensitive electronics.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with specific kilowatt thresholds for motor protection and SCCR requirements for the 2018 edition.
