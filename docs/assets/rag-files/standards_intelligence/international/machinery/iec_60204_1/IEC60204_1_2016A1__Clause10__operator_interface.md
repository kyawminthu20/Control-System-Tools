<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "10"
  clause_title: "Operator interface and machine-mounted control devices"

INDEX_TAGS:
  topics: ["operator_interface", "hmi", "controls"]
-->

Clause 10 of **IEC 60204-1** focuses on the "Human-Machine Interface" (HMI). It ensures that the devices an operator touches—buttons, switches, and touchscreens—are intuitive, durable, and designed to prevent accidental activation. This clause turns ergonomic best practices into mandatory safety requirements.

---

## 0. Scope

This clause covers the requirements for **operator interface devices** mounted on the machine or in control stations. This includes:

* **Push-buttons** and selector switches.
* **Indicator lights** and display screens (HMIs).
* **Emergency Stop devices** (buttons, pull-cords).
* **Enable devices** (e.g., three-position "dead-man" switches).

## 1. Control Device Behavior

The physical behavior and color of a button must match its function to ensure the operator does not make a critical error during a high-stress event.

* **Colors of Push-buttons:**
* **RED:** Emergency Stop and Stop (Stop/Off).
* **GREEN:** Start/On (preferred, though White is also allowed).
* **YELLOW:** Abnormal condition/Reset.
* **BLUE:** Mandatory action (e.g., must press to reset a fault).


* **Indicator Lights (Colors and Meanings):**
* **RED:** Emergency (Danger, immediate action required).
* **YELLOW:** Abnormal (Warning, attention required).
* **GREEN:** Normal (Machine ready, safe to proceed).
* **BLUE:** Mandatory (Operator action required).


* **Standardized Symbols:** Whenever possible, buttons should be marked with standardized symbols, such as **"I"** for Start/On and **"O"** for Stop/Off.

## 2. Ergonomic Considerations

The physical layout of the controls must protect the operator and prevent "unintended operation."

* **Location:** Control devices must be mounted between **0.6m and 1.9m** above the floor (1.7m is recommended for frequent use). They must be placed so the operator is not in a "danger zone" while operating them.
* **Prevention of Accidental Activation:** Buttons that initiate a hazardous motion (like a "Cycle Start") must be **shrouded** or recessed so they cannot be bumped by an elbow or a passing cart.
* **Feedback:** The operator must receive clear feedback that a command was received. This can be tactile (a "click"), visual (the button lights up), or audible.
* **HMI (Touchscreen) Safety:** Touchscreens are generally not permitted for Emergency Stop or any function where the failure of the screen could lead to a hazardous situation. Physical, "hard-wired" buttons are required for these critical tasks.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Added 2018 requirements for HMI display limitations and standardized button color meanings.

