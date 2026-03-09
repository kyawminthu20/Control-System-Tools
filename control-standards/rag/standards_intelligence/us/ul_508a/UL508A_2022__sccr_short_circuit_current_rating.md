<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 2022

UL_HIERARCHY:
  section: "SB"
  title: "Short-Circuit Current Rating (SCCR)"

INDEX_TAGS:
  topics: ["sccr", "short_circuit_rating"]
  risks: ["equipment_failure", "fire"]
-->

# UL 508A — Supplement SB — SCCR

## 0. Why SCCR exists
SCCR exists so the panel's marked fault withstand capability can be compared to the available fault current at the installation site. Without this comparison, a fault can destroy the panel before the upstream protective device clears it.

## 1. SCCR determination methods
In practice, SCCR is determined by either:

- a tested assembly or tested component combination
- an approved method such as the Supplement SB weakest-link approach and permitted current-limiting combinations

The marked SCCR must be supported by documentation, not just by the rating printed on the largest upstream breaker.

## 2. Weakest-link logic
The most important practical rule is this:

- the panel SCCR is limited by the lowest short-circuit withstand rating in the relevant power circuit unless an approved combination rating allows a higher value

That means a high-interrupting breaker by itself does not make the whole panel high-SCCR. Lower-rated downstream devices such as:

- contactors
- motor starters
- fuse holders
- power distribution blocks
- surge protective devices

can become the limiting component.

Current-limiting fuse classes and listed disconnect/fuse combinations are often used because they can support higher assembly SCCR when applied correctly.

## 3. Typical SCCR pitfalls
Common SCCR errors include:

- equating main breaker interrupting rating with panel SCCR
- forgetting to evaluate downstream power-circuit devices
- relying on vendor marketing language instead of the actual rating basis
- failing to keep a record of the SCCR determination method
- marking a higher SCCR than the weakest permitted component combination can support

## 4. Labeling requirements
The final SCCR must be permanently marked on the completed panel nameplate or equivalent required marking. It should be visible as part of the external identification of the assembly so the installer or inspector can compare it with site available fault current.

## 5. Change log
- 2026-01-15 — Initial draft created
* 2026-03-09 — Added weakest-link and panel-marking guidance from migrated practical panel notes and aligned with NEC 409 concepts.
