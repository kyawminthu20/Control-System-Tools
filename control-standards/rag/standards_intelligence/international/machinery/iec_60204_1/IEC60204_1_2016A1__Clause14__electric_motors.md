<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "14"
  clause_title: "Electric motors and associated equipment"

INDEX_TAGS:
  topics: ["motors", "drives"]
-->

Clause 14 of **IEC 60204-1** (2016+AMD1:2021) provides the requirements for the selection and application of electric motors and their associated drive systems (VFDs, servos, etc.). As motors are the primary source of mechanical motion and potential kinetic energy hazards, this clause ensures they are controlled and protected against electrical and mechanical stress.

---

## 0. Scope

This clause applies to the **selection and installation** of electric motors and their control gear (drives). It focuses on:

* Ensuring the motor is suitable for the environment and the mechanical load.
* The coordination between the motor and the power electronics (VFDs/Servos).
* The safety of personnel during motor maintenance and unintended restarts.

## 1. Motor Protection and Control

Protection is mandatory to prevent motor failure from causing fire or electric shock.

* **Overload Protection:** Motors exceeding **0.5 kW** must have overload protection. This is typically achieved via thermal sensors (PTC/KTY) embedded in the windings or electronic overload relays that model the motor's "thermal envelope."
* **Protection against Over-speed:** If a motor can reach dangerous speeds (e.g., during a drive failure or a mechanical runaway), independent over-speed detection must be provided to initiate a Stop Category 0 or 1.
* **Safe Isolation:** Every motor must be capable of being isolated from its power source for maintenance. For smaller motors, this can be the main disconnect; for larger or remote motors, a local lockable "repair switch" is often required.

## 2. Drive Integration

Modern machines rely heavily on **Power Drive Systems (PDS)**. Clause 12 dictates how these must be integrated into the machine’s safety architecture:

* **STO (Safe Torque Off):** When a drive is used as part of a safety function (like an E-stop), it must use a certified STO input to ensure the drive cannot generate torque, even if the internal logic fails.
* **Braking and Energy Dissipation:** If the motor acts as a generator during stopping (regenerative braking), the drive system must manage the excess energy via braking resistors or regenerative units to prevent "Overvoltage" faults that could disable the braking function.
* **EMC Considerations:** Drives are major sources of electromagnetic noise. Clause 12 requires the use of **shielded motor cables** and proper 360° bonding of the shield at both the drive and motor ends to prevent interference with sensors and control logic.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated to include STO requirements and specific guidance on 360° shield bonding for EMC.
