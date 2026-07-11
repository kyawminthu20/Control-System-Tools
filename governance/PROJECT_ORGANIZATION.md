# Project Organization

**Authoritative.** Any person or AI agent working in this repository follows
this document. Entry points [AGENTS.md](../AGENTS.md) and
[CLAUDE.md](../CLAUDE.md) require it. Last restructure: Phase 31–36
(2026-07-11).

## The Two Tracks

This repository is one repo with two products that share a knowledge base:

1. **The site** — *Control Systems Engineering Field Guide*
   (`docs/`, Jekyll, GitHub Pages) — presentation layer only.
2. **The toolkit** — the `cst` Python package (`src/cst/`) — standards-cited
   engineering calculators and generators.

Both draw on the **reference library** (`control-standards/rag/`), which is
the single authoritative knowledge source. Information flows one way:

```
control-standards/rag/  ──►  docs/ (site pages, rag-files mirror)
                        ──►  src/cst/ (methods, not table values)
```

The site and the toolkit NEVER write into `control-standards/rag/`.
Corpus changes go through the promotion workflow in
[control-standards/governance/](../control-standards/governance/).

## Directory Roles

| Path | Role | Trust level for AI |
|---|---|---|
| `control-standards/rag/` | Authoritative reference library (clause-level source notes) | Canonical — prefer for standards questions |
| `control-standards/governance/` | Corpus promotion checklist, decision log, change policy | Canonical policy |
| `control-standards/work/` | Work-in-progress notes | Non-authoritative; never cite as fact |
| `control-standards/archive/` | Timestamped historical snapshots | Context only |
| `control-standards/restricted/` | Quarantined licensed/private material | **AI-forbidden**; never read, never track in git |
| `docs/` | The Jekyll site (source root; `_config.yml` lives here) | Presentation only |
| `docs/assets/rag-files/` | Generated mirror of the corpus (by `tools/generate_rag_tree.py`) | Generated — never edit directly |
| `docs/assets/templates/` | Downloadable engineering templates | See ENGINEERING_STANDARDS.md |
| `src/cst/` | The Python toolkit (installable package) | See ENGINEERING_STANDARDS.md |
| `tests/` | pytest suite for `src/cst/` and `tools/fe_study/` | Must pass before merge |
| `data/standards_tables/` | Licensed table values (user-supplied, gitignored) + committed schemas/samples | Never commit values |
| `data/examples/` | Committed worked-example inputs (e.g. the example I/O list) | Committed |
| `tools/` | Repo automation and validation scripts ONLY — no engineering calculations | Utility |
| `project_state/` | Operational tracking (phase, change log, environment, runbook) | Must be updated with every meaningful change |
| `planning/` | Planning artifacts, saved external reviews | Context; loose personal material stays out of git |
| `governance/` | THIS directory — repo-wide standards | Canonical policy |

## Site Information Architecture (Phase 31)

One taxonomy; the top nav and the sidebar (`docs/_data/navigation.yml`) must
always tell the same story. Current top-level sections:

**Home · Fundamentals · Standards · Design · Lifecycle · Communications ·
Industries · Tools** (About lives under Tools at `/about/`).

Where new content belongs:

| New content | Home |
|---|---|
| A standard's detail page | `docs/standards/<family>/<standard>/` |
| Training / fundamentals module | `docs/fundamentals/<topic-group>/` |
| Lifecycle stage material | `docs/lifecycle/` (stages) or `docs/lifecycle/guides/` |
| Network/protocol page | `docs/communications/` (see CONTENT_STANDARDS.md templates) |
| Industry overlay | `docs/industries/<industry>/` |
| Worked scenario | `docs/tools/scenarios/` |
| Downloadable template | `docs/assets/templates/` + listed on `/tools/templates/` |
| Calculator / generator | `src/cst/` — **documented on the site, never ported to JS** |
| Vendor/directory data | `docs/_data/manufacturers/*.yml` (data-driven pages) |

Never create a new top-level section without an explicit owner decision; the
taxonomy is deliberately small.

## Naming and URL Conventions

- Page slugs: kebab-case, lowercase (`rs485-physical-layer`)
- Every page is `dir/index.md` (no bare `foo.md` pages)
- **Moving a page requires `redirect_from`** with every old URL, and old
  section indexes become `redirect_to` stubs. Check for self-redirects
  (including the `/<page>/index.html` form) — they overwrite the real page.
- All internal links use `{{ '/path/' | relative_url }}` — never absolute
  URLs, never hardcoded `baseurl`.
- Data files: `docs/_data/*.yml` snake_case.

## Related Documents

- [CONTENT_STANDARDS.md](CONTENT_STANDARDS.md) — how to write site content
- [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md) — code, data, templates
- [AI_WORKFLOW.md](AI_WORKFLOW.md) — how agents must operate here
- [control-standards/governance/](../control-standards/governance/) — corpus promotion
