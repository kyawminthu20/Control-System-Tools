# Control Standards Structure Summary

**Last Updated:** 2026-03-05

## Product Layout

```text
control-standards/
├── rag/
│   ├── standards_intelligence/
│   │   ├── us/
│   │   ├── international/
│   │   └── crosswalks/
│   ├── design_framework/
│   ├── troubleshooting_engine/
│   ├── commissioning_checklists/
│   └── training_modules/
├── governance/
├── work/
│   ├── design/
│   └── general/
├── restricted/
│   ├── legacy_drafts/
│   └── do_not_read/
├── archive/
├── exports/
├── templates/
└── tools/
```

## Current Reality

- `rag/standards_intelligence/` contains the real content signal.
- `rag/design_framework/`, `rag/commissioning_checklists/`, and `rag/training_modules/` are mostly structure.
- `rag/troubleshooting_engine/` currently contains only its top-level index file.
- `work/` and `restricted/` are non-authoritative.

## Standards Grouping

- `us/`: NEC, NFPA 79, UL 508A
- `international/machinery/`: IEC 60204-1
- `international/functional_safety/`: ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511
- `crosswalks/`: overlap matrices and detailed comparison notes
