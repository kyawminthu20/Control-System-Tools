<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_ROADMAP
-->

# Build Sequence

## Objective

Build the semiconductor facility library in a way that produces usable reference value early instead of collecting random files.

## Prompt rules

When a future session works one phase from this roadmap, the prompt should always specify:

- the exact phase and topic boundary
- the target folder and expected deliverables
- the source boundary: public-safe only for planning, no protected text
- the required separation between system, control, instrumentation, and standards content
- the validation or review step before closeout
- the intended promotion target if the work stabilizes

## Phase 1

### Goal

Establish the governance, source-control, and routing foundation so later semiconductor-facility content can be added without ambiguity about trust level, source handling, or topic ownership.

### Suggested execution prompt

```text
Complete Phase 1 of the semiconductor facility library.
Work only in `planning/semi_facility/`.
Tighten the governance, source register, manual catalog, system map, and standards-routing files so later phases can build on a clean public-safe foundation.
Do not create authoritative `control-standards/rag/` content yet unless a stable promotion target is explicitly requested.
Keep source handling explicit, preserve AI boundary rules, and end with: updated files, remaining gaps, and the next recommended phase step.
```

- lock the public-content rules
- keep a source register
- keep a manual catalog
- define the facility systems map
- define the standards and code gap map

## Phase 2

### Goal

Build usable system-level coverage for the core fab utility domains so the library can answer facility-architecture questions system by system instead of as scattered notes.

### Suggested execution prompt

```text
Complete Phase 2 for one semiconductor facility system family.
Normalize the topic into a clean system note under `planning/semi_facility/systems/` using only public-safe and local-derived sources.
Keep the topic boundary explicit and separate: system architecture, control objectives, instrumentation implications, standards anchors, and likely reference outputs.
Update the source register if new public sources are introduced.
End with: what was normalized, what is still weak, and which design-framework file this could later promote into.
```

- normalize bulk specialty gas references
- normalize bulk chemical and wet-process references
- normalize water and wastewater references
- normalize exhaust, abatement, and vacuum references
- normalize HVAC and cleanroom references

## Phase 3

### Goal

Turn the system notes into reusable engineering guidance by adding instrumentation logic, control architecture, shutdown structure, and repeatable interlock or alarm patterns.

### Suggested execution prompt

```text
Complete Phase 3 for the semiconductor facility library.
Use the existing system notes as the base and build reusable guidance under `planning/semi_facility/instrumentation/` and related control or safety notes.
Add device-family logic, shutdown hierarchy, alarm philosophy, permissive/interlock/trip patterns, and links back to specific system notes.
Do not overstate SIL, PL, or standards claims where the local corpus is incomplete.
End with: reusable patterns created, affected systems, and unresolved verification gaps.
```

- build the instrumentation library by device family
- add common control architectures and shutdown hierarchies
- add alarm, permissive, interlock, and trip patterns
- connect system notes to specific manual notes

## Phase 4

### Goal

Make the library operationally useful for execution and field work by adding commissioning guidance, interface definitions, crosswalks, and visual packages that help readers move from reference to application.

### Suggested execution prompt

```text
Complete Phase 4 for the semiconductor facility library.
Focus on execution-facing outputs: commissioning guidance, tool-facility interfaces, crosswalks, and visual packages that are usable on the GitHub Pages site.
Prefer concise field-usable tables, sequence narratives, and Mermaid diagrams that match the existing site pattern.
Cross-link the new material to the system, control, and standards pages it depends on.
End with: deliverables created, where they fit on the site, and what still needs testing or verification.
```

- add commissioning, startup, and maintenance references
- add tool and facility interface notes
- add crosswalks between systems, instruments, and standards families
- add scenario-specific tool visual packages for workflow, permissives, trips, and access interlocks, starting with [Semiconductor Fab Tool Visual Aid Reference](../semiconductor_fab_tool_visual_aids.md)

## Chemical-specific overlay

### Goal

Insert the missing media-driven engineering layer that connects chemical behavior to materials, controls, interlocks, shutdown ownership, and failure modes across Phases 2 through 4.

### Suggested execution prompt

```text
Execute the chemical-specific overlay for the semiconductor facility library.
Build the missing media-driven layer that links chemical behavior to material compatibility, instrumentation fit, permissives, interlocks, trips, shutdown ownership, and failure modes.
Start with the pilot topics already prioritized in the roadmap: HF and the hazardous gas cabinet package.
Keep all content public-safe, condition-dependent, and explicit about `TO VERIFY` gaps.
End with: completed pilot assets, reusable templates or matrices created, and promotion targets in `control-standards/rag/design_framework/semiconductor_facility/`.
```

The April 13 chemical-specific expansion cuts across Phases 2 through 4.

Use [Chemical-Specific Buildout Plan](chemical_specific_buildout_plan.md) for:

- HF-first pilot sequencing
- gas-cabinet companion package
- chemical class pages
- control-oriented compatibility and interaction matrices
- promotion gates back into the authoritative semiconductor-facility design framework

## Definition of done for one topic

- topic boundary is clear
- source links are recorded
- protected text is not copied
- system, control, and instrumentation concerns are separated clearly
- promotion target is named
