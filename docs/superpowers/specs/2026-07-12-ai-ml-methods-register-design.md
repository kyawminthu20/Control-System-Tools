# AI/ML Methods Register for Control Systems — Design

**Date:** 2026-07-12
**Status:** Design approved. Phase 49a (source-closure sprint) authorised. 49b and 49c are NOT.
**Supersedes scope of:** `planning/2026-07-12-ai-ml-control-systems-presentation-plan.md` (that plan's
authority-first principle is retained; its 7-page topic structure is replaced by the register + layer pages)
**Source material:** `control-standards/work/research/ai-ml-control-systems/` (work tier, non-authoritative)

---

## 1. What this is

A design-and-setup reference on the site covering how to **set up and design** the SCADA/interface
layer, the digital-twin layer, the PINN/hybrid layer, and the chemical and biological model layers so
that they carry real intelligence — with **every method type enumerated** so a reader can see the whole
landscape and choose between them on evidence.

It is not a reference implementation. Working code may follow later; it is not a deliverable here.

## 2. The structural problem, and the resolution

The Phase 49 presentation plan argues — correctly — that a **topic-first tree is unsafe**: a reader
landing on "CNNs" from a search engine meets the capability without ever encountering the authority
ladder or the safety boundary. But an exhaustive **methods catalogue is inherently topic-first**. The
two requirements pull against each other.

**Resolution: make the catalogue a data-driven method register** (the Phase 48 pattern — YAML data →
rendered tables), where the gate is not a page the reader might skip but a **set of columns on every
row**. Each method carries its maximum authority level, the basis for that ceiling, the validation it
demands, how it fails, and what must remain independent of it.

Complete enumeration and the safety property, in one artifact. A capability cannot be presented
without its gate, because the gate is a field.

## 3. Decomposition

Three sub-projects. Each has its own gate. **Only 49a is authorised by this design.**

| Phase | Deliverable | Gate to start |
|---|---|---|
| **49a — Source closure** | Updated `source-register.md` + per-claim evidence table with strength grades, in `control-standards/work/research/`. Nothing ships to the site. | **Authorised now.** |
| **49b — Method register** | `docs/_data/ai-methods/*.yml` (~40–60 methods) → rendered catalogue page. | 49a done, and its written recommendation says proceed. It is allowed to say no for a given domain. |
| **49c — Layer design pages** | SCADA/interface · digital twin · PINN/hybrid · chemical · biological. How to set each layer up, how its methods compose, what it hands to the layer above. | 49b done. |

Placement stays as the presentation plan recommends: **one subsection under Design**
(`/design/ai-integration/`), not split across Fundamentals and Design — co-location of capability and
gate is a safety property, not a filing preference. **Owner confirmation of this placement is still
outstanding** and is a precondition for 49b, not 49a.

## 4. Scope of the enumeration

Four domains, all four in scope, all using one schema:

1. **Core AI/ML + interface layers** — SCADA/data interface (OPC UA, MQTT/Sparkplug, historians,
   edge), digital twin (state sync, calibration, simulation), CNN/perception, PINN/hybrid physics,
   LLM/agentic.
2. **Classical & deterministic baselines** — MPC, Kalman/EKF/UKF, state observers, system
   identification, SPC/statistical methods, rule engines, first-principles models. **Load-bearing:**
   every ML row must name what it has to beat, and this domain is that column's vocabulary. Without
   it the register cannot answer "when NOT to use ML."
3. **Chemical & process models** — reaction kinetics, equilibrium, transport, electrochemistry,
   combustion, thermodynamics, and how each couples to the twin as governing model, constraint, or
   soft sensor.
4. **Biological & microbiological** — growth/metabolic models, fermentation, contamination and
   biofilms, physiology, ecological response; bioprocess control.

## 5. Register schema

One row per method. Same fields for a 1D CNN, a Kalman filter, Monod kinetics, and an LLM agent —
uniformity is the point, because it makes "should I use ML here at all?" answerable by reading **across
a row** instead of across five pages.

**Identity and placement**

- `method`, `family` — perception · estimation · physics-informed · language/agentic ·
  classical-deterministic · chemical-kinetic · biological · optimisation
- `does` — one line: what it actually computes
- `layer` — device · edge · supervisory · historian/analytics · engineering workstation ·
  enterprise/cloud

  *This field is a design check, not a label.* It is what catches errors like routing kHz vibration
  data through OPC UA tag polling — a sampling-rate impossibility that forces edge inference, with
  only the **result** (class, confidence, model version, freshness) crossing into SCADA.

**Justification — the "when NOT to use ML" machinery**

- `deterministic_alternative` — what it must beat. A method with no named alternative is a red flag;
  the register surfaces that rather than hiding it.
- `justified_when` / `poor_fit_when` — **both required.** A row that can only say when a method is
  good is marketing.
- `data_requirement` — what it costs to train and to keep valid.

**The gate**

- `max_authority` — ceiling on the ladder (0 offline → 1 read-only → 2 advisory → 3 operator-approved
  → 4 bounded supervisory → 5 closed-loop). **Sourced, not asserted.** Where no evidence supports a
  ceiling above advisory, the row says so.
- `authority_basis` — the citation, **or the explicit admission that it is engineering judgement.**
  This field is the register's integrity check and the first thing a reviewer should read.
- `validation_required` — test sets, uncertainty, out-of-distribution behaviour, drift monitoring,
  rollback.
- `failure_modes` — how it goes wrong, including the quiet ways.
- `safety_independence` — what must remain independent of it and stay effective when it is wrong,
  stale, unavailable, or compromised.

**Evidence honesty**

- `evidence_strength` — peer-reviewed · standards body · vendor claim · preprint · engineering
  judgement
- `maturity` — research · piloted · industrially routine

  A CNN for surface inspection and a PINN for real-time state estimation are **not** in the same
  place. A flat catalogue presenting them side by side without this column would quietly lie.

## 6. Phase 49a — the sprint

**Execution: multi-agent workflow** (owner explicitly authorised). Fan-out across workstreams, then an
adversarial verification stage.

### Workstreams, in priority order

1. **AI in machinery and functional safety** — *everything else waits on this.* Targets to verify
   (**candidates, not facts** — my knowledge has a cutoff and Phase 45's lesson was not to trust an
   unverified edition claim): **IEC TR 5469** (functional safety and AI systems); the **EU Machinery
   Regulation 2023/1230** AI/self-evolving-behaviour provisions (the site already carries its
   20 Jan 2027 transition from Phase 45); the **EU AI Act** high-risk pathway for AI in safety
   components of machinery; **ISO/IEC 42001** and **ISO/IEC 23894** alongside the NIST AI RMF already
   in the register. Also: whether IEC 61508 / ISO 13849 / IEC 61511 address learned components **at
   all**. Output: the vocabulary for `authority_basis`.
2. **PINN failure modes** — optimisation difficulty, spectral bias, where PINNs lose to classical
   numerics. **The negatives matter more than the successes.**
3. **Safe / constrained learning control** — does anything credible support **authority level 5** in a
   safety context? Expectation: no. A *sourced* "no" is among the most valuable rows in the register.
4. **CNN and temporal models for industrial fault diagnosis** — surveys, plus reproducible public
   datasets (Paderborn — which carries vibration **and** motor current from the same rig on the same
   faults; CWRU) so later examples rest on real data.
5. **Interfaces and edge** — OPC UA information models, MQTT/Sparkplug primary spec, ONNX Runtime edge
   deployment, NIST SP 800-82 Rev. 3 for placement without breaking segmentation.
6. **Chemical and biological governing models** — kinetics, transport, Monod/bioprocess control;
   textbooks and peer-reviewed work, not vendor material.

### Source-quality rules (carried from Phase 45)

- **Every edition claim is verified against the publisher** — IEC webstore, ISO OBP, EUR-Lex, NIST —
  never from model memory.
- Anything the publisher's free text cannot settle is recorded **UNVERIFIABLE** and flagged, not
  guessed.
- **No URL enters the register that was not actually retrieved.**
- Vendor material is logged as an implementation example, never as proof of general capability.
- Paraphrase only; no reproduction of standards text or table values (CONTENT_STANDARDS §2).

### Adversarial verification

Every proposed authority ceiling gets an independent pass whose job is to **refute** it. The failure
mode here is not a missing citation — it is a plausible-sounding ceiling that no source actually
supports. Claims that survive are cited; claims that do not are demoted to engineering judgement and
**labelled as such** in `authority_basis`.

### Negative results are results

"No standard currently addresses X" and "no published evidence supports Y at this authority level" are
findings the register needs — and the findings a vendor-sourced view of this field will never supply.

### Done criteria

- [ ] Every gap in `source-register.md` either closed with a verified primary source, or explicitly
      recorded as still-open **with a reason**
- [ ] Per-claim evidence table with strength grades
- [ ] The two 2024 arXiv preprints (LLM4PLC; Xia et al.) re-checked against the publisher for
      peer-reviewed status
- [ ] Written recommendation on whether 49b may proceed — **allowed to come back "no"** for any of the
      four domains
- [ ] `project_state/` updated per CLAUDE.md

## 7. Out of scope

- Any site or corpus page (49b/49c, separately gated)
- Reference implementation / working code
- Employer or customer data of any kind (CONTENT_STANDARDS §7)
- The `/design/ai-integration/` placement decision — **owner's call, still outstanding**, and a
  precondition for 49b rather than 49a
