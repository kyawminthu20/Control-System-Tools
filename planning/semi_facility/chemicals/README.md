<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_CHEMICAL_LAYER
-->

# Chemical-Specific Engineering Layer

## Purpose

This folder holds the chemical-specific layer that sits between broad facility-system architecture and detailed instrument or standards notes.

Its job is to organize semiconductor-facility knowledge by:

- chemical behavior
- control implications
- interlocks and safe states
- material compatibility
- instrumentation failure modes
- facility interaction risks

This is the missing layer identified in [phase_20260413.md](../phase_20260413.md).

## Why this is separate from `systems/`

The `systems/` folder explains facility domains such as bulk chemicals, gas systems, UPW, exhaust, and HVAC.

This folder explains what changes when the media itself changes.

Examples:

- `systems/bulk_chemical_distribution_and_wet_process.md` explains transfer, containment, and leak-response architecture.
- This folder explains why HF, HCl, IPA, NH3, silane, LN2, or CMP slurry change the material choice, detector choice, permissives, trip behavior, and maintenance burden.

## What belongs here

Use this folder for documents that answer questions like:

- What control pattern changes for corrosive acids versus pyrophoric gases?
- What materials are acceptable for a given chemical family and under what caution?
- What failure modes appear because of chemical attack, coating, plugging, or vapor exposure?
- Which interlocks are local sequence protection versus facility shutdown candidates?
- Which chemical interactions require segregation or shared monitoring?

## What does not belong here

Do not duplicate:

- high-level system architecture already covered in `systems/`
- general instrumentation-selection logic already covered in `instrumentation/`
- standards-family routing already covered in `standards/`

Instead, link back to those notes and only add the chemical-specific delta.

## Planned document families

| Document family | Purpose | Typical outputs |
| --- | --- | --- |
| Pilot pages | establish the first complete exemplars | HF page, one hazardous gas cabinet package |
| Chemical classes | group chemicals by behavior and control implications | corrosive acids, toxic gases, pyrophoric gases, flammable solvents, oxidizers, cryogens, CMP slurries |
| Shared matrices | capture reusable lookup content | compatibility matrix, interaction-risk matrix |
| Shared control patterns | avoid repeating the same logic on every page | permissive matrix, interlock matrix, trip patterns, state models |
| Reliability and maintenance notes | capture field failure behavior | sensor drift, plugging, coating, diaphragm attack, seal degradation |

## Working rules for this folder

- Group by engineering behavior first, not by arbitrary chemical lists.
- Record concentration, temperature, and phase when compatibility is discussed.
- Separate operator alarms from interlocks and trips.
- Distinguish facility PLC logic, local skid logic, hardwired safety, and tool-owned shutdown logic.
- Treat SIL or PL claims as provisional unless backed by the local corpus or an explicitly verified external work package.
- Route standards claims through `standards/` instead of embedding unsupported requirements here.

## Minimum structure for one chemical page

Each chemical-specific page should cover:

1. scope and process-use boundary
2. engineering class and hazard profile
3. material compatibility constraints
4. instrumentation and detector implications
5. permissives, interlocks, and trips
6. safe-state and shutdown ownership
7. common failure modes and maintenance concerns
8. facility interaction risks
9. source anchors and open verification gaps

Use [chemical_control_and_safety_template.md](chemical_control_and_safety_template.md) as the default starting point.

## Initial build order

1. HF pilot page
2. one hazardous gas cabinet package
3. class pages for corrosive acids and toxic or pyrophoric gases
4. control-oriented compatibility matrix
5. interaction-risk matrix
6. instrumentation failure-by-exposure note

## Promotion target

Stable, well-sourced notes from this folder should later promote into:

- `control-standards/rag/design_framework/semiconductor_facility/`

Likely promotion targets are:

- a chemical-specific engineering overview
- a control-oriented compatibility note
- gas-cabinet control and safety patterns
- updates to bulk chemical, bulk gas, safety, and control-philosophy pages
