<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "9"
  chapter_title: "Control Circuits and Control Functions"

INDEX_TAGS:
  topics: ["control_circuits", "stop_functions", "emergency_stop"]
-->


## 0. Control Philosophy

The core philosophy is **predictability and fail-safe operation**. A control system must be designed so that any failure—whether it be a broken wire, a welded relay contact, or a software crash—does not result in a hazardous condition.

* **De-energization to Stop:** Most control circuits are designed such that "opening" the circuit (removing power) triggers a stop.
* **Voltage Limits:** Control circuits are typically required to operate at a lower voltage (e.g., 120VAC or 24VDC) via a control transformer or power supply to protect operators at the HMI or pushbutton stations.

## 1. Start/Stop Behavior

The standard is very specific about how a machine enters and exits motion:

* **Start Functions:** A start command must only be effective if all safety guards are closed and no E-stops are active. Sustained "hold-to-run" or "two-hand control" may be required for specific hazardous manual operations.
* **Stop Categories:** * **Category 0:** Immediate removal of power (uncontrolled stop).
* **Category 1:** Controlled stop with power available to the actuators, followed by power removal once stopped.
* **Category 2:** A controlled stop where power is left available to the machine (not suitable for emergency stops).



## 2. Emergency Stop Concepts

The Emergency Stop (E-Stop) is a "supplementary" safety measure and must never be used as a substitute for proper guarding.

* **Priority:** The E-stop function must override all other functions and operating modes.
* **Resetting:** Resetting an E-stop button must **not** restart the machine. It must only "permit" a restart, which then requires a separate, deliberate action (like pressing a "Start" button).
* **Device Requirements:** E-stop buttons must be red, mushroom-headed, and have a yellow background. They must be "self-latching," meaning they stay pushed in until manually twisted or pulled out.

## 3. Safety vs. Standard Control Separation

With the rise of Safety PLCs, the 2024 edition emphasizes the integrity of the safety signal path.

* **Independence:** Safety-related control functions must be able to perform their task regardless of the state of the "standard" (non-safety) PLC or HMI.
* **Software Safety:** If safety is handled via software, it must be done in a **Safety-Rated Controller** (SIL or Performance Level rated) using validated safety function blocks. Standard "user-defined" rungs in a regular PLC are generally not permitted for critical safety interlocking.
* **Monitoring:** The system should monitor for "faults in the control circuit," such as a cross-short between two 24V wires that might "trick" the system into thinking a gate is closed when it is actually open.

---
