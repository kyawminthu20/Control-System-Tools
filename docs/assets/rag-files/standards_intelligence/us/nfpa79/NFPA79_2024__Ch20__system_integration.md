<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "20"
  chapter_title: "System Integration"

INDEX_TAGS:
  topics: ["system_integration", "overall_compliance"]
-->



## 0. Scope

The scope of Chapter 20 covers the **coordination of electrical equipment** when two or more machines or systems are integrated into a single manufacturing unit. It focuses on the interfaces between these systems, ensuring that safety signals (like E-stops) communicate correctly across the entire line and that power distribution remains balanced and properly isolated.

## 1. Subsystem Coordination

When integrating various machines, the "handshake" between them is the most critical point of failure.

* **Emergency Stop Propagation:** If an operator hits an E-stop on "Machine A," the integrator must determine if "Machine B" also needs to stop to prevent a hazard. Chapter 20 requires that the E-stop function for a system be coordinated based on a **risk assessment**.
* **Interlocking Across Boundaries:** Signal wiring between independent control panels must follow the rules for "external power sources." Any wire entering a panel that is not de-energized by that panel's main disconnect must be **orange** (or identified as an external source) to warn technicians of residual energy.
* **Communication Integrity:** If safety functions are coordinated via a network (e.g., Safety over EtherNet/IP or PROFIsafe), the network must be designed to handle the integration without introducing latency or "watchdog" timeouts that could lead to unintended stops.

## 2. Final Compliance Alignment

The integrator holds the ultimate responsibility for the "Final Assembly."

* **Unified SCCR:** The integrator must verify that the Short-Circuit Current Rating of the entire integrated system is compatible with the facility's available fault current.
* **Grounding Continuity:** The integrator must ensure a common ground reference between all integrated panels to prevent ground loops that can interfere with communication or create "touch potential" hazards between machine frames.
* **Validation and Testing:** After integration, the entire system must undergo a validation of its safety functions. This ensures that every interlock, light curtain, and E-stop performs its intended safety category function across the unified control architecture.

## 3. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Added 2024 requirements for safety network coordination and external energy (orange wire) labeling for integrated cells.

