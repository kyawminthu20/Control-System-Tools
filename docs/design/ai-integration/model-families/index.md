---
layout: default
title: "AI Model Families & Fit"
description: "The three learned families the register leans on — convolutional/temporal perception, physics-informed networks, and large language models — shown as capability and poor fit, and scored against the authority gate."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Model Families & Fit"
review:
  standard: "Project evidence register (peer-reviewed + preprint sources)"
  edition: "Phase 49a findings, 2026-07-13; Slice D source-gap closures 2026-07-17"
  status: "Review pending"
  coverage: "CNN/perception, PINN, and LLM families — capability and poor-fit. Chemical and biological families remain Planned and are not covered here."
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/model_families.md"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "Safety & Security Boundaries"
    url: "/design/ai-integration/safety-boundaries/"
  - name: "Method Register"
    url: "/design/ai-integration/method-register/"
  - name: "Interfaces & Handshakes"
    url: "/design/ai-integration/interfaces/"
lifecycle_stage:
  - name: "Concept Design"
    slug: "concept-design"
  - name: "Detailed Design"
    slug: "detailed-design"
---

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>AI Model Families &amp; Fit</h1>
  <p>The learned families the register leans on, shown twice: where each is the right tool, and where it is the wrong one. Choosing the wrong family is the more common and more expensive mistake, so the poor-fit case gets equal weight.</p>
</div>

This page is part of the [AI &amp; ML Integration]({{ '/design/ai-integration/' | relative_url }})
section; read the [authority gate]({{ '/design/ai-integration/' | relative_url }}) first, then
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }})
for why a learned component cannot hold a safety function. This page is an explainer that arrives
*after* the gate — every family here is scored against the authority ladder, and no learned family is
assigned level 5 or a safety function. Review pending.

## The rule that frames every family

A learned family earns its place only where a named deterministic method genuinely cannot do the job.
The recurring result across every family below is that the classical method — a solver, a filter, an
interlock, a first-principles balance — is faster, bounded, analysable, and frequently more accurate.
Name the deterministic alternative first; make the learned family demonstrate a specific, validated
advantage before it earns any authority.

<div class="table-scroll" markdown="1">

| Family | Genuine fit | Poor fit | Register ceiling |
|---|---|---|---:|
| **CNN / temporal perception** | Machine-vision inspection; condition-monitoring advisories | A trip, interlock, or any safety credit; trusting a lab accuracy figure | 2 · advisory |
| **PINN / physics-informed** | Inverse problems, parameter ID; hybrid closure of *unclosed* terms | A forward solver where FEM applies; a control-loop state estimator | 1–2 (0 if the loop closes on it) |
| **LLM / language & agentic** | Draft-then-verify code with a human owner; read-only copilot | Raw output as a control artefact; agentic end-to-end control | 0 draft · 2 copilot |

</div>

## Convolutional and temporal perception (CNN)

A model that learns spatial or temporal features directly from data — 2-D CNNs for images, 1-D CNNs
and temporal transformers for signals such as vibration or motor current. The register places every
row in this family at **advisory (level 2)**: it may raise a flag a person evaluates, never a trip,
interlock, or any part of a safety function.

**Where it fits.** Machine-vision inspection, where a wrong call is caught downstream and carries no
direct safety authority; and condition-monitoring advisories — a wear flag ranked for a human, feeding
a maintenance decision rather than an automated action.

**Why the ceiling is advisory.**

- **The literature is contaminated by train/test leakage, and the effect is measured.** Under a strict
  bearing-wise split, 1-D CNN performance collapses from near-perfect to near-chance: CWRU macro-AUROC
  falls 100.0 → 66.4, and Paderborn 99.9 → 53.2, where 50 is a coin toss. A peer-reviewed result
  reports 95% → 53% on CWRU when the split changes from by-load to by-fault-size. **Near-100% numbers
  in this field are, as a class, an artefact of the split** — assume a vendor accuracy figure is leaky
  until the split protocol is disclosed.
- **No source measures learned bearing diagnosis on a real industrial fleet.** Every quantitative
  result comes from a laboratory rig. The lab-to-field gap is asserted by the literature and quantified
  by nothing — itself the strongest argument for the low ceiling.
- **The binding constraint is component diversity in training, not the algorithm.** A fleet operator
  whose training set holds many of its *own* bearings may legitimately earn more; the ceiling describes
  the available evidence, not a claim that CNNs are worthless.

**A sensor-choice result worth carrying.** On the Paderborn rig — motor phase current and
bearing-housing vibration recorded synchronously on the same bearings at 64 kHz — **vibration beat
motor-current classification in every case tested** (98.3% vs 93.3% on real damage; 75.0% vs 45.9%
training on artificial and testing on real damage). Motor-current bearing diagnosis is a cost-driven
degradation, not an equivalent. *Choose the sensor before the model.*

> **Data-licence note.** The Paderborn dataset is CC BY-NC 4.0 (NonCommercial) — usable with
> attribution, not in a commercial offering. The CWRU dataset publishes no licence and no terms of use;
> third-party mirrors asserting Creative Commons terms trace to no grant. Cite and link CWRU; never
> redistribute it.

## Physics-informed and hybrid models (PINN)

A neural network trained to satisfy a governing differential equation's residual as well as (or instead
of) data, and its hybrid variants where a learned term closes a first-principles model. The register
places the pure-PINN rows at **1–2**, and at **0 for any output on which control is closed**.

**Where it fits.** Inverse problems and parameter identification — the one niche the literature
genuinely favours. And hybrid residual modelling of *unclosed terms only*: ML applied to the subgrid or
kinetic closure a first-principles model leaves open, never to the conservation equations. The
conservation law stays the hard constraint; the learned term lives inside it.

**Why control must not close on it.**

- **PINNs lose to the finite element method, badly, on forward problems.** Grossmann et al.
  (*IMA J. Appl. Math.* 89(1), 2024): *"In all the examples that we have studied, the FEM solutions
  were faster at the same or at a higher accuracy."* FEM was faster by 2–3 orders of magnitude on
  Poisson and Schrödinger and **5–6 orders on Allen-Cahn**, where the PINN could not be trained at all
  at small diffusivity.
- **The failure is silent.** The PDE residual loss can converge while the solution is wrong
  (Krishnapriyan et al., NeurIPS 2021). Because a residual-based health monitor watches the same
  quantity that is already low, **it can be fooled.** Silent, plausible, unmonitorable failure is the
  worst failure class in process control.
- **The state-estimator role, specifically.** Chuang & Barba observed a data-driven PINN sustaining the
  correct unsteady dynamics only while fed data and *"reverting to the steady state solution when the
  data flow stops."* A state observer propagates state *between* measurement updates — operationally,
  "the data flow stopped." *Honest caveat:* the step from a CFD result to a control-loop observer
  re-anchored by a sensor every scan is an **inference, not a measured result** — nobody appears to have
  run that experiment. It is presented as reasoning by analogy.
- **No computable a posteriori error bound in the general case** (De Ryck & Mishra, *Acta Numerica* 33,
  2024). "This output is within X of truth, right now, computably" is being proposed in the literature,
  not used — exactly the capability a safety case requires.

> **The FP64 caveat — a deployment-hardware trap.** A 2025 result (Xu et al., "FP64 is All You Need,"
> NeurIPS 2025) reframes several canonical PINN failure modes as **artefacts of single-precision (FP32)
> arithmetic**: in FP32 the optimiser's convergence test trips early and freezes the network in a
> spurious failure; double precision (FP64) rescues it. But **embedded targets run FP32 or
> fixed-point**, so a PINN well-behaved on an FP64 workstation could fail on the very hardware it is
> deployed to. Bench accuracy in FP64 does not transfer to an FP32 edge device — **validate at the
> deployment precision.**

## Large language and agentic models (LLM)

A model that generates text — PLC/structured-text code, engineering documents, or agent actions over
structured plant events. The register places code generation at **offline (level 0)** and a read-only
engineering copilot at **advisory (level 2)**. No LLM row touches control authority.

**Where it fits — draft-then-verify, engineer owns.** Fakih et al., "LLM4PLC" (peer-reviewed, ICSE
2024 Software-Engineering-in-Practice track), report that state-of-the-art LLMs fail to produce valid
PLC programs from a prompt alone, and build a pipeline that feeds model output through a grammar
checker, a compiler, and a formal (SMV) verifier with user feedback. The pipeline raised the generation
success rate from **47% to 72%** and expert-rated code quality from 3.0/10 to 7.2/10. The load-bearing
point is the architecture: **the value is in the verification tools around the model, not in the raw
output**, and a human owns the result. A read-only copilot — summarising documentation, drafting
procedures over read-only context, every output reviewed — is the other genuine fit.

**Where it does not fit.**

- **Raw LLM output is not a control artefact.** It is non-deterministic and unverifiable in the sense a
  safety case needs; generated code compiling is necessary but does not establish requirement
  completeness, correct abnormal-condition behaviour, or safety suitability. That is why code generation
  stays offline.
- **Agentic end-to-end control is a research architecture, not a deployment pattern.** Xia et al.,
  "Control Industrial Automation System with Large Language Model Agents" (peer-reviewed, IEEE ETFA
  2025), is a proof-of-concept to critique for latency, authority, determinism, cybersecurity, and
  safety boundaries — not evidence that an LLM may command a plant. Keep the agent out of the safety and
  control path.

## The families on the ladder

Each family sits where its evidence — not its marketing — places it. The full row-by-row comparison,
with the deterministic alternative each method must beat, lives on the
[method register]({{ '/design/ai-integration/method-register/' | relative_url }}).

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    subgraph L0["0 · Offline"]
      A["LLM code draft<br/>(behind compiler + formal check)"]
    end
    subgraph L2["2 · Advisory"]
      B["CNN / temporal perception<br/>(inspection · condition flag)"]
      C["LLM read-only copilot"]
      D["PINN inverse / parameter ID"]
    end
    subgraph L0b["0 · for any output the loop closes on"]
      E["PINN as a control-loop<br/>state estimator — do not"]
    end
    A --> B
    classDef offline fill:#f2f2ef,stroke:#a0a09a,color:#1e1e1e
    classDef advisory fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef forbidden fill:#faeeec,stroke:#a33327,color:#1e1e1e,stroke-width:2px
    class A offline
    class B,C,D advisory
    class E forbidden
</pre>
</div>

## What this means for design

- **CNN / perception:** advisory only. Assume published accuracy is leakage-inflated until the split is
  disclosed; validate on held-out *components*, not held-out windows; choose the sensor before the model.
- **PINN:** compare against an established numerical solver; never close a control loop on a PINN
  estimate; treat low training loss as no evidence of a correct field; and **validate at the deployment
  numerical precision** — FP32 edge hardware can break a workstation-validated model.
- **LLM:** keep generation offline and behind grammar/compiler/formal verification with a human owner;
  keep agentic control in the research column, not the plant.

## Review status

Distilled from a corpus-owned Draft note and **Review pending**. Return to the
[authority gate]({{ '/design/ai-integration/' | relative_url }}), the
[method register]({{ '/design/ai-integration/method-register/' | relative_url }}),
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}),
or [Interfaces &amp; Handshakes]({{ '/design/ai-integration/interfaces/' | relative_url }}).
