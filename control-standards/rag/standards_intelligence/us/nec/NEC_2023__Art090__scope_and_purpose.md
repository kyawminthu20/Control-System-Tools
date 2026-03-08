<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "90"
  article_title: "Introduction — Scope and Purpose"

INDEX_TAGS:
  topics: ["scope", "purpose", "ahj", "adoption", "enforcement"]
  systems: ["all"]
-->

# NEC 2023 — Article 90 — Introduction: Scope and Purpose

## 0. Why this article matters for control engineers

Article 90 defines the legal and jurisdictional framework within which all other NEC articles operate. Understanding its boundaries prevents a common engineering error: applying NEC rules to wiring that is outside its scope (e.g., internal machine wiring governed by NFPA 79) or assuming NEC applies uniformly everywhere (it requires local adoption).

## 1. Purpose and legal status (90.1)

The NEC is a **minimum safety standard**, not a design guide or optimization document. Its purpose is the practical safeguarding of persons and property from hazards arising from the use of electricity. Key points:

- It is a **private standard** published by NFPA, not federal law.
- It becomes legally enforceable only when **adopted by a local AHJ** (city, county, state). Most US jurisdictions adopt a version of the NEC, but editions vary — some jurisdictions use NEC 2017 or 2020 rather than 2023.
- Compliance with NEC does not guarantee a system is efficient, convenient, or adequate for good service. Meeting NEC minimums is the floor, not the ceiling.

## 2. Scope — what NEC covers (90.2(a))

NEC applies to **premises wiring** — electrical conductors, equipment, and raceways installed in or on buildings, structures, or other premises. This includes:

- Industrial facilities, commercial buildings, and residences
- Yards, parking lots, and carnivals
- Mobile homes, recreational vehicles, and floating buildings
- Electric vehicle charging infrastructure

For control engineers: NEC governs the **facility wiring that supplies power to machines** — service entrance, feeders, branch circuits, and the point of connection to the machine.

## 3. What NEC does NOT cover (90.2(b))

The following are explicitly outside NEC scope:

| Excluded Area | Governing Authority |
|---------------|-------------------|
| Utility supply lines (transmission, distribution) | NESC (ANSI C2) |
| Internal wiring of listed factory-assembled equipment | Equipment listing standard (e.g., UL 508A) |
| Wiring in mines | MSHA regulations |
| Ships, watercraft, railway rolling stock | ABYC / FRA standards |
| Internal wiring of industrial machines | NFPA 79 (not NEC) |

**Critical boundary for machine builders:** NFPA 79 governs the electrical equipment on or inside the machine itself. NEC governs the supply wiring from the facility up to the machine's supply terminal (the point of connection defined in Article 670). The machine's main disconnect and supply conductors straddle this boundary.

## 4. AHJ authority (90.4)

The Authority Having Jurisdiction (AHJ) has the final word on:

- Approving equipment, materials, and installations
- Granting special permission for alternative methods
- Requiring safety measures beyond NEC minimums

**Practical implication:** Even if your installation strictly follows NEC, an AHJ can require additional measures. Engage the local AHJ early on non-standard installations, large projects, and anything involving unusual equipment or occupancies.

## 5. Enforcement and inspection

- AHJs typically issue permits before work begins and conduct inspections before energization.
- Non-compliant installations result in failed inspections, required corrections, and delay.
- Listed equipment (UL, ETL, CSA, etc.) is presumed compliant with NEC construction requirements; the AHJ verifies installation compliance.

## 6. Change log

- 2026-03-08 — Initial draft created; established NEC/NFPA 79 scope boundary.
