# Control System Tools Workspace

This repository combines two related concerns:

- an industrial automation standards intelligence knowledge base, published as a
  static site (the **Standards Atlas**, live on GitHub Pages)
- a Python engineering tools suite (the **`cst` package**) built on top of that
  knowledge: standards-cited calculators, motion utilities, and (planned)
  panel-design and commissioning generators

The authoritative engineering content lives in `control-standards/rag/`. The active project-tracking workflow lives in `project_state/`.

## The `cst` Tools Suite

```bash
uv sync                 # install (editable) with the `cst` console script
uv run pytest           # 65 tests
uv run cst voltage-drop --amps 20 --feet 100 --awg 12 --volts 120
uv run cst wire-size    --amps 32 --feet 250 --volts 480 --phases 3
uv run cst encoder      --ppr 1024 --gear 5 --lead 10 --rpm 3000
uv run cst enclosure    --watts 350 --height 1.6 --width 0.8 --depth 0.5
uv run cst fan          --watts 400 --max-temp 45
```

Package map (`src/cst/`):

| Subpackage | Contents | Status |
|---|---|---|
| `common/` | units (ASTM B258 AWG), `CalcResult` citation framework, licensed-table loader with SAMPLE fallback | ✅ |
| `calc/` | voltage drop + min wire size (NEC K-factor), enclosure thermal (IEC/TR 60890 method) | ✅ |
| `calc/` | ampacity w/ corrections (NEC 310.15), motor branch circuit (Art. 430 chain), transformer OCPD (Table 450.3(B)), panel SCCR (UL 508A SB4), fault current (infinite-bus + point-to-point) | ✅ logic; bulk table values user-supplied |
| `motion/` | encoder scaling: counts ↔ units ↔ RPM ↔ linear speed | ✅ |
| `panel/`, `commissioning/` | I/O list → BOM → wire schedule → nameplates; loop sheets, FAT/SAT | Phase 3 |
| `plc/`, `diagnostics/`, `docgen/` | tag DB / address maps / pycomm3, SBM anomaly detection, design packages | Phase 4 |

Every calculator cites its source standard/formula and lists its assumptions in
the result. **Licensed table values are never committed** — calculators that
need them read `data/standards_tables/*.json`, which you populate from your own
licensed copies (schemas are committed; see `data/standards_tables/README.md`).

## Start Here

- [PROJECT_STARTUP_CONTEXT.md](PROJECT_STARTUP_CONTEXT.md) for repository orientation
- [control-standards/README.md](control-standards/README.md) for the product root
- [project_state/project_state.md](project_state/project_state.md) for the current implementation phase and backlog
- [project_state/environment.md](project_state/environment.md) for runtime and deployment requirements
- [project_state/how_to.md](project_state/how_to.md) for setup and run instructions
- [project_state/change_log.md](project_state/change_log.md) for project-level changes

## Repository Roles

- `src/cst/`: the Python engineering tools suite (importable package + `cst` CLI)
- `control-standards/`: product content, standards knowledge, governance, work areas, and archive
- `docs/`: the Jekyll site (presentation layer over the corpus)
- `project_state/`: active project tracking for state, run requirements, and workflow notes
- `tools/`: local repo automation and validation scripts
- `tests/`: pytest suite for `src/cst/` and `tools/fe_study/`
- `planning/`: reorganization and planning artifacts
- `data/`: local datasets, including user-supplied licensed standards tables (gitignored)

## Important Boundary

The website or application layer is not the authoritative standards source.

Authoritative standards guidance remains in `control-standards/rag/`. Any site or app built in this repository should be treated as a presentation and navigation layer on top of that corpus.
