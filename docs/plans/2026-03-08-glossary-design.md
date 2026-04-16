# Glossary Page — Design Document

**Date:** 2026-03-08
**Status:** Approved
**Phase:** Reference expansion

---

## Purpose

Add a cross-linked glossary encyclopedia at `/tools/glossary/` covering all key acronyms and terms a control or machine safety engineer will encounter when using this site (SIL, PL, SL, NEC, NFPA, SCCR, AHJ, HFT, SFF, MTTFd, DC, Category, PLC, SIS, LOPA, and more).

---

## Placement

URL: `/tools/glossary/`

Sidebar: added to the existing **Reference** section as a third entry between Software Stack and About.

```
Reference
  Software Stack
  Glossary          ← new
  About / Trust Boundary
```

Follows the same pattern as `/design/software-stack/` and `/repository/about/` — top-level URL, linked under the Reference sidebar section. No new section or subdirectory required.

---

## Data Architecture

Terms stored in `docs/_data/glossary.yml`. One YAML block per term. The glossary page renders entries via Liquid — adding a term requires only a new YAML block, no template editing.

### Entry schema

```yaml
- term: Safety Integrity Level
  acronym: SIL
  domain: safety                    # safety | electrical | standards-bodies | regulatory
  definition: >
    A discrete level (SIL 1–4) specifying the required risk reduction that a safety
    function must achieve. Defined in IEC 61508 and used in IEC 62061 for machinery
    and IEC 61511 for process safety. Higher SIL levels require greater reliability
    and stricter architectural constraints.
  standard_pages:
    - url: /standards/functional-safety/iec-62061/
      label: IEC 62061
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
    - slug: risk-assessment
      label: Risk Assessment
  related_terms:
    - PL
    - SL
    - HFT
    - SFF
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `term` | string | Full term name |
| `acronym` | string | Acronym or short form (used as anchor and sort key) |
| `domain` | string | One of: `safety`, `electrical`, `standards-bodies`, `regulatory` |
| `definition` | string | 3–5 sentence definition |
| `standard_pages` | list | Links to relevant standard pages on this site |
| `lifecycle_stages` | list | Lifecycle stages where the term is most relevant |
| `related_terms` | list | Acronyms of related glossary entries (for See also links) |

---

## Page Structure

**File:** `docs/tools/glossary/index.md`
**Layout:** `default`

```
[A–Z anchor strip]
  A · B · C · D · ... (letter skipped if no entries start with it)

[Term blocks, sorted alphabetically by acronym]

  ## AHJ                          ← h2 with id="ahj" for anchor links
  Authority Having Jurisdiction
  [domain badge]
  Definition text (3–5 sentences)

  Standard:  NEC  NFPA 79         ← relative_url links to standard pages
  Lifecycle: Installation          ← relative_url links to lifecycle pages
  See also:  NEC · NFPA · UL 508A ← anchor links within glossary
```

- Sorted alphabetically by `acronym` field
- Domain shown as a badge (not grouped — keeps A-Z navigation simple)
- A-Z strip at the top: each letter is a jump anchor
- Letters with no entries are omitted from the strip
- Each term block is a `<div class="glossary-entry">` for distinct styling
- Anchor IDs are lowercase acronym (e.g., `#sil`, `#pl`, `#sccr`)

---

## Initial Term List (seed)

Minimum viable set for launch:

**Safety**
- SIL — Safety Integrity Level
- PL — Performance Level
- SL — Security Level (IEC 62443)
- HFT — Hardware Fault Tolerance
- SFF — Safe Failure Fraction
- MTTFd — Mean Time To Dangerous Failure
- DC — Diagnostic Coverage
- Category — Safety architecture category (ISO 13849-1)
- PFH — Probability of Dangerous Failure per Hour
- SIS — Safety Instrumented System
- SIF — Safety Instrumented Function
- LOPA — Layer of Protection Analysis
- E-stop — Emergency Stop

**Electrical**
- SCCR — Short-Circuit Current Rating
- AIC — Ampere Interrupting Capacity
- AFC — Available Fault Current
- PLC — Programmable Logic Controller
- SPD — Surge Protective Device
- VFD — Variable Frequency Drive

**Standards Bodies**
- NFPA — National Fire Protection Association
- NEC — National Electrical Code (NFPA 70)
- UL — Underwriters Laboratories
- IEC — International Electrotechnical Commission
- ISO — International Organization for Standardization
- SEMI — Semiconductor Equipment and Materials International

**Regulatory**
- AHJ — Authority Having Jurisdiction
- CE — Conformité Européenne
- OSHA — Occupational Safety and Health Administration

---

## Styling

No new CSS classes required at launch. Reuse existing site patterns:
- `.badge` for domain labels
- Standard `<table>` for metadata rows, or definition-list `<dl>` style
- If distinct card styling is needed, add `.glossary-entry` to `main.css`

---

## Sidebar Change

Add one line to `docs/_includes/sidebar.html` in the Reference section:

```html
<li><a href="{{ '/tools/glossary/' | relative_url }}">Glossary</a></li>
```

---

## Out of Scope

- Search/filter within the glossary (lunr.js already handles site-wide search)
- Separate pages per term
- Automated term extraction from RAG corpus
- External links to standards bodies or purchase pages

---

## Files Changed

| File | Action |
|------|--------|
| `docs/_data/glossary.yml` | Create — term data |
| `docs/tools/glossary/index.md` | Create — rendered page |
| `docs/_includes/sidebar.html` | Edit — add Glossary link to Reference section |
| `docs/assets/css/main.css` | Edit — add `.glossary-entry` styles if needed |
