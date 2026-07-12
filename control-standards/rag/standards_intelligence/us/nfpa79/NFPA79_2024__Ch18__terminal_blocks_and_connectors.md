<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "18"
  chapter_title: "Terminal Blocks, Connectors, and Wiring Devices"

INDEX_TAGS:
  topics: ["terminal_blocks", "connectors", "field_wiring"]
-->



## 0. Scope

This chapter specifies the requirements for **terminal blocks, plug-and-socket connectors, and other wiring devices** used to terminate conductors. It focuses on ensuring that connections are vibration-resistant, properly identified, and protected against accidental contact. It also establishes the rules for "quick-disconnect" style connectors increasingly used in modular automation.

## 1. Field Wiring Interfaces

The interface between the control panel and the factory floor is a common point of electrical failure. Chapter 18 mandates:

* **Separation of Voltages:** Terminal blocks must be arranged so that high-voltage power terminals (e.g., 480V) are physically separated or partitioned from low-voltage control terminals (e.g., 24V).
* **Terminal Identification:** Each terminal must be marked to correspond with the wire number and the electrical schematics. This marking must be permanent and legible.
* **Connection Integrity:** Terminals must be designed to ensure a "positive" connection. In the 2024 edition, there is a strong preference for **spring-cage (push-in)** or **screw-clamp** terminals that provide constant pressure, as traditional "spade" or "ring" lugs can vibrate loose over time.
* **Plug-and-Socket Connectors:** If used for power circuits, these connectors must have a "first-make, last-break" grounding contact to ensure the machine remains grounded during the mating process.

## 2. Maintenance Implications

How a technician interacts with these devices determines the long-term safety of the machine:

* **Accessibility:** Terminals and connectors must be located so that they can be reached for testing or replacement without dismantling large portions of the machine or creating a hazard from nearby live parts.
* **Protection Against Mis-mating:** Where multiple similar connectors are used (e.g., on a manifold), they must be **keyed or clearly labeled** to prevent a sensor being plugged into a power output, which could cause a "fail-to-on" condition.
* **Touch-Safety:** When disconnected, any "live" side of a plug-and-socket connector must be the female (socket) end or otherwise guarded to prevent accidental finger contact with energized pins.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Updated with 2024 requirements for keyed connectors and "first-make, last-break" grounding rules for power plugs.
