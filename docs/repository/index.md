---
layout: default
title: "Repository and Project Info"
description: "GitHub repository link, build stack, contribution notes, and project metadata for the Control System Standards Atlas."
breadcrumb:
  - name: "Repository"
---

<div class="page-header">
  <span class="page-header__label">Repository</span>
  <h1>Repository and Project Info</h1>
  <p>Links to the source repository, a summary of how the site is built, and project metadata. For scope, trust boundary, and disclaimers see <a href="{{ '/repository/about/' | relative_url }}">About</a>.</p>
</div>

## Links

- **GitHub:** [kyawminthu20/Control-System-Tools](https://github.com/kyawminthu20/Control-System-Tools)
- **About this site:** [/repository/about/]({{ '/repository/about/' | relative_url }}) — purpose, trust boundary, and content limitations
- **Glossary:** [/tools/glossary/]({{ '/tools/glossary/' | relative_url }}) — terms and acronyms
- **RAG file browser:** [/tools/rag-browser/]({{ '/tools/rag-browser/' | relative_url }}) — canonical corpus explorer

## How This Site is Built

- **Site generator:** [Jekyll](https://jekyllrb.com/) 4.x, built and deployed via GitHub Pages
- **Authoritative content:** RAG corpus under `control-standards/rag/` — the presentation layer (`docs/`) never modifies authoritative standards content
- **Diagrams:** [Mermaid](https://mermaid-js.github.io/) (via CDN, neutral theme) and [Cytoscape.js](https://js.cytoscape.org/) 3.28.1 for the standards relationship graph
- **Redirects:** `jekyll-redirect-from` plugin — old URLs from prior navigation restructures continue to resolve
- **Internal link checker:** `tools/check_internal_links.py` runs against the built `_site/` tree before every release

## Content Source of Truth

| Topic | Source of truth |
|---|---|
| Authoritative standards content | `control-standards/rag/` |
| Current phase, status, backlog | `project_state/project_state.md` |
| Dated project-level changes | `project_state/change_log.md` |
| Runtime, tooling, deployment | `project_state/environment.md` |
| Setup, run, validation, deploy steps | `project_state/how_to.md` |
| Jekyll site source | `docs/` |

## Contributing

This is a personal-use knowledge base. There is no public contribution workflow. Site edits are made directly against `master`, with a [Phase 26 plan](https://github.com/kyawminthu20/Control-System-Tools/blob/master/docs/superpowers/plans/2026-04-14-phase26-nav-restructure.md) tracking the ongoing navigation restructure.
