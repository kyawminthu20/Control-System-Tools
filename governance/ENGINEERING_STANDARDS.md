# Engineering Standards — Code, Data, Templates

**Authoritative.** Rules for the `cst` package, data files, and the
downloadable templates.

## 1. The `cst` Package (`src/cst/`)

**Design principles (all three are load-bearing):**

1. **Every result carries its citations.** Calculators return a `CalcResult`
   (see `cst/common/cite.py`) holding the value, unit, standard/clause
   citations, assumptions, and warnings. A calculation without provenance
   does not ship.
2. **Licensed table values are never distributed.** Rule *logic* (formulas,
   well-known multipliers with clause citations) lives in code; bulk table
   values (NEC 310.16, 430.250, Bussmann C-values, UL SB4.1 defaults) load
   at runtime from `data/standards_tables/*.json` via
   `cst.common.tables.load_table`. Clearly-marked SAMPLE files under
   `samples/` let everything run; results computed from samples carry a
   SAMPLE warning; `allow_sample=False` is the design-use mode.
3. **One I/O list drives everything.** Panel and commissioning generators
   consume the canonical I/O-list CSV (`cst/panel/io_list.py`) so outputs
   stay mutually consistent.

**Code rules:**

- Python ≥3.12; the core package is **stdlib-only**. Optional integrations
  are dependency extras (e.g. `plc = ["pycomm3"]`) behind guarded imports
  with actionable error messages.
- Type hints on all signatures; docstrings state the standard/formula a
  module implements; explicit `ValueError`s with the offending values.
- Never invent standard values. If not certain of a number, it becomes
  user-supplied data with a schema, not a constant. Constants that ARE
  embedded (e.g. 430.52 percentages) carry the clause citation in code.
- Live-PLC helpers read and verify only — never wrap writes to a running
  controller.
- Every new module ships with golden-value tests in `tests/cst/`.
  `uv run pytest` must be green before merge. Doctested examples must be
  arithmetically verified (compute the expected value, don't guess it).
- CLI: one `cst` entry point, one subcommand per tool, argparse, exit 2 on
  `ValueError` with a clean message.

## 2. Data Files

- `data/standards_tables/*.json` — **gitignored.** User transcribes from
  licensed copies. Committed: `schemas/` (JSON Schema per table) and
  `samples/` (few rows, marked "verify against a licensed copy"). Every
  table file must carry a `source` provenance block or the loader rejects it.
- `docs/_data/*.yml` — site data (navigation, manufacturers, lifecycle
  stages). Data-driven pages loop over these; extend the data file, not the
  page. Directory data (manufacturers) is extracted from vetted sources —
  never invent vendors, families, or regions.
- `data/examples/` — committed, fictional, and small.

## 3. Downloadable Templates (`docs/assets/templates/`)

Two origins, both listed on `/tools/templates/` with their origin labeled:

- **Generated** — produced by `tools/generate_site_templates.py` from the
  example I/O list. Never hand-edit generated files; change the generator or
  the example input and re-run. Regeneration is documented in
  `project_state/how_to.md`.
- **Original** — hand-authored skeletons (design basis, SRS, MOC form, …).
  Requirements: original content only, no standards values, an
  adapt-before-use note in the file (HTML comment for md, header row
  conventions for CSV), and generic example rows using invented tags.

Every template page entry states origin and format. New template ⇒ file +
table row on `/tools/templates/` + (if generated) generator update.

## 4. Repo Automation (`tools/`)

- `tools/` holds repo/site automation only — engineering calculations belong
  in `src/cst/`.
- Paths derive from `__file__`, never hardcoded absolute paths.
- Scripts that write committed artifacts (STRUCTURE_SUMMARY, rag mirror,
  site templates) must be re-runnable and idempotent.
- `tools/project_automator.py` IGNORE_DIRS must exclude private/quarantine
  trees (`restricted`, `drafts_DO_NOT_READ`, `archive`) — the generated
  summary is public.

## 5. Verification Matrix (run what the change touches)

| Change | Required checks |
|---|---|
| `src/cst/` or `tests/` | `uv run pytest` (all green) + doctests |
| `docs/` content | Jekyll build + `check_internal_links.py` (zero broken) |
| Corpus (`control-standards/rag/`) | promotion checklist + `validate_ai_boundaries.py` + `generate_rag_tree.py` re-run |
| Templates | regenerate via script; verify listing page |
| Any meaningful change | `project_state/` updates (see AI_WORKFLOW.md) |
