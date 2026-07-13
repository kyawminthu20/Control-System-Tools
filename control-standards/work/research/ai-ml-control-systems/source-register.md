# Initial Source Register

**Source policy:** Prefer peer-reviewed papers, standards bodies, government
guidance, and official project documentation. Record vendor material only as an
implementation example, not as proof of general capability. Notes below are
paraphrases, not copied source text.

## Foundations and model families

### Physics-informed neural networks

- **Raissi, Perdikaris, and Karniadakis, “Physics-informed neural networks,”
  Journal of Computational Physics 378 (2019), DOI 10.1016/j.jcp.2018.10.045.**
  <https://www.sciencedirect.com/science/article/abs/pii/S0021999118307125>
  - Foundational PINN paper combining neural approximation with governing
    differential-equation residuals for forward and inverse problems.
  - Relevance: foundation for the PINN section; does not by itself establish
    industrial real-time suitability or formal control guarantees.

### Convolutional neural networks

- **Krizhevsky, Sutskever, and Hinton, “ImageNet Classification with Deep
  Convolutional Neural Networks,” NeurIPS 2012.**
  <https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html>
  - Landmark deep-CNN result for visual classification.
  - Relevance: foundation for explaining convolution, learned spatial features,
    and why CNNs became central to machine vision. Industrial validation must be
    researched separately.

## LLMs and industrial automation

- **Fakih et al., “LLM4PLC: Harnessing Large Language Models for Verifiable
  Programming of PLCs in Industrial Control Systems,” 2024 preprint.**
  <https://arxiv.org/abs/2401.05443>
  - Proposes an iterative PLC-code pipeline using compilers, grammar checking,
    and formal verification rather than trusting raw model output.
  - Relevance: useful evidence for an “LLM drafts; tools verify; engineer owns”
    architecture. Treat results as research, not general production proof.

- **Xia et al., “Control Industrial Automation System with Large Language
  Models,” 2024 preprint.**
  <https://arxiv.org/abs/2409.18009>
  - Proof-of-concept architecture using structured events and an LLM agent for
    automation tasks.
  - Relevance: candidate end-to-end architecture to critique for latency,
    authority, determinism, cybersecurity, and safety boundaries.

## Industrial interoperability and edge deployment

- **OPC Foundation, OPC UA Part 1: Overview and Concepts.**
  <https://reference.opcfoundation.org/specs/OPC-10000-1/4>
  - Defines OPC UA as a platform-independent framework for secure, reliable,
    semantically structured industrial information exchange.
  - Relevance: primary source for the interface architecture. OPC UA capability
    to carry commands must be separated from authorization for AI control.

- **OPC Foundation, “OPC UA for AI: Enhancing Automation with Artificial
  Intelligence,” 2024.**
  <https://opcconnect.opcfoundation.org/2024/06/opc-ua-for-ai-enhancing-automation-with-artificial-intelligence/>
  - Describes industry work on exposing standardized automation semantics to AI.
  - Relevance: direction-setting source; claims are not a substitute for
    independent validation or a deployed-system safety case.

- **ONNX Runtime, “Deploy ML Models on IoT and Edge Devices.”**
  <https://onnxruntime.ai/docs/tutorials/iot-edge/>
  - Official deployment documentation covering cross-platform edge inference and
    practical tradeoffs such as latency, offline operation, model size, and
    limited compute.
  - Relevance: implementation option for a later edge-inference walkthrough.

## Risk, security, and governance

- **NIST, Artificial Intelligence Risk Management Framework 1.0.**
  <https://www.nist.gov/itl/ai-risk-management-framework>
  - Organizes AI risk work around govern, map, measure, and manage functions.
  - Relevance: baseline vocabulary for trustworthiness, lifecycle risk, testing,
    and monitoring. It is general guidance rather than control-system design law.

- **NIST SP 800-82 Rev. 3, Guide to Operational Technology Security.**
  <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
  - Covers OT architectures, threats, vulnerabilities, segmentation, and
    countermeasures for PLC, DCS, SCADA, and related systems.
  - Relevance: baseline for placing AI services without bypassing OT security
    zones, conduits, least privilege, or operational availability needs.

## Sources still needed

- Peer-reviewed surveys of CNN/temporal models for industrial fault diagnosis
- PINN reviews emphasizing failure modes, optimization difficulty, uncertainty,
  and comparisons with classical numerical methods
- Hybrid-model and neural state-estimation/control papers with reproducible data
- Constrained/safe learning-control research and explicit stability guarantees
- Current standards or guidance for AI in machinery, functional safety, and
  critical infrastructure
- MQTT Sparkplug primary specifications and secure OT deployment guidance
- Model lifecycle, drift, calibration, uncertainty, and out-of-distribution tests
- Public industrial datasets suitable for reproducible examples

---

# Phase 49a Additions (2026-07-13) — sprint-verified

**Verification tally across the sprint: 98 claims — 72 VERIFIED_AT_PUBLISHER, 21 SECONDARY_ONLY
(content sound, publisher metadata blocked by paywall), 3 UNVERIFIABLE, 2 NOT_FOUND (searched, absent).**
Full detail in `evidence-table.md`; ceilings in `authority-ceilings.md`; go/no-go in `49a-findings.md`.

## Functional safety and AI — the authority basis

- **ISO/IEC TR 5469:2024, "Artificial intelligence — Functional safety and AI systems."**
  Ed. 1.0, published 2024-01-08, 73 pp. Joint ISO/IEC JTC 1/SC 42. VERIFIED at the IEC webstore.
  - **It is a Technical REPORT — guidance, not a certifiable requirement set.** The requirement-bearing
    successor ISO/IEC TS 22440 is still at committee-draft stage.
  - Relevance: **the** source for the authority ceiling. Its existence is itself the argument: it was
    written because compliance with the existing functional-safety standards *cannot be shown directly*
    for AI. **Its body is paywalled and was NOT read** — nothing may imply knowledge of its clauses.
    NOTE: it is ISO/IEC TR 5469, **not** "IEC TR 5469."

- **Regulation (EU) 2023/1230 (Machinery).** Official OJ text retrieved via the EU Publications Office.
  - Annex I Part A items 5 and 6 list **safety components with fully or partially self-evolving
    behaviour using machine learning**. Mandatory notified-body assessment; self-declaration unavailable.
  - Annex III EHSR 1.2.1 imposes a **statutory authority ceiling**: no action beyond the defined task and
    movement space; correctable at all times; no hazardous self-modification of safety rules **including
    during the learning phase**.
  - **Date:** applies **20 January 2027** — correct *only via the Corrigendum of 4.7.2023*; the
    uncorrected OJ text says 14 January. (Confirms the site's Phase 45 date.)

- **Regulation (EU) 2024/1689 (AI Act).** Official text retrieved.
  - Art. 6(1): high-risk where the AI is a safety component of a product requiring third-party
    conformity assessment. Art. 6(1) obligations apply **2 August 2027** — ~6 months after the Machinery
    Regulation.

- **ISO/IEC 42001:2023** (AI management systems) and **ISO/IEC 23894:2023** (AI risk guidance).
  Both VERIFIED at the IEC webstore. **Neither confers any technical permission for AI to participate in
  a safety function**, and neither is harmonised for machinery.

- **Required negative check — answered "no".** IEC 61508 remains Ed. 2.0 (2010); ISO 13849-1:2023 is a
  deterministic methodology. **None provides a validation route for a learned component.**
  **UNVERIFIED and NOT TO BE PUBLISHED:** the IEC 61508-3 Table A.2 "AI — not recommended" ratings, and
  any IEC 61508 Ed. 3 or TS 22440 date.

## PINN limits

- **Grossmann, Komorowska, Latz & Schönlieb, "Can physics-informed neural networks beat the finite
  element method?", IMA J. Appl. Math. 89(1), 2024.** FEM faster at equal-or-better accuracy in every
  case; 5–6 orders of magnitude on Allen-Cahn.
- **Krishnapriyan et al., NeurIPS 2021** — the failure is optimisation, not expressivity.
- **Chuang & Barba (arXiv:2306.00230)** — PINN *reverts to the steady-state solution when the data flow
  stops*. The basis for refusing a PINN the authoritative-estimator role. **NOTE: the step to a
  control-loop observer is an inference, not a measured result.**
- **De Ryck & Mishra, Acta Numerica 33 (2024)** — training error is the unresolved bottleneck; no
  computable a posteriori error bound in the general case.

## Learned closed-loop control

- **Brunke et al., Annual Review of Control, Robotics and Autonomous Systems (2022).** Safe-learning
  survey. Its own open challenge: guarantees *"rely on a set of assumptions… difficult to verify prior
  to operation."* **A proof conditioned on an unverifiable premise is a conditional theorem, not a
  safety case.**
- **EASA AI Concept Paper Issue 02** (fetched). Supervised, **offline learning only**, model frozen at
  approval; the system must present *no capability of adaptive learning*. The hardest sector position found.
- Documented real deployments (tokamak coil control; an 840-hour RL distillation-column run; a learned
  road-vehicle planner) **all keep a non-learned layer holding the veto.**

## Fault diagnosis — datasets and the leakage problem

- **Lessmeier et al., PHM Europe 2016** (open access, PDF retrieved) — the Paderborn reference paper.
  Confirms **synchronous 64 kHz vibration AND motor phase current, same rig, same 32 bearings**, and
  that **vibration beat motor-current classification in every case** (98.3% vs 93.3%; 75.0% vs 45.9%
  train-artificial/test-real).
- **Leakage:** under a strict bearing-wise split, 1D-CNN performance collapses to near chance
  (Paderborn AUROC 99.9 → 53.2; CWRU 100.0 → 66.4). **Near-100% results in this literature are, as a
  class, an artefact of the split.**
- **LICENCES — decisive.** Paderborn: **CC BY-NC 4.0 (NonCommercial)**. CWRU: **no licence, no terms of
  use, no redistribution statement of any kind**; third-party mirrors assert CC terms traceable to no
  grant. **Cite and link CWRU; never redistribute.**

## Interfaces and edge

- **OPC UA Parts 3/4/5/9/18** (OPC Foundation, retrieved). Sampling is **best-effort** with a
  server-imposed floor (`MinSupportedSampleRate`); the server *"has no knowledge of the data update
  logic"* of the decoupled source. **Write-authority separation is fully spec-backed** — the well-known
  **Observer** role (browse/read/subscribe, no write) maps exactly onto a publish-only inference service.
  **NEGATIVE: OPC UA has no native field for confidence, model version, or staleness, and no AI/ML
  companion specification exists.** Sparkplug B is better provisioned out of the box.
- **NIST SP 800-82 Rev. 3** — supports edge-local computation and read-only monitoring as a distinct,
  lower-impact class. **Cite NIST; do not cite IEC 62443 clause numbers (unverified).**
- **CORRECTION:** "kHz cannot go through OPC UA" is **FALSE as a protocol claim** (PubSub/UADP over TSN
  measured at a 250 µs cycle). The edge-inference conclusion stands on the four constraints above, not
  on protocol speed.

## Chemical and biological

- **Conservation laws are hard constraints; kinetic closures are not.** Mass/energy/charge balances,
  stoichiometry, Sv=0 with flux bounds and thermodynamic feasibility can bound a learned output;
  Arrhenius/Monod/Butler–Volmer cannot (fitted, regime-limited, often unidentifiable). The hybrid
  literature applies ML **only to the unclosed terms, never to the conservation equations.**
- **Rathore et al., Life (2021)** — industrial bioprocess control is still **PI/PID plus open-loop
  pre-computed feed profiles**; MPC/ANN remain research/pilot.
- **NOT VERIFIED:** the canonical chemical-engineering textbooks (publisher 403), so the
  **equilibrium/thermodynamics family currently has no verified source.**

## Still needed (carried forward)

- **ISO/IEC TR 5469:2024 full text** (purchase) — its Usage Level × Technology Class matrix is the
  highest-value missing artefact in the entire programme.
- **IEC 62061** — never checked for ML/self-evolving content.
- Smith & Randall 2015; Hendriks et al. 2022; Naser 2025 (PINNs in an engineering-systems framing);
  the lab-to-field transfer-learning assessment — all paywalled, all carrying load-bearing numbers.
- **The FP64 question** — a 2025 preprint reportedly argues canonical PINN failures are FP32 artefacts.
  Sharp implication: embedded targets run FP32, so a PINN healthy on a workstation could fail on the
  deployment hardware.
- Adversarial coverage for the **chemical and biological** families (they have none).
- An ISO-verified vibration sample-rate/bandwidth figure (ISO's platform refused retrieval).
- **The two 2024 arXiv preprints (LLM4PLC; Xia et al.) remain PREPRINTS** — every claim resting on them
  inherits `preprint` strength.
