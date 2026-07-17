---
layout: default
title: "AI Worked Architectures"
description: "Four end-to-end examples — a vision inspection cell, a predictive-maintenance pipeline, a PINN soft sensor, and a read-only LLM copilot — each walked through the authority ladder: which rung, what evidence, and what stays independent when the model is wrong."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Worked Architectures"
review:
  standard: "Composes the AI-integration section (register + Slices B–F); no new claims"
  edition: "Phase 51 Slice G, 2026-07-17"
  status: "Review pending"
  coverage: "Vision cell, predictive-maintenance pipeline, PINN soft sensor, read-only LLM copilot — each on the authority ladder. Reuses verified positions from Slices B–F; introduces no new technical claims."
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/worked_architectures.md"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "Model Families & Fit"
    url: "/design/ai-integration/model-families/"
  - name: "Interfaces & Handshakes"
    url: "/design/ai-integration/interfaces/"
  - name: "Validation & Lifecycle"
    url: "/design/ai-integration/validation-lifecycle/"
  - name: "Safety & Security Boundaries"
    url: "/design/ai-integration/safety-boundaries/"
lifecycle_stage:
  - name: "Concept Design"
    slug: "concept-design"
  - name: "Detailed Design"
    slug: "detailed-design"
---

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>Worked Architectures</h1>
  <p>Four end-to-end examples, each walked through the authority ladder: which rung the evidence supports, and what stays independent when the model is wrong. One worked example beats three abstractions.</p>
</div>

This page is the closing page of the [AI &amp; ML Integration]({{ '/design/ai-integration/' | relative_url }})
section; read the [authority gate]({{ '/design/ai-integration/' | relative_url }}) first. It introduces
**no new claims** — it composes the positions already established across the section into four concrete
architectures. Review pending.

## How to read each example

Every architecture answers four questions in the same order — **the job**, **the rung** (highest
authority the evidence supports, and why not higher), **what stays independent** when the model fails,
and **the seam and the contract** where the result crosses into control. The recurring shape is the
[envelope architecture]({{ '/design/ai-integration/' | relative_url }}#the-envelope-architecture): the
learned component informs or proposes; a verified non-learned layer decides and protects; no safety
function routes through the learned path.

<div class="table-scroll" markdown="1">

| Architecture | Model family | Rung | What stays independent |
|---|---|---:|---|
| Vision inspection cell | 2-D CNN | 2 · advisory | Reject/divert actuation, part-tracking, interlocks (PLC-owned) |
| Predictive-maintenance pipeline | 1-D CNN / temporal | 2 · advisory | Protection and process control; maintenance planning absorbs errors |
| PINN soft sensor | Physics-informed | 1–2 (0 if the loop closes on it) | Real instruments, deterministic estimators, the control loops |
| Read-only LLM copilot | LLM | 2 advisory · 0 for drafted code | Everything — the copilot cannot act |

</div>

## 1. Vision inspection cell

**The job.** A 2-D CNN inspects each part — presence/absence, defect class, or a measurement — so the
cell can reject or pass it.

**The rung — advisory (level 2), PLC owns the action.** The CNN classifies; a deterministic rule or a
person sets the accept/reject policy, and the **PLC owns the reject-trigger timing and actuation.** Not
higher: a perception model's field accuracy cannot be inferred from its bench accuracy, so a
misclassification must be caught downstream, not trusted as a plant fact.

**What stays independent.** The reject/divert mechanism, part-tracking, and any interlock are
deterministic and outside the model. A missed or false classification degrades yield or passes a bad
part to a downstream check — it defeats no safety function, because none depends on the CNN.

**The seam and the contract.** The CNN runs at the cell ([edge inference]({{ '/design/ai-integration/interfaces/' | relative_url }}))
and publishes a result — class, confidence, model version, timestamp, quality — that the PLC reads and
gates. Low confidence or a stale result routes to the defined response (hold, divert to manual
inspection), never a silent pass.

## 2. Predictive-maintenance pipeline

**The job.** A 1-D CNN or temporal model watches vibration (and possibly motor current) on a rotating
asset and flags likely bearing or gearbox wear for maintenance planning.

**The rung — advisory (level 2).** It flags; a person schedules. Not higher: the fault-diagnosis
literature's near-100% accuracies are, as a class, an artefact of train/test leakage — under a
leakage-free component-wise split the honest number can fall to near chance, and **no source measures
learned diagnosis on a real industrial fleet** (see [Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }})).
A fleet operator whose training set holds many of its own bearings may earn more — but that is a claim
the operator's own validation must make. Sensor choice matters: on the reference rig, vibration beat
motor current in every case.

**What stays independent.** Nothing trips, derates, or issues an automated work order on the model's
say-so above advisory; protection and process control are untouched. A missed or false flag is absorbed
by the planning process.

**The seam and the contract.** Acquire and infer at the edge (a kHz waveform cannot be reconstructed by
oversampling a decoupled tag); publish the verdict — class, confidence, model version, freshness — into
the historian/CMMS, not the raw waveform. Drift monitoring decides when the flag is no longer
trustworthy.

## 3. PINN soft sensor

**The job.** A physics-informed model estimates an unmeasured or hard-to-measure variable from sparse
instruments — a soft sensor feeding operator awareness.

**The rung — read-only to advisory (level 1–2); level 0 for anything the loop closes on.** A PINN may
support estimation and calibration, but it must **not** be the authoritative estimator in a control
loop: a data-driven PINN can revert to a steady-state solution when the data flow stops (operationally,
between measurement updates), and because the PDE residual can stay low while the solution is wrong, a
residual-based health monitor can be fooled — silent, plausible, wrong. Compare against an established
numerical solver, and **validate at the deployment numerical precision** — an FP32 edge target can break
a PINN that was healthy in FP64.

**What stays independent.** The real instruments, the deterministic estimators (EKF/UKF/observers), and
the control loops that would otherwise use them. The soft sensor is a second opinion cross-checked
against measurements, not a replacement; the loop never closes on it.

**The seam and the contract.** The estimate crosses with an explicit uncertainty band and a freshness
bound; when it drifts out of the validated regime or disagrees with an independent measurement, it is
flagged and the operator falls back to the measured/deterministic value.

## 4. Read-only LLM copilot

**The job.** An LLM answers engineering and maintenance questions over the plant's own documentation,
alarms, history, and model evidence — and can draft procedures or code for a human to verify.

**The rung — advisory (level 2) for the copilot; offline (level 0) for any code it drafts.** It consumes
**curated, read-only** context through allow-listed tools, never raw tag streams, and holds **no write
access.** Drafted control code goes through grammar/compiler/formal verification with a human owner
before it is anything more — raw output is not a control artefact. The
[NIST AI RMF Generative AI Profile]({{ '/design/ai-integration/validation-lifecycle/' | relative_url }})
is the relevant companion, and confabulation (fluent, plausible, wrong output) is the failure mode to
design against.

**What stays independent.** Everything. The copilot cannot act; it can only inform. Its worst failure is
a wrong answer a reviewing engineer must catch — which is why every output is reviewed and every drafted
artefact verified before use.

**The seam and the contract.** Read-only, least-privilege access inside the OT security zones (NIST SP
800-82r3 placement); each answer cites the twin state, document, or model evidence it rests on, so a
human can check it. No proposal reaches the plant without schema validation, authorization, and — where
required — human confirmation.

## What the four share

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    subgraph LEARNED["Learned component — informs / proposes"]
      M["Vision · vibration · PINN · LLM<br/>result + confidence + version + freshness"]
    end
    subgraph GATE["Verified non-learned layer — decides / protects"]
      ENV["Envelope: fresh? in-distribution?<br/>confident? corroborated?"]
    end
    SAFE["Safety functions · interlocks · protection<br/>(independent of the learned path)"]
    ACT["Plant action"]
    M -->|gated contract| ENV
    ENV -->|"pass"| ACT
    ENV -.->|"stale / low-confidence:<br/>defined failure response"| ACT
    SAFE --> ACT
    classDef learned fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef verified fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e
    classDef safety fill:#faeeec,stroke:#a33327,color:#1e1e1e,stroke-width:2px
    classDef io fill:#f2f2ef,stroke:#a0a09a,color:#1e1e1e
    class M learned
    class ENV verified
    class SAFE safety
    class ACT io
</pre>
</div>

- **The ladder, not the model, sets the authority.** Three of the four top out at advisory; none holds a
  safety function; none closes a control loop on a learned estimate.
- **The non-learned envelope always holds the veto**, and the safety-function path never routes through
  the learned component.
- **The result crosses as a gated contract** — class/estimate, confidence/uncertainty, model version,
  timestamp, freshness — not a raw stream; a stale or low-confidence result triggers the defined
  response.
- **Authority is perishable** — each example depends on drift monitoring, honest (leakage-free,
  deployment-condition) validation, and a maintained
  [model-evidence ledger]({{ '/assets/templates/ai_model_evidence_ledger.md' | relative_url }}) to keep
  its rung.

## Review status

Distilled from a corpus-owned Draft note and **Review pending**. This page introduces no new technical
claims; it composes the positions verified across the section. Return to the
[authority gate]({{ '/design/ai-integration/' | relative_url }}), the
[method register]({{ '/design/ai-integration/method-register/' | relative_url }}), or any of
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}),
[Interfaces &amp; Handshakes]({{ '/design/ai-integration/interfaces/' | relative_url }}),
[Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }}),
[The Digital Twin]({{ '/design/ai-integration/digital-twin/' | relative_url }}), and
[Validation &amp; Lifecycle]({{ '/design/ai-integration/validation-lifecycle/' | relative_url }}).
