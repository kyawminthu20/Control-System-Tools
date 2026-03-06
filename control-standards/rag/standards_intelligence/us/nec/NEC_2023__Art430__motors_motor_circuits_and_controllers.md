<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "430"
  article_title: "Motors, Motor Circuits, and Controllers"

INDEX_TAGS:
  topics: ["motors", "drives", "motor_protection"]
-->


# NEC 2023 — Article 430 — Motors, Motor Circuits, and Controllers

## 0. Scope for control panels

Article 430 covers motors, their branch-circuit conductors, and their controllers. In an industrial control panel, this article is the primary guide for selecting and sizing motor starters, variable frequency drives (VFDs), overload relays, and the short-circuit/ground-fault protection (breakers/fuses) specifically for motor loads.

## 1. Motor protection concepts

Motor protection is split into two distinct parts to allow for the high "inrush" current (Locked Rotor Amps) that occurs when a motor starts.

* **Motor Overload Protection (Part III):** Protects the motor and conductors from excessive heat caused by mechanical overloads (e.g., a jammed conveyor).
* *Implementation:* Sized based on the **Nameplate Full Load Amps (FLA)** of the motor, typically at 115% to 125%.


* **Motor Branch-Circuit Short-Circuit and Ground-Fault Protection (Part IV):** Protects against "hard" faults.
* *Implementation:* Sized using **NEC Tables 430.247 through 430.250** (Full Load Current - FLC), not the motor nameplate.
* *Sizing:* Typically **250%** for Inverse Time Breakers and **175%** for Dual-Element Fuses (per Table 430.52).



## 2. VFD considerations (Part X)

Variable Frequency Drives (Adjustable-Speed Drive Systems) have specific requirements under Article 430:

* **Conductor Sizing (430.122):** Circuit conductors supplying a VFD must have an ampacity of at least **125%** of the VFD's rated input current.
* **Disconnecting Means (430.128):** A VFD must have a disconnecting means located within sight of the drive.
* **Protection:** Many VFDs require specific semiconductor fuses (High-Speed) to maintain their listing and SCCR. Using a standard thermal-magnetic breaker instead can void the panel's compliance.

## 3. Coordination with UL 508A

While Article 430 provides the math, **UL 508A** (Section 31) provides the specific assembly rules for panels:

* **Group Motor Rules:** Allows multiple motors to be protected by a single OCPD under strict conditions (must be listed for "Group Installation").
* **Wire Sizing:** UL 508A often allows for smaller internal "tap" conductors than a standard NEC field installation would permit, provided they meet the "1/3rd ampacity" or "10-foot" rules.

## 4. Change log

* 2026-01-15 — Initial draft created; clarified the distinction between FLA (Nameplate) and FLC (NEC Tables).

