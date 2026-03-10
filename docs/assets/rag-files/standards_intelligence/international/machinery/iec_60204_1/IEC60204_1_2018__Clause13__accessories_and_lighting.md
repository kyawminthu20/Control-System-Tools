<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: 2018

IEC_HIERARCHY:
  clause: "13"
  clause_title: "Accessories and Lighting"

INDEX_TAGS:
  topics: ["accessories", "lighting"]
-->

Clause 13 of **IEC 60204-1** (2018) covers the electrical requirements for peripheral components that support the machine's operation but are not part of the primary power or control logic. This includes the illumination of work areas and the integration of auxiliary devices like power outlets for service tools.

---

## 0. Scope

This clause specifies the requirements for **lighting circuits** and **auxiliary equipment** (such as socket-outlets) that are attached to or integrated into the machine. The goal is to ensure these accessories do not compromise the machine's overall electrical safety or create a shock hazard for maintenance personnel.

## 1. Machine Lighting

Proper illumination is essential for safe operation and maintenance, but it must be wired to avoid interference with the machine's main safety functions.

* **Connection:** Lighting circuits must be connected to the load side of the main supply disconnecting device unless they are designated as "exception circuits" (e.g., for maintenance lighting when the main power is off).
* **Voltage Limits:** To reduce shock risk, lighting circuits should preferably be supplied at a nominal voltage not exceeding **50V**. If higher voltages are used (up to 230V), specific protection measures (like RCDs/GFCIs) are required.
* **Protection:** Every lighting circuit must have its own overcurrent protection (fuses or breakers) independent of other circuits.
* **Fittings and Lampholders:** Lighting units must be suitable for the machine's environment (e.g., resistant to oil, vibration, or coolants) and must be securely mounted to prevent accidental contact or breakage.

## 2. Auxiliary Equipment

This section primarily deals with **socket-outlets** used for handheld tools or programming terminals.

* **Socket-Outlets:** If the machine provides power outlets (e.g., for a laptop or drill), they must be protected by a **Residual Current Device (RCD)** with a rated tripping current not exceeding **30mA**.
* **Identification:** Socket-outlets that remain energized when the main disconnect is in the "OFF" position must be clearly identified with a warning label and should use the color **Orange** for the internal wiring to indicate an external power source.
* **Current Limitation:** Auxiliary circuits must be limited in capacity to ensure they do not overload the machine's primary supply connection.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Added 2018 requirements for RCD protection on all general-purpose socket-outlets and clarified "exception circuit" labeling.

---

### Would you like me to move on to **Clause 14**, which covers **Conductors and Cables** (sizing, insulation, and current-carrying capacity rules)?