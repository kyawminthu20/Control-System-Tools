<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_CHEMICAL_ROADMAP
-->

# Chemical-Specific Buildout Plan

## Objective

Turn [phase_20260413.md](../phase_20260413.md) into an execution sequence that extends the semiconductor-facility library with a chemical-specific engineering layer.

The goal is not to add random chemical notes. The goal is to build a reusable mapping between:

- chemical behavior
- control logic
- interlocks and safe states
- hardware and material selection
- likely failure modes

## Prompt design rules

For this roadmap, a good prompt should always state:

- the exact subphase being executed
- the target file or folder to create or refine
- the existing local notes that must be used as inputs
- the required output structure
- the source discipline and what must remain `TO VERIFY`
- the likely promotion target if the work stabilizes

## Subphase goals at a glance

| Subphase | Goal |
| --- | --- |
| Phase 2A | freeze the information architecture so chemical-specific content has a clear home and document pattern |
| Phase 2B | prove the chemical-page model with one strong HF reference exemplar |
| Phase 2C | prove the gas-side model with one strong gas-cabinet reference exemplar |
| Phase 3A | normalize chemical families by engineering behavior instead of by random chemical lists |
| Phase 3B | extract reusable matrices and logic patterns so pages stop repeating the same tables and shutdown logic |
| Phase 3C | cross-link the chemical layer back into the existing system and instrumentation notes |
| Phase 4A | add visuals and structured engineering outputs that make the pages faster to scan and apply |
| Phase 4B | promote only the stable, well-routed parts into the authoritative design-framework layer |

## Current baseline in this repo

## Already present

- system-level notes for bulk gas, bulk chemicals, UPW, exhaust, HVAC, tool interface, and shutdown architecture
- instrumentation notes for device families, use matrix, selection principles, and alarm strategy
- standards routing for SEMI, NFPA, ISA, ISO 14644, and machinery or process-safety families
- promoted design-framework notes under `control-standards/rag/design_framework/semiconductor_facility/`

## Missing or still weak

- no dedicated chemical-specific folder in the planning set until this phase
- no complete pilot page that ties one chemical to materials, detectors, interlocks, and failure modes
- no control-oriented compatibility matrix
- no facility interaction-risk matrix
- no normalized gas-cabinet package that links state model, exhaust proof, detection, and safe shutdown
- local functional-safety depth is still limited, so detailed SIL or PL claims remain provisional unless separately verified

## Design rules for this buildout

1. Keep the chemical layer separate from broad system architecture.
2. Group by engineering behavior first, not by arbitrary chemical names.
3. Tie every page back to an existing system note, instrumentation note, and standards route.
4. Keep integrity targets provisional where the local corpus is incomplete.
5. Promote only after source traceability and wording discipline are strong enough for `control-standards/rag/`.

## Phase map

This buildout cuts across the existing roadmap:

- Phase 2 work: chemical and gas-system normalization
- Phase 3 work: control philosophy, instrumentation, interlocks, alarm logic
- Phase 4 work: visuals, crosswalks, and promotion-ready reference packages

To avoid losing the thread, use the subphases below.

## Phase 2A: Information Architecture Freeze

### Goal

Define exactly where chemical-specific content lives and what it owns.

### Suggested execution prompt

```text
Complete Phase 2A of the semiconductor facility chemical-specific buildout.
Work in `planning/semi_facility/chemicals/` and related roadmap files only.
Freeze the information architecture: define folder ownership, page families, document templates, and the boundary between `systems/`, `instrumentation/`, and `chemicals/`.
Do not expand into full chemical content yet; focus on structure, routing, and reuse.
End with: created or updated scaffolding, ownership rules, and the next pilot page to build.
```

### Required inputs

- [Bulk Chemical Distribution and Wet Process Systems](../systems/bulk_chemical_distribution_and_wet_process.md)
- [Bulk Specialty Gas Systems](../systems/bulk_specialty_gas_systems.md)
- [Common Control Philosophy](../systems/common_control_philosophy.md)
- [Safety and Shutdown Architecture](../systems/safety_and_shutdown_architecture.md)
- [Semiconductor Facility Standards Landscape](../standards/semiconductor_facility_standards_landscape.md)
- [Instrumentation Use Matrix](../instrumentation/semiconductor_facility_instrumentation_use_matrix.md)

### Actions

- create the top-level `chemicals/` planning folder
- define the page families: pilot, classes, matrices, patterns
- define the minimum section structure for one chemical page
- define what remains system-owned versus chemical-owned
- define promotion targets in the authoritative design-framework path

### Deliverables

- [Chemical-Specific Engineering Layer](../chemicals/README.md)
- [Chemical Control And Safety Template](../chemicals/chemical_control_and_safety_template.md)
- this roadmap file

### Done criteria

- no ambiguity about whether a future note belongs in `systems/`, `instrumentation/`, or `chemicals/`
- every future chemical page has a common template
- the next build queue is explicit

## Phase 2B: HF Pilot Page

### Goal

Build one complete exemplar for a corrosive liquid chemical.

### Suggested execution prompt

```text
Complete Phase 2B of the semiconductor facility chemical-specific buildout by creating or refining the HF pilot page.
Target `planning/semi_facility/chemicals/hf_control_and_safety.md`.
Use the bulk chemical, instrumentation, safety, and standards-routing notes already in the repo.
Cover: scope, hazard profile, compatibility conditions, instrumentation implications, permissives, interlocks, trips, shutdown ownership, failure modes, and facility interaction risks.
Keep all integrity targets provisional unless directly supported locally.
End with: promotion targets, open `TO VERIFY` gaps, and whether the page is strong enough to serve as the template for other chemicals.
```

### Why HF first

- it exposes the missing link between hazard profile, material compatibility, leak response, and instrumentation choice
- it forces the repo to define what "chemical-specific" means in practical terms
- it is the fastest way to prove the template before multiplying pages

### Planned file

- `planning/semi_facility/chemicals/hf_control_and_safety.md`

### Required content blocks

- scope: bulk tank, day tank, transfer skid, point of use, drain, exhaust dependency if applicable
- class: corrosive acid
- material restrictions with condition notes
- detector and instrument implications
- permissives, interlocks, and trips
- shutdown ownership
- leak-response cause and effect
- failure modes caused by chemical attack or vapor exposure
- facility interaction notes and segregation cautions

### Required inputs

- system note for bulk chemicals
- selection principles and device family notes
- standards routes through SEMI liquid-material families and facility code overlays
- public-safe hazard references and material or component family sources

### Evidence gate

The page may explain likely SIF candidates, but it must not claim a final SIL target unless the supporting method and sources are present.

### Done criteria

- the page can be used as a copy-and-adapt model for later chemicals
- unsupported requirements are marked `TO VERIFY`
- the page points to at least one likely promotion target in `control-standards/rag/design_framework/semiconductor_facility/`

## Phase 2C: Hazardous Gas Cabinet Reference Package

### Goal

Build one complete gas-side exemplar that is more control-sequence-heavy than HF.

### Suggested execution prompt

```text
Complete Phase 2C of the semiconductor facility chemical-specific buildout by creating or refining the hazardous gas cabinet reference package.
Target `planning/semi_facility/chemicals/gas_cabinet_control_and_safety.md`.
Use the bulk specialty gas, control philosophy, shutdown architecture, and gas-detection notes already in the repo.
Cover: architecture, states, purge behavior, permissives, interlocks, trips, exhaust-loss response, shutdown ownership, and the visual package needed for the site.
Keep the output vendor-neutral and pattern-oriented rather than tied to a single drawing.
End with: reusable gas-cabinet patterns, visual assets created, and promotion targets.
```

### Planned file

- `planning/semi_facility/chemicals/gas_cabinet_control_and_safety.md`

### Scope

This should be a facility-side gas-cabinet pattern package, not yet a chemically exhaustive gas encyclopedia.

### Required content blocks

- architecture blocks: source, panel or cabinet, purge path, exhaust proof, detection, tool permit
- states: idle, precheck, purge, ready, flow, fault, shutdown, post-purge
- permissives, interlocks, and trips
- exhaust-loss behavior
- gas-detection behavior
- manual-mode discipline
- shutdown ownership between cabinet logic, facility logic, and tool controller
- visual package candidates: architecture, state model, cause and effect, safety layer

### Required inputs

- bulk specialty gas system note
- common control philosophy
- safety and shutdown architecture
- SEMI gas-family routing
- gas-detection manufacturer references already registered

### Done criteria

- the page explains gas-cabinet behavior in reusable patterns rather than one vendor’s drawing
- hazardous interlocks are separated clearly from operator advisories
- it becomes the companion exemplar to the HF page

## Phase 3A: Chemical Class Pages

### Goal

Normalize chemical families by engineering behavior so future pages inherit stable patterns.

### Suggested execution prompt

```text
Complete Phase 3A of the chemical-specific buildout.
Create or refine one or more chemical-class pages under `planning/semi_facility/chemicals/`.
Group chemicals by engineering behavior, not by arbitrary lists, and explain what each class changes in containment, sensing, shutdown behavior, maintenance burden, and material selection.
Cross-link each class page to the system, instrumentation, and standards-routing notes it depends on.
End with: class pages added, inheritance rules for future chemical pages, and remaining gaps that still need chemical-specific overrides.
```

### Planned class files

- `planning/semi_facility/chemicals/corrosive_acids.md`
- `planning/semi_facility/chemicals/toxic_gases.md`
- `planning/semi_facility/chemicals/pyrophoric_gases.md`
- `planning/semi_facility/chemicals/flammable_solvents.md`
- `planning/semi_facility/chemicals/oxidizers.md`
- `planning/semi_facility/chemicals/cryogenic_liquids.md`
- `planning/semi_facility/chemicals/cmp_slurries.md`

### Content each class page must cover

- why the class matters to containment, sensing, and shutdown behavior
- common materials themes
- common instrument technologies and anti-patterns
- common permissive and trip patterns
- common facility interactions
- common maintenance or failure burdens
- boundaries where chemical-specific pages still need to override the class pattern

### Done criteria

- future chemical pages can inherit from a class page instead of re-explaining fundamentals
- cross-links to system, standards, and instrumentation notes are in place

## Phase 3B: Shared Matrices And Pattern Library

### Goal

Pull repeated logic out of one-off chemical pages and make it reusable.

### Suggested execution prompt

```text
Complete Phase 3B of the chemical-specific buildout.
Create reusable shared assets under `planning/semi_facility/chemicals/` such as the compatibility matrix, control logic patterns, SIF mapping, interaction-risk matrix, or instrumentation exposure-failure note.
Make the outputs reusable by later pages and keep all material and integrity claims condition-dependent rather than absolute.
End with: shared files created, which future pages should link to them, and any claims that must stay `TO VERIFY`.
```

### Planned files

- `planning/semi_facility/chemicals/control_oriented_compatibility_matrix.md`
- `planning/semi_facility/chemicals/control_logic_patterns_by_chemical_type.md`
- `planning/semi_facility/chemicals/chemical_system_sif_mapping.md`
- `planning/semi_facility/chemicals/facility_interaction_risk_matrix.md`
- `planning/semi_facility/chemicals/instrumentation_failure_due_to_chemical_exposure.md`

### What each file should own

`control_oriented_compatibility_matrix.md`

- pipe, valve, seal, sensor, and detector implications
- caution that concentration, temperature, purity, and vendor qualification still matter
- links back to class pages instead of pretending to be a full material handbook

`control_logic_patterns_by_chemical_type.md`

- representative permissive sets
- representative interlocks
- representative trip conditions
- state model variations by chemical class

`chemical_system_sif_mapping.md`

- initiating events mapped to sensor, logic owner, and final element
- explicit warning that integrity assignments remain `TO VERIFY` unless formally supported

`facility_interaction_risk_matrix.md`

- incompatible adjacency
- drain-mixing concerns
- shared exhaust dependencies
- segregation or shared-monitoring logic

`instrumentation_failure_due_to_chemical_exposure.md`

- drift, coating, plugging, diaphragm attack, seal failure, detector poisoning, and sensor expiry patterns

### Done criteria

- chemical pages start linking to shared lookup pages instead of copying the same tables everywhere
- unsupported "one material always works" or "one detector always fits" claims are avoided

## Phase 3C: Crosswalk Back Into Existing System Notes

### Goal

Prevent the new chemical layer from drifting away from the system notes that already exist.

### Suggested execution prompt

```text
Complete Phase 3C of the chemical-specific buildout.
Update the existing `systems/`, `instrumentation/`, and control or safety notes so the new chemical-specific pages are visible from the broader semiconductor facility reference flow.
Prefer links, concise cross-references, and clarified boundaries over duplicated prose.
End with: files cross-linked, duplicated content reduced, and any remaining navigation gaps.
```

### Required updates

- add links from `systems/bulk_chemical_distribution_and_wet_process.md` to the new chemical layer
- add links from `systems/bulk_specialty_gas_systems.md` to gas-cabinet pattern content
- add links from `systems/common_control_philosophy.md` to chemical-specific state and interlock patterns
- add links from `systems/safety_and_shutdown_architecture.md` to chemical interaction and shutdown ownership notes
- add links from instrumentation notes to exposure-driven failure pages where relevant

### Done criteria

- the repo has one visible path from system architecture to chemical-specific execution detail
- duplicated paragraphs across folders are reduced instead of multiplied

## Phase 4A: Visual And Reference Package Expansion

### Goal

Add the minimum visuals and structured reference outputs that make the new pages faster to scan and reuse.

### Suggested execution prompt

```text
Complete Phase 4A of the chemical-specific buildout.
Create the visual and structured outputs that make the pilot pages usable on the GitHub Pages site: Mermaid architecture diagrams, state models, cause-and-effect views, shutdown ownership tables, and interlock or trip matrices.
Follow the site’s existing Mermaid wrapper pattern and keep diagrams compact enough to render well on GitHub Pages.
End with: visuals added, where they belong on the site, and any diagrams that should later become SVG instead of Mermaid.
```

### Priority visual package

1. HF architecture
2. HF state or response flow
3. gas cabinet architecture
4. gas cabinet state model
5. cause-and-effect or shutdown ownership diagrams
6. facility interaction map

### Priority structured outputs

- interlock matrix
- trip matrix
- cause-and-effect table
- representative tag naming pattern
- shutdown ownership table

### Done criteria

- at least the two pilot pages have complete visual support
- visuals reinforce the text instead of duplicating it

## Phase 4B: Promotion Readiness And Authoritative Integration

### Goal

Promote only the stable, paraphrased, well-routed parts of this work into the authoritative RAG area.

### Suggested execution prompt

```text
Complete Phase 4B of the chemical-specific buildout.
Review the draft chemical-specific planning assets and promote only the parts that are stable enough for `control-standards/rag/design_framework/semiconductor_facility/`.
Keep wording paraphrased, preserve metadata discipline, and remove or mark unsupported claims before promotion.
End with: promoted files, draft files left behind, and the reasons any content was kept out of the authoritative layer.
```

### Likely promotion targets

- new chemical-specific overview under `control-standards/rag/design_framework/semiconductor_facility/`
- updates to `bulk_chemical_distribution.md`
- updates to `bulk_specialty_gas.md`
- updates to `common_control_philosophy.md`
- updates to `safety_and_shutdown.md`
- possible addition of a compatibility or exposure-failure note if the content becomes stable enough

### Promotion gate

All candidate content should pass these checks first:

- source traceability is recorded
- wording is paraphrased and non-copyrighted
- unsupported standards claims are marked `TO VERIFY` or removed
- planning-only speculation is stripped out
- metadata is converted to authoritative form where appropriate

## Priority queue after this roadmap

1. build the HF pilot page
2. build the hazardous gas cabinet reference package
3. build corrosive-acid and pyrophoric or toxic-gas class pages
4. build the control-oriented compatibility matrix
5. build the instrumentation exposure-failure note
6. cross-link the new chemical layer into system and instrumentation notes

## Source and evidence gaps to manage early

These are the gaps most likely to cause weak content if ignored:

- `NFPA 318` appears in the standards planning notes but does not yet have a local derived note
- detailed functional-safety methods remain incomplete locally, so integrity assignments must stay provisional
- compatibility claims need condition language, not generic "works/does not work" statements
- gas-cabinet patterns need public-safe support from standards routing and manufacturer or detector documentation, not copied drawings

## Definition of success

This buildout is succeeding when the repo can answer all of these without hand-waving:

- what changes in controls when the media changes
- what materials or instruments are immediately suspect for a given chemical class
- what must be a permissive versus an interlock versus a trip
- who owns final shutdown under abnormal conditions
- which claims are supported locally and which still need verification
