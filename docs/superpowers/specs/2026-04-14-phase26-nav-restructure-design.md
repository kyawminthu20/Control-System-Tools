# Phase 26 Design: Navigation Restructure and Link Audit

**Date:** 2026-04-14
**Status:** Approved
**Phase:** 26

---

## Overview

Restructure the site navigation from the current 5-group file-structure mirror into a 10-group intent-based architecture (following the FE_Study proposal). Physically reorganize page files to match new groups. Install `jekyll-redirect-from` so old URLs continue to work. Build an internal link checker tool and drive broken-link count to zero.

---

## New URL Structure (10 groups)

| New URL root | Source of pages | Notes |
|---|---|---|
| `/fundamentals/` | `/training/fundamentals/` + control theory subset of `/training/control-systems/` | Electrical, control, safety fundamentals |
| `/standards/` | Keep as-is | Already logically grouped |
| `/design/` | `/engineering-workflow/` + architecture pages from `/tools/reference-hub/` | Design & engineering tasks |
| `/implementation/` | `/commissioning-templates/` + `/scenarios/` | Commissioning, startup, scenarios |
| `/verification/` | `/lifecycle/` stage pages + risk assessment pages | Risk assessment, SIL/PL, validation |
| `/industries/` | Keep as-is | Already logically grouped |
| `/troubleshooting/` | **NEW** section | Requires new landing page; pulls from existing troubleshooting module content where present |
| `/training/` | Trimmed — retains structured learning paths; control-systems modules move to `/fundamentals/` where applicable | Structured study/learning paths only |
| `/tools/` | `/tools/rag-browser/` + `/tools/glossary/` + crosswalks + calculator pages | Interactive and reference tools |
| `/repository/` | **NEW** section | GitHub link, contribution notes |

Every moved page gets `redirect_from:` front matter listing the old URL so bookmarks continue to work.

---

## Redirect Mechanism

Enable the `jekyll-redirect-from` plugin:

1. Add to `docs/Gemfile`:
   ```ruby
   gem "jekyll-redirect-from"
   ```
2. Add to `docs/_config.yml` under `plugins:`:
   ```yaml
   plugins:
     - jekyll-redirect-from
     # ...existing plugins
   ```
3. Per moved page, add front matter:
   ```yaml
   redirect_from:
     - /old/path/
     - /old/path/index.html
   ```

Plugin is GitHub Pages-compatible (included in the GitHub Pages whitelist). Jekyll builds a lightweight meta-refresh HTML stub at each old URL.

---

## Broken Link Audit

### Tool: `tools/check_internal_links.py`

Python script that walks the built `_site/` directory and verifies every internal `<a href>` resolves to a real file on disk.

Requirements:
- Python 3.12+ (already required by project)
- No new dependencies — use `html.parser` from stdlib; avoid BeautifulSoup
- Input: path to `_site/` directory
- Output: text report — one line per broken link — `SOURCE_PAGE: BROKEN_TARGET`
- Exit code 0 on zero broken links, 1 otherwise

Internal link definition:
- Starts with `/` — site-root relative
- Or starts with `./` or `../` — relative
- Excludes `#` anchors unless combined with a path
- Excludes external links (`http://`, `https://`, `mailto:`)

### Workflow

1. Build site: `cd docs && bundle exec jekyll build`
2. Run checker: `python3 tools/check_internal_links.py docs/_site/`
3. Fix broken links in source markdown (never in `_site/`)
4. Rebuild and re-check until clean

---

## Build Order

1. **Setup**
   - Add `jekyll-redirect-from` to Gemfile and `_config.yml`
   - Create `tools/check_internal_links.py`
   - Run `bundle install` to pull plugin

2. **Baseline link audit**
   - Run link checker against current site
   - Fix every pre-existing broken link in the CURRENT structure before restructuring
   - This separates "existing broken" from "restructure-caused broken"

3. **Per-group migrations** (one group per commit set, in order):
   1. `/fundamentals/` — fundamentals + control theory modules
   2. `/standards/` — minor reorg inside; no file moves
   3. `/design/` — engineering-workflow + reference architecture pages
   4. `/implementation/` — commissioning-templates + scenarios
   5. `/verification/` — lifecycle stages + risk/compliance pages
   6. `/industries/` — minor reorg inside; no file moves
   7. `/tools/` — rag-browser + glossary + crosswalks + calculators
   8. `/training/` — trim to learning paths only
   9. `/troubleshooting/` — NEW section; create landing page
   10. `/repository/` — NEW section; create landing page

   For each group:
   - Move files to new path
   - Add `redirect_from:` front matter listing every old URL
   - Update all internal cross-links in the moved pages to new paths
   - Rebuild site
   - Run link checker
   - Commit

4. **Navigation rewrite**
   - Rewrite `docs/_data/navigation.yml` into the 10-group structure
   - Each group has its own top-level entry and child list

5. **Final link audit**
   - Run full link checker
   - Fix every remaining broken link
   - Zero broken links required to close Phase 26

6. **Validation and project_state update**
   - Clean Jekyll build (zero errors, zero warnings)
   - AI boundary validator (no regression)
   - Update `project_state/project_state.md` and `project_state/change_log.md`

---

## Scope Summary

- ~160 pages moved with `redirect_from` front matter
- 1 new tool: `tools/check_internal_links.py`
- 2 new landing pages: Troubleshooting, Repository
- Complete rewrite of `docs/_data/navigation.yml`
- All internal cross-links updated to new paths
- `jekyll-redirect-from` added to Gemfile and `_config.yml`

---

## Out of Scope

- Content rewrites for clarity (Phase 27+ handles content quality)
- New content pages (except the 2 required landing pages)
- Site-wide search feature
- URL changes to RAG corpus — RAG stays untouched
- Breadcrumb redesign
- CSS or typography changes

---

## Constraints

- GitHub Pages compatibility — only whitelisted plugins
- Jekyll build must remain clean (0 errors, 0 warnings)
- RAG corpus must not be modified or moved
- No external link checks — internal only
- No new runtime dependencies (Python stdlib only for the link checker)

---

## Success Criteria

- Every page on the new site is reachable via the new 10-group sidebar
- Every old URL still resolves (via `redirect_from` stub)
- `python3 tools/check_internal_links.py docs/_site/` exits 0
- Jekyll build is clean
- `project_state/project_state.md` reflects Phase 26 complete
