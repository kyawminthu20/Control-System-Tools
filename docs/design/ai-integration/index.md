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

## Authority ladder

<div class="table-scroll" markdown="1">

| Level | Name | Meaning |
|---:|---|---|
{% for item in register.authority_levels %}| {{ item.level }} | **{{ item.label }}** | {{ item.meaning }} |
{% endfor %}
</div>

Level 4 is not permission for learned safety control. It means bounded supervisory action inside
independently implemented constraints and vetoes. Project risk assessment, applicable standards,
verification, cybersecurity, and management of change still apply.

## Method register

Use the family sections to scan by problem type. Each entry puts the poor-fit and failure cases beside
the claimed value so method selection does not become a capability catalogue.

{% assign families = "classical-deterministic,estimation,optimisation,perception,physics-informed,language/agentic,interface,chemical-kinetic,biological" | split: "," %}
{% for family in families %}
### {{ family | replace: "-", " " | capitalize }}

{% assign family_methods = register.methods | where: "family", family %}
{% for item in family_methods %}
<details class="method-register-entry">
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

OPC UA and Sparkplug provide transport and state mechanisms, but neither gives an AI result a
standard semantic meaning or authority. Define and test that application contract explicitly.

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
