<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "6"
  clause_title: "Protection Against Electric Shock"

INDEX_TAGS:
  topics: ["electric_shock", "touch_safe"]
-->

Clause 6 of **IEC 60204-1** is one of the most critical sections for ensuring operator safety. It defines the strategy for preventing injury from electrical energy, moving from the prevention of contact with live parts to the safety of the machine frame itself during a failure.

---

## 0. Hazard Model

The standard views electrical safety through a "two-layer" hazard model to prevent current from passing through the human body:

* **Basic Protection (Direct Contact):** Preventing a person from touching parts that are normally "live" (e.g., terminal blocks or busbars).
* **Fault Protection (Indirect Contact):** Preventing a person from being shocked by touching parts that are normally "dead" (like the machine frame or motor housing) but have become energized due to an insulation failure.

## 1. Protective Measures

To mitigate the risks identified in the hazard model, specific engineering measures must be implemented:

### Basic Protection Measures

* **Enclosures:** Live parts must be inside an enclosure rated to at least **IP2X** or **IPXXB**. If the top surface is accessible, it must be **IP4X** or **IPXXD** to prevent small items from falling in.
* **Insulation:** Live parts must be completely covered by insulation that can only be removed by destruction (e.g., wire jacketing).
* **Residual Voltage:** After disconnecting power, any remaining stored energy (like in VFD capacitors) must be discharged to below **60V** within **5 seconds**.

### Fault Protection Measures

* **Automatic Disconnection of Supply:** This is the most common method. It relies on a "Protective Bonding Circuit" (grounding) to create a low-impedance path back to the source. In the event of a fault, the current surges, causing the circuit breaker or fuse to trip immediately.
* **Disconnection Times:** For TN systems, the supply must typically be disconnected within **0.4 seconds** for 230V circuits to prevent heart fibrillation.

## 2. Control Voltage Considerations

One of the most effective ways to provide protection is to reduce the energy available. This leads to the use of **PELV (Protective Extra-Low Voltage)**:

* **Threshold:** PELV circuits operate at voltages not exceeding **25V AC** or **60V DC** (ripple-free).
* **Safety Isolation:** The voltage must be supplied by a safety isolating transformer or an equivalent power supply.
* **Touch Safety:** Because the voltage is so low, "Basic Protection" (insulating the wires) is still required, but "Fault Protection" (grounding the frame) is considered inherently addressed for the control circuit itself.
* **Grounding:** Unlike SELV (Safety Extra-Low Voltage), a **PELV** circuit is connected to the protective bonding circuit (grounded). This ensures that a fault between the power circuit and the control circuit will trip the primary protection.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Added discharge timing for residual voltage and specific disconnection times for TN systems.

---

### Would you like me to move on to **Clause 7**, which covers **Protection of Equipment** (overcurrent, thermal, and earth fault protection)?