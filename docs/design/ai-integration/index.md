---
layout: default
title: "AI & ML Integration"
description: "The authority gate for putting a model in a control system: how much the plant may act on a model's output, and what independent protection stays effective when it is wrong."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
review:
  standard: "Project evidence register"
  edition: "Phase 49a findings, 2026-07-13"
  status: "Review pending"
  coverage: "Phase 49b method register; chemical and biological authority evidence remains open"
  last_reviewed: "2026-07-13"
repo_path: "control-standards/rag/design_framework/ai_integration/methods.yml"
related_standards:
  - name: "ISO 13849-1 — safety functions"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061 — safety functions"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511 — process safety (SIS)"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508 — E/E/PE lifecycle"
    url: "/standards/functional-safety/iec-61508/"
  - name: "IEC 62443 — OT cybersecurity"
    url: "/standards/cybersecurity/iec-62443/"
  - name: "Software Stack & Cybersecurity"
    url: "/design/software-stack/"
lifecycle_stage:
  - name: "Risk Assessment"
    slug: "risk-assessment"
  - name: "Safety Architecture"
    slug: "safety-architecture"
  - name: "Detailed Design"
    slug: "detailed-design"
---

{% assign register = site.data.ai_methods.methods %}

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>AI &amp; ML Integration — the authority gate</h1>
  <p>Start with the decision and its allowed authority—not the model. Every method must beat a named deterministic alternative, survive validation, and fail without defeating independent protection. This page is the gate; the <a href="{{ '/design/ai-integration/method-register/' | relative_url }}">method register</a> and the pages below are scored against it.</p>
</div>

> **Safety boundary:** no learned method in this register is assigned direct closed-loop authority
> (level 5) or a safety function. “Planned” means the evidence supports discussing the method, but
> does not yet support an operational authority claim. For *why* a learned component cannot hold a
> safety function today — the deterministic standards, the guidance-only AI documents, and the EU law
> that already caps it — see [Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}).

## The idea in plain terms

“AI/ML integration” in industrial automation means putting a model — something that classifies,
estimates, predicts, or optimises from data — somewhere in the path between plant measurements and
plant actions. The engineering question is not whether the model is impressive; it is how much the
plant is allowed to act on the model’s output without a person or an independent check in between.
This page calls that permission **authority**, and grades every method by the highest authority the
evidence currently supports.

Two kinds of method appear throughout:

- A **deterministic method** computes the same answer from the same inputs by an explicit,
  inspectable rule — PID control, a Kalman filter, an interlock, a mass balance. Its behaviour can
  be verified.
- A **learned method** gets its behaviour from training data — a neural network, a boosted tree, a
  reinforcement-learning policy, an LLM. Its behaviour can be tested, but not exhaustively
  verified, and it can fail in unfamiliar conditions without signalling that it has.

That difference is why this page keeps repeating three demands: a method must **beat a named
deterministic alternative** (otherwise use the simpler thing), it must **survive validation**
designed to catch its specific failure modes, and **independent protection** must keep the plant
safe when it is wrong.

### Terms used throughout

| Term | Meaning here |
|---|---|
| Authority | The highest level of plant action allowed on a method’s output. |
| Deterministic method | Rule-based, verifiable computation (PID, interlock, balance, solver). |
| Learned method | Behaviour comes from training data; testable, not exhaustively verifiable. |
| Must beat | The named simpler method a candidate has to demonstrably outperform. |
| Envelope | Hard limits (range, rate, task space) enforced outside the learned method. |
| Veto | The non-learned check that can reject or replace any proposed action. |
| Independent protection | Interlocks and safety functions that still work when the model is wrong. |
| Safety function | Risk reduction implemented and verified per ISO 13849-1 / IEC 62061 / IEC 61511. |
| Planned | Evidence supports discussing the method, not an operational authority claim. |

## The question to answer before proceeding

**What decision will this method influence, at what maximum authority, and what independent
protection stays effective when its result is wrong, stale, unavailable, or compromised?**

If those three parts cannot be answered and tested, keep the method offline. If a deterministic
alternative meets the requirement, prefer it unless the proposed method demonstrates a specific,
validated advantage.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A{"Can you answer and test all three?<br/>the decision it will influence · its maximum authority ·<br/>the independent protection that stays effective when the result<br/>is wrong, stale, unavailable, or compromised"}
    A -->|No| E["Keep the method offline<br/>authority 0"]
    A -->|Yes| B{"Does a deterministic<br/>alternative meet the requirement?"}
    B -->|Yes| C{"Specific, validated advantage<br/>demonstrated over that alternative?"}
    C -->|No| D["Use the deterministic method<br/>(the register's 'must beat' baseline)"]
    C -->|Yes| F{"Survives the register's validation<br/>requirements for this method?"}
    B -->|No| F
    F -->|No| E
    F -->|Yes| G["Assign the lowest authority level<br/>that delivers the claimed value"]
    G --> H{"Learned method?"}
    H -->|Yes| I["Ceiling: level 4 — bounded supervisory.<br/>The safety function stays in a<br/>verified non-learned layer"]
    H -->|No| J["Authority per validation evidence<br/>and the applicable safety lifecycle"]
    classDef q fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef stop fill:#faeeec,stroke:#a33327,color:#1e1e1e
    classDef go fill:#eef4ed,stroke:#3a6b35,color:#1e1e1e
    classDef warn fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e
    class A,B,C,F,H q
    class E stop
    class D,J go
    class I warn
    class G q
</pre>
</div>

## Authority ladder

Authority is climbed, not granted — each level up demands more evidence. The diagram is generated
from the same register data as the table below it.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart BT
{% for item in register.authority_levels %}    L{{ item.level }}["<b>{{ item.level }} · {{ item.label }}</b><br/>{{ item.meaning }}"]
{% endfor %}    L0 --> L1 --> L2 --> L3 --> L4
    L4 -.->|"no learned method is assigned level 5 in this register"| L5
    classDef ok fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef ceiling fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e,stroke-width:2px
    classDef reserved fill:#faeeec,stroke:#a33327,color:#1e1e1e,stroke-dasharray:5 4,stroke-width:2px
    class L0,L1,L2,L3 ok
    class L4 ceiling
    class L5 reserved
    linkStyle 4 stroke:#a33327,stroke-width:2px
</pre>
</div>

<div class="table-scroll" markdown="1">

| Level | Name | Meaning |
|---:|---|---|
{% for item in register.authority_levels %}| {{ item.level }} | **{{ item.label }}** | {{ item.meaning }} |
{% endfor %}
</div>

Level 4 is not permission for learned safety control. It means bounded supervisory action inside
independently implemented constraints and vetoes. Project risk assessment, applicable standards,
verification, cybersecurity, and management of change still apply.

Level 4 here is an architectural **ceiling** for a learned method placed behind an independently
verified envelope — not an authority any learned row is currently assigned. Every method presently
at level 4 in the register (Kalman filter, model predictive control, first-principles numerical
model) is deterministic or model-based; no learned row in this register exceeds level 3.

### One task up the ladder

To make the levels concrete, here is the same job — condition monitoring and control on a critical
pump — at every level. The scenario is illustrative; each level names a method that can actually
hold that level in this register.

<div class="table-scroll" markdown="1">

| Level | What it looks like on the pump |
|---:|---|
| 0 · Offline | Exported vibration data is analysed at a desk; findings go into a report. Nothing on the plant changes. |
| 1 · Read-only | A live dashboard shows spectra and health indicators. People look; nothing acts. |
| 2 · Advisory | A diagnosis model (a 1D CNN, for example) flags “bearing wear likely — inspect at next stop.” A person decides. This is the register’s current ceiling for learned diagnosis. |
| 3 · Operator-approved | The system prepares a specific action — reduce speed to 80 % — and it runs only after the operator confirms it. |
| 4 · Bounded supervisory | A model predictive controller trims the flow setpoint on its own, but only inside hard limits and rate clamps enforced by logic it cannot modify. |
| 5 · Direct closed-loop | The PID loop holding the flow — deterministic, verified control acting every scan. No learned method is assigned this level here. |

</div>

## The envelope architecture

In plain terms: the model may adjust how the plant runs, inside a fence it cannot move — and
keeping the plant safe does not depend on the model at any point. This is the pattern the
register's placement and independent-protection fields point at: the learned policy holds
operational authority inside an envelope; a verified non-learned layer holds the safety function
and the veto. The safety-function path never routes through the learned layer.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    S["Sensors /<br/>process state"]
    subgraph LL["Learned layer — operational authority ≤ 4 (architectural ceiling)"]
      M["Learned policy<br/>(model, optimiser, soft sensor)"]
    end
    subgraph VL["Verified non-learned layer — holds the safety function"]
      ENV["Envelope check<br/>range · rate · task space<br/>freshness · plausibility"]
      VETO["Veto / clamp /<br/>defined failure response"]
    end
    SIS["Safety functions<br/>ISO 13849-1 · IEC 62061 · IEC 61511<br/>(independent of everything above)"]
    ACT["Actuators"]
    S --> M
    M -->|"proposal +<br/>result contract"| ENV
    ENV -->|in envelope| VETO
    ENV -.->|"out of envelope:<br/>reject, alarm, log"| VETO
    VETO --> ACT
    S --> SIS
    SIS --> ACT
    classDef learned fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef verified fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e
    classDef safety fill:#faeeec,stroke:#a33327,color:#1e1e1e,stroke-width:2px
    classDef io fill:#f2f2ef,stroke:#a0a09a,color:#1e1e1e
    class M learned
    class ENV,VETO verified
    class SIS safety
    class S,ACT io
</pre>
</div>

The veto layer as code. On a failed check it applies the application's **hazard-analysis-derived
failure response** — which may be bumpless transfer to a base controller, a controlled hold with a
bounded lifetime, manual takeover, a defined safe state, or shutdown. A deterministic fallback is
more amenable to specification and verification, but it is not automatically safe: the correct
response is whatever the risk assessment requires for that loop.

```python
# Verified, non-learned layer. Runs unchanged when the model misbehaves.
# on_fail() is the application's hazard-analysis-derived response, NOT a
# universal default — bumpless transfer, bounded-lifetime hold, manual
# takeover, a defined safe state, or shutdown, per the risk assessment.
def gate(proposal: Setpoint, state: PlantState) -> Setpoint:
    if not fresh(proposal, max_age_ms=500):
        alarm("model result stale")
        return on_fail(state, reason="stale")
    if not in_task_space(proposal, ENVELOPE):
        alarm("proposal outside envelope")          # the envelope vetoes every
        return on_fail(state, reason="out_of_envelope")  # unsafe or out-of-scope action
    return clamp(proposal, RATE_LIMIT, RANGE_LIMIT)
# The safety functions (e-stop, interlocks, SIF) do not pass through here.
# They act on the actuators regardless of what this gate returns.
```

## Method register

The full comparison — **42 methods across nine families**, each with the deterministic alternative
it must beat, its authority ceiling, required validation, and failure modes — now lives on its own
page so it can be scanned by problem type without scrolling past the gate above.

**→ [Open the AI &amp; ML Method Register]({{ '/design/ai-integration/method-register/' | relative_url }})** — the full family-by-family comparison.

Every row is scored against the ladder and the envelope architecture on this page: no learned method
is assigned level 5 or a safety function, and chemical and biological rows remain Planned.

## Model families and fit

The register scores individual methods; the families behind them — convolutional/temporal perception,
physics-informed networks, and large language models — each have a genuine fit and a poor fit that is
easy to miss. A CNN belongs on an advisory, not a trip; a PINN belongs on inverse problems, not a
control-loop estimator; an LLM belongs behind a compiler and a human owner, not in the loop.

**→ [Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }})** shows
each family as capability *and* poor fit, including the train/test-leakage trap in the fault-diagnosis
literature and the FP64/FP32 precision trap that can break a PINN on edge hardware.

## The digital twin as integration spine

The working architecture is a synchronized twin with these model families hanging off it — not "AI
wired to a PLC." The twin is where the models live; it grants none of them authority. A live data
mirror (one-way synchronization) is not a behavioural twin, and getting data *in* honestly is a
different problem from letting the twin act *out*.

**→ [The Digital Twin]({{ '/design/ai-integration/digital-twin/' | relative_url }})** grounds the twin
vs data-mirror distinction in ISO 23247, treats the physical-to-digital and digital-to-physical
directions as separate problems, and shows the device-communication seam still gated by the envelope.

## Validation, drift, and the model lifecycle

The authority a method holds is perishable: a learned model degrades as the plant drifts away from what
it learned, and nothing about its output announces the change. So authority must be re-earned — data
lineage, honest test sets, uncertainty, drift detection, a defined failure response, rollback, and
change control — or dropped when the evidence lapses.

**→ [Validation &amp; Lifecycle]({{ '/design/ai-integration/validation-lifecycle/' | relative_url }})**
maps those demands onto the NIST AI RMF Govern/Map/Measure/Manage functions (with the Generative AI
Profile for LLM components) and provides a downloadable
[model-evidence ledger]({{ '/assets/templates/ai_model_evidence_ledger.md' | relative_url }}).

## Interfaces and high-rate data

Analyse the fast signal where it is measured; send the verdict — not the waveform — across the
network. Neither OPC UA nor Sparkplug assigns an AI result a standard meaning or authority, so the
inference service stays **publish-only** and you define the result contract explicitly.

**→ [Interfaces &amp; Handshakes]({{ '/design/ai-integration/interfaces/' | relative_url }})** covers
the four constraints that put inference at the edge (not "the protocol is too slow"), what OPC UA and
Sparkplug do and do not give you, write-authority separation via the OPC UA Observer role, and the
result-contract payload.

## Domain limits

- **Chemical and process models:** conservation is a hard engineering check; kinetics, equilibrium,
  transport closures, and properties still need application-specific validation. Their authority rows
  remain Planned.
- **Biological models:** classical PI/PID, recipes, and open-loop feed profiles are the reality
  baseline. Advanced models and soft sensors remain research or pilot patterns here, not authority
  claims.
- **PINNs:** compare against established numerical solvers. Low training loss is not evidence of a
  correct field, parameter, boundary condition, or safe extrapolation.
- **Generated code and agentic workflows:** remain offline drafts. Compilation is necessary but does
  not establish requirement completeness, correct abnormal behaviour, or safety suitability.

## Review status

This page is generated from a corpus-owned Draft register and is **Review pending**. It is intended to
make the next engineering question explicit, not to replace hazard analysis, detailed design review,
or the applicable safety and cybersecurity lifecycle.
