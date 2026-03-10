<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "12"
  chapter_title: "Motors and Associated Equipment"

INDEX_TAGS:
  topics: ["motors", "drives", "motor_protection"]
-->


## 0. Scope

This chapter covers the requirements for **motors, motor-control equipment, and variable speed drives (VFDs)**. It establishes the rules for how these devices must be sized, how they should respond to faults, and how they must be protected from overloads (which differ from the short-circuit protection discussed in earlier chapters).

## 1. Motor Control Integration

Motor control is more than just turning a shaft; it is about safe and predictable movement.

* **Direction of Motion:** The control system must be designed so that the direction of motor rotation is predictable. If reversing a motor could cause damage or injury (e.g., a pump that must not run dry), the control circuit must be physically or logically interlocked to prevent simultaneous "forward" and "reverse" commands.
* **Overload Protection:** Each motor rated at more than  horsepower must be provided with individual overload protection (e.g., thermal heaters or electronic overload relays). This protects the motor windings from overheating due to excessive mechanical load.
* **Restarting:** A motor must not automatically restart after a power failure or an overload trip if such a restart could cause a hazard. A deliberate "Start" action must be required.

## 2. Drive Protection Considerations

With the prevalence of Variable Frequency Drives (VFDs) and Servo Drives, Chapter 12 provides specific guidance for electronic power conversion:

* **Safe Torque Off (STO):** When a drive is used as part of a safety function, it must have a certified "Safe Torque Off" input that physically prevents the drive from generating torque, even if the control logic is still active.
* **Cabling for VFDs:** Due to high-frequency electrical noise, specialized **VFD cable** (with appropriate shielding and grounding) is often required to meet the bonding requirements of Chapter 8 and to prevent "stray" voltages from damaging motor bearings or interfering with sensors.
* **Dynamic Braking:** If a machine has high inertia (like a large flywheel), the drive system must be equipped with dynamic braking or a mechanical brake to ensure the motor stops within the time limits required by the safety assessment.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated to include STO (Safe Torque Off) and VFD-specific cabling requirements for 2024 compliance.

