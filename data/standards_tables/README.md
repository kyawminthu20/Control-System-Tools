# Licensed Standards Table Data

Calculators in `src/cst/` that depend on **table values from copyrighted
standards** (NEC ampacity Table 310.16, motor full-load current Tables
430.248/430.250, OCPD percentages Table 430.52, UL 508A SB4.1 SCCR defaults,
etc.) load those values at runtime from JSON files in this directory.

**The values are never committed.** `.gitignore` excludes `*.json`/`*.yaml`
here (schemas and clearly-marked samples are allowed). This keeps the
calculation code open and shareable while table content stays within your
standard license — the same boundary the RAG corpus follows
(`control-standards/governance/promotion_checklist_drafts_to_rag.md`).

## Populating a table

1. Find the schema in `schemas/` (e.g. `schemas/ampacity.schema.json`).
2. Create `<table_name>.json` in this directory, transcribing values from
   **your licensed copy** of the standard.
3. Every file must carry a `source` block (standard, edition, table number)
   — the loader (`cst.common.tables.load_table`) rejects files without it,
   and calculators echo it into their citations.

## File layout

```
data/standards_tables/
├── README.md            (committed)
├── schemas/             (committed — JSON Schema per table)
├── samples/             (committed — structure examples with FAKE values)
└── *.json               (NOT committed — your transcribed licensed values)
```
