<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "5"
  clause_title: "Incoming Supply"

INDEX_TAGS:
  topics: ["incoming_supply", "supply_disconnect"]
-->

Clause 5 of **IEC 60204-1** defines how the machine connects to the world. It dictates the "boundary" between the facility’s electrical installation and the machine’s internal electrical system. This clause is critical for the safety of maintenance personnel, as it governs how the machine is isolated from its power source.

---

## 0. Scope

This clause specifies the requirements for the **incoming supply connection** and the devices used for **disconnection and switching**. It covers:

* How the power enters the machine (terminals).
* The electrical characteristics the machine is designed to handle.
* The physical requirements for the main "supply disconnecting device" (the main switch).

## 1. Supply Characteristics

The machine builder must specify the electrical parameters required for the machine to operate safely.

* **Voltage and Frequency:** The machine must be designed to withstand a steady-state voltage of  to  times the nominal voltage.
* **Harmonics and Transients:** The equipment must be immune to specified levels of voltage dips, surges, and harmonic distortion common in industrial grids.
* **Type of System:** The documentation must state whether the machine is compatible with **TN, TT, or IT** earthing systems.

## 2. Isolation and Disconnect Rules

Every machine must have a **supply disconnecting device** that meets specific criteria:

* **Accessibility:** It must be easily accessible and located between m and m above the servicing level.
* **Clear Indication:** It must have only two positions (ON and OFF), with the OFF position clearly marked with "O" or "OFF".
* **Lockability:** It must be lockable in the OFF position (e.g., for LOTO) without the need for a key to be kept in the lock.
* **Breaking Capacity:** The device must be capable of breaking the current of the largest motor when stalled, plus the sum of all other loads.
* **Handle Color:** * If the switch is also used for **Emergency Switching (Emergency Stop)**, the handle must be **Red** with a **Yellow** background.
* Otherwise, it is typically Black or Gray.



## 3. Comparison to NFPA 79 Ch.5

While very similar, there are a few key differences between the IEC and North American (NFPA) approaches:

| Feature | IEC 60204-1 (Clause 5) | NFPA 79 (Chapter 5) |
| --- | --- | --- |
| **Neutral Handling** | Neutral must generally be disconnected if it is a current-carrying conductor. | Neutral is often not disconnected if it is solidly grounded. |
| **Operating Height** | Max height of m (m recommended). | Max height of m ( ft  in). |
| **Exception Circuits** | Called "Exception Circuits" (e.g., lighting, sensors). | Called "Line Side Taps" or "Always-on" circuits. |
| **Color Coding** | Black/Gray for normal; Red/Yellow for E-stop. | Red/Yellow for E-stop is common but requires specific "listed" handle types. |

## 4. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with specific earthing system (TN/TT/IT) requirements and color convention details.

---

### Would you like me to move on to **Clause 6**, which covers **Protection Against Electric Shock** (the rules for "basic" and "fault" protection)?