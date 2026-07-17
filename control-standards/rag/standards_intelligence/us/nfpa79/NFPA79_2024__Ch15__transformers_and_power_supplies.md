<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "15"
  chapter_title: "Transformers and Power Supplies"

INDEX_TAGS:
  topics: ["transformers", "power_supplies", "control_power"]
-->


## 0. Scope

This chapter covers the requirements for **control transformers and DC power supplies** used to provide power to control circuits, signaling devices, and electronic equipment. It establishes the rules for sizing, protecting, and isolating these devices to ensure that the control system remains stable and safe even during electrical transients.

## 1. Control Power Architectures

The way power is distributed within a machine depends on the complexity of the control system:

* **Isolation Requirements:** Control transformers must have separate primary and secondary windings (isolated). Using an "autotransformer" (which shares a winding) is generally prohibited for control circuits because it doesn't provide the necessary safety isolation from the line voltage.
* **DC Power Supplies:** Switched-mode power supplies (SMPS) are now the standard for 24V DC control. Under NFPA 79, these must be **short-circuit protected** and, in many cases, "Class 2" rated if they are used to power certain types of limited-energy sensors or networks.
* **Sizing for Inrush:** Transformers must be sized not just for the "steady-state" load, but for the **inrush current** of all solenoids and contactors hitting the circuit at once. A transformer that is too small will cause a "voltage sag," which can lead to safety relays "chattering" or PLC CPUs rebooting.

## 2. Grounding of Secondaries

This is one of the most technical safety areas in the standard. How you ground the secondary side of a transformer or power supply determines how the system reacts to a wire fault.

* **Grounded Systems (Common):** One side of the secondary circuit (usually the "common" or X2 terminal) is bonded to the machine's protective earth (PE). This ensures that a ground fault on any signal wire will immediately trip the fuse or breaker, stopping the machine.
* **Ungrounded Systems (Rare):** If the secondary is left "floating" (ungrounded), a ground-fault detection system must be installed to provide an alert or a stop command. This is usually only seen in specific continuous-process industries where an immediate trip is more hazardous than a single ground fault.
* **Overcurrent Protection:** Every transformer must have overcurrent protection on the secondary side. Primary side protection is also required, and the sizing must follow the primary/secondary overcurrent-protection ratios specified in NFPA 79:2024 Chapter 15 [table reference unverified against the licensed text — confirm the exact table number before citing], which account for the high "magnetizing" inrush of the transformer itself.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with 2024 specifics on DC power supply Class 2 requirements and magnetizing inrush protection.
