# Phase 49a — AI/ML Source-Closure Sprint — Implementation Plan

> **For agentic workers:** This plan is executed as a **multi-agent Workflow** (owner explicitly
> authorised). Steps use checkbox (`- [ ]`) syntax for tracking. This is a **research** phase — it
> produces sourced evidence, not code. The TDD analogue: **every claim starts unverified and must
> survive publisher verification and an adversarial refutation pass before it may enter the register.**

**Goal:** Close the source gaps that Phase 49 was gated on, producing a verified evidence base strong
enough that the method register's `authority_basis` and `evidence_strength` columns can be filled
honestly — or an explicit, reasoned "no" for any domain where they cannot.

**Architecture:** Six independent research workstreams fan out in parallel; each returns structured
claims. Every claim carrying an **authority ceiling** then goes through an adversarial verification
stage whose job is to *refute* it. Survivors are cited; casualties are demoted to engineering
judgement and labelled. A final synthesis writes the evidence table and the go/no-go recommendation.

**Tech Stack:** Workflow tool (multi-agent orchestration), WebSearch + WebFetch for retrieval,
Markdown outputs under `control-standards/work/research/ai-ml-control-systems/`.

**Spec:** `docs/superpowers/specs/2026-07-12-ai-ml-methods-register-design.md`

## Global Constraints

Every task's requirements implicitly include these. They are non-negotiable and copied from the spec
and `governance/CONTENT_STANDARDS.md`.

- **Publisher verification.** Every edition/existence claim is verified against the actual publisher —
  IEC webstore, ISO OBP, EUR-Lex, NIST CSRC, OPC Foundation. **Never from model memory.**
- **UNVERIFIABLE is a valid result.** Anything the publisher's free text cannot settle is recorded as
  `UNVERIFIABLE` with the reason. **Guessing is a failure; admitting is a pass.**
- **No fabricated URLs.** No URL enters any output that was not actually retrieved in-session. A
  remembered URL is a fabricated URL.
- **Paraphrase only.** No reproduction of standards text or table values (CONTENT_STANDARDS §2).
- **Vendor material is an example, never proof** of general capability.
- **Negative results are results.** "No standard addresses X" and "no evidence supports Y" are
  first-class findings and must be recorded with the same rigour as positives.
- **Work tier only.** All output lands in `control-standards/work/research/` — non-authoritative.
  **No site page, no corpus file, no `docs/` content is written in this phase.**
- **No employer or customer data** of any kind (CONTENT_STANDARDS §7).
- Sub-agents never edit `project_state/` (AI_WORKFLOW). The orchestrator does that at the end.

---

## File Structure

| File | Responsibility |
|---|---|
| `control-standards/work/research/ai-ml-control-systems/source-register.md` | **Modify.** Existing register; gaps closed, each entry gaining a verification status and strength grade. |
| `control-standards/work/research/ai-ml-control-systems/evidence-table.md` | **Create.** Per-claim evidence table: claim → source → verification status → strength → what it does and does not support. The artifact 49b reads to fill `authority_basis`. |
| `control-standards/work/research/ai-ml-control-systems/authority-ceilings.md` | **Create.** Per-method-family authority ceiling, its basis, and the refutation attempt it survived (or didn't). |
| `control-standards/work/research/ai-ml-control-systems/49a-findings.md` | **Create.** The go/no-go recommendation per domain, open gaps with reasons, and what 49b may and may not claim. |
| `project_state/project_state.md`, `project_state/change_log.md` | **Modify.** Orchestrator only, at the end. |

---

### Task 1: Run the six-workstream research fan-out

**Files:**
- Create (workflow scratch): agent returns are collected in-memory by the Workflow script
- Test: verification is Task 2; this task must NOT self-certify its own claims

**Interfaces:**
- Produces: a list of claim objects consumed by Task 2. Each claim:
  `{id, workstream, claim, source_url, source_title, publisher, verification_status, strength, supports, does_not_support, authority_ceiling_proposed?}`
  - `verification_status` ∈ `VERIFIED_AT_PUBLISHER` | `SECONDARY_ONLY` | `UNVERIFIABLE` | `NOT_FOUND`
  - `strength` ∈ `standards_body` | `peer_reviewed` | `preprint` | `vendor_claim` | `engineering_judgement`

- [ ] **Step 1: Workstream 1 — AI in machinery and functional safety (BLOCKING — everything waits on this)**

Targets, all stated as **candidates to verify, not facts**:
- **IEC TR 5469** — functional safety and AI systems. Verify existence, exact title, edition/year, and
  scope **at the IEC webstore**. If it exists as expected, its vocabulary becomes the backbone of
  `authority_basis`.
- **EU Machinery Regulation 2023/1230** — verify at **EUR-Lex** whether it addresses safety components
  with self-evolving / AI behaviour, and quote-free-paraphrase what it actually requires. The site
  already carries its 20 Jan 2027 transition (Phase 45).
- **EU AI Act** — verify at EUR-Lex whether AI in safety components of machinery falls in the high-risk
  pathway, and what conformity assessment that triggers.
- **ISO/IEC 42001** (AI management systems) and **ISO/IEC 23894** (AI risk) — verify at **ISO OBP**.
- **Negative check, required:** do IEC 61508 / ISO 13849-1 / IEC 61511 address learned or
  non-deterministic components **at all**? A sourced "no" is a required finding, not a failure.

- [ ] **Step 2: Workstream 2 — PINN failure modes**

Seek reviews honest about optimisation difficulty, spectral bias, convergence pathologies, and cases
where PINNs **lose** to classical numerical methods. **The negatives are the deliverable.** A
workstream returning only PINN successes has failed and must be re-run.

- [ ] **Step 3: Workstream 3 — Safe / constrained learning control**

The question: does **any** credible published evidence support **authority level 5** (direct learned
closed-loop control) in a safety context? Expectation is **no**. Return the strongest candidate
evidence found *and* the strongest counter-evidence, so Task 2 can adjudicate rather than rubber-stamp.

- [ ] **Step 4: Workstream 4 — CNN / temporal models for industrial fault diagnosis**

Peer-reviewed surveys. Plus the reproducible public datasets: **Paderborn** (carries vibration **and**
motor current from the same rig on the same faults — verify this, it is what makes the
accelerometer-vs-drive-current comparison answerable with evidence) and **CWRU**. Record licence terms
for each dataset — a dataset that cannot be redistributed changes what 49c can publish.

- [ ] **Step 5: Workstream 5 — Interfaces and edge**

OPC UA information models (OPC Foundation), MQTT/Sparkplug primary specification, ONNX Runtime edge
deployment, **NIST SP 800-82 Rev. 3** for placing AI services without breaking OT segmentation.
Specific question to answer with a source: **the sampling-rate ceiling of SCADA/OPC UA tag paths**, and
therefore why kHz-rate signal inference must be an edge concern with only the result crossing into
SCADA.

- [ ] **Step 6: Workstream 6 — Chemical and biological governing models**

Reaction kinetics, transport, thermodynamics; Monod/growth kinetics, fermentation, bioprocess control.
Textbooks and peer-reviewed work — **not vendor material**. For each: what it governs, what it
constrains, and how it couples to a twin (governing model / constraint / soft sensor).

---

### Task 2: Adversarially verify every authority ceiling

**Files:**
- Create: `control-standards/work/research/ai-ml-control-systems/authority-ceilings.md`

**Interfaces:**
- Consumes: claim objects from Task 1 where `authority_ceiling_proposed` is set
- Produces: `{method_family, ceiling, basis, refutation_attempted, survived: bool, downgraded_to?}`

- [ ] **Step 1: Refute, don't confirm**

For each proposed ceiling, dispatch **independent** verifiers whose instruction is to **refute** it —
default to `refuted = true` when uncertain. The failure mode being defended against is **not** a
missing citation; it is a *plausible-sounding ceiling that no source actually supports*. A ceiling
that only survives because nobody attacked it is exactly the artifact this phase exists to prevent.

- [ ] **Step 2: Adjudicate**

- Survives refutation **and** has `VERIFIED_AT_PUBLISHER` / `peer_reviewed` backing → ceiling stands,
  `authority_basis` = the citation.
- Survives but rests on `preprint` / `vendor_claim` → ceiling stands **provisionally**,
  `authority_basis` = "engineering judgement, weak evidence" and the row says so.
- Refuted, or no evidence found → **demote to advisory (level 2) or lower**, `authority_basis` =
  "engineering judgement — no source supports a higher ceiling."

- [ ] **Step 3: Record the negatives explicitly**

Every demotion is written down **with the reason**. `authority-ceilings.md` must be readable as a list
of what we could **not** justify, because that is the list 49b is forbidden to overstate.

---

### Task 3: Synthesise the evidence table and the go/no-go

**Files:**
- Create: `control-standards/work/research/ai-ml-control-systems/evidence-table.md`
- Create: `control-standards/work/research/ai-ml-control-systems/49a-findings.md`
- Modify: `control-standards/work/research/ai-ml-control-systems/source-register.md`

- [ ] **Step 1: Write the evidence table**

One row per claim: claim → source (title, publisher, URL retrieved) → verification status → strength →
**what it supports** → **what it does NOT support**. That last column is what stops 49b from stretching
a citation past its reach.

- [ ] **Step 2: Close the source register**

Every entry under "Sources still needed" is either closed with a verified primary source, or **remains
open with a written reason**. Re-check the two 2024 arXiv preprints (LLM4PLC; Xia et al.) against the
publisher for peer-reviewed status — if they are still preprints, they are graded `preprint` and every
claim resting on them inherits that grade.

- [ ] **Step 3: Write the go/no-go recommendation**

Per domain (core AI/ML + interfaces · classical baselines · chemical · biological): may 49b proceed?
**"No" is an allowed and expected answer for at least some domains.** State what 49b would be permitted
to claim and what it must not.

- [ ] **Step 4: Orchestrator updates project tracking**

Update `project_state/project_state.md` (phase, next steps) and `project_state/change_log.md` per
CLAUDE.md. **Sub-agents must not touch these files.**

- [ ] **Step 5: Commit**

```bash
git add control-standards/work/research/ai-ml-control-systems/ project_state/
git commit -m "research(ai-ml): Phase 49a — source closure sprint, evidence table, authority ceilings"
```

---

## Self-Review

**Spec coverage:** §6's six workstreams → Task 1. §6 adversarial verification → Task 2. §6 done-criteria
(gaps closed-or-reasoned, evidence table, preprints re-checked, go/no-go allowed to say no,
project_state updated) → Task 3 steps 1–4. §6 source-quality rules → Global Constraints. §7 out-of-scope
(no site/corpus content, no code, placement decision deferred) → Global Constraints + spec §7.

**Placeholder scan:** No TBDs. Each workstream names its actual targets and its actual publisher to
verify against.

**Consistency:** `verification_status` and `strength` enums are defined once in Task 1's Interfaces
block and used unchanged in Tasks 2 and 3. Authority levels use the ladder from the spec (0–5)
throughout.

**Known risk, accepted:** the four standards named in Workstream 1 are the orchestrator's recollection,
not verified fact. If IEC TR 5469 does not exist in the expected form, Workstream 1 returns largely
negative and the register's authority column rests on engineering judgement — which the schema already
accommodates via `authority_basis`. **The plan is designed to survive its own primary hypothesis being
wrong.**
