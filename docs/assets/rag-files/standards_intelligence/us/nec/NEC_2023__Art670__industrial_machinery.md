<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "670"
  article_title: "Industrial Machinery"

INDEX_TAGS:
  topics: ["industrial_machinery", "machine_wiring", "disconnects"]
  systems: ["machine", "robot_cell", "conveyor"]
-->

# NEC 2023 — Article 670 — Industrial Machinery

## 0. Scope and relationship to NFPA 79

Article 670 applies to the definition and supply-side requirements of industrial machinery. It acts as the bridge to **NFPA 79** (Electrical Standard for Industrial Machinery).

* **Scope:** Covers machines consisting of a combination of equipment (including control panels) that process material by cutting, forming, or assembling.
* **Relationship:** NEC 670 governs the **supply conductors** and **disconnecting means**, while NFPA 79 governs the **internal machine wiring** and safety circuits.

## 1. Machine disconnecting means

A machine must have a primary disconnecting means (670.4(B)) that meets several criteria:

* **Accessibility:** It must be "readily accessible"—reachable without the need to climb over obstacles or use portable ladders.
* **Type:** It must be a motor-circuit switch rated in horsepower, a molded-case circuit breaker, or a molded-case switch.
* **Locking:** It must be capable of being locked in the open (OFF) position and the provision for locking must remain in place whether the lock is installed or not.
* **Location:** Must be located at the point of supply to the machine.

## 2. Where NEC 670 ends and NFPA 79 begins

The "Point of Delivery" is the technical boundary:

* **NEC Article 670 Responsibility:** * Sizing the supply branch circuit conductors (125% of largest motor + sum of others).
* Ensuring the supply overcurrent protection is correct.
* Verifying the machine nameplate data.


* **NFPA 79 Responsibility:** * Emergency Stop (E-Stop) performance categories.
* Color coding of internal wiring (e.g., Red for AC control, Blue for DC control).
* Operator interface safety.



## 3. Common inspection items

1. **Nameplate Completeness (670.3):** Inspectors will fail a machine if the nameplate is missing the **Short-Circuit Current Rating (SCCR)** or the full-load current of the largest motor.
2. **Clearance (670.5):** The "Working Space" requirements of **110.26** apply to industrial machinery control panels. Often, machines are installed too close to walls or other equipment, violating the 3-foot clearance rule.
3. **Supply Wire Sizing:** Using conductors that only match the total full-load current without adding the mandatory 25% "headroom" for the largest motor in the system.
4. **Inadequate SCCR:** The machine nameplate shows 5kA SCCR, but the factory floor has 42kA available. This is a "Red Flag" that frequently stops production during commissioning.

## 4. Change log

* 2026-01-15 — Initial draft created; defined the handover points between NEC 670 and NFPA 79.

