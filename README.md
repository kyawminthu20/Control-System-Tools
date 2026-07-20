# Control System Tools Workspace

This repository combines two related concerns:

- an industrial automation standards intelligence knowledge base, published as a
  static site (the **Control Systems Engineering Field Guide**, live on GitHub Pages)
- a Python engineering tools suite (the **`cst` package**) built on top of that
  knowledge: standards-cited calculators, motion utilities, and (planned)
  panel-design and commissioning generators

The authoritative engineering content lives in `control-standards/rag/`. The active project-tracking workflow lives in `project_state/`.

## Scope and Intent

**This is defensive industrial-automation engineering.** The purpose of every
part of this repository is to help control systems comply with published safety
standards and stay bounded by established science. Nothing here is offensive,
and nothing here is research into creating hazards.

Some domain vocabulary in this repository reads as sensitive out of context.
It is not:

| Term you will see | What it actually means here |
|---|---|
| "chemical" / "chem" | Process-industry **control**: chemical plants, bulk chemical distribution in semiconductor fabs, pH neutralization in water treatment. Thermodynamics and transport phenomena as **governing equations a controller must respect**. Never synthesis routes, never hazardous-agent production. |
| "biological" / "bio" | **Bioprocess** control: bioreactors, activated-sludge wastewater treatment, microbial growth kinetics (Monod, ADM1) as process models. Never pathogens, never biological agents. |
| "hazardous" / "explosive atmospheres" | IEC 60079 / NEC Article 500 area classification — how to **prevent** ignition in a plant. Prevention engineering. |
| "safety" / "SIL" / "functional safety" | IEC 61508 / 61511 / ISO 13849 — designing systems that **fail safe** and protect people from machinery. |
| "security" / IEC 62443 | Compliance and **defensive** network segmentation posture for ICS. No exploits, no attack tooling, no offensive techniques. |
| "adversarial pass" | An internal **review technique** — argue against your own conclusion to test it. Refute-by-default epistemics, not adversarial attacks on systems. |

### The governing constraint

The repository's central engineering position is a **restriction**, not a
capability. Established scientific law is the ceiling, and learned models sit
underneath it:

- **Hard layer — the laws.** Conservation of mass, momentum, and energy;
  chemical equilibrium by Gibbs-energy minimization; documented growth
  kinetics. Deterministic. **Holds the veto.**
- **Soft layer — fitted closures and ML.** Soft sensors, correlations,
  supervisory optimization. Capped at **advisory authority**, and **zero
  authority over any safety function.**

Research phases in `control-standards/work/research/` exist to *enforce* this
ceiling. Phase 49c, for example, ran an adversarial review that attempted to
justify giving machine-learning models more control authority in chemical and
bioprocess plants — and **refuted every such attempt**, pushing safety-function
participation to zero. The output of that work is a tighter limit on what AI is
permitted to do, not a wider one.

### Sourcing

Claims are traceable to published standards bodies and peer-reviewed literature
(IEC, ISO, NFPA, UL, NEC, NIST, IUPAC), each carrying a verification tag
recording whether it was confirmed at the publisher. Licensed table values are
never committed. Speculative or unestablished science is out of scope by
policy — see [`governance/ENGINEERING_STANDARDS.md`](governance/ENGINEERING_STANDARDS.md).

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
| `panel/` | I/O list model + validation → BOM (spares/densities) → wire/terminal schedule → legend & panel nameplates | ✅ |
| `commissioning/` | per-point loop test sheets (5-pt analog checks), FAT/SAT protocol skeleton | ✅ |
| `plc/` | tag DB w/ IEC 61131-3 identifier rules, tags-from-I/O generator, Modbus register maps, pycomm3 read/verify helpers (`--extra plc`) | ✅ |
| `diagnostics/` | SBM-style anomaly detection (stdlib, kernel autoassociative), Saleae Logic 2 post-processing (pulse stats, glitches, quadrature decode) | ✅ |
| `docgen/` | design-package assembler — stitches I/O summary, BOM, wire schedule, nameplate, and cited calc results into one markdown document | ✅ |

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
