<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Model families and fit — capability and poor fit

This note is the corpus source for the site's Model Families & Fit page. It records what the three
learned families the register actually leans on — convolutional/temporal perception, physics-informed
networks, and large language models — can and cannot do in an industrial control setting, with the
poor-fit case given equal weight to the capability case. It is a decision aid, not permission to
deploy. Claims trace to the publisher or official text; where evidence is a preprint or engineering
judgement, it says so. The families here are scored against the [authority gate](README.md) and the
[safety boundary](safety_boundary.md); no learned family is assigned a safety function or level 5.

## 0. The rule that frames every family

A learned family earns its place only where a named deterministic method genuinely cannot do the job.
The recurring result across every family below is that the classical method — a solver, a filter, an
interlock, a first-principles balance — is faster, bounded, analysable, and frequently more accurate.
So each family is presented twice: where it is the right tool, and where it is the wrong one. The
poor-fit case is not a caveat appended to a capability; it is half the content, because choosing the
wrong family is the more common and more expensive mistake.

## 1. Convolutional and temporal perception (CNN / 1-D CNN / transformer)

**What it is.** A model that learns spatial or temporal features directly from data — 2-D CNNs for
images (the ImageNet lineage), 1-D CNNs and temporal transformers for signals such as vibration or
motor current. The register places every row in this family at **advisory (level 2)**: it may raise a
flag a person evaluates, never a trip, interlock, or any part of a safety function.

**Where it fits.**

- **Machine vision inspection** — presence/absence, defect classification, and measurement on a
  production line, where a wrong call is caught downstream and carries no direct safety authority.
- **Condition-monitoring advisories** — a bearing- or gearbox-wear flag ranked for a human, feeding a
  maintenance decision, not an automated action.

**Where it does not fit, and why the ceiling is advisory.**

- **The literature is contaminated by train/test leakage, and the effect is now measured.** Under a
  strict bearing-wise split, 1-D CNN performance collapses from near-perfect to near-chance: on the
  CWRU dataset macro-AUROC falls 100.0 → 66.4; on Paderborn 99.9 → 53.2, where 50 is a coin toss
  (Zhang et al. leakage-benchmark preprint, corroborated by the peer-reviewed Hendriks et al. result
  of 95% → 53% on CWRU when the split changes from by-load to by-fault-size). **Near-100% numbers in
  this field are, as a class, an artefact of the split** — a vendor accuracy figure must be assumed
  leaky until the split protocol is disclosed.
- **No source measures learned bearing diagnosis on a real industrial fleet.** Every quantitative
  result available comes from a laboratory test rig. The lab-to-field gap is asserted by the
  literature and quantified by nothing — which is itself the strongest argument for the low ceiling.
- **The binding constraint is component diversity in training, not the algorithm.** A fleet operator
  whose training set contains many of its own bearings may legitimately earn more than a lab result on
  a handful of bearings suggests; the ceiling is a statement about the available evidence, not a claim
  that CNNs are worthless.

**A sensor-choice result worth carrying.** On the Paderborn rig, which recorded motor phase current
and bearing-housing vibration synchronously on the same bearings at 64 kHz, **vibration beat
motor-current classification in every case tested** (98.3% vs 93.3% on real damage; 75.0% vs 45.9%
training on artificial and testing on real damage). Motor-current bearing diagnosis is a cost-driven
degradation — the current sensor is already in the drive — not an equivalent to a dedicated
accelerometer. Choose the sensor before the model.

**Data-licence note.** The Paderborn dataset is **CC BY-NC 4.0 (NonCommercial)** — usable with
attribution, but not in a commercial offering. The CWRU dataset publishes **no licence and no terms of
use of any kind**; third-party mirrors asserting Creative Commons terms trace to no grant by CWRU.
Cite and link CWRU; never redistribute it.

## 2. Physics-informed and hybrid models (PINN)

**What it is.** A neural network trained to satisfy a governing differential equation's residual as
well as (or instead of) data — the Raissi et al. formulation — and its hybrid variants, where a
learned term corrects or closes a first-principles model. The register places the pure-PINN rows at
**1–2**, and at **0 for any output on which control is closed**; the hybrid residual model sits at 2.

**Where it fits.**

- **Inverse problems and parameter identification** — recovering an unknown coefficient, source, or
  boundary condition from sparse data. This is the one niche the literature genuinely favours, though
  even that rests more on reputation than on numbers gathered here.
- **Hybrid residual modelling of unclosed terms only** — ML applied to the subgrid or kinetic closure
  a first-principles model leaves open, **never to the conservation equations themselves.** The
  conservation law remains the hard constraint; the learned term lives inside it.

**Where it does not fit, and why control must not close on it.**

- **PINNs lose to the finite element method, badly, on forward problems.** Grossmann et al.
  (*IMA J. Appl. Math.* 89(1), 2024): *"In all the examples that we have studied, the FEM solutions
  were faster at the same or at a higher accuracy."* FEM was faster by 2–3 orders of magnitude on
  Poisson and Schrödinger and **5–6 orders on Allen-Cahn**, where the PINN could not be trained at all
  at small diffusivity. For a well-posed forward problem, the deterministic solver simply wins.
- **The failure is silent.** The PDE residual loss can converge while the solution is wrong
  (Krishnapriyan et al., NeurIPS 2021 — the network *can* represent the answer the optimiser cannot
  find). Because a residual-based health monitor watches the same quantity that is already low, **it
  can be fooled.** Silent, plausible, unmonitorable failure is the worst failure class in process
  control.
- **The kill shot for the state-estimator role.** Chuang & Barba (preprint) observed that a
  data-driven PINN sustains the correct unsteady dynamics only while it is fed data and *"reverts to
  the steady state solution when the data flow stops."* A state observer's whole job is to propagate
  state *between* measurement updates — operationally identical to "the data flow stopped" — so a PINN
  in that role can relax to a bland, physically plausible, wrong state. **Honest caveat:** the step
  from a CFD result to a control-loop observer re-anchored by a sensor every scan is an *inference, not
  a measured result*; nobody appears to have run that experiment. Present it as reasoning by analogy.
- **No computable a posteriori error bound in the general case.** De Ryck & Mishra (*Acta Numerica* 33,
  2024) identify training error as the unresolved bottleneck; the ability to say "this PINN's output is
  within X of truth, right now, computably" is being proposed in the 2026 literature, not used. That
  is exactly the capability a safety case requires.

**The FP64 caveat — a deployment-hardware trap.** A 2025 result (Xu et al., "FP64 is All You Need,"
NeurIPS 2025) reframes several canonical PINN failure modes as **artefacts of single-precision (FP32)
arithmetic**: with FP32 the optimiser's convergence test trips early and freezes the network in a
spurious failure phase, and upgrading to double precision (FP64) rescues it. The control-systems
implication is sharp and cuts the wrong way for deployment: **embedded targets run FP32 or
fixed-point**, so a PINN that is well-behaved on an FP64 workstation could fail on the very hardware it
is deployed to. Bench accuracy in FP64 does not transfer to an FP32 edge device — validate at the
deployment precision.

## 3. Large language and agentic models (LLM)

**What it is.** A model that generates text — here, PLC/structured-text code, engineering documents, or
agent actions over structured plant events. The register places code generation at **offline (level 0)**
and a read-only engineering copilot at **advisory (level 2)**. No LLM row touches control authority.

**Where it fits — draft-then-verify, engineer owns.**

- **LLM drafts, tools verify, the engineer owns.** Fakih et al., "LLM4PLC" (**peer-reviewed, ICSE 2024
  Software-Engineering-in-Practice track**), report that state-of-the-art LLMs fail to produce valid
  PLC programs from a prompt alone, and build a pipeline that feeds model output through a grammar
  checker, a compiler, and a formal (SMV) verifier with user feedback. The pipeline raised the
  generation success rate from **47% to 72%** and expert-rated code quality from 3.0/10 to 7.2/10. The
  load-bearing point is the architecture: **the value is in the verification tools around the model,
  not in the raw output**, and a human owns the result.
- **Read-only engineering copilot** — summarising plant documentation, drafting procedures, or
  answering questions over read-only context, where every output is reviewed before use.

**Where it does not fit.**

- **Raw LLM output is not a control artefact.** It is non-deterministic and unverifiable in the sense a
  safety case needs; generated code compiling is necessary but does not establish requirement
  completeness, correct abnormal-condition behaviour, or safety suitability. That is why code
  generation stays offline.
- **Agentic end-to-end control is a research architecture, not a deployment pattern.** Xia et al.,
  "Control Industrial Automation System with Large Language Model Agents" (**peer-reviewed, IEEE ETFA
  2025**), is a proof-of-concept using structured events and an LLM agent for automation tasks — a
  candidate architecture to critique for latency, authority, determinism, cybersecurity, and safety
  boundaries, not evidence that an LLM may command a plant. Treat it as a demonstration to reason
  against, and keep the agent out of the safety and control path.

## 4. What this means for design

- **Name the deterministic alternative first.** If a solver, filter, interlock, or balance meets the
  requirement, use it; make the learned family demonstrate a specific, validated advantage before it
  earns any authority.
- **CNN/perception:** advisory only. Assume published accuracy is leakage-inflated until the split
  protocol is disclosed; validate on held-out *components*, not held-out windows; choose the sensor
  (vibration over motor current for bearings) before the model.
- **PINN:** compare against an established numerical solver; never close a control loop on a PINN
  estimate; treat low training loss as no evidence of a correct field; and **validate at the
  deployment numerical precision**, because FP32 edge hardware can break a workstation-validated model.
- **LLM:** keep generation offline and behind grammar/compiler/formal verification with a human owner;
  keep agentic control in the research column, not the plant.

## Sources

- Krizhevsky, Sutskever & Hinton, "ImageNet Classification with Deep CNNs," NeurIPS 2012 — CNN lineage.
- Lessmeier et al., "Condition Monitoring of Bearing Damage…," PHM Europe 2016 (open access) —
  Paderborn synchronous current + vibration at 64 kHz; vibration beats motor current in every case.
- Zhang et al., "Towards a more realistic evaluation of ML models for bearing fault diagnosis,"
  arXiv:2509.22267 (preprint) — bearing-wise leakage collapse (CWRU 100.0 → 66.4; Paderborn 99.9 → 53.2).
- Hendriks, Dumond & Knox, "Towards better benchmarking using the CWRU dataset," *Mech. Syst. Signal
  Process.* 169 (2022) — peer-reviewed 95% → 53% leakage result (accessed at one remove; secondary).
- Paderborn KAt-DataCenter (CC BY-NC 4.0); CWRU Bearing Data Center (no licence, no terms of use).
- Raissi, Perdikaris & Karniadakis, "Physics-informed neural networks," *J. Comput. Phys.* 378 (2019).
- Grossmann et al., "Can physics-informed neural networks beat the finite element method?,"
  *IMA J. Appl. Math.* 89(1) (2024) — FEM faster at equal-or-better accuracy in every case.
- Krishnapriyan et al., "Characterizing possible failure modes in PINNs," NeurIPS 2021 — silent,
  optimisation-driven failure.
- Chuang & Barba, "Predictive Limitations of PINNs in Vortex Shedding," arXiv:2306.00230 (preprint) —
  reversion to steady state when the data flow stops.
- De Ryck & Mishra, "Numerical analysis of PINNs…," *Acta Numerica* 33 (2024) — training error as the
  unresolved bottleneck; no general computable a posteriori bound.
- Xu, Liu, Nassereldine & Xiong, "FP64 is All You Need: Rethinking Failure Modes in PINNs," NeurIPS
  2025 (arXiv:2505.10949) — several canonical PINN failures are FP32 artefacts rescued by FP64.
- Fakih et al., "LLM4PLC…," ICSE 2024 SEIP (arXiv:2401.05443) — draft-then-verify pipeline; 47% → 72%.
- Xia et al., "Control Industrial Automation System with Large Language Model Agents," IEEE ETFA 2025
  (arXiv:2409.18009, DOI 10.1109/ETFA65518.2025.11205539) — agentic proof-of-concept, critique target.

## Changelog

- 2026-07-17 — Slice D corpus note drafted from the Phase 49a evidence findings. Two source gaps
  named in the build plan were closed at the publisher during this slice: the **FP64/PINN** claim
  (verified as Xu et al., NeurIPS 2025) and the publication status of the two 2024 LLM preprints —
  **LLM4PLC** is a peer-reviewed ICSE 2024 SEIP paper and **Xia et al.** is a peer-reviewed IEEE ETFA
  2025 paper (both remain proof-of-concept demonstrations, not production evidence). Review pending.
