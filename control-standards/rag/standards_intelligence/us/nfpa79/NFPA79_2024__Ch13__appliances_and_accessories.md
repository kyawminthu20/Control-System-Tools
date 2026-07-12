<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "13"
  chapter_title: "Appliances and Accessories"

INDEX_TAGS:
  topics: ["appliances", "auxiliary_devices"]
-->


## 0. Scope

This chapter applies to electrical appliances and accessories that are either part of the machine or are connected to it. This includes items like **work lights, cooling units (AC/Fans), heating elements, and power outlets** for maintenance tools.

The primary goal is to ensure these accessories are:

* Properly grounded and protected.
* Rated for the industrial environment of the machine.
* Logically integrated so they don't interfere with the machine’s primary safety functions.

## 1. Typical Control-System Use Cases

In modern industrial machinery, several specific accessories fall under these rules:

* **Machine Lighting:** Local lighting (task lighting) must be protected from physical damage (e.g., using tempered glass or poly shields) and must be switched such that it doesn't create a strobe effect with moving parts.
* **Enclosure Cooling (Air Conditioners/Heat Exchangers):** These are considered "appliances." They must be wired so that if they fail or trip their breaker, the control system receives a "high temp" alarm to initiate a controlled stop before electronics are damaged.
* **Maintenance Receptacles:** If the machine includes a 120V outlet for a laptop or tool, it **must be GFCI protected** and should ideally be fed from a separate circuit so that a tool fault doesn't trip the machine's main control power.
* **Soldering Irons/Glue Pots:** Integrated heating accessories must have clear "Power On" indicators and over-temperature protection to prevent fire hazards during machine downtime.

## 2. Change Log

* 2026-01-15 — Initial draft created.
* 2026-01-16 — Expanded use cases to include enclosure cooling and maintenance receptacle requirements for the 2024 edition.
