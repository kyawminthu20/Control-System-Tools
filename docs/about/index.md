---
layout: default
title: "About — Trust Boundary and Disclaimer"
description: "About the Control System Standards Atlas: purpose, trust boundary, and content limitations."
breadcrumb:
  - name: "About"
---

<div class="page-header">
  <span class="page-header__label">About This Site</span>
  <h1>Control System Standards Atlas — About</h1>
</div>

## Purpose

This site is a **personal-use engineering reference** for industrial automation standards. It is a navigation aid and paraphrase layer — not a reproduction of standards text and not a legal document.

**What it is:**
- A directory of industrial automation standards and their relationships
- A routing guide for selecting applicable standards based on project type and market
- A navigation aid pointing to the authoritative RAG corpus in `control-standards/rag/`
- A paraphrase of key concepts to aid understanding

**What it is not:**
- A reproduction of licensed standards text
- A substitute for the purchased, published editions of standards
- A compliance checklist or legal interpretation
- A substitute for professional engineering judgment

---

## Content Source and Governance

All content is derived from the local RAG corpus at `control-standards/rag/standards_intelligence/`.

The RAG corpus is:
- Built from paraphrase and synthesis of published standards
- A personal reference, not a licensed reproduction
- Subject to revision and may not reflect the current published edition

**Content separation principle:**
- `control-standards/rag/` — authoritative corpus (source of truth)
- `docs/` — presentation layer (this site) — reads from RAG, never modifies it

---

## Content Status Badges

This site uses the following badges to indicate content reliability:

| Badge | Meaning |
|-------|---------|
| <span class="badge badge--local">LOCAL</span> | Content is confirmed in the local corpus |
| <span class="badge badge--verify">TO VERIFY</span> | Coverage is planned or limited — verify against published standard |
| <span class="badge badge--gap">NOT IN CORPUS</span> | Standard or topic not covered in local repository |
| <span class="badge badge--inferred">INFERRED</span> | Content is inferred from related material, not directly sourced |

---

## Known Gaps

| Standard / Topic | Status |
|-----------------|--------|
| ISO 13849-1 detail pages | Planned — TO VERIFY |
| IEC 62061 detail pages | Planned — TO VERIFY |
| IEC 61508 detail pages | Planned — TO VERIFY |
| IEC 61511 detail pages | Planned — limited coverage |
| SEMI S2, S8, S14 | Not in corpus |
| IEC 60079 family (hazardous area) | Not confirmed in corpus |
| IEC 62443 detail pages | Routing reference only |
| IEC 60601 (medical) | Not in corpus |
| NERC CIP (energy grid) | Not in corpus |
| Marine class rules | Not in corpus |

---

## Trust Boundary

This site is hosted on GitHub Pages as a static site. It is intended for personal use by a single engineer as a reference and navigation tool.

**Do not use this site for:**
- Compliance determinations
- Safety-critical design decisions without independent verification
- Legal or regulatory interpretation
- Customer-facing compliance claims

Always verify against the current published edition of the relevant standard. Standards are revised periodically — the editions referenced in this corpus may not be the current edition at the time of your project.
