---
layout: default
title: "AI Validation, Drift & Model Lifecycle"
description: "What has to stay true over time for a learned component to keep its authority — data lineage, honest test sets, uncertainty, drift/OOD detection, a defined failure response, rollback, and change control — with the NIST AI RMF vocabulary and a downloadable model-evidence ledger."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Validation & Lifecycle"
review:
  standard: "NIST AI RMF 1.0 (AI 100-1); NIST AI RMF Generative AI Profile (AI 600-1); NIST SP 800-82r3"
  edition: "AI RMF 1.0 (Jan 2023); GenAI Profile (26 Jul 2024, verified at publisher)"
  status: "Review pending"
  coverage: "Lifecycle demands mapped to Govern/Map/Measure/Manage; drift/OOD; failure response; rollback; model-evidence ledger template. NIST AI RMF framed as process guidance, not safety permission."
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/validation_lifecycle.md"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "Model Families & Fit"
    url: "/design/ai-integration/model-families/"
  - name: "The Digital Twin"
    url: "/design/ai-integration/digital-twin/"
  - name: "Safety & Security Boundaries"
    url: "/design/ai-integration/safety-boundaries/"
  - name: "Engineering Templates"
    url: "/tools/templates/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design"
  - name: "Commissioning"
    slug: "commissioning"
  - name: "Operations & Maintenance"
    slug: "operations-maintenance"
---

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>Validation, Drift &amp; Model Lifecycle</h1>
  <p>A learned component is not validated once and finished. Its authority is only as current as the last evidence that it still behaves — so the lifecycle, not the commissioning test, is the point.</p>
</div>

This page is part of the [AI &amp; ML Integration]({{ '/design/ai-integration/' | relative_url }})
section; read the [authority gate]({{ '/design/ai-integration/' | relative_url }}) first. Everything the
register grants a method is **conditional on the work below**. The frameworks named here are process
guidance, not functional-safety permission — none lets a learned component hold a safety function (see
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }})).
Review pending.

## Why the lifecycle is the point

A learned model's behaviour comes from training data, so it degrades as the plant, sensors, product,
and environment drift away from what it learned. A model that was advisory-grade at commissioning can
silently become worse than useless a year later, and **nothing about its output announces the change.**
So the authority a method holds is perishable: it must be re-earned, or dropped when the evidence
lapses. The lifecycle is the mechanism that keeps the authority claim honest.

## The vocabulary: NIST AI Risk Management Framework

Two published NIST documents give this work a shared, non-proprietary vocabulary — used here for
**structure**, not as evidence that a model may hold authority:

- **NIST AI RMF 1.0 (NIST AI 100-1, Jan 2023)** organises AI risk work around four functions —
  **Govern, Map, Measure, Manage** — and a set of trustworthiness characteristics. Voluntary guidance.
- **NIST AI RMF: Generative AI Profile (NIST AI 600-1, 26 Jul 2024)** is a *"cross-sectoral profile of
  and companion resource for the AI RMF 1.0"* (verified at NIST) — it does not replace it. It adds
  generative-AI-specific risks (for example **confabulation** — plausible, fluent, wrong output — plus
  information integrity, data privacy, and information security) and is the relevant companion whenever
  an **LLM** is in the architecture.

## The lifecycle demands, mapped to the four functions

<div class="table-scroll" markdown="1">

| Function | What it demands of a learned component |
|---|---|
| **Govern** | A named owner for the model and its authority; management of change on every retrain, update, or authority change; an audit trail that can reconstruct a decision from data, version, context, and human action. |
| **Map** | Data lineage (provenance, licence, collection conditions); the validated operating envelope and the known-invalid regimes; coupling and interface ownership inside a twin. |
| **Measure** | Leakage-free test sets split by held-out *component*, not window; uncertainty reported with every output; validation at the **deployment** conditions — hardware and numerical precision, not only the bench. |
| **Manage** | Drift / out-of-distribution monitoring against the validated envelope; a defined, hazard-analysis-derived failure response; retained, re-deployable model versions for fast rollback; human review on a cadence and on every anomaly. |

</div>

Two of these carry traps documented elsewhere in this section. **Measure:** split by held-out
components — window-level or by-load splits inflate fault-diagnosis accuracy to near-100% while the
honest number is near chance (see [Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }})).
**Manage:** a residual monitor is necessary but not sufficient — a PINN can relax to a plausible, wrong
state while its residual stays low, so independent cross-checks matter.

## The failure response is the envelope's job

When the model is stale, low-confidence, out-of-distribution, unavailable, or contradicted, the
**non-learned envelope** applies the hazard-analysis-derived response — never a universal default. This
is the same envelope as the [gate page]({{ '/design/ai-integration/' | relative_url }}#the-envelope-architecture):

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    R["Model result<br/>+ confidence · version · freshness"] --> C{"Fresh? in-distribution?<br/>confident? corroborated?"}
    C -->|Yes| USE["Use at the allowed authority level"]
    C -->|No| FR["on_fail — hazard-analysis-derived"]
    FR --> O1["Bumpless transfer to base controller"]
    FR --> O2["Bounded-lifetime hold"]
    FR --> O3["Manual takeover"]
    FR --> O4["Defined safe state / shutdown"]
    RB["Rollback to last known-good version"] -.-> R
    classDef q fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef go fill:#eef4ed,stroke:#3a6b35,color:#1e1e1e
    classDef warn fill:#fdf6e3,stroke:#8b6914,color:#1e1e1e
    class C q
    class USE go
    class FR,O1,O2,O3,O4 warn
    class RB warn
</pre>
</div>

## The model-evidence ledger

The durable artefact of all of the above is a per-component **model-evidence ledger** — one record that
makes a learned component's evidence auditable in one place: domain and phenomenon; governing
assumptions and boundary conditions; parameters and their sources; datasets with licence and
provenance; calibration and uncertainty; resolution; coupling and interface ownership; solver and
deployment precision; validation experiments and acceptance limits; known-invalid regimes and fallback
behaviour; and model version, authority level, owner, and change history.

**→ [Download the AI / model evidence ledger]({{ '/assets/templates/ai_model_evidence_ledger.md' | relative_url }})**
— a blank, fill-in template (also on the [Engineering Templates]({{ '/tools/templates/' | relative_url }})
page). Start it at design time and maintain it across the model's life, rather than reconstructing it
after an incident.

## What this means for design

- **Treat authority as perishable** — schedule revalidation, monitor drift, and drop the authority when
  the evidence lapses.
- **Split test sets by component, carry uncertainty, and validate at deployment conditions** — bench
  accuracy is not field accuracy.
- **Wire the failure response into the non-learned envelope**, hazard-analysis-derived, and keep every
  model version rollback-ready.
- **Keep a model-evidence ledger from day one**, and put model changes through management of change.
- **Use NIST AI RMF for structure and vocabulary** (and the GenAI Profile for any LLM component) —
  remembering it is process guidance, not a route to safety authority.

## Review status

Distilled from a corpus-owned Draft note and **Review pending**. NIST AI RMF is framed as process
vocabulary, not safety permission. Return to the [authority gate]({{ '/design/ai-integration/' | relative_url }}),
[Model Families &amp; Fit]({{ '/design/ai-integration/model-families/' | relative_url }}),
[The Digital Twin]({{ '/design/ai-integration/digital-twin/' | relative_url }}), or
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}).
