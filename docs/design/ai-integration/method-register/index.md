---
layout: default
title: "AI & ML Method Register"
description: "Authority-first comparison of 42 classical, learned, interface, chemical, and biological methods — each with the deterministic alternative it must beat, its authority ceiling, validation, and failure modes."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Method Register"
review:
  standard: "Project evidence register"
  edition: "Phase 49a findings, 2026-07-13"
  status: "Review pending"
  coverage: "Phase 49b method register; chemical and biological authority evidence remains open"
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/methods.yml"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "ISO 13849-1 — safety functions"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 61511 — process safety (SIS)"
    url: "/standards/functional-safety/iec-61511/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design"
---

{% assign register = site.data.ai_methods.methods %}
{% assign sources = site.data.ai_methods.sources.sources %}

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>AI &amp; ML Method Register</h1>
  <p>Forty-two methods, compared by the decision they influence and the authority the evidence supports — not by capability. Read the <a href="{{ '/design/ai-integration/' | relative_url }}">authority gate</a> first; it defines the ladder and the envelope this table is scored against.</p>
</div>

> **Safety boundary:** no learned method in this register is assigned direct closed-loop authority
> (level 5) or a safety function. “Planned” means the evidence supports discussing the method, but
> does not yet support an operational authority claim. The safety-function path never routes through
> a learned layer — see the [safety boundary]({{ '/design/ai-integration/' | relative_url }}#the-envelope-architecture).

## How to read the register

Use the family sections to scan by problem type. Each family opens with a comparison table; the
entries below it put the poor-fit and failure cases beside the claimed value so method selection
does not become a capability catalogue.

**How to read an entry.** Every entry answers the same questions, in the same order: what
it computes; a concrete example; where it runs; the simpler method it must beat; when it earns its
place; when it does not; how much data it needs; why its authority is capped where it is; the tests
it must pass; how it fails; what keeps the plant safe anyway; and how strong the evidence is. If an
entry's "poor fit" line describes your situation, the answer is usually the entry's own "must beat"
method. The example lines are illustrative — a typical use that stays within the method's stated
scope, not a documented deployment or an endorsement of a specific product.

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
    <dt>Example</dt><dd><em>{{ item.example }}</em></dd>
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

This register is generated from a corpus-owned Draft register and is **Review pending**. It is a
decision aid to make the next engineering question explicit — it does not replace hazard analysis,
detailed design review, or the applicable safety and cybersecurity lifecycle. Return to the
[authority gate]({{ '/design/ai-integration/' | relative_url }}) for the ladder, the pre-flight
question, and the envelope architecture every row is scored against.
