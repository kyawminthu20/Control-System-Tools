# How To

**Last Updated:** 2026-07-17
**Status:** Active

## Purpose

This file is the operational runbook for the project.

Use it to track how to:

- set up the local environment
- run the current project
- refresh project automation
- validate repository state
- deploy or prepare the GitHub Pages phase when that exists

## Initial Setup

1. Install Python `3.13` or another compatible Python version `>=3.12`.
2. Install `uv` if you want to use the preferred workflow.
3. Clone the repository.
4. From the repository root, sync the environment if needed:

```bash
uv sync
```

If `uv` is not available, use the local Python environment directly for the current project state.

## Run The Tools Suite (cst)

`uv sync` installs the `cst` package (editable) with its console script. Examples:

```bash
uv run cst voltage-drop --amps 20 --feet 100 --awg 12 --volts 120
uv run cst wire-size --amps 32 --feet 250 --volts 480 --phases 3
uv run cst encoder --ppr 1024 --gear 5 --lead 10 --rpm 3000
uv run cst enclosure --watts 350 --height 1.6 --width 0.8 --depth 0.5
uv run cst fan --watts 400 --max-temp 45
```

Or import it: `from cst.calc.voltage_drop import voltage_drop`. Every result
is a `CalcResult` with `.report()` for cited plain-text output.

Calculators that need licensed table values (NEC 310.16, 430.250, ...) read
them from `data/standards_tables/*.json` — populate from your licensed copies
per `data/standards_tables/README.md`. Values are gitignored.

## Regenerate Site Templates

After changing the cst generators or `data/examples/io_list_example.csv`:

```bash
uv run python tools/generate_site_templates.py
```

Writes the generated example templates to `docs/assets/templates/` (served
at `/tools/templates/` on the site).

## Run Tests

```bash
uv run pytest
```

The normal suite currently contains 300 tests. Calculator doctests are a
separate governed check (10 doctests):

```bash
uv run pytest --doctest-modules src/cst
```

## Refresh Project Automation

Update the generated structure summary:

```bash
python3 tools/project_automator.py
```

## Validate Repository State

Run the complete read-only release gate:

```bash
uv run python tools/release_check.py --profile full
```

Focused profiles are `toolkit`, `corpus`, `site`, and `metadata`. The full
profile runs pytest, toolkit doctests, the AI-boundary validator, exact RAG
mirror comparison, metadata non-regression checks, a temporary Jekyll build,
and the rendered-link checker. CI runs the same profile before deployment.

Validate AI-readable content boundaries:

```bash
python3 tools/validate_ai_boundaries.py
```

Fix common AI-boundary issues:

```bash
python3 tools/fix_ai_boundaries.py
```

Audit the historical repository reorganization state when specifically needed:

```bash
bash tools/validate_reorg.sh all
```

This is a legacy migration audit, not the release gate; several checks target
superseded artifacts and it invokes `project_automator.py`.

## Update Project Tracking

After meaningful code, documentation, architecture, workflow, or deployment changes:

1. Update `project_state/project_state.md`
2. Update `project_state/change_log.md`
3. Update `project_state/environment.md` if requirements changed
4. Update `project_state/how_to.md` if setup or run steps changed

The pre-commit hook stages `project_state/change_log.md`, but it does not replace manual project-log updates.

## Jekyll Site (GitHub Pages)

The site lives under `docs/`. Jekyll is installed in `docs/vendor/bundle/` using Ruby 2.6 / Bundler 2.4.22.

### Build

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Output: `docs/_site/`

### Serve locally

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve
```

Preview at `http://localhost:4000/Control-System-Tools/`

### Deploy to GitHub Pages

```bash
git push
```

Then in repo Settings → Pages → Source: **GitHub Actions** (workflow at `.github/workflows/pages.yml`).

Live URL: `https://kyawminthu20.github.io/Control-System-Tools/`

### Notes

- CI uses Ruby 3.2 via `ruby/setup-ruby@v1`
- `baseurl: "/Control-System-Tools"` is set in `docs/_config.yml`
- `docs/_site/`, `docs/vendor/`, `docs/.jekyll-cache/` are gitignored

---

## Adding New RAG Files

RAG files live in `control-standards/rag/`. After adding or editing files there, run these steps to make them visible in the RAG file browser on the site.

### 1. Add your `.md` file(s)

Place the file anywhere under `control-standards/rag/`, maintaining the existing folder structure.

```
control-standards/rag/
  standards_intelligence/us/nec/        ← US standards
  standards_intelligence/international/ ← International standards
  training_modules/                     ← Training content
  design_framework/                     ← Design guides and workflows
  commissioning_checklists/             ← Checklists
  meta/                                 ← Status and admin files
```

### 2. Regenerate the tree and static assets

From the **repo root**:

```bash
python3 tools/generate_rag_tree.py
```

This does two things:
- Copies all `.md` files from `control-standards/rag/` into `docs/assets/rag-files/` (served by GitHub Pages)
- Rewrites `docs/_data/rag_tree.json` (the file tree baked into the browser page)

### 3. Build locally to verify (optional)

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Check that your file appears in `docs/_site/assets/rag-files/` and that `docs/_site/rag-browser/index.html` contains a button for it.

### 4. Stage, commit, and push

```bash
git add control-standards/rag/<your-file>.md \
        docs/_data/rag_tree.json \
        docs/assets/rag-files/

git commit -m "feat(rag): add <description>"
git push
```

GitHub Actions will rebuild the site. Once deployed, the file appears in the RAG browser at:
`https://kyawminthu20.github.io/Control-System-Tools/rag-browser/`

### Notes

- `docs/assets/rag-files/` is a generated mirror of `control-standards/rag/` — never edit files there directly; always edit in `control-standards/rag/` and re-run the generator.
- `README.md` files inside `control-standards/rag/` are intentionally skipped by the generator.
- Files with spaces in their names are supported but prefer underscores for consistency.
