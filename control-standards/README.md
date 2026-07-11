# Control Standards Repository

**Version:** 2.0
**Last Updated:** 2026-03-05

This directory is the product root for the industrial automation knowledge base.

## Current Product Structure

- `rag/`: authoritative AI-readable knowledge
- `governance/`: promotion rules, change policies, decision logs
- `work/`: non-authoritative active work
- `restricted/`: AI-forbidden raw, vendor, or copyrighted material
- `archive/`: superseded and historical content
- `exports/`: generated deliverables
- `templates/`: reusable product templates
- `tools/`: product module READMEs and solution areas

## Standards Layout

Authoritative standards content is grouped under `rag/standards_intelligence/`:

- `us/nec/`
- `us/nfpa79/`
- `us/ul_508a/`
- `international/machinery/iec_60204_1/`
- `international/functional_safety/`
- `crosswalks/`

## Working Model

- Start design exploration in `work/design/`.
- Keep loose notes and inbox material in `work/general/`.
- Keep copyrighted standard text and proprietary vendor material in `restricted/`.
- Promote verified paraphrased engineering guidance into `rag/`.
- Use `governance/` before promoting content into `rag/`.

## Priority Content Areas

- Most populated: `rag/standards_intelligence/`
- Mostly scaffolded: `rag/design_framework/`, `rag/commissioning_checklists/`, `rag/training_modules/`
- Nearly empty: `rag/troubleshooting_engine/`

## First Files To Read

- [QUICK_START.md](control-standards/QUICK_START.md)
- [STRUCTURE_SUMMARY.md](control-standards/STRUCTURE_SUMMARY.md)
- [rag/standards_intelligence/_index.yaml](control-standards/rag/standards_intelligence/_index.yaml)
- [rag/standards_intelligence/_standards_map.md](control-standards/rag/standards_intelligence/_standards_map.md)
