---
layout: default
title: "AI & ML Integration Method Register"
description: "Authority-first comparison of classical, learned, interface, chemical, and biological methods for control-system work."
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
---

{% assign register = site.data.ai_methods.methods %}
{% assign sources = site.data.ai_methods.sources.sources %}

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>AI &amp; ML Integration Method Register</h1>
  <p>Start with the decision and its allowed authority—not the model. Every method must beat a named deterministic alternative, survive validation, and fail without defeating independent protection.</p>
</div>

> **Safety boundary:** no learned method in this register is assigned direct closed-loop authority
> (level 5) or a safety function. “Planned” means the evidence supports discussing the method, but
> does not yet support an operational authority claim.

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

## The envelope architecture

The pattern the register's placement and independent-protection fields point at: the learned policy
holds operational authority inside an envelope; a verified non-learned layer holds the safety
function and the veto. The safety-function path never routes through the learned layer.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    S["Sensors /<br/>process state"]
    subgraph LL["Learned layer — operational authority ≤ 4"]
      M["Learned policy<br/>(model, optimiser, soft sensor)"]
    end
    subgraph VL["Verified non-learned layer — holds the safety function"]
      ENV["Envelope check<br/>range · rate · task space<br/>freshness · plausibility"]
      VETO["Veto / clamp /<br/>deterministic fallback"]
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

The veto layer as code. On any failed check it falls back to the deterministic baseline the method
had to beat — the register guarantees one exists for every entry:

```python
# Verified, non-learned layer. Runs unchanged when the model misbehaves.
def gate(proposal: Setpoint, state: PlantState) -> Setpoint:
    if not fresh(proposal, max_age_ms=500):
        alarm("model result stale")
        return baseline.compute(state)      # deterministic fallback, not hold-last
    if not in_task_space(proposal, ENVELOPE):
        alarm("proposal outside envelope")  # the envelope vetoes every
        return baseline.compute(state)      # unsafe or out-of-scope action
    return clamp(proposal, RATE_LIMIT, RANGE_LIMIT)
# The safety functions (e-stop, interlocks, SIF) do not pass through here.
# They act on the actuators regardless of what this gate returns.
```

## Method register

Use the family sections to scan by problem type. Each family opens with a comparison table; the
entries below it put the poor-fit and failure cases beside the claimed value so method selection
does not become a capability catalogue.

**Maturity** describes deployment reality: *industrially routine* (widely deployed practice),
*piloted* (documented industrial pilots), *research* (literature and lab evidence only).
**Evidence strength** names the best available source class for the row: *standards body*,
*peer-reviewed*, *preprint*, *mixed*, or *engineering judgement*.

{% assign families = "classical-deterministic,estimation,optimisation,perception,physics-informed,language/agentic,interface,chemical-kinetic,biological" | split: "," %}
{% for family in families %}
### {{ family | replace: "-", " " | capitalize }}

{% assign family_methods = register.methods | where: "family", family %}
<div class="table-scroll" markdown="1">

| Method | Max authority | Must beat | Maturity |
|---|---|---|---|
{% for item in family_methods %}| [{{ item.method }}](#{{ item.method | slugify }}) | {% if item.max_authority == "Planned" %}Planned{% else %}≤ {{ item.max_authority }}{% endif %} | {{ item.deterministic_alternative }} | {{ item.maturity }} |
{% endfor %}
</div>
{% if family == "perception" %}
> **Split your data the way the plant is split.** Random train/test splits overstate perception
> performance. Leakage in some form — label, future, or normal-data contamination — appears in
> this family's failure modes, and each row's validation names the matching leakage-aware split:
> asset-held-out, lot-held-out, or a temporal split with a leakage audit.
{% endif %}
{% for item in family_methods %}
<details class="method-register-entry" id="{{ item.method | slugify }}">
  <summary><strong>{{ item.method }}</strong> — authority {% if item.max_authority == "Planned" %}Planned{% else %}≤ {{ item.max_authority }}{% endif %} · {{ item.maturity }}</summary>

  <dl>
    <dt>Computes</dt><dd>{{ item.does }}</dd>
    <dt>Placement</dt><dd>{{ item.layer }}</dd>
    <dt>Must beat</dt><dd>{{ item.deterministic_alternative }}</dd>
    <dt>Use when</dt><dd>{{ item.justified_when }}</dd>
    <dt>Poor fit when</dt><dd>{{ item.poor_fit_when }}</dd>
    <dt>Data burden</dt><dd>{{ item.data_requirement }}</dd>
    <dt>Authority basis</dt><dd>{{ item.authority_basis }}</dd>
    <dt>Validation</dt><dd>{{ item.validation_required }}</dd>
    <dt>Failure modes</dt><dd>{{ item.failure_modes }}</dd>
    <dt>Independent protection</dt><dd>{{ item.safety_independence }}</dd>
    <dt>Evidence / maturity</dt><dd>{{ item.evidence_strength }} / {{ item.maturity }}</dd>
    <dt>Sources</dt>
    <dd>
      {% for source_id in item.sources %}
        {% assign matched = sources | where: "id", source_id | first %}
        {% if matched.url %}{% if matched.url contains "://" %}<a href="{{ matched.url }}">{{ matched.title }}</a>{% else %}<a href="{{ matched.url | relative_url }}">{{ matched.title }}</a>{% endif %}{% else %}{{ matched.title }}{% endif %}{% unless forloop.last %}; {% endunless %}
      {% endfor %}
    </dd>
  </dl>
</details>
{% endfor %}
{% endfor %}

## Interface rule for high-rate data

Do not assume a conventional PLC scan → embedded OPC UA server → historian polling path can
reconstruct a kHz waveform. Perform high-rate acquisition and inference where the signal is sampled,
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
