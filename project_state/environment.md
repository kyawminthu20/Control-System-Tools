# Environment

**Last Updated:** 2026-03-09
**Status:** Active

## Purpose

This file tracks everything required to run, validate, and eventually deploy the project.

If a dependency, version, environment variable, toolchain rule, or deployment target changes, update this file.

## Runtime Baseline

- Python requirement from `pyproject.toml`: `>=3.12`
- Local pinned Python version from `.python-version`: `3.13`
- Project package manager/workflow: `uv` is present and preferred, but direct `python3` usage also works for the current codebase

## Current Project Surface

- `main.py` is the current placeholder entry point (not the site)
- `docs/` contains the Phase 1 Jekyll static site
- `tools/` contains the main local automation and validation scripts
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

- none declared beyond the standard library

## Environment Variables

- none required currently

## Site Analytics

- Google tag (`gtag.js`) installed in `docs/_layouts/default.html`
- Measurement ID: `G-RPL3G47EFZ`
- Applies to all pages using the shared default Jekyll layout

## Validation And Automation Commands

- `python3 tools/project_automator.py`
- `python3 tools/validate_ai_boundaries.py`
- `python3 tools/fix_ai_boundaries.py`
- `bash tools/validate_reorg.sh all`

## Deployment Target For Phase 1

- GitHub Pages
- personal use
- static output only
- no server-side runtime assumed

## Environment Notes For Future Website Work

- If a frontend framework is added, record its version requirements here.
- If GitHub Actions are added for deployment, record their expectations here.
- If build-time environment variables appear, list them here explicitly.
