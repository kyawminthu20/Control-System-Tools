# Phase 49a — Authority Ceilings After Adversarial Verification

**Generated:** 2026-07-13 · **Status:** Work tier — non-authoritative research capture.
**Raw verdicts:** `adversarial-verdicts.md` · **Claim evidence:** `evidence-table.md`

This document is written to be read as **a list of what could not be justified.** That is its
purpose. Phase 49b (the method register) is forbidden to exceed it.

## The ladder

| Level | Meaning |
|---|---|
| 0 | Offline analysis — no online interface |
| 1 | Read-only monitoring — visualisation and logging |
| 2 | Advisory — operator evaluates and acts separately |
| 3 | Operator-approved — proposed command confirmed through a governed workflow |
| 4 | Bounded supervisory — a non-learned layer independently checks enable, range, rate, mode, freshness, permissives |
| 5 | Direct learned closed-loop control, including safety-related action |

## How these ceilings were produced

Research agents proposed 80 ceilings. Each was then attacked by verifiers instructed to **refute**,
and to **default to refuted when uncertain**. **76 of the 80 were refuted** — and in essentially every
case the refutation pushed the ceiling **down**, not up. That asymmetry is the headline result of the
adversarial stage.

**Coverage caveat, stated up front.** The run hit a session limit partway through the refute stage.
Only 2 of 80 ceilings received all three lenses; most received one. **The chemical and biological
families received no adversarial coverage at all** and their ceilings below are therefore *unattacked
research proposals*, not adjudicated positions. They are marked accordingly and must not be treated as
equivalent to the rest.

---

## The one finding that governs everything else

**No learned component may hold the safety function. Level 5 is unsupported in every domain examined,
and the ceiling is not merely engineering convention — it is now written into EU law.**

But the naive form of that claim is **false and must not be written.** Learned closed-loop control on
real, hazardous plant *does* exist and is documented: reinforcement learning commanding 19 coils on the
TCV tokamak; an RL controller running a JSR distillation column for 840 consecutive hours; an ML
planner taking complete control of a road vehicle. What every one of these cases converges on is not
absence of learned control — it is an **authority ceiling**:

> **The learned policy holds *operational* authority inside an envelope. A verified, non-learned layer
> holds the *safety* function and the veto.**

Yokogawa's own account states safety was ensured with the existing interlocks; the ESD and F&G systems
were untouched. The learned road-vehicle planner's authors — while driving a real car — state plainly
that ML cannot offer safety guarantees, and interpose a rule-based fallback. Three independent sources
converge on the same architecture, and so does the standards position: ISO/IEC TR 5469's own recommended
architecture is a **supervision function with constraints** bounding the AI's behaviour.

**Write:** *"Learned control is used in the loop; it is never given the safety function."*
**Do not write:** *"Learned control is never used in the loop."*

---

## Ceilings by method family

### PINN / physics-informed hybrid — **ceiling 1–2; level 0 for anything the loop closes on**

The most heavily attacked family (22 adjudicated ceilings) and the one demoted furthest. Research
proposed level 3; verification pushed it to **1–2**, and to **0** for any output on which control is
closed.

The evidence is unusually damning and it is peer-reviewed, not speculative:

- **PINNs lose to the finite element method, badly.** Grossmann et al. (*IMA J. Appl. Math.* 89(1), 2024):
  *"In all the examples that we have studied, the FEM solutions were faster at the same or at a higher
  accuracy."* FEM faster by 2–3 orders of magnitude on Poisson and Schrödinger, **5–6 orders** on
  Allen-Cahn — where the PINN could not be trained at all at small ε. For forward problems on
  well-posed domains, the deterministic method simply wins.
- **The failure is optimisation, not expressivity** (Krishnapriyan et al., NeurIPS 2021). The network
  *can* represent the answer; the optimiser cannot find it.
- **The kill shot for state estimation.** Chuang & Barba: a data-driven PINN produces vortex shedding
  while fed data and *"reverts to the steady state solution when the data flow stops."* A state
  estimator propagating between measurement updates **is** "the data flow stopped" — so a PINN in that
  role can silently relax to a bland, physically-plausible, **wrong** state. And because the PDE
  residual can be small while the solution is wrong, **a residual-based health monitor can be fooled.**
  Silent, plausible, unmonitorable failure is the worst failure class in process control.

**Honest caveat, and it matters:** the step from "reverts to steady state on a CFD problem" to "will do
so in a control-loop observer" is an **inference, not a measured result**. A PINN observer re-anchored
by a sensor reading every scan might not exhibit the reversion. Nobody appears to have run that
experiment. Any page must present this as reasoning by analogy, clearly labelled.

**Where PINNs genuinely earn their place:** inverse problems and parameter identification. That is the
one niche the literature favours — and even that rests on reputation, not on evidence gathered here.

### CNN / learned perception — **ceiling 1–2, advisory only; never a trip, interlock, or safety function**

Research proposed level 2; verification largely held the number but **demoted its basis** and in
several cases pushed to level 1.

- **The literature is contaminated by train/test leakage, and the effect is now measured.** Under a
  strict bearing-wise split, 1D-CNN performance collapses: CWRU macro-AUROC 100.0 → **66.4**; Paderborn
  99.9 → **53.2** (50 = chance). A separate result reports 95% → 53% on CWRU when the split changes
  from by-load to by-fault-size. **Near-100% numbers in this field are, as a class, an artefact of the
  split.**
- **No source measures CNN bearing diagnosis on a real industrial fleet.** Every quantitative result
  available comes from a laboratory test rig. The lab-to-field gap is asserted by the literature and
  quantified by nothing — which is itself the strongest argument for the low ceiling.

### Reinforcement learning / learned policies — **ceiling 3; level 4 only behind a verified non-learned veto**

Research proposed 4 on the strength of the documented industrial cases; verification pushed to **3** as
the default, with 4 available only inside the bounded-and-vetoed architecture above.

### Online / self-evolving learning — **ceiling 0 in certified aviation; ≤4 and heavily constrained under EU machinery law**

EASA's AI concept paper scopes itself to **supervised, offline learning only, model frozen at
approval**, and requires the applicant to ensure the system *"presents no capability of adaptive
learning"* — such applications *"will not be accepted at this stage."* This is the hardest position
found in any sector.

### Robust MPC / predictive safety filters / CBF — **ceiling 2–3; the guarantees are conditional theorems**

This is the strongest *honest* case for constraint satisfaction, and it indicts itself on exactly the
point at issue. Brunke et al. (*Annual Review of Control, Robotics and Autonomous Systems*, 2022) list
as an open challenge that safety guarantees *"rely on a set of assumptions… it is difficult to verify
these assumptions prior to a robot's operation."*

> **A proof conditioned on an unverifiable premise is not a safety case. It is a conditional theorem.**
> That distinction is stated by the field's own leading survey, and it is the single most useful
> sentence the sprint recovered.

### Classical deterministic methods (MPC, EKF/UKF/MHE, observers, SPC, first-principles) — **the baseline, and usually the winner**

Not a learned family, and the register's most important column exists to compare against it. The
recurring pattern across every workstream: the deterministic method is faster, bounded, analysable, and
frequently more accurate. Where a learned method is proposed, **the burden of proof sits with the
proposer.**

### Chemical governing models — **UNATTACKED. Research proposal only.**

The key structural finding (which *is* well sourced): **conservation laws are hard constraints;
kinetic closures are not.** Mass/energy/charge balances, stoichiometry, Sv=0 with flux bounds, and
thermodynamic feasibility can legitimately bound a learned model's output. Arrhenius, Monod, and
Butler–Volmer **cannot** — their parameters are fitted, regime-limited, and often unidentifiable. The
hybrid-modelling literature applies ML **only to the unclosed subgrid/kinetic terms, never to the
conservation equations.** That split should be the spine of the chemical layer page.

**No adversarial coverage. No verified source for the equilibrium/thermodynamics family** (publisher
returned 403). Treat as provisional.

### Biological / microbiological — **UNATTACKED. Research proposal only.**

Verified reality check: industrial bioprocess control today is still **PI/PID regulatory loops plus
open-loop pre-computed feed profiles.** MPC, fuzzy, and ANN control remain research/pilot, blocked by
model inaccuracy, scarce data, and the absence of validated model-validation protocols for regulators.
The narrow real exception is Raman/PLS-driven glucose feedback in CHO fed-batch. **No source
authorises a learned model to hold unsupervised closed-loop authority in a bioprocess.**

**No adversarial coverage.** Treat as provisional.

---

## What we could NOT justify — the prohibition list

1. **Any learned method holding a safety function (level 5), in any domain.** No certification route was
   found under IEC 61508, IEC 61511, or ISO 13849. Absence of a route is not permission.
2. **Any SIL or PL claim for a learned component.** No standard tells an engineer how good an ML model
   must be to be trusted with any safety authority. That void is itself a finding.
3. **A PINN as the authoritative state estimator in a control loop.**
4. **A CNN raising a trip or interlock**, or any perception model with safety credit.
5. **Online/adaptive learning in a certified-safety context.**
6. **Any performance threshold for ML in a safety role** — none exists to cite.

## Claims that MUST NOT be published (verification failed)

- **IEC 61508-3:2010 Annex A Table A.2 ratings for "AI — fault correction."** Widely repeated in
  secondary literature; the standard is paywalled and every retrieval attempt was refused. **Do not
  publish the ratings.** The defensible statement is: *IEC 61508 (Ed. 2.0, 2010) provides no route to
  qualify a learned component.*
- **Any IEC 61508 Edition 3 date.** A revision is referenced in secondary sources; the IEC webstore
  still shows Ed. 2.0 as current. Unverified.
- **Any ISO/IEC TS 22440 publication date.** Committee-draft stage; not verifiable at the publisher.
- **The contents of ISO/IEC TR 5469:2024.** Its *designation, title, edition (1.0), date (2024-01-08),
  73 pp, Published status and three-part scope* are publisher-verified. **Its body is not** — it is
  paywalled. The Usage Level (A1/A2/B1/B2/C/D) × Technology Class (I/II/III) framework was read from
  the publicly posted **final draft**, and clause numbers may have changed. Any page citing that ladder
  must say so, or the published TR must be purchased first.
- **Any ISO 13373 numeric guidance on vibration sample rate.** ISO's platform refused retrieval. The
  kHz-bandwidth requirement is currently **engineering judgement only**.
- **Any IEC 62443 clause number.** Not verified at the publisher. Cite NIST SP 800-82r3, and mention
  62443 only as referenced *by* NIST.
