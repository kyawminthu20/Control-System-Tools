# How To

**Last Updated:** 2026-03-06
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

## Run The Current Project

Current app entry point:

```bash
python3 main.py
```

Or with `uv`:

```bash
uv run python main.py
```

Current expected behavior:

- prints a placeholder message

## Refresh Project Automation

Update the generated structure summary:

```bash
python3 tools/project_automator.py
```

## Validate Repository State

Validate AI-readable content boundaries:

```bash
python3 tools/validate_ai_boundaries.py
```

Fix common AI-boundary issues:

```bash
python3 tools/fix_ai_boundaries.py
```

Validate the repository reorganization state:

```bash
bash tools/validate_reorg.sh all
```

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
