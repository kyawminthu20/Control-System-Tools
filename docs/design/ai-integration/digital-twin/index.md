---
layout: default
title: "The Digital Twin as Integration Spine"
description: "What a digital twin is versus a live data mirror (ISO 23247), why physical-to-digital and digital-to-physical are separate problems, and how the authority gate still governs anything the twin's models feed back to the plant."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Digital Twin"
review:
  standard: "ISO 23247 (Digital Twin Framework for Manufacturing); NIST SP 800-82r3"
  edition: "ISO 23247 Parts 1–4:2021, Part 5:2026 (Part 5 existence/title/date re-confirmed at the ISO catalogue July 2026); definition and functional twin ladder verified via NIST government publication (ISO body not read)"
  status: "Review pending"
  coverage: "Twin vs data mirror, physical/digital directions, digital-to-physical authority ladder, twin maturity ladder M0–M4 (functional progression cited to NIST; synchronization grading is project engineering judgement), data contract, model families in the twin. Chemical and biological twins out of scope."
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/digital_twin.md"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "Model Families & Fit"
    url: "/design/ai-integration/model-families/"
  - name: "Interfaces & Handshakes"
    url: "/design/ai-integration/interfaces/"
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
  <h1>The Digital Twin as Integration Spine</h1>
  <p>The working architecture is not "AI wired to a PLC" — it is a synchronized twin with models hanging off it. The twin is where the models live; it grants none of them authority. A live data mirror is not a behavioural twin, and the two synchronization directions are separate engineering problems.</p>
</div>

This page is part of the [AI &amp; ML Integration]({{ '/design/ai-integration/' | relative_url }})
section; read the [authority gate]({{ '/design/ai-integration/' | relative_url }}) first. The twin
does not relax any ceiling in the [method register]({{ '/design/ai-integration/method-register/' | relative_url }})
or any boundary in [Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}):
a learned model inside a twin holds exactly the authority the register assigns it, and no safety
function routes through the twin. Review pending.

## What a digital twin is — and the distinction that matters

A published framework already defines the term. **ISO 23247 (Digital Twin Framework for Manufacturing)**
defines a digital twin as a *"fit for purpose digital representation of an observable manufacturing
element with synchronization between the element and its digital representation."* Two words carry the
weight: **synchronization** (the digital side is kept current with the physical side) and **fit for
purpose** (the twin is scoped to a use case, not a general-purpose replica).

The distinction the rest of this page turns on is the *direction and richness* of that synchronization:

- **A live data mirror** — dashboards, tags, historian trends — has **one-way** synchronization: it
  receives data and shows it. It is useful, and it is not a behavioural twin. (Long-standing jet-engine
  monitoring "twins" receive data from the physical object but give no control feedback — one-way
  synchronization.)
- **A behavioural twin** adds asset identity and relationships, calibrated behavioural models
  (estimation, simulation, prediction, diagnosis, optimisation), lifecycle history, and validated use
  cases on top of the synchronized state. It answers "what is happening that I cannot measure" and
  "what happens next," not only "what does the sensor read."

A dashboard becomes more twin-like as it gains those properties — it is a spectrum, not a badge.

> **Honest caveat.** The field has no single agreed definition. ISO 23247 is a *manufacturing*
> framework and a reference architecture — **not** a functional-safety or model-validation standard.
> Synchronization is not authority: being current says nothing about being correct, and nothing in ISO
> 23247 lets a learned model hold a safety function. (The ISO body was not read; the definition and
> reference model here are verified via a NIST government publication that cites the standard.)

## The framework's shape — named seams, not a product

ISO 23247 is a **four-part series (2021)** — Part 1 overview, Part 2 reference architecture, Part 3
digital representation, Part 4 information exchange — extended by Part 5:2026 (digital thread). Its
reference model is organised as four domains, and the seam that matters for AI safety is the one that
can turn a digital output into a physical action.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TB
    subgraph OME["Observable manufacturing domain"]
      P["Equipment · material · process · personnel<br/>(the thing being twinned)"]
    end
    subgraph DC["Device communication domain — the seam that matters"]
      SYNC["Data exchange + synchronization<br/>…and command / actuation signals"]
    end
    subgraph DT["Digital twin domain"]
      STATE["Synchronized state + models<br/>(CNN · PINN · LLM)"]
    end
    subgraph USER["User domain"]
      U["Applications · operators"]
    end
    P -->|"physical → digital<br/>(telemetry)"| SYNC
    SYNC --> STATE
    STATE --> U
    STATE -.->|"digital → physical<br/>(gated by the envelope)"| SYNC
    SYNC -.->|"approved / bounded action"| P
    X["Cross-system entity<br/>data translation · assurance · security"]
    X -.- DC
    classDef phys fill:#f2f2ef,stroke:#a0a09a,color:#1e1e1e
    classDef seam fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e,stroke-width:2px
    classDef digi fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    class P phys
    class SYNC seam
    class STATE,U digi
    class X phys
</pre>
</div>

The **device communication domain** carries data exchange *and synchronization*, and — the standard is
explicit — also transfers commands and signals for control and actuation. That is where the authority
question lives, and where the [interfaces & result contract]({{ '/design/ai-integration/interfaces/' | relative_url }})
mechanics apply.

## Two directions, two different problems

Treating "the twin" as one bidirectional pipe hides the two hardest questions. Split it.

**Physical-to-digital — getting the twin honest.** This is a data-integrity problem, not a modelling
one: identify each input's asset/unit/range/meaning; preserve source and acquisition timestamps,
quality, and missing-data state; align to scan, trigger, batch, recipe, and mode; **reject or mark**
stale, substituted, frozen, impossible, and out-of-sequence data; record which twin values are
**measured, derived, or predicted** — never let a prediction silently read as a measurement; and
monitor residuals and drift between predicted and observed state.

**Digital-to-physical — letting the twin act, carefully.** A twin's model output is not privileged by
living in a twin. It is capped at the register ceiling for that model family, and an independent
non-learned layer holds the veto:

<div class="table-scroll" markdown="1">

| Level | Twin / model output | Control-system treatment |
|---:|---|---|
| 0 | Offline analysis | No online interface |
| 1 | Monitoring result | Read-only visualisation and logging |
| 2 | Advisory recommendation | Operator evaluates and acts separately |
| 3 | Proposed command / setpoint | Operator confirms through a governed workflow |
| 4 | Bounded supervisory output | A non-learned layer independently checks enable, range, rate, mode, freshness, permissives |
| 5 | Direct learned control | Not assigned to any learned twin output here |

</div>

Regardless of level, independent trips, interlocks, safety functions, equipment limits, and manual
fallback stay effective when the twin or its models are **wrong, stale, unavailable, or compromised**.
This is the same [envelope architecture]({{ '/design/ai-integration/' | relative_url }}#the-envelope-architecture)
as the gate — the twin is where the models live; the envelope is still what protects the plant.

## Twin maturity — a ladder of synchronization, not authority

Two different questions get confused whenever someone calls a twin "advanced". *Maturity* describes how
much the twin computes and how tightly it tracks the plant. *Authority* describes what the plant lets its
output do. **They are orthogonal, and only one of them is a permission.** A maximally mature twin holds
exactly the authority the [method register]({{ '/design/ai-integration/' | relative_url }}) assigns its
composing models — advisory for twin state synchronization, read-only for the physics-informed families
feeding it. Nothing on this page raises a ceiling.

The functional progression below is **NIST's published five-category twin ladder** (descriptive →
diagnostic → predictive → prescriptive → intelligent, ordered by "increasing complexity, more decision
support, and greater value"). The **synchronization grading** — what the data link and state estimation
actually do at each level — is this project's engineering judgement, not any standard's; no standard we
have read defines a graded synchronization scale. M0 sits *below* NIST's scale, which presumes a live twin.

<div class="table-scroll" markdown="1">

| Level | Name | Synchronization character | What it answers | Prerequisites | NIST category |
|---|---|---|---|---|---|
| **M0** | Offline model | No live link; snapshot or historical data | "What would happen, in principle?" | Step 1 | *(below NIST's scale)* |
| **M1** | Connected shadow | One-way, live telemetry inbound; no return path | "What happened, or is happening?" | Steps 1–4 | Descriptive |
| **M2** | Synchronized twin | State estimation reconciles model with plant; measured / derived / predicted labelled distinctly | "What is wrong, and why?" | Steps 1–6 | Diagnostic |
| **M3** | Predictive twin | Validated forward prediction over a stated horizon, with residual and drift monitoring | "What is likely to happen?" | Steps 1–7 | Predictive |
| **M4** | Bounded closed-loop twin | Twin output crosses the seam under the full gated envelope | "How can we make it happen?" | Steps 1–7, the data contract, and an independent non-learned gate | Prescriptive / Intelligent |

</div>

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    M0["M0<br/>Offline model<br/><i>no live link</i>"]
    M1["M1<br/>Connected shadow<br/><i>one-way telemetry</i>"]
    M2["M2<br/>Synchronized twin<br/><i>reconciled state</i>"]
    M3["M3<br/>Predictive twin<br/><i>validated horizon</i>"]
    M4["M4<br/>Bounded closed-loop<br/><i>described, not authorized</i>"]
    M0 --> M1 --> M2 --> M3
    M3 -.-> M4
    GATE["Authority is set by the method register at every level —<br/>maturity is never an authority argument"]
    GATE -.- M2
    classDef live fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef off fill:#f2f2ef,stroke:#a0a09a,color:#1e1e1e
    classDef future fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e,stroke-width:2px,stroke-dasharray:4 3
    classDef note fill:#ffffff,stroke:#a0a09a,color:#4a4a4a
    class M0 off
    class M1,M2,M3 live
    class M4 future
    class GATE note
</pre>
</div>

**M4 is described here, not authorized.** No method row grants a twin-composed learned output more than
advisory authority, so reaching M4 needs a new evidence case at the register — not a reinterpretation of
this page. The published ladder agrees: NIST states intelligent twins are *"envisaged to"* control their
physical counterparts, in the future tense. The internal register and the external source describe the
top rung the same way — somewhere the field intends to go, not somewhere it is.

Two rules follow. **Declare the target maturity per use case at concept design**, and refuse features
belonging to a higher level than the data-integrity work supports — a twin asked for M3 answers on M1
plumbing is not ambitious, it is unvalidated. And **a maturity claim never appears in an authority
argument**: "the twin is mature enough to close the loop" is not an engineering statement. The register
row is the only authority statement, and it is reached through evidence, not capability.

## The data contract across the seam

Because the device-communication seam can carry an action, its payload must be self-describing enough to
be *gated*: asset and signal identifiers; a request/correlation ID; source and inference timestamps;
input and output quality; value, class, prediction horizon, and uncertainty; model, feature-pipeline,
and calibration versions; a valid-until / maximum-age; twin synchronization state; service health and
fallback state; the **requested authority level and action type**; and acknowledgment, rejection
reason, and audit identity. The last items are what let a verifiable non-learned layer accept, clamp,
or veto a proposal — and let an audit reconstruct the decision afterwards.

## The model families inside the twin

The twin is a spine; the models hanging off it are the same families the register scores, at the same
ceilings (see [Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }})):

- **CNN / perception** turns images, thermal frames, and 1-D signals into features or classes —
  advisory only; a classification must not silently become a plant fact.
- **PINN / physics models** connect sparse measurements to unmeasured state (parameter/field estimation,
  calibration, surrogates) — the physics term constrains learning but does not prove accuracy, stability,
  real-time performance, or validity outside the calibrated regime; never close a loop on it.
- **LLM / knowledge** operates over the twin's semantic and historical context through read-only,
  allow-listed tools — curated twin context, not raw tag streams, with schema validation and (where
  required) human confirmation on any proposal.

## What this means for design

- **Say which state is measured, inferred, simulated, or manually entered**, and keep predictions
  visibly distinct from measurements in the twin's own state.
- **Design the two directions separately** — solve staleness, aliasing, and provenance on the way in
  before trusting any model output on the way out.
- **The twin grants no authority.** A model's rung comes from the register and the safety boundary, not
  from living in a twin; the device-communication seam is gated by the non-learned envelope.
- **Match synchronization tightness and prediction horizon to the process**, and define what happens
  when AI output is late, missing, low-confidence, or contradictory.
- **Own model change control** — who approves a model change, and who approves a change to its allowed
  authority, before either happens.

## Review status

Distilled from a corpus-owned Draft note and **Review pending**. The twin definition and reference
model are grounded in ISO 23247 (verified via a NIST government publication; the ISO body was not read).
Return to the [authority gate]({{ '/design/ai-integration/' | relative_url }}),
[Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }}),
[Interfaces &amp; Handshakes]({{ '/design/ai-integration/interfaces/' | relative_url }}), or
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}).
