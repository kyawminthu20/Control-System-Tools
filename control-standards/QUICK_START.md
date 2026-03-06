# Quick Start Guide

**Last Updated:** 2026-03-05

## Core Structure

```text
control-standards/
├── rag/                    # Authoritative AI-readable knowledge
├── governance/             # Promotion rules and decision logs
├── work/
│   ├── design/             # Read with caution
│   └── general/            # Non-authoritative notes
├── restricted/             # AI-forbidden source material
├── archive/                # Historical content
├── exports/                # Generated output
└── templates/              # Reusable templates
```

## Standards Locations

- NEC: `rag/standards_intelligence/us/nec/`
- NFPA 79: `rag/standards_intelligence/us/nfpa79/`
- UL 508A: `rag/standards_intelligence/us/ul_508a/`
- IEC 60204-1: `rag/standards_intelligence/international/machinery/iec_60204_1/`
- Functional safety: `rag/standards_intelligence/international/functional_safety/`
- Cross-standard notes: `rag/standards_intelligence/crosswalks/`

## Typical Workflows

### Look Up a Standard

```bash
cd control-standards/rag/standards_intelligence/us/nfpa79
cat NFPA_OVERVIEW.md
cat NFPA79_2024__Ch08__grounding_and_bonding.md
```

### Start a Design

```bash
cd control-standards/work/design
```

Use `work/design/` for active design material, then promote verified patterns into `rag/design_framework/`.

### Handle Copyrighted Material

```bash
cd control-standards/restricted/legacy_drafts
```

Keep purchased standards, vendor documents, and raw notes in `restricted/`. Do not promote verbatim text into `rag/`.

## Useful Commands

```bash
python3 tools/validate_ai_boundaries.py
python3 tools/project_automator.py
bash tools/validate_reorg.sh all
```

## First References

- `rag/standards_intelligence/_index.yaml`
- `rag/standards_intelligence/_standards_map.md`
- `governance/promotion_checklist_drafts_to_rag.md`
- `work/design/README.md`
