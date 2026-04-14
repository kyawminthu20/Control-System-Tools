<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_LIBRARY_PLAN
-->

# Semiconductor Facility Reference Library Draft

## What this folder is

This folder is a staging area for a public-source semiconductor facility engineering library.

The goal is to centralize facility systems, controls, instrumentation, safety, and tool-interface references so they can be found in one place and later promoted into `control-standards/rag/`.

## Core rules

- Public-safe only: public documents, public manuals, public datasheets, public university or government material, and original paraphrased notes.
- No protected IP: no NDA drawings, no customer packages, no licensed standards text, and no large verbatim copies of copyrighted manuals.
- Draft status: content here is working material until it is cleaned, cited, and promoted.

## Start here

1. Read [Public Content Rules](governance/public_content_rules.md).
2. Use [Facility Reference Taxonomy](taxonomy/facility_reference_taxonomy.md) to decide where new content belongs.
3. Register every new source in [Public Source Register](sources/public_source_register.md).
4. Summarize manuals through [Manual Catalog](manuals/manual_catalog.md) and [Instrument Manual Note Template](manuals/instrument_manual_note_template.md).
5. Build reusable device knowledge under [Instrumentation](instrumentation/README.md).
6. Normalize stable knowledge under [Systems](systems/README.md).
7. Keep rough captures in [Drafts](drafts/README.md).

## Folder layout

- `governance/`: public-content and IP handling rules.
- `taxonomy/`: system map and document taxonomy.
- `standards/`: candidate standards and code families to catalog.
- `systems/`: normalized system-level engineering notes.
- `chemicals/`: chemical-specific hazards, compatibility, interlocks, shutdown behavior, and failure-mode notes.
- `sources/`: public-source register and note templates.
- `manuals/`: catalog and summary notes for instrumentation manuals.
- `instrumentation/`: device families, selection logic, and range or alarm guidance.
- `roadmap/`: build order and gap-closing plan.
- `drafts/`: preserved rough notes that still need normalization.

## High-value detailed notes

- Instrument selection and standards fit: [Instrumentation Use Matrix](instrumentation/semiconductor_facility_instrumentation_use_matrix.md)
- Vendor and product-family comparison: [Manufacturer and Product Family Comparison](instrumentation/manufacturer_product_family_comparison.md)
- Standards explainer with flowcharts: [Standards README](standards/README.md)
- Semiconductor-facility standards landscape: [Standards Landscape](standards/semiconductor_facility_standards_landscape.md)
- Chemical-specific expansion plan: [Chemical-Specific Buildout Plan](roadmap/chemical_specific_buildout_plan.md)

## Local standards anchors already in this repo

- [SEMI S2](../../control-standards/rag/standards_intelligence/international/semiconductor/semi/SEMI_S2__equipment_safety.md)
- [SEMI S8](../../control-standards/rag/standards_intelligence/international/semiconductor/semi/SEMI_S8__ergonomics.md)
- [SEMI S14](../../control-standards/rag/standards_intelligence/international/semiconductor/semi/SEMI_S14__fire_risk_assessment.md)
- [IEC 60204-1](../../control-standards/rag/standards_intelligence/international/machinery/iec_60204_1)
- [ISO 13849-1](../../control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1)
- [IEC 61511](../../control-standards/rag/standards_intelligence/international/functional_safety/iec_61511)
- [NEC 2023](../../control-standards/rag/standards_intelligence/us/nec)
- [NFPA 79](../../control-standards/rag/standards_intelligence/us/nfpa79)
- [UL 508A](../../control-standards/rag/standards_intelligence/us/ul_508a)

## Recommended first build order

- Build the standards and code gap map first.
- Build the facility systems map second.
- Start the manual catalog before adding PDFs or vendor documents.
- Normalize one system at a time: gas, chemicals, water, exhaust, HVAC, controls, safety.
- Promote only after sources and constraints are clearly documented.

## Promotion path

This folder is draft-only. Once a topic is well-sourced, paraphrased, and stable, promote it into the authoritative paths under `control-standards/rag/` with approved metadata.
