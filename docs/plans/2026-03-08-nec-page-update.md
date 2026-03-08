# NEC Page Update Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Upgrade the NEC page from a navigation node to a working engineering reference by adding clearer scope boundaries, two missing articles, a machine-builder checklist, and improved metadata.

**Architecture:** All changes are in-place edits to `docs/standards/us-electrical/nec/index.md`. No new files. Content driven by `control-standards/work/design/nec_update.md` spec. Jekyll front-matter extended; page body restructured in Markdown.

**Tech Stack:** Jekyll 4.2, Markdown, YAML front-matter, vanilla site layout (no JS changes required)

---

## Task 1: Update front-matter metadata

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md:1-22`

**Step 1: Open the file and locate the YAML front-matter block (lines 1–22)**

Current front-matter ends at `---` on line 22. The block is missing: last-reviewed date, edition-adoption caveat, primary audience, and companion standards.

**Step 2: Replace the front-matter**

Replace the existing front-matter with:

```yaml
---
layout: default
title: "NEC (NFPA 70) — National Electrical Code"
description: "NEC 2023 — key articles for industrial control panels and machinery: 409, 409.70, 430, 670, 670.6, 250, 725."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "US Electrical"
    url: "/standards/us-electrical/"
  - name: "NEC"
repo_path: "control-standards/rag/standards_intelligence/us/nec/"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design/"
  - name: "Installation"
    slug: "installation/"
last_reviewed: "2026-03-08"
primary_audience: "Panel designers, machine builders, controls engineers, AHJ-facing documentation"
edition_note: "Always verify the edition adopted by the local AHJ. Many jurisdictions are not on the current NEC cycle."
companion_standards:
  - "NFPA 79"
  - "UL 508A"
  - "ISO 12100"
  - "ISO 13849-1"
  - "IEC 60204-1"
---
```

**Step 3: Build site to verify front-matter parses cleanly**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: `done in X seconds` with no YAML errors.

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): extend front-matter with reviewed date, audience, companion standards"
```

---

## Task 2: Update Standard Overview table and add adoption warning

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md` — Standard Overview section

**Step 1: Locate the Standard Overview table (around lines 32–42)**

Current table has 8 rows. Target: tighten the Jurisdiction row and add an adoption warning below the table.

**Step 2: Replace the Standard Overview block**

Replace the current table + Purpose paragraph with:

```markdown
## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | NEC (NFPA 70) |
| **Edition** | 2023 |
| **Publisher** | National Fire Protection Association (NFPA) |
| **Jurisdiction** | United States — adopted by state and local governments, enforced by AHJ |
| **Scope** | Electrical installations in the US |
| **Repository** | `rag/us/nec/` — 10 articles |
| **Status in Corpus** | Complete |
| **Legal status** | Adopted as law in most US jurisdictions; enforced by AHJ |
| **Last reviewed** | 2026-03-08 |
| **Primary audience** | Panel designers, machine builders, controls engineers |

> **Adoption warning:** The NEC is revised every three years. Each state or municipality adopts a specific edition independently. Always verify the edition in force with the local **Authority Having Jurisdiction (AHJ)** before using NEC requirements on a project.

**Purpose:** NEC is the minimum standard for electrical installations. It governs *how electrical systems are installed in a facility*, not how machines are internally designed. NFPA 79 and UL 508A add requirements on top for machine electrical design and panel construction respectively.
```

**Step 3: Build and verify**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build, no errors.

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): tighten overview table, add AHJ adoption warning"
```

---

## Task 3: Add "Use this page for…" and "Not covered here" sections

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md` — insert after the `---` separator following Standard Overview

**Step 1: Locate the separator after the Standard Overview block**

Find the `---` that separates Standard Overview from Key Articles.

**Step 2: Insert two new sections between Standard Overview and Key Articles**

Insert this block:

```markdown
---

## Use this page for

Use NEC requirements when dealing with:

- Feeder sizing and branch circuit protection
- Grounding and bonding of equipment and enclosures
- Disconnecting means requirements
- Conductor sizing and insulation ratings
- Installation rules for wiring methods and raceways
- Industrial control panel installation (Article 409)
- Motor circuit protection (Article 430)

## Not covered here

NEC does **not** by itself determine:

- Machine risk assessment
- Safety Integrity Level (SIL) or Performance Level (PL) target
- Safety controller architecture or category
- Emergency stop design category (stop category 0/1/2)
- Guarding strategy or safeguarding method

These areas are governed by other standards. See [NFPA 79]({{ '/standards/us-electrical/nfpa-79/' | relative_url }}), [ISO 13849-1]({{ '/standards/functional-safety/iso-13849/' | relative_url }}), and [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}).
```

**Step 3: Build and verify**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build.

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): add scope boundary sections (use for / not covered here)"
```

---

## Task 4: Add Articles 409.70 and 670.6 to Key Articles table

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md` — Key Articles table

**Step 1: Locate the Key Articles table**

Currently lists: 250, 310, 409, 430, 440, 670, 725.

**Step 2: Replace the Key Articles table**

Replace with:

```markdown
## Key Articles for Industrial Control Systems

| Article | Topic | Relevance |
|---------|-------|-----------|
| **250** | Grounding and bonding | Foundation for all electrical installations |
| **300** | Wiring methods | Installation rules for cables, conduits, and raceways |
| **310** | Conductors for general wiring | Conductor sizing and insulation ratings |
| **409** | Industrial control panels | Panel installation; SCCR marking required (409.110) |
| **409.70** | Surge protection — control panels | Surge protective devices for industrial control panel circuits (NEC 2023) |
| **430** | Motors, motor circuits, and controllers | Motor branch circuit protection, overload, disconnects |
| **440** | Air-conditioning equipment | HVAC-related motor control |
| **670** | Industrial machinery | Machine installation; supply circuit requirements |
| **670.6** | Overvoltage protection — machinery | Overvoltage protection requirements for industrial machinery (NEC 2023) |
| **725** | Class 1, 2, 3 remote-control circuits | Control and signaling circuit wiring methods |
```

**Step 3: Build and verify**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build.

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): add articles 409.70 (surge) and 670.6 (overvoltage) to key articles table"
```

---

## Task 5: Tighten Article 409 section and soften Article 670 statement

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md` — Article 409 and Article 670 sections

**Step 1: Replace the Article 409 section**

Current text says "requires UL listing or field evaluation" — replace the whole section:

```markdown
## Article 409 — Industrial Control Panels

NEC Article 409 governs industrial control panels installed in facilities.

Key requirements:

- Panels must be **properly marked**
- **Short-Circuit Current Rating (SCCR)** must be determined and displayed on the panel (409.110)
- The panel must be **installed within its marked SCCR**
- **Surge protection** requirements for panel circuits (409.70 — NEC 2023)

The NEC does not mandate a single method for determining SCCR. However, **UL 508A Supplement SB** is a widely used approved method for calculating SCCR. A panel does not need to be UL 508A *listed* to comply with Article 409 — it must use an *approved method* to establish SCCR.

Typical required panel markings include:

- Nominal voltage and phase
- Frequency
- SCCR
- Panel identification
```

**Step 2: Replace the Article 670 section**

Current wording says "Article 670 makes NFPA 79 the *effective* electrical design standard" — soften and expand:

```markdown
## Article 670 — Industrial Machinery

Article 670 covers industrial machines as installed equipment in a facility.

Key requirements:

- Machine **disconnecting means**
- **Supply circuit** sizing and protection
- **Overcurrent protection** at point of supply
- **Overvoltage protection** where required (670.6 — NEC 2023)

For many detailed electrical design aspects of machines, Article 670 points engineers toward **NFPA 79**, which provides requirements for machine control circuits, emergency stops, safety circuits, and machine wiring practices.

In practice:

- **NEC governs installation of the machine in the facility**
- **NFPA 79 governs the electrical design of the machine itself**
```

**Step 3: Build and verify**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build.

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): tighten 409 UL 508A statement, soften 670 NFPA 79 relationship, add 409.70/670.6 detail"
```

---

## Task 6: Add machine-builder compliance checklist

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md` — insert before the Relationship section

**Step 1: Locate the Relationship to Other Standards section**

This is the last major section before the closing link.

**Step 2: Insert checklist section before Relationship**

```markdown
---

## Practical Compliance Checklist

Before installing a machine or panel in a facility, verify the following:

- [ ] Determine available fault current at the installation point
- [ ] Establish control panel **SCCR** and verify it meets available fault current
- [ ] Verify feeder and branch-circuit **conductor sizing**
- [ ] Verify motor branch **short-circuit and ground-fault protection** (430.52)
- [ ] Verify motor **overload protection** (430.32)
- [ ] Verify machine **disconnecting means** location and rating (670 / 430.102)
- [ ] Verify **grounding and bonding** (250)
- [ ] Verify **surge and overvoltage protection** where safety circuits are involved (409.70 / 670.6)
- [ ] Verify applicable **NEC edition** adopted by local AHJ
```

**Step 3: Build and verify**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build.

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): add machine-builder compliance checklist"
```

---

## Task 7: Improve Relationship to Other Standards section

**Files:**
- Modify: `docs/standards/us-electrical/nec/index.md` — Relationship section

**Step 1: Replace the existing ASCII diagram + relationship section**

Current section is a short ASCII block. Replace with a full table + cleaner prose:

```markdown
---

## Relationship to Other Standards

NEC is the *installation* code. Other standards govern machine design, panel construction, and safety.

| Standard | Scope | Relationship to NEC |
|----------|-------|---------------------|
| **NEC (NFPA 70)** | Electrical installation code | Enforced by AHJ; baseline for all others |
| **NFPA 79** | Electrical design of industrial machinery | Article 670 points to NFPA 79 for machine electrical design |
| **UL 508A** | Industrial control panel construction | Supplement SB commonly used for SCCR determination under Art. 409 |
| **ISO 12100** | Machine risk assessment | Upstream of all electrical/safety standards |
| **ISO 13849-1** | Safety control system Performance Levels | Governs safety circuit design; NEC does not address PL |
| **IEC 60204-1** | Electrical equipment of machinery (international) | International counterpart to NFPA 79 |

> **Summary:** NEC governs *how electrical systems are installed*. NFPA 79 governs *how machines are electrically designed*. UL 508A governs *how control panels are constructed*. ISO/IEC standards govern *machine safety and risk reduction*.
```

**Step 2: Build and verify**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build.

**Step 3: Verify the page renders correctly**

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll serve --detach 2>&1 | tail -3
# Open http://localhost:4000/Control-System-Tools/standards/us-electrical/nec/
# Confirm: table renders, checklist renders, no broken links
# Stop server
kill $(lsof -ti:4000) 2>/dev/null
```

**Step 4: Commit**

```bash
git add docs/standards/us-electrical/nec/index.md
git commit -m "feat(nec): replace ASCII diagram with full standards relationship table and summary"
```

---

## Task 8: Update project_state tracking

**Files:**
- Modify: `project_state/change_log.md`
- Modify: `project_state/project_state.md`

**Step 1: Append to change_log.md**

Add entry:

```markdown
## 2026-03-08 — NEC page upgraded to engineering reference

- Added "Use this page for / Not covered here" scope boundary sections
- Added Articles 409.70 (surge protection) and 670.6 (overvoltage protection) to key articles table
- Tightened Article 409 UL 508A statement (approved method, not mandatory listing)
- Softened Article 670 NFPA 79 statement (removed "effective standard" absolute phrasing)
- Added machine-builder compliance checklist (8 items with article references)
- Replaced ASCII relationship diagram with full standards comparison table
- Extended front-matter: last_reviewed, primary_audience, edition_note, companion_standards
- Added AHJ adoption warning in overview
```

**Step 2: Update project_state.md current implementation state**

Update the NEC page status from "navigation node" to "engineering reference".

**Step 3: Commit**

```bash
git add project_state/change_log.md project_state/project_state.md
git commit -m "chore: update project_state for NEC page upgrade"
```

---

## Validation

After all tasks, run:

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | grep -E "error|warn|done"
```

Expected: `done in X seconds` — no errors or warnings.

Spot-check the built page:

```bash
grep -c "409.70\|670.6\|checklist\|AHJ\|Not covered" docs/_site/standards/us-electrical/nec/index.html
```

Expected: count ≥ 5 (all new sections present in built output).
