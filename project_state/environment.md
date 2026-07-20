# Environment

**Last Updated:** 2026-07-19
**Status:** Active

## Purpose

This file tracks everything required to run, validate, and eventually deploy the project.

If a dependency, version, environment variable, toolchain rule, or deployment target changes, update this file.

## Runtime Baseline

- Python requirement from `pyproject.toml`: `>=3.12`
- Local pinned Python version from `.python-version`: `3.13`
- Project package manager/workflow: `uv` is present and preferred, but direct `python3` usage also works for the current codebase

## Current Project Surface

- `src/cst/` is the installable Python tools package (console script: `cst`)
- `main.py` is a legacy placeholder (superseded by `cst.cli`)
- `docs/` contains the Jekyll static site
- `tools/` contains repo automation and validation scripts (not engineering tools)
- `data/standards_tables/` holds user-supplied licensed table values (gitignored) + committed schemas
- `.github/workflows/pages.yml` deploys the site to GitHub Pages on push to master

## Jekyll Site Requirements

- **Ruby:** 2.6+ (local: system Ruby 2.6.10); CI uses Ruby 3.2 via `ruby/setup-ruby@v1`
- **Bundler:** 2.4.22 (user-installed at `~/.gem/ruby/2.6.0/bin/bundle`)
- **Jekyll:** 4.3.x (in `docs/vendor/bundle/`)
- **Gems:** `jekyll-seo-tag`, `webrick` — see `docs/Gemfile`
- **Local build:** `cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build`
- **CI build:** `bundle exec jekyll build` (Ruby 3.2, standard PATH)

## Required Tools

- `python3`
- `git`
- `bash` or compatible shell for shell scripts
- `ruby` (2.6+ for local Jekyll dev; 3.2 used in CI)

## Recommended Tools

- `uv`

## Dependency Files

- `.python-version`
- `pyproject.toml`
- `uv.lock`

## Current Python Dependencies

- `src/cst/` package: standard library only (by design) — core install has **no runtime dependencies** (`pip show control-system-tools` → `Requires:` empty)
- `pymupdf`, `pypdf`: PDF extractors for `tools/fe_study/` only, now an **optional extra** (`[project.optional-dependencies] fe-study`), no longer core deps. Install with `uv sync --extra fe-study`. The fe_study pipeline degrades gracefully when they are absent (lazy, ImportError-guarded).
- `pycomm3`: optional extra `plc` (live PLC comms helpers)
- Dev group: `pytest` (installed by `uv sync`)
- Packaging: hatchling build backend; `uv sync` installs the project editable with the `cst` console script. The wheel force-includes `data/standards_tables/{samples,schemas}` as `cst/_bundled_tables/` so an installed toolkit finds samples/schemas without a source checkout.

## Environment Variables

- `CST_TABLES_DIR` (optional) — directory holding user-transcribed licensed
  standards-table JSON. Highest-priority location for `cst.common.tables.load_table`;
  lets an installed wheel find licensed data with no source checkout. When unset,
  the loader falls back to the repo `data/standards_tables/` (checkout) then the
  samples/schemas bundled in the package.

## Site Analytics

- Google tag (`gtag.js`) installed in `docs/_layouts/default.html`
- Measurement ID: `G-RPL3G47EFZ`
- Applies to all pages using the shared default Jekyll layout

## Validation And Automation Commands

- `uv run python tools/release_check.py --profile full` (governed release/deployment gate)
- `uv run pytest` (297 tests: cst package + repository tools)
- `uv run pytest --doctest-modules src/cst` (calculator doctests)
- `python3 tools/project_automator.py`
- `python3 tools/validate_ai_boundaries.py`
- `python3 tools/fix_ai_boundaries.py`
- `bash tools/validate_reorg.sh all` (legacy migration audit; not a release gate)

## Deployment Target For Phase 1

- GitHub Pages
- personal use
- static output only
- no server-side runtime assumed

## Environment Notes For Future Website Work

- If a frontend framework is added, record its version requirements here.
- If GitHub Actions are added for deployment, record their expectations here.
- If build-time environment variables appear, list them here explicitly.
