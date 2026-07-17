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
> does not yet support an operational authority claim.

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

## Interface rule for high-rate data

In plain terms: analyse the fast signal where it is measured, and send the verdict — not the
waveform — across the network. Do not assume a conventional PLC scan → embedded OPC UA server →
historian polling path can reconstruct a kHz waveform. Perform high-rate acquisition and inference where the signal is sampled,
then publish the lower-rate result with its class or estimate, confidence or uncertainty, model
version, timestamp, quality, and freshness. OPC UA PubSub/TSN can support different architectures;
the limitation is the chosen acquisition path, not OPC UA as a whole.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    subgraph BAD["✗ This acquisition path cannot reconstruct a kHz waveform"]
      direction LR
      V1["Vibration sensor<br/>sampled at kHz"] --> P1["Conventional PLC scan<br/>(ms-class)"] --> O1["Embedded OPC UA server<br/>sampling floor · no knowledge of the<br/>source's update logic, so the waveform<br/>cannot be recovered by oversampling"] --> H1["Historian polling<br/>+ compression by design"]
    end
    subgraph GOOD["✓ Acquire and infer where the signal is sampled"]
      direction LR
      V2["Vibration sensor<br/>sampled at kHz"] --> EDGE["Edge acquisition<br/>+ inference at the source"] --> R["Result contract<br/>class · confidence · model version<br/>timestamp · quality · freshness"] --> O2["OPC UA / Sparkplug<br/>publish at process rate"] --> C2["PLC / SCADA /<br/>historian"]
    end
    classDef bad fill:#faeeec,stroke:#a33327,color:#1e1e1e
    classDef good fill:#eef4ed,stroke:#3a6b35,color:#1e1e1e
    classDef neutral fill:#f2f2ef,stroke:#a0a09a,color:#1e1e1e
    class V1,P1,O1,H1 bad
    class EDGE,R,O2 good
    class V2,C2 neutral
</pre>
</div>

Network segmentation between the cell and supervisory layers constrains the same path further:
publishing a compact result crosses zone boundaries on terms a raw waveform stream does not.

OPC UA and Sparkplug provide transport and state mechanisms, but neither gives an AI result a
standard semantic meaning or authority. Define and test that application contract explicitly.
As a payload, the required fields look like this:

```json
{
  "result":        "bearing_outer_race_fault",
  "confidence":    0.87,
  "model_version": "vib-cnn 2.3.1",
  "timestamp_utc": "2026-07-16T09:41:07Z",
  "quality":       "GOOD",
  "freshness_ms":  250
}
```

Two optional fields strengthen the contract: a training-set identifier makes drift auditable, and
an explicit authority tag lets consumers enforce the ceiling at the point of use.

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
