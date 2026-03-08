# Standards Decision Workflow Enhancements Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement all 8 recommendations from `control-standards/work/design/decision_workflow.md` into the live site page.

**Architecture:** Single-file content update to `docs/crosswalks/standards-decision-workflow/index.md`. No new files, no layout changes, no config changes. All additions are Markdown + Mermaid compatible with the existing Jekyll site.

**Tech Stack:** Jekyll 4.2, Mermaid.js (CDN, neutral theme), vanilla HTML/CSS via existing layout.

---

### Task 1: Add front-matter metadata (edition refs + last reviewed)

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md` (front matter, lines 1–17)

**Step 1: Add `last_reviewed` and `standards_editions` to front matter**

Replace the existing front matter block with:

```yaml
---
layout: default
title: "Standards Decision Workflow"
description: "Which standards apply to your project? Decision tree routing by machine type, market, and safety requirements."
last_reviewed: "2026-03-08"
standards_editions:
  - "NEC 2023"
  - "NFPA 79 2024"
  - "UL 508A 2022"
  - "IEC 60204-1 2018"
  - "ISO 12100 2010"
  - "ISO 13849-1 2023"
breadcrumb:
  - name: "Crosswalks"
    url: "/crosswalks/"
  - name: "Decision Workflow"
repo_path: "control-standards/rag/standards_intelligence/routing/standards_applicability.md"
related_standards:
  - name: "US Electrical Standards"
    url: "/standards/us-electrical/"
  - name: "International Machinery"
    url: "/standards/machinery/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
---
```

**Step 2: Verify Jekyll still builds**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```
Expected: `done in X seconds` with no errors.

**Step 3: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add last_reviewed and standards editions to front matter"
```

---

### Task 2: Add purpose statement section

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Insert purpose statement block immediately after the `<div class="page-header">` closing `</div>` tag**

```markdown
## Purpose

This workflow helps engineers determine **which standards apply at each stage of industrial machine design and installation** in the United States.

**Intended for:**
- Control engineers
- Machine builders
- Panel designers
- System integrators

**Standards covered:**

| Standard | Role |
|----------|------|
| ISO 12100 | Risk assessment methodology |
| ISO 13849-1 / IEC 62061 | Functional safety architecture |
| NFPA 79 | Machine electrical design |
| UL 508A | Control panel construction |
| NEC | Electrical installation in buildings |

> **Scope note:** This workflow covers US-market industrial machines. EU/CE requirements add IEC 60204-1 and the Machinery Directive. Process safety systems follow IEC 61511 instead of ISO 13849.

---
```

**Step 2: Build and verify**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```

**Step 3: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add purpose statement with audience and scope"
```

---

### Task 3: Add lifecycle Mermaid diagram

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Add lifecycle diagram section after the existing Quick Decision Tree section and before Step 1**

The existing diagram is a branching router (machine vs process). This adds the complementary **sequential lifecycle view**.

```markdown
## Lifecycle Workflow

The diagram below shows the **sequence** standards apply across a machine's design and installation lifecycle.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Machine Concept] --> B[Risk Assessment<br/>ISO 12100]
    B --> C[Safety Function Requirements]
    C --> D{Safety framework?}
    D -->|PL route| E[ISO 13849-1]
    D -->|SIL route| F[IEC 62061]
    E --> G[Machine Electrical Design<br/>NFPA 79]
    F --> G
    G --> H[Control Panel Construction<br/>UL 508A]
    H --> I[Electrical Installation<br/>NEC]
    I --> J[Inspection & Approval<br/>AHJ]
</pre>
</div>

---
```

**Step 2: Build and check Mermaid renders**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```

Open `docs/_site/crosswalks/standards-decision-workflow/index.html` and confirm the `<pre class="mermaid">` block is present.

**Step 3: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add sequential lifecycle Mermaid diagram"
```

---

### Task 4: Add decision questions to Steps 1–3

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Prepend a "Key question" block to Step 1 (Identify Your Market)**

Before the existing Step 1 table, add:

```markdown
**Key question:** What markets will this machine be sold or installed in?

**Outputs:**
- Required standard set
- Whether CE marking applies
```

**Step 2: Prepend a "Key question" block to Step 2 (Identify Machine/System Type)**

```markdown
**Key question:** What is the machine or system doing, and what is its risk context?

**Outputs:**
- Core applicable standards
- Whether functional safety standards apply
```

**Step 3: Prepend a "Key question" block to Step 3 (Identify Safety Requirements)**

```markdown
**Key question:** Does this system perform safety functions, and in what environment?

**Outputs:**
- Additional standards required
- Safety integrity target (PL or SIL)
```

**Step 4: Build and verify**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```

**Step 5: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add decision questions and outputs to steps 1-3"
```

---

### Task 5: Add NFPA 79 / NEC / UL 508A boundary clarification

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Add boundary clarification section after Step 3 and before Step 4**

```markdown
## Standard Scope Boundaries

Many engineers confuse these three overlapping standards. The table below clarifies where each one applies.

| Standard | Governs | Applies To |
|----------|---------|------------|
| **NFPA 79** | Electrical design of the machine itself | Machine wiring, enclosures, control devices |
| **UL 508A** | Construction of industrial control panels | Panel shop fabrication, listing |
| **NEC** | Electrical installation in buildings | Facility wiring from the panel to the machine |

> **Key boundary:** NFPA 79 stops at the machine connection point. NEC governs everything from the building supply to that point. UL 508A governs how the panel is built, not where it connects.

---
```

**Step 2: Build and verify**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```

**Step 3: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add NFPA 79 / NEC / UL 508A boundary clarification table"
```

---

### Task 6: Add Common Engineering Mistakes section

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Add after the Standard Scope Boundaries section**

```markdown
## Common Engineering Mistakes

1. **Designing safety circuits before risk assessment** — the required Performance Level (PLr) comes from ISO 12100 risk assessment; skipping this step produces safety circuits with no verified integrity basis.
2. **Assuming NEC defines machine electrical design** — NEC governs facility installation; NFPA 79 governs the machine. Using NEC rules inside a machine is a compliance error.
3. **Ignoring SCCR when selecting components** — Short Circuit Current Rating must be coordinated across all panel components. Mismatches cause failures at listing.
4. **Installing panels without verifying available fault current** — UL 508A SCCR must meet or exceed the available fault current at the installation point (NEC 110.10).
5. **Mixing NFPA 79 and UL 508A requirements incorrectly** — NFPA 79 governs machine-mounted enclosures; UL 508A governs separately mounted control panels. Requirements differ.
6. **Skipping AHJ coordination** — The Authority Having Jurisdiction has final approval authority. Engage early on non-standard installations.

---
```

**Step 2: Build and verify**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```

**Step 3: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add common engineering mistakes section"
```

---

### Task 7: Add Typical Compliance Stack summary

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Add after Common Engineering Mistakes**

```markdown
## Typical Machine Compliance Stack

For a standard US industrial machine with safety functions, the full compliance stack is:

| Layer | Standard | Edition |
|-------|----------|---------|
| Risk assessment | ISO 12100 | 2010 |
| Functional safety architecture | ISO 13849-1 or IEC 62061 | 2023 / 2021 |
| Machine electrical design | NFPA 79 | 2024 |
| Control panel construction | UL 508A | 2022 |
| Facility electrical installation | NEC | 2023 |
| Final inspection | AHJ jurisdiction | — |

> For EU/CE markets, add **IEC 60204-1 (2018)** alongside NFPA 79 and design to the more restrictive requirement at each point.

---
```

**Step 2: Build and verify**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -5
```

**Step 3: Commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add typical machine compliance stack table with editions"
```

---

### Task 8: Add practical example (conveyor system)

**Files:**
- Modify: `docs/crosswalks/standards-decision-workflow/index.md`

**Step 1: Add after Typical Compliance Stack and before the Routing Source note**

```markdown
## Worked Example — Automated Conveyor System

The following traces a US-market conveyor through the full workflow.

**System:** Belt conveyor with automated loading, pinch points at drive and tail sections, maintenance access door.

| Step | Action | Standard Applied |
|------|--------|-----------------|
| 1 | US market, no CE marking required | NEC + NFPA 79 + UL 508A |
| 2 | Industrial machinery with guarding | NFPA 79 + NEC Art. 670 + UL 508A |
| 3 | Risk assessment identifies pinch hazard at access door | ISO 12100 |
| 4 | Safety function required: guard door interlock (Category 3, PLd) | ISO 13849-1 |
| 5 | Machine wiring designed to NFPA 79 | NFPA 79 2024 |
| 6 | Control panel built and listed to UL 508A | UL 508A 2022 |
| 7 | Machine installed per NEC, SCCR verified against available fault current | NEC 2023 |
| 8 | AHJ inspection completed, permit issued | AHJ |

**Key decisions made:**
- ISO 13849-1 chosen over IEC 62061 (single machine, PL route simpler)
- PLd required (ISO 12100 risk graph: severe injury possible, frequent access, avoidance difficult)
- Category 3 dual-channel interlock with cross-monitoring

---
```

**Step 2: Build and verify full site**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -10
```
Expected: clean build, page count ≥ 48.

**Step 3: Final commit**

```bash
git add docs/crosswalks/standards-decision-workflow/index.md
git commit -m "feat(workflow): add conveyor worked example tracing all 8 standards"
```

---

## Verification

After all tasks complete:

```bash
cd docs && bundle exec jekyll build 2>&1 | grep -E "done|error|warn"
```

Check `docs/_site/crosswalks/standards-decision-workflow/index.html` contains:
- `Purpose` section
- Two `<pre class="mermaid">` blocks
- `Common Engineering Mistakes`
- `Typical Machine Compliance Stack`
- `Worked Example`

Update `project_state/change_log.md` with the enhancement entry.
