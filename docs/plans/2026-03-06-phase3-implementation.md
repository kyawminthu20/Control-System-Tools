# Phase 3 — Functional Safety Deep Coverage Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Upgrade all five functional safety standard pages from shallow stubs to full-depth reference pages, backed by clause-level RAG corpus files.

**Architecture:** Hybrid — create structured RAG corpus `.md` files per clause, then deepen each Jekyll site page to surface that content. Three dependency-ordered groups: ISO 12100 (foundation) → ISO 13849-1 + IEC 62061 (PL/SIL pair) → IEC 61508 + IEC 61511 (parent/process pair). Each group commits independently.

**Tech Stack:** Jekyll 4.2, Markdown, vanilla HTML/CSS. No new plugins or JS. Build: `cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build`.

---

## RAG File Format Reference

Every RAG corpus file MUST start with this HTML comment front matter, then follow the structure below. **Refer to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art409__industrial_control_panels.md` as the canonical format example.**

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: [e.g. ISO, IEC]
STANDARD_ID: [e.g. ISO_13849]
EDITION: [e.g. 2023]

HIERARCHY:
  clause: "[clause number]"
  clause_title: "[clause title]"

INDEX_TAGS:
  topics: ["topic1", "topic2"]
  systems: ["control_system"]
-->

# [Standard] — [Clause] — [Topic]

## 0. Why this clause matters
[2-3 sentences on practical relevance]

## 1. [First major concept]
[Content]

## 2. [Second major concept]
[Content]

## N. Relationship to other standards
[Cross-references]
```

## _index.yaml Format

```yaml
standard_id: [e.g. ISO_12100]
edition: [year]
publisher: [ISO or IEC]
corpus_status: phase3_complete
files:
  - filename: [filename.md]
    clause: "[number]"
    topic: "[topic]"
```

## Site Page Badge Update

Change this in each site page front matter — no front matter change needed. Change the badge line in the page body:

```html
<!-- FROM: -->
<span class="badge badge--verify">PLANNED — TO VERIFY local detail coverage</span>

<!-- TO: -->
<span class="badge badge--complete">Phase 3 Complete</span>
```

The `badge--complete` class already exists in `docs/assets/css/main.css` (green, used on other pages).

## Jekyll Build Validation Command

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected output ends with: `done in X seconds.` — no errors, no warnings.

---

## Group 1: ISO 12100

### Task 1: ISO 12100 RAG corpus — _index.yaml

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/_index.yaml`

**Step 1: Create the file**

```yaml
standard_id: ISO_12100
edition: 2010
publisher: ISO
corpus_status: phase3_complete
scope: Risk assessment and risk reduction for machinery — the foundation Type A standard
files:
  - filename: ISO12100_2010__Clause04__risk_assessment_principles.md
    clause: "4"
    topic: Risk assessment principles and methodology
  - filename: ISO12100_2010__Clause05__risk_estimation.md
    clause: "5"
    topic: Risk estimation — severity, probability, avoidance
  - filename: ISO12100_2010__Clause06__risk_evaluation.md
    clause: "6"
    topic: Risk evaluation — acceptability decision
  - filename: ISO12100_2010__Clause07__risk_reduction.md
    clause: "7"
    topic: Risk reduction — three-step method
  - filename: ISO12100_2010__AnnexA__hazard_list.md
    clause: "Annex A"
    topic: Normative hazard list and examples
```

**Step 2: Verify file exists**

```bash
ls "control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/"
```

Expected: `_index.yaml`

---

### Task 2: ISO 12100 RAG corpus — Clause 4 (Risk Assessment Principles)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/ISO12100_2010__Clause04__risk_assessment_principles.md`

**Step 1: Create the file**

Content must cover:
- Front matter comment block (see RAG File Format Reference above)
- `## 0. Why this clause matters` — ISO 12100 Clause 4 defines the iterative risk assessment process that underpins CE marking and all subsequent safety function design
- `## 1. The iterative process` — describe the three-step loop: identify hazards → estimate risk → evaluate risk → reduce if needed → repeat
- `## 2. Scope of the risk assessment` — machinery lifecycle stages covered (design, construction, transport, installation, use, maintenance, decommissioning)
- `## 3. Documentation requirements` — what must be recorded
- `## 4. Relationship to other standards` — ISO 12100 is Type A; ISO 13849-1 and IEC 62061 are Type C; this clause defines where they plug in

**Step 2: Check front matter is present**

```bash
head -5 "control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/ISO12100_2010__Clause04__risk_assessment_principles.md"
```

Expected: starts with `<!--`

---

### Task 3: ISO 12100 RAG corpus — Clause 5 (Risk Estimation)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/ISO12100_2010__Clause05__risk_estimation.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — risk estimation produces the inputs for PL determination (ISO 13849-1 Annex A uses S, F, P parameters derived from this clause)
- `## 1. Elements of risk` — severity of harm (S1/S2), probability of harm components
- `## 2. Severity parameters (S)` — S1 (slight, normally reversible) vs S2 (serious, normally irreversible including death)
- `## 3. Frequency and exposure (F)` — F1 (seldom/infrequent) vs F2 (frequent/continuous)
- `## 4. Possibility of avoiding or limiting harm (P)` — P1 (possible under specific conditions) vs P2 (scarcely possible)
- `## 5. Relationship to ISO 13849-1` — the S/F/P parameters feed directly into the PLr determination graph (Annex A of ISO 13849-1)

---

### Task 4: ISO 12100 RAG corpus — Clause 6 (Risk Evaluation)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/ISO12100_2010__Clause06__risk_evaluation.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — this is the decision gate: is the estimated risk acceptable or must it be reduced?
- `## 1. Acceptability criteria` — ISO 12100 does not define a single numeric threshold; acceptability depends on state of the art, legal requirements, and common technical practice
- `## 2. Factors influencing acceptability` — relevant legal requirements, state of the art, reasonable expectations of use, known incidents
- `## 3. Outcome` — acceptable (document and close) or not acceptable (proceed to Clause 7 risk reduction)

---

### Task 5: ISO 12100 RAG corpus — Clause 7 (Risk Reduction — Three-Step Method)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/ISO12100_2010__Clause07__risk_reduction.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — the three-step method is the legal hierarchy for CE marking and the backbone of every machine safety design
- `## 1. Step 1 — Inherently safe design` — eliminate hazard at source; examples: no sharp edges, reduced speed, lower force, guarded geometry
- `## 2. Step 2 — Safeguarding and protective measures` — guards (fixed, movable), safety devices (light curtains, interlocks, two-hand controls), protective equipment
- `## 3. Step 3 — Information for use` — warnings, labels, operating instructions, training requirements; residual risk only
- `## 4. Hierarchy enforcement` — Step 2 and 3 cannot substitute for Step 1 where Step 1 is reasonably practicable
- `## 5. Relationship to ISO 13849-1 and IEC 62061` — Step 2 safety devices require performance level (PL) or SIL determination; those standards provide the method

---

### Task 6: ISO 12100 RAG corpus — Annex A (Hazard List)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/ISO12100_2010__AnnexA__hazard_list.md`

Content must cover:
- Front matter comment block
- `## 0. Why this annex matters` — normative; provides the checklist basis for hazard identification in Clause 4
- `## 1. Mechanical hazards` — crushing, shearing, cutting, entanglement, drawing-in, impact, stabbing/puncture, friction/abrasion, ejection
- `## 2. Electrical hazards` — contact with live parts, electrostatic phenomena
- `## 3. Thermal hazards` — contact with flames/explosions, radiation from heat sources
- `## 4. Noise hazards` — hearing loss, interference with speech
- `## 5. Vibration hazards` — hand-arm, whole-body
- `## 6. Radiation hazards` — low-frequency, RF, optical, ionizing
- `## 7. Material/substance hazards` — contact with harmful fluids, biological agents
- `## 8. Ergonomic hazards` — unhealthy posture, over-exertion, cognitive load
- `## 9. Hazards from neglecting ergonomic principles` — mental overload, stress, inadequate local lighting

---

### Task 7: ISO 12100 site page — deepened

**Files:**
- Modify: `docs/standards/functional-safety/iso-12100/index.md`

**Step 1: Read the current file**

```bash
cat "docs/standards/functional-safety/iso-12100/index.md"
```

**Step 2: Rewrite the file**

Keep existing front matter exactly as-is. Replace everything after the front matter `---` with the following structure (~300 lines):

```markdown
<div class="page-header">
  <span class="page-header__label">Functional Safety · ISO 12100</span>
  <h1>ISO 12100:2010 — Risk Assessment and Risk Reduction</h1>
  <span class="badge badge--complete">Phase 3 Complete</span>
</div>

## Quick Start

If you are new to ISO 12100, start here:

- ISO 12100 is the **foundation standard** for machinery safety. Apply it first, before ISO 13849-1, IEC 62061, or IEC 60204-1.
- It gives you a structured method to **identify hazards, estimate risk, and decide whether to reduce it**.
- The output of ISO 12100 is the **required PLr** (or SIL target) that ISO 13849-1 or IEC 62061 then helps you meet.
- The **three-step method** (Clause 7) is legally required for CE marking under the EU Machinery Directive.
- ISO 12100 is a Type A standard — it applies to all machinery. Type B and C standards may override specific requirements.

## Standard Overview
[existing table — keep]

## The Iterative Risk Assessment Process

ISO 12100 Clause 4 defines a four-step loop that repeats until risk is acceptable:

| Step | Activity | ISO 12100 Clause |
|------|-----------|-----------------|
| 1 | Define limits of the machine | 5.3 |
| 2 | Identify hazards (use Annex A checklist) | 5.4 |
| 3 | Estimate risk (S × F × P) | 5.5 |
| 4 | Evaluate risk — acceptable? | 5.6 |
| → if not acceptable | Apply Clause 7 risk reduction, then repeat | 6 |

## Risk Parameters (Clause 5)

| Parameter | Options | Definition |
|-----------|---------|-----------|
| **S — Severity** | S1: Slight (reversible) | Minor injury, no permanent harm |
| | S2: Serious (irreversible or death) | Amputation, crushing, fatality |
| **F — Frequency** | F1: Seldom to infrequent | Exposure < once per shift, or short duration |
| | F2: Frequent to continuous | Regular or prolonged exposure |
| **P — Avoidance** | P1: Possible under specific conditions | Hazard is visible, speed is low, operator trained |
| | P2: Scarcely possible | Sudden hazard, high speed, restricted access |

**These S/F/P parameters feed directly into the PLr determination graph in ISO 13849-1:2023 Annex A.**

## The Three-Step Method (Clause 7)

The Clause 7 hierarchy is legally binding for CE marking. Steps must be applied in order; lower steps cannot substitute for higher steps where higher steps are reasonably practicable.

| Step | Method | Examples |
|------|--------|---------|
| **1 — Inherently safe design** | Eliminate hazard at source | Remove sharp edges, reduce force/speed, enclose moving parts by geometry |
| **2 — Safeguarding** | Guards and safety devices | Fixed guards, interlocked guards, light curtains, two-hand controls, AOPD |
| **3 — Information for use** | Warnings and instructions | Labels, manuals, training requirements, PPE |

Step 2 safety devices require a **Performance Level (PL)** per ISO 13849-1 or a **Safety Integrity Level (SIL)** per IEC 62061. ISO 12100 does not specify which — it simply requires that the chosen method is applied.

## Key Clauses

| Clause | Topic | Key Output |
|--------|-------|-----------|
| 4 | Risk assessment framework | Iterative process, documentation requirements |
| 5.3 | Machine limits | Use phases, user populations, space/time limits |
| 5.4 | Hazard identification | Annex A checklist, systematic hazard enumeration |
| 5.5 | Risk estimation | S, F, P parameter values per hazard |
| 5.6 | Risk evaluation | Acceptability decision, state of the art |
| 6 | Risk reduction — three-step method | Hierarchy of measures |
| Annex A | Hazard list (normative) | 9 hazard categories with examples |
| Annex B | Risk reduction strategy examples | Non-normative worked examples |

## When To Use ISO 12100

| Situation | Use ISO 12100? |
|-----------|---------------|
| CE marking a machine for EU market | Yes — mandatory |
| Designing a US machine (no CE requirement) | Recommended — provides structured hazard identification |
| Determining if a safety function is needed | Yes — Clause 5.5–5.6 makes this decision |
| Determining what PL/SIL a safety function must achieve | Yes — Clause 5.5 parameters → ISO 13849-1 Annex A |
| Designing the safety circuit itself | No — use ISO 13849-1 or IEC 62061 for that step |

## Common Mistakes

1. **Skipping ISO 12100 and going straight to ISO 13849-1.** ISO 13849-1 requires a PLr — that PLr comes from ISO 12100 Clause 5. Without ISO 12100, you are guessing.
2. **Using Step 2 or Step 3 measures without considering Step 1.** If the hazard can be eliminated by design, the Directive requires you to try that first.
3. **Treating the risk assessment as a one-time document.** ISO 12100 requires re-evaluation after every design change, incident, or new use case.
4. **Mixing up S1/S2 with F1/F2.** Severity (S) is about the outcome if the hazard is realized. Frequency (F) is about how often the operator is exposed to the hazard zone.
5. **Not covering all lifecycle phases.** Maintenance, cleaning, and decommissioning are mandatory phases — they often produce the highest risk scores.
6. **Missing the Annex A hazard checklist.** Annex A is normative. Skipping it during hazard identification creates gaps that auditors will find.

## Practical Checklist

Before closing the risk assessment for any machine:

- [ ] Machine limits documented: intended use, user population, space, time
- [ ] All lifecycle phases covered: normal use, foreseeable misuse, maintenance, cleaning, decommissioning
- [ ] Annex A hazard list used as the identification checklist
- [ ] Every identified hazard has S, F, P values assigned
- [ ] Risk evaluation decision documented for every hazard (acceptable / not acceptable)
- [ ] For each "not acceptable" hazard, Clause 7 three-step method applied in order
- [ ] Every Step 2 safety device has a PLr assigned (→ use ISO 13849-1 or IEC 62061)
- [ ] Risk assessment reviewed after all design changes
- [ ] Risk assessment document retained as part of technical file

## Lifecycle Application

| Stage | ISO 12100 Activity |
|-------|-------------------|
| Concept | Define machine limits (Clause 5.3) |
| Risk Assessment | Hazard identification, estimation, evaluation (Clauses 5.4–5.6) |
| Safety Architecture | Risk reduction — select Step 1/2/3 measures (Clause 6) |
| Detailed Design | PLr determination for safety devices → hand off to ISO 13849-1/IEC 62061 |
| Commissioning | Verify residual risk documentation; update technical file |

## Next Steps After ISO 12100

Once PLr targets are determined:

- [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — design and verify SRP/CS to achieve PLr using Category + MTTFd + DC
- [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) — alternative SIL-based path for SRECS on machinery
```

**Step 3: Validate the build**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: ends with `done in X seconds.` — no errors.

**Step 4: Commit Group 1**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add control-standards/rag/standards_intelligence/international/functional_safety/iso_12100/
git add docs/standards/functional-safety/iso-12100/index.md
git commit -m "$(cat <<'EOF'
feat: phase3 group1 — ISO 12100 RAG corpus and deepened site page

5 clause-level RAG corpus files + _index.yaml. Site page expanded to ~300
lines with Quick-Start, three-step method, risk parameters, common
mistakes, practical checklist. Badge updated to Phase 3 Complete.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Group 2: ISO 13849-1 + IEC 62061

### Task 8: ISO 13849-1 RAG corpus — _index.yaml

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/_index.yaml`
- Note: delete `file_structure.md` from this directory after creating all corpus files — it is superseded

```yaml
standard_id: ISO_13849_1
edition: 2023
publisher: ISO
corpus_status: phase3_complete
scope: Safety-related parts of control systems — Performance Level (PL) determination and verification
files:
  - filename: ISO13849_2023__Clause04__design_strategy.md
    clause: "4"
    topic: Design strategy and safety function specification
  - filename: ISO13849_2023__Clause05__srp_cs.md
    clause: "5"
    topic: SRP/CS requirements — MTTFd, DC, CCF
  - filename: ISO13849_2023__Clause06__categories.md
    clause: "6"
    topic: Categories B, 1, 2, 3, 4 — architecture requirements
  - filename: ISO13849_2023__Clause07__validation.md
    clause: "7"
    topic: Validation of PL
  - filename: ISO13849_2023__AnnexA__risk_assessment.md
    clause: "Annex A"
    topic: PLr determination — S/F/P risk parameters graph
  - filename: ISO13849_2023__AnnexF__ccf.md
    clause: "Annex F"
    topic: Common Cause Failure scoring
```

---

### Task 9: ISO 13849-1 RAG corpus — Clause 4 (Design Strategy)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/ISO13849_2023__Clause04__design_strategy.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — defines the required safety function specification before any architecture or calculation work begins
- `## 1. Safety function specification` — each safety function needs: description, initiation event, response action, required PL (PLr), relevant ISO 12100 hazard
- `## 2. Design strategy overview` — PL approach: specify PLr → select Category architecture → calculate PL → verify PL ≥ PLr
- `## 3. PL levels defined` — PLa through PLe with PFHd ranges table
- `## 4. Relationship to ISO 12100` — PLr comes from ISO 12100 Annex A risk graph; Clause 4 consumes that output

---

### Task 10: ISO 13849-1 RAG corpus — Clause 5 (SRP/CS Requirements)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/ISO13849_2023__Clause05__srp_cs.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — defines the three quantitative parameters (MTTFd, DC, CCF) that determine achievable PL within a chosen Category
- `## 1. MTTFd — Mean Time To Dangerous Failure` — per channel; Low/Medium/High ranges; from component datasheets or Annex C/D tables
- `## 2. DC — Diagnostic Coverage` — None (<60%), Low (60–90%), Medium (90–99%), High (≥99%); determined by diagnostic measures implemented
- `## 3. CCF — Common Cause Failure` — score from Annex F (must reach 65 points for Categories 2/3/4); covers separation, diversity, protection from environment
- `## 4. Combined PL determination` — Category + MTTFd + DC → PL from Table 5 of the standard (include the table)
- `## 5. PFHd calculation` — PFHd = f(MTTFd, DC, Category); required when comparing to IEC 62061 SIL

---

### Task 11: ISO 13849-1 RAG corpus — Clause 6 (Categories)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/ISO13849_2023__Clause06__categories.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — Category is the single most important architecture decision; it determines the fault detection and fault tolerance of the SRP/CS
- `## 1. Category B` — basic safety principles only; single channel; no fault detection; suitable only for PLa
- `## 2. Category 1` — well-tried components and safety principles; single channel; no fault detection; PLa–PLc possible
- `## 3. Category 2` — single channel with periodic test channel; fault detection via test; PLa–PLd possible
- `## 4. Category 3` — dual channel (redundant); single fault does not cause loss of safety function; fault detected before or at next demand; PLa–PLd or PLe possible
- `## 5. Category 4` — dual channel with high DC; single fault detected immediately; accumulation of faults considered; PLe achievable
- `## 6. Category selection table` — table: Category vs. achievable PL vs. fault tolerance vs. DC requirement vs. typical application
- `## 7. Common architecture examples` — Category 3: two-channel E-stop with cross-monitoring relay; Category 4: dual-channel safety PLC

---

### Task 12: ISO 13849-1 RAG corpus — Clause 7 (Validation)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/ISO13849_2023__Clause07__validation.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — validation is the mandatory proof that the designed SRP/CS actually achieves the specified PLr; without it, the design is incomplete
- `## 1. Validation plan` — must be established before validation begins; covers analysis and test methods
- `## 2. Analysis methods` — FMEA, fault tree analysis, structured design review
- `## 3. Test requirements` — functional testing of each safety function; confirmation that each fault in the Category architecture is detected as designed
- `## 4. Software validation` — if embedded software is involved, additional requirements apply per IEC 62061 or IEC 61508-3
- `## 5. Validation documentation` — validation report content requirements; must be retained in technical file

---

### Task 13: ISO 13849-1 RAG corpus — Annex A (PLr Determination)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/ISO13849_2023__AnnexA__risk_assessment.md`

Content must cover:
- Front matter comment block
- `## 0. Why this annex matters` — Annex A is the bridge between ISO 12100 risk estimation and ISO 13849-1 design; it converts S/F/P parameters into a required PLr
- `## 1. Risk parameters` — S1/S2 (severity), F1/F2 (frequency), P1/P2 (avoidance) — same parameters as ISO 12100 Clause 5.5
- `## 2. PLr determination table` — reproduce the S/F/P → PLr lookup as a text table (since the standard uses a graph): all S/F/P combinations → PLr values
- `## 3. How to use the table` — worked example: E-stop on a robot cell: S2 (amputation), F2 (operator enters zone frequently), P2 (no warning of restart) → PLd
- `## 4. When PLe is required` — PLe is rare; typically only for applications where a single failure is catastrophic and no other risk reduction is possible

PLr lookup table to include:

| S | F | P | PLr |
|---|---|---|-----|
| S1 | F1 | P1 | PLa |
| S1 | F1 | P2 | PLb |
| S1 | F2 | P1 | PLb |
| S1 | F2 | P2 | PLc |
| S2 | F1 | P1 | PLc |
| S2 | F1 | P2 | PLd |
| S2 | F2 | P1 | PLd |
| S2 | F2 | P2 | PLe |

---

### Task 14: ISO 13849-1 RAG corpus — Annex F (CCF)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/ISO13849_2023__AnnexF__ccf.md`

Content must cover:
- Front matter comment block
- `## 0. Why this annex matters` — CCF scoring is mandatory for Categories 2, 3, and 4; failure to score ≥65 points makes the Category invalid
- `## 1. What CCF addresses` — common cause failure = a single event that simultaneously fails both channels of a redundant system (e.g., same EMI spike taking out both channels)
- `## 2. Scoring table` — reproduce the Annex F scoring table with all measures and their point values
- `## 3. Typical score path to 65 points` — worked example: separation (15 pts) + different technology (20 pts) + protection against overvoltage (15 pts) + use of well-tried components (5 pts) + training (5 pts) + common mode analysis (5 pts) = 65 pts
- `## 4. Common pitfalls` — same cable duct for both channels (fails separation), same component supplier/batch (fails diversity)

---

### Task 15: ISO 13849-1 site page — deepened

**Files:**
- Modify: `docs/standards/functional-safety/iso-13849-1/index.md`

**Step 1: Read the current file**

```bash
cat "docs/standards/functional-safety/iso-13849-1/index.md"
```

**Step 2: Rewrite the body** (~350 lines) with this structure:

```markdown
<div class="page-header">
  <span class="page-header__label">Functional Safety · ISO 13849-1</span>
  <h1>ISO 13849-1:2023 — Safety-Related Parts of Control Systems (PL)</h1>
  <span class="badge badge--complete">Phase 3 Complete</span>
</div>

## Quick Start
- ISO 13849-1 gives you the method to design and verify a safety function to a required Performance Level (PLa–PLe).
- You need a PLr before starting — get it from ISO 12100 Annex A using S/F/P risk parameters.
- Three decisions drive everything: **Category** (architecture), **MTTFd** (component reliability), **DC** (diagnostic coverage).
- PLd is the most common target for industrial guarding, E-stop, and light curtain applications.
- If your safety device uses complex electronics or software, consider IEC 62061 (SIL path) instead or in addition.

## Standard Overview [keep existing table, update Repository and Status rows]

## PLr Determination (from ISO 12100)
[include the S/F/P → PLr table from Annex A RAG file]

## PL Levels and PFHd
[include PL vs PFHd range table from existing stub — keep but verify values]

## Design Parameters
[expanded version of existing table — add column for how to determine each parameter]

## Category Architecture
[full Category B/1/2/3/4 table with fault tolerance, DC requirement, achievable PL, typical use]

## Worked Example: E-Stop for Robot Cell
[S2/F2/P2 → PLd; Category 3 dual-channel; MTTFd high; DC medium → achieves PLd; CCF scored at 65]

## PL vs SIL — When To Choose This Standard
[comparison table: ISO 13849-1 PL path vs IEC 62061 SIL path; link to IEC 62061 page]

## Common Mistakes
1. Specifying PLd without running the ISO 12100 S/F/P analysis — guessing PLr
2. Using Category 3 without achieving 65 CCF points — the dual channel is invalid
3. Taking MTTFd from a component's MTBF figure — MTTFd and MTBF are not the same
4. Ignoring DC — high MTTFd with zero DC only achieves PLc at best (Category 1)
5. Forgetting that software in the safety path requires additional validation per Clause 7
6. Treating PL verification as a one-time step — must be repeated after any design change

## Practical Checklist
- [ ] PLr determined from ISO 12100 S/F/P analysis (not assumed)
- [ ] Each safety function documented: initiation event, response, PLr
- [ ] Category selected and justified
- [ ] MTTFd values sourced from component datasheets or Annex C/D tables
- [ ] DC measures identified and DC level confirmed
- [ ] CCF scored at ≥65 points (for Categories 2/3/4)
- [ ] PL calculated and confirmed PL ≥ PLr
- [ ] Validation plan written before validation begins
- [ ] Functional tests documented
- [ ] Validation report retained in technical file

## Lifecycle Application [expand existing section]
```

**Step 3: Validate build** (same command as Task 7 Step 3)

---

### Task 16: IEC 62061 RAG corpus — _index.yaml

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/_index.yaml`

```yaml
standard_id: IEC_62061
edition: 2021
publisher: IEC
corpus_status: phase3_complete
scope: Functional safety of safety-related electrical control systems on machinery — SIL determination and SRECS design
files:
  - filename: IEC62061_2021__Clause04__scope_context.md
    clause: "4"
    topic: Scope, context, and relationship to IEC 61508
  - filename: IEC62061_2021__Clause06__srecs_design.md
    clause: "6"
    topic: SRECS design — SIL determination and allocation
  - filename: IEC62061_2021__Clause07__subsystem_design.md
    clause: "7"
    topic: Subsystem design — PFHd calculation
  - filename: IEC62061_2021__AnnexA__silcl_tables.md
    clause: "Annex A"
    topic: SILCL and SIL capability tables
```

---

### Task 17: IEC 62061 RAG corpus — Clause 4 (Scope and Context)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/IEC62061_2021__Clause04__scope_context.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — defines when to use IEC 62061 vs. ISO 13849-1; both are valid for machinery but differ in approach and scope
- `## 1. Scope` — applies to SRECS (Safety-Related Electrical Control Systems) on machines; covers E/E/PE systems; does not cover pneumatic/hydraulic-only safety functions
- `## 2. Relationship to IEC 61508` — IEC 62061 is a sector-specific standard derived from IEC 61508; it is simpler to apply to machinery because it scopes out software-intensive systems handled by 61508-3
- `## 3. IEC 62061 vs. ISO 13849-1 comparison table` — include table: metric used (SIL vs PL), applicable system types, software handling, quantitative basis, equivalent levels (SIL1≈PLc, SIL2≈PLd, SIL3≈PLe)
- `## 4. When to use IEC 62061` — preferred when: complex programmable safety controllers (safety PLCs), system integrates subsystems from different suppliers, SIL2/SIL3 is required

---

### Task 18: IEC 62061 RAG corpus — Clause 6 (SRECS Design)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/IEC62061_2021__Clause06__srecs_design.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — defines the top-level SRECS architecture and SIL allocation process
- `## 1. Safety function specification` — same requirement as ISO 13849-1 Clause 4: document each safety function with initiation, response, and target SIL
- `## 2. SIL determination` — from ISO 12100 S/F/P parameters converted to SIL: S1/F1/P1 → SIL1 min; S2/F2/P2 → SIL3; include the IEC 62061 K-factor table
- `## 3. SRECS decomposition` — breaking the SRECS into subsystems (input device, logic, output device); each subsystem gets a SIL Claim Limit (SILCL)
- `## 4. SIL allocation` — subsystem PFHd values sum to give total SRECS PFHd; total must be ≤ PFHd limit for required SIL
- `## 5. SIL levels and PFHd limits` — table: SIL1 (10⁻⁵ to 10⁻⁶ /hr), SIL2 (10⁻⁶ to 10⁻⁷ /hr), SIL3 (10⁻⁷ to 10⁻⁸ /hr)

---

### Task 19: IEC 62061 RAG corpus — Clause 7 (Subsystem Design)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/IEC62061_2021__Clause07__subsystem_design.md`

Content must cover:
- Front matter comment block
- `## 0. Why this clause matters` — provides the formulas for calculating subsystem PFHd from component failure rates and architecture
- `## 1. Subsystem architectures` — 1oo1 (single channel), 1oo2 (dual channel — both must fail), 2oo2 (both channels required for output)
- `## 2. PFHd formula for 1oo1` — PFHd = λDe (dangerous detected failure rate × proof test interval)
- `## 3. PFHd formula for 1oo2` — reduced by diagnostic coverage and redundancy; approximately PFHd = (λDe)² × T1
- `## 4. Component failure rate sources` — manufacturer datasheets (preferred), IEC 61508-2 generic data tables, SISTEMA library
- `## 5. Diagnostic coverage (DC)` — same concept as ISO 13849-1; DC reduces the dangerous undetected failure rate

---

### Task 20: IEC 62061 RAG corpus — Annex A (SILCL Tables)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/IEC62061_2021__AnnexA__silcl_tables.md`

Content must cover:
- Front matter comment block
- `## 0. Why this annex matters` — SILCL defines the maximum SIL a subsystem can claim regardless of calculated PFHd; set by architecture and systematic capability
- `## 1. SILCL definition` — SIL Claim Limit; a subsystem cannot claim higher SIL than its SILCL even if PFHd is low enough
- `## 2. SILCL determination` — based on: hardware fault tolerance (HFT), safe failure fraction (SFF), and systematic integrity
- `## 3. HFT and SFF table` — reproduce the SILCL vs HFT vs SFF table (Type A and Type B subsystems)
- `## 4. Systematic integrity` — software, documentation, and process requirements that set the systematic SILCL ceiling

---

### Task 21: IEC 62061 site page — deepened

**Files:**
- Modify: `docs/standards/functional-safety/iec-62061/index.md`

Rewrite body (~350 lines) with same template as ISO 13849-1 (Task 15), adapted for SIL:
- Quick Start (5 bullets, SIL-focused)
- Standard Overview (keep existing table)
- SIL Determination from ISO 12100 parameters (K-factor table)
- SIL Levels and PFHd (expand existing table)
- SRECS Architecture: input → logic → output subsystem decomposition
- Worked Example: light curtain on press: SIL2; 1oo2 input + SIL2 safety PLC + 1oo2 output; PFHd sum calculation
- PL vs SIL — When To Choose This Standard (mirror/complement the ISO 13849-1 page section; cross-link)
- Common Mistakes (6 items, SIL-specific)
- Practical Checklist (~10 items)
- Lifecycle Application (expanded)

**Step 3: Validate build** (same command as Task 7 Step 3)

**Step 4: Delete superseded file**

```bash
rm "control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/file_structure.md"
```

**Step 5: Commit Group 2**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/
git add control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/
git add docs/standards/functional-safety/iso-13849-1/index.md
git add docs/standards/functional-safety/iec-62061/index.md
git commit -m "$(cat <<'EOF'
feat: phase3 group2 — ISO 13849-1 + IEC 62061 RAG corpus and deepened site pages

ISO 13849-1: 6 clause RAG files + _index.yaml. IEC 62061: 4 clause RAG
files + _index.yaml. Both site pages ~350 lines with PL/SIL decision pair
sections, worked examples, common mistakes, checklists. Removes
superseded file_structure.md placeholder.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Group 3: IEC 61508 + IEC 61511

### Task 22: IEC 61508 RAG corpus — _index.yaml

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/_index.yaml`

```yaml
standard_id: IEC_61508
edition: 2010
publisher: IEC
corpus_status: phase3_complete
scope: Functional safety of E/E/PE safety-related systems — the parent standard for IEC 62061 and IEC 61511
files:
  - filename: IEC61508_2010__Part1__framework.md
    clause: "Part 1"
    topic: General requirements — safety lifecycle, SIL, risk-based approach
  - filename: IEC61508_2010__Part2__hardware.md
    clause: "Part 2"
    topic: Hardware requirements — HFT, SFF, PFDAVG
  - filename: IEC61508_2010__Part3__software.md
    clause: "Part 3"
    topic: Software requirements — SIL-appropriate development practices
  - filename: IEC61508_2010__Clause07__safety_lifecycle.md
    clause: "7"
    topic: Overall safety lifecycle — 16 phases
```

---

### Task 23: IEC 61508 RAG corpus — Part 1 (Framework)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/IEC61508_2010__Part1__framework.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — IEC 61508 is the parent standard; understanding it explains why IEC 62061 and IEC 61511 are structured the way they are
- `## 1. Scope` — all E/E/PE safety-related systems across all industries; deliberately broad; sector standards (62061, 61511) narrow the scope
- `## 2. Risk-based approach` — tolerable risk is defined by the application; SIL is determined by the gap between existing risk and tolerable risk
- `## 3. SIL levels` — SIL1–SIL4; SIL4 is extremely rare (nuclear, aviation); most industrial applications use SIL1–SIL3
- `## 4. The seven-part structure` — Part 1 (general), Part 2 (hardware), Part 3 (software), Parts 4-7 (guidelines and examples)
- `## 5. Relationship to sector standards` — IEC 62061 applies IEC 61508 to machinery; IEC 61511 applies it to process industry; using the sector standard is preferred over applying IEC 61508 directly

---

### Task 24: IEC 61508 RAG corpus — Part 2 (Hardware)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/IEC61508_2010__Part2__hardware.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — Part 2 defines how to quantify hardware safety integrity; the SILCL tables in IEC 62061 Annex A derive from here
- `## 1. Hardware fault tolerance (HFT)` — number of faults system can tolerate while maintaining safety function; HFT 0 = single channel, HFT 1 = dual channel
- `## 2. Safe failure fraction (SFF)` — proportion of failures that are safe or detected; higher SFF allows higher SIL claim with lower HFT
- `## 3. Type A vs Type B subsystems` — Type A: all failure modes known and quantifiable; Type B: not all failure modes known (complex electronics, PLCs)
- `## 4. PFDAVG vs PFHd` — PFDAVG for low-demand mode (tested periodically, process industry); PFHd for high-demand mode (machinery, continuous)
- `## 5. Random hardware integrity tables` — SIL vs HFT vs SFF (Type A and B) — same tables reflected in IEC 62061 Annex A

---

### Task 25: IEC 61508 RAG corpus — Part 3 (Software)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/IEC61508_2010__Part3__software.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — Part 3 is what makes IEC 61508 complex to apply directly; its software requirements are extensive and drive most organizations to use sector standards instead
- `## 1. Software safety integrity levels` — software SIL matches hardware SIL; techniques and measures tables (Annex A) prescribe what is required per SIL
- `## 2. Software lifecycle` — concept → requirements → architecture → design → integration → validation → modification
- `## 3. Key software requirements by SIL` — SIL1: structured programming, test coverage; SIL2: adds formal reviews, static analysis; SIL3: adds formal methods, full MC/DC coverage
- `## 4. Application software vs. embedded software` — application software (ladder logic in safety PLC) has different requirements than the PLC firmware itself; most machinery projects only deal with application software
- `## 5. Why this drives use of certified safety PLCs` — using a TÜV-certified safety PLC shifts the Part 3 software burden to the PLC manufacturer; the machine builder only validates application code

---

### Task 26: IEC 61508 RAG corpus — Clause 7 (Safety Lifecycle)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/IEC61508_2010__Clause07__safety_lifecycle.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — Clause 7 defines the 16-phase overall safety lifecycle that both IEC 62061 and IEC 61511 adopt and simplify
- `## 1. The 16 phases` — list all 16 phases grouped into: concept (1-3), overall scope (4), hazard and risk analysis (5), overall safety requirements (6), safety requirements allocation (7), overall planning (8-10), realization (11-13), overall installation and commissioning (14), overall safety validation (15), overall operation and maintenance (16)
- `## 2. Functional safety management` — documentation, competency, and independence requirements that run across all phases
- `## 3. Lifecycle in practice for machinery` — for a machine builder using IEC 62061, phases 1-7 map roughly to ISO 12100 + IEC 62061 Clause 5-6; phases 8-16 map to design, build, commission, maintain

---

### Task 27: IEC 61508 site page — deepened

**Files:**
- Modify: `docs/standards/functional-safety/iec-61508/index.md`

Rewrite body (~300 lines):
- Quick Start: frame as "parent reference standard — use IEC 62061 or IEC 61511 for application work"
- Standard Overview (keep existing table)
- Seven-Part Structure overview table
- SIL levels and PFHd/PFDAVG table
- Hardware concepts: HFT, SFF, Type A/B
- Safety Lifecycle: 16-phase summary table
- When To Use IEC 61508 Directly vs. a Sector Standard
- Common Mistakes (6 items — e.g. applying Part 3 software requirements directly when a certified safety PLC is used)
- Practical Checklist
- Lifecycle Application

---

### Task 28: IEC 61511 RAG corpus — _index.yaml

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/_index.yaml`

```yaml
standard_id: IEC_61511
edition: 2016
publisher: IEC
corpus_status: phase3_complete
scope: Functional safety of safety instrumented systems for the process industry — SIS design, SIL verification, LOPA
files:
  - filename: IEC61511_2016__Part1__framework.md
    clause: "Part 1"
    topic: General requirements — SIS lifecycle, SIL, process sector context
  - filename: IEC61511_2016__Clause09__sis_design.md
    clause: "9"
    topic: SIS design requirements — architecture, SIL verification
  - filename: IEC61511_2016__Clause11__lopa.md
    clause: "11 / Annex F"
    topic: Layer of Protection Analysis (LOPA) for SIL determination
  - filename: IEC61511_2016__AnnexA__risk_assessment.md
    clause: "Annex A"
    topic: Risk assessment methods for process industry
```

---

### Task 29: IEC 61511 RAG corpus — Part 1 (Framework)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__Part1__framework.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — IEC 61511 is the process industry's equivalent of IEC 62061; it covers SIS (Safety Instrumented Systems) such as emergency shutdown systems, pressure safety systems, burner management
- `## 1. Scope` — process industry E/E/PE safety-related systems; not machinery (use IEC 62061); not nuclear (use IEC 61513)
- `## 2. SIS definition` — Safety Instrumented System: sensor + logic solver + final element, dedicated to a safety instrumented function (SIF)
- `## 3. SIL in process context` — typically determined by LOPA or risk graph; SIL1 most common; SIL3 rare; SIL4 not used in process industry
- `## 4. Low-demand mode` — most process SIS operate in low-demand mode (PFDavg used, not PFHd); proof test interval is critical parameter
- `## 5. Relationship to IEC 61508` — IEC 61511 is the sector standard; clause 1.5 of IEC 61511 permits using "prior use" justification for proven components (not allowed under IEC 61508 directly)

---

### Task 30: IEC 61511 RAG corpus — Clause 9 (SIS Design)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__Clause09__sis_design.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — Clause 9 is the core design chapter; it defines how to architect a SIS to meet the required SIL
- `## 1. SIS architecture` — sensor voting (1oo1, 1oo2, 2oo3), logic solver redundancy, final element redundancy
- `## 2. SIL verification` — calculate PFDavg for each subsystem; sum to get SIF PFDavg; compare to SIL target PFDavg range
- `## 3. Proof test interval` — PFDavg = λDU × T1/2 for 1oo1; longer proof test interval increases PFDavg (degrades SIL); must be balanced against process availability
- `## 4. Common architectures` — 1oo2 sensors (higher availability, same SIL as 1oo1 with lower PFDavg); 2oo3 voting (highest availability, avoids spurious trips)
- `## 5. Independence requirements` — SIS must be independent of BPCS (Basic Process Control System) in hardware, software, and communications

---

### Task 31: IEC 61511 RAG corpus — Clause 11 / Annex F (LOPA)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__Clause11__lopa.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — LOPA is the standard method for determining SIL requirements in process industry; it is referenced by IEC 61511 and used in virtually all SIS projects
- `## 1. LOPA concept` — each layer of protection (BPCS, relief valve, dike, SIS) reduces the consequence frequency; SIL is determined by the gap remaining after all other IPLs are credited
- `## 2. LOPA inputs` — initiating event frequency, consequence severity, tolerable event frequency, IPL credit factors
- `## 3. SIL determination from LOPA` — required PFD = tolerable frequency / (initiating event frequency × all IPL credits); SIL assigned from PFD range
- `## 4. IPL credit table` — typical IPL credit factors: BPCS (10⁻¹), pressure relief valve (10⁻²), operator response with >10 min (10⁻¹), dike (10⁻²)
- `## 5. LOPA limitations` — single consequence per scenario; independent IPLs required; not suitable for complex multi-cause scenarios (use fault tree analysis)

---

### Task 32: IEC 61511 RAG corpus — Annex A (Risk Assessment)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__AnnexA__risk_assessment.md`

Content must cover:
- Front matter comment block
- `## 0. Why this matters` — Annex A provides guidance on risk assessment methods accepted under IEC 61511, including the risk graph method as an alternative to LOPA
- `## 1. Risk graph method` — C (consequence), F (frequency), P (probability of avoiding), W (demand rate) → SIL; qualitative alternative to LOPA for lower-consequence applications
- `## 2. Risk matrix method` — 2D matrix of consequence vs. likelihood → risk ranking → SIL; simpler but less rigorous than LOPA
- `## 3. Quantitative risk analysis (QRA)` — full probabilistic consequence modeling; used for high-consequence applications or regulatory requirements
- `## 4. Method selection guidance` — LOPA preferred for most SIS projects; risk graph acceptable for well-defined, lower-consequence SIFs; QRA for major hazard facilities

---

### Task 33: IEC 61511 site page — deepened

**Files:**
- Modify: `docs/standards/functional-safety/iec-61511/index.md`

Rewrite body (~300 lines):
- Quick Start: frame as "process industry SIS standard — if you build machinery, use IEC 62061 instead"
- Standard Overview (keep existing table)
- SIS Architecture: sensor → logic solver → final element
- SIL in Low-Demand Mode: PFDavg table, proof test interval impact
- LOPA overview: concept, IPL credits, SIL determination
- Common voting architectures: 1oo1, 1oo2, 2oo3 — table with availability and SIL tradeoffs
- When To Use IEC 61511 vs IEC 62061
- Links to: Process Skid scenario page, IEC 61508 page
- Common Mistakes (6 items — e.g. using PFHd instead of PFDavg for low-demand SIS)
- Practical Checklist
- Lifecycle Application

**Step 3: Validate build** (same command as Task 7 Step 3)

**Step 4: Commit Group 3**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add control-standards/rag/standards_intelligence/international/functional_safety/iec_61508/
git add control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/
git add docs/standards/functional-safety/iec-61508/index.md
git add docs/standards/functional-safety/iec-61511/index.md
git commit -m "$(cat <<'EOF'
feat: phase3 group3 — IEC 61508 + IEC 61511 RAG corpus and deepened site pages

IEC 61508: 4 RAG files + _index.yaml (parent standard reference depth).
IEC 61511: 4 RAG files + _index.yaml (process industry SIS + LOPA).
Both site pages ~300 lines. All five functional safety pages now Phase 3
Complete — no remaining PLANNED badges.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Final Task: Update project_state/

### Task 34: Update project_state/project_state.md and change_log.md

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

**Step 1: Update project_state.md**

Change:
- Current Phase line → `Phase 3 complete — all functional safety pages deepened, ready to push`
- Current Direction section → reflect Phase 3 complete
- Add Phase 3 scope as COMPLETED section (mirror Phase 1/2 format)
- Phase 4 Backlog → Interactive standards graph, SEMI S2/S8/S14

**Step 2: Update change_log.md**

Add entry:

```markdown
### 2026-03-06 — Phase 3 Implementation Complete

**Summary:** All five functional safety standard pages deepened and backed by clause-level RAG corpus.

**What changed:**
- 22 new RAG corpus files across iso_12100, iso_13849_1, iec_62061, iec_61508, iec_61511
- 5 site pages rewritten to ~300–350 lines each with Quick-Start, technical reference, common mistakes, practical checklists
- All "PLANNED — TO VERIFY" badges replaced with "Phase 3 Complete"
- Superseded file_structure.md placeholder removed from iso_13849_1/

**Architecture:** Hybrid — clause-level RAG files + deepened site pages. All additive. No new plugins or JS.

**Next step:** `git push` then consider Phase 4 (interactive standards graph).
```

**Step 3: Commit**

```bash
cd "/Users/kyawminthu/Dev/Control System Tools"
git add project_state/project_state.md project_state/change_log.md
git commit -m "$(cat <<'EOF'
docs: update project state for Phase 3 completion

All five functional safety pages complete. Phase 4 backlog captured.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```
