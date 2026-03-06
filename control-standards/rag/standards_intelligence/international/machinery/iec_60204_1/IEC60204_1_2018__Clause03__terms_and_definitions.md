<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "3"
  clause_title: "Terms and Definitions"

INDEX_TAGS:
  topics: ["definitions", "terminology"]
-->

Clause 3 of **IEC 60204-1** acts as the "legal dictionary" for the standard. Precise terminology is critical here because a misunderstanding of a term—such as the difference between "reset" and "restart"—can lead to a machine design that fails safety certification or, worse, causes an accident.

---

## 0. Key Definitions for Control Engineers

Several terms form the foundation of the technical requirements found in later clauses:

* **Protective Bonding Circuit:** The whole of the protective conductors and conductive parts used for protection against electric shock in the event of an insulation failure.
* **Control Circuit:** The circuit used for the control of the machine and for the protection of the power circuits.
* **Safety Function:** A function of a machine whose failure can result in an immediate increase of the risk(s).
* **Interlock (for safety):** An arrangement that connects a guard or device with the control system so that the machine cannot operate until the guard is closed.

## 1. Terms That Affect Design Decisions

The standard defines specific machine states that dictate how an engineer must program the PLC logic:

* **Stop Category 0:** Stopping by immediate removal of power to the machine actuators (i.e., an uncontrolled stop).
* **Stop Category 1:** A controlled stop with power available to the machine actuators to achieve the stop and then removal of power when the stop is achieved.
* **Emergency Stop:** A function that is intended to avert arising or reduce existing hazards to persons, damage to machinery or to work in progress.
* **Fault:** The state of an item characterized by inability to perform a required function, excluding the inability during preventive maintenance or other planned actions.

## 2. Common Misinterpretations

Misunderstanding these specific terms often leads to compliance "rejections" during final inspections:

* **Neutral (N) vs. Protective Earth (PE):** While both are technically grounded in the facility, IEC 60204-1 treats them very differently. The Neutral is a **current-carrying** conductor; the PE is **not** intended to carry current except during a fault.
* **Reset vs. Start:** A "Reset" (e.g., after an E-Stop is pulled out) must only restore the safety system to a state where it *can* be started. It must **never** initiate motion by itself.
* **Direct Contact vs. Indirect Contact:**
* *Direct:* Touching a live wire (Basic Protection).
* *Indirect:* Touching the machine frame that has become live due to a fault (Fault Protection).



## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Expanded stop category definitions and added distinction between N and PE conductors for clarity.

---

### Would you like me to move on to **Clause 4**, which covers **General Requirements**—including the mandatory "Operating Conditions" (temperature, humidity, and altitude) that a machine must survive?