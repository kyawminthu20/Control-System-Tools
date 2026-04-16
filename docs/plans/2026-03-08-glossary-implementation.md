# Glossary Page Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a cross-linked glossary encyclopedia at `/tools/glossary/` covering ~30 key terms (SIL, PL, SCCR, AHJ, NEC, NFPA, etc.) with domain badges, standard page links, lifecycle stage links, and See Also cross-links.

**Architecture:** Term data lives in `docs/_data/glossary.yml` (one YAML block per term). The page `docs/glossary/index.md` renders all terms via Liquid — sorted alphabetically, grouped under A–Z letter anchors with a jump strip at the top. Each term block links to standard pages, lifecycle stages, and related terms within the glossary.

**Tech Stack:** Jekyll 4.2 · Liquid templating · vanilla CSS · `docs/_data/` pattern (same as any existing `_data/` files in the site)

---

## Task 1: Create `docs/_data/glossary.yml`

**Files:**
- Create: `docs/_data/glossary.yml`

**Step 1: Create the data file with all seed terms**

Create `docs/_data/glossary.yml` with the following content exactly — 30 terms covering all four domains. Order in the file does not matter; the page template will sort alphabetically by `acronym`.

```yaml
# Glossary term data
# Fields: term, acronym, domain, definition, standard_pages, lifecycle_stages, related_terms
# domain values: safety | electrical | standards-bodies | regulatory
# related_terms: list of acronym values that exist in this file

- term: Authority Having Jurisdiction
  acronym: AHJ
  domain: regulatory
  definition: >
    The organization, office, or individual responsible for enforcing the requirements
    of a code or standard, or their designated representative. In electrical work, the
    AHJ inspects and approves installations against the adopted edition of the NEC.
    The applicable AHJ varies by project location and system type — it may be a local
    building department, fire marshal, or federal agency such as OSHA.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
  lifecycle_stages:
    - slug: installation
      label: Installation
  related_terms:
    - NEC
    - OSHA

- term: Available Fault Current
  acronym: AFC
  domain: electrical
  definition: >
    The maximum short-circuit current available at a given point in an electrical
    system, expressed in amperes. Panel SCCR must meet or exceed the AFC at the
    installation point. AFC is determined from the utility transformer capacity
    and the impedance of all conductors between the transformer and the panel.
    Required for NEC Article 409 compliance.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
    - url: /standards/us-electrical/ul-508a/
      label: UL 508A
  lifecycle_stages:
    - slug: detailed-design
      label: Detailed Design
    - slug: installation
      label: Installation
  related_terms:
    - SCCR
    - AIC

- term: Ampere Interrupting Capacity
  acronym: AIC
  domain: electrical
  definition: >
    The maximum fault current a protective device (circuit breaker or fuse) can
    safely interrupt without damage or arcing. AIC must equal or exceed the AFC
    at the point of installation. Also referred to as Interrupting Rating (IR).
    Selecting protective devices with insufficient AIC is a common and serious
    NEC violation.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
    - url: /standards/us-electrical/ul-508a/
      label: UL 508A
  lifecycle_stages:
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - AFC
    - SCCR

- term: Safety Architecture Category
  acronym: Category
  domain: safety
  definition: >
    A classification (B, 1, 2, 3, 4) defined in ISO 13849-1 describing the structural
    and behavioral properties of a safety-related control system. Category B is the
    baseline; Category 4 requires dual-channel architecture with cross-monitoring and
    tolerance of any single fault. Category is one input to determining Performance
    Level — higher categories enable higher achievable PL.
  standard_pages:
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - PL
    - MTTFd
    - DC

- term: Conformité Européenne
  acronym: CE
  domain: regulatory
  definition: >
    A marking indicating that a product conforms to all applicable EU directives
    and regulations. For industrial machinery, CE marking requires compliance with
    the EU Machinery Directive (and soon the EU Machinery Regulation), which mandates
    a risk assessment per ISO 12100 and functional safety evaluation per ISO 13849-1
    or IEC 62061. CE marking is mandatory for placing machinery on the EU market.
  standard_pages:
    - url: /standards/machinery/iso-12100/
      label: ISO 12100
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
  lifecycle_stages:
    - slug: concept
      label: Concept
    - slug: risk-assessment
      label: Risk Assessment
  related_terms:
    - PL
    - SIL

- term: Diagnostic Coverage
  acronym: DC
  domain: safety
  definition: >
    The fraction of dangerous failures detected by automatic diagnostic tests,
    expressed as a percentage. Defined in ISO 13849-1 and IEC 61508. DC values
    are classified as None (<60%), Low (60–90%), Medium (90–99%), and High (≥99%).
    DC, MTTFd, and Category together determine the achievable Performance Level
    of a safety function.
  standard_pages:
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - PL
    - MTTFd
    - Category
    - SFF

- term: Emergency Stop
  acronym: E-stop
  domain: safety
  definition: >
    A safety function that brings a machine to a safe state as quickly as possible
    when activated. Defined in IEC 60204-1 and NFPA 79. Stop categories 0 (immediate
    power removal), 1 (controlled stop then power removal), and 2 (controlled stop,
    power maintained) determine how the drive system responds. E-stop circuits must
    be designed to achieve a required Performance Level per ISO 13849-1 or SIL per
    IEC 62061.
  standard_pages:
    - url: /standards/us-electrical/nfpa-79/
      label: NFPA 79
    - url: /standards/machinery/iec-60204-1/
      label: IEC 60204-1
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - PL
    - SIL
    - Category

- term: Hardware Fault Tolerance
  acronym: HFT
  domain: safety
  definition: >
    The number of faults a system can tolerate while maintaining its safety function.
    Defined in IEC 61508 and IEC 62061. HFT 0 means one fault causes loss of safety
    function; HFT 1 means two simultaneous faults are required to cause loss. Higher
    SIL levels require higher HFT, which typically means redundant (dual-channel)
    architecture.
  standard_pages:
    - url: /standards/functional-safety/iec-62061/
      label: IEC 62061
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - SIL
    - SFF
    - PFH

- term: International Electrotechnical Commission
  acronym: IEC
  domain: standards-bodies
  definition: >
    The international standards body responsible for electrotechnical standards,
    including IEC 61508 (functional safety), IEC 62061 (machinery functional safety),
    IEC 60204-1 (electrical equipment of machinery), IEC 61511 (process safety),
    and IEC 62443 (industrial cybersecurity). IEC standards are adopted by many
    national bodies, often with local modifications.
  standard_pages: []
  lifecycle_stages: []
  related_terms:
    - ISO

- term: International Organization for Standardization
  acronym: ISO
  domain: standards-bodies
  definition: >
    The international standards body responsible for standards such as ISO 12100
    (machine risk assessment), ISO 13849-1 (machinery safety — Performance Level),
    and many other engineering standards. ISO and IEC collaborate extensively on
    dual-logo standards in the functional safety domain.
  standard_pages: []
  lifecycle_stages: []
  related_terms:
    - IEC

- term: Layer of Protection Analysis
  acronym: LOPA
  domain: safety
  definition: >
    A semi-quantitative risk assessment method used to determine the required Safety
    Integrity Level (SIL) for safety instrumented functions. LOPA identifies
    independent protection layers (IPLs) between a hazard and its consequence,
    and calculates the risk reduction needed from the SIF. Commonly used in process
    industries in conjunction with IEC 61511.
  standard_pages:
    - url: /standards/functional-safety/iec-61511/
      label: IEC 61511
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: risk-assessment
      label: Risk Assessment
  related_terms:
    - SIL
    - SIS
    - SIF

- term: Mean Time To Dangerous Failure
  acronym: MTTFd
  domain: safety
  definition: >
    The average time until a component fails in a dangerous (undetected) way,
    expressed in years. Defined in ISO 13849-1. MTTFd is classified as Low (<10 yr),
    Medium (10–30 yr), and High (30–100 yr) per channel. Together with Category and
    Diagnostic Coverage, MTTFd determines the achievable Performance Level of a
    safety function.
  standard_pages:
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - PL
    - DC
    - Category
    - PFH

- term: National Electrical Code
  acronym: NEC
  domain: standards-bodies
  definition: >
    Published by NFPA as NFPA 70, the NEC is the primary electrical installation
    code enforced in the United States. It is adopted into law by most states and
    local jurisdictions and enforced by the AHJ. For industrial machinery, NEC
    Article 670 governs facility installation while NFPA 79 governs machine
    electrical design. Key industrial articles include 250, 409, 430, and 670.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
  lifecycle_stages:
    - slug: installation
      label: Installation
  related_terms:
    - NFPA
    - AHJ
    - SCCR

- term: National Fire Protection Association
  acronym: NFPA
  domain: standards-bodies
  definition: >
    A US standards organization that publishes the NEC (NFPA 70) and NFPA 79
    (Electrical Standard for Industrial Machinery), among hundreds of other codes
    and standards. NFPA standards are voluntary but are widely adopted into law
    by US jurisdictions. NFPA 79 is the primary standard for the electrical
    design of industrial machines sold in the US market.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
    - url: /standards/us-electrical/nfpa-79/
      label: NFPA 79
  lifecycle_stages: []
  related_terms:
    - NEC

- term: Occupational Safety and Health Administration
  acronym: OSHA
  domain: regulatory
  definition: >
    The US federal agency responsible for workplace safety regulations.
    OSHA 29 CFR 1910 (General Industry) and 1926 (Construction) reference
    electrical standards and machine guarding requirements. OSHA enforces
    the use of nationally recognized testing laboratory (NRTL) listed equipment
    in workplace installations, which drives UL listing requirements in practice.
  standard_pages: []
  lifecycle_stages: []
  related_terms:
    - AHJ
    - UL

- term: Performance Level
  acronym: PL
  domain: safety
  definition: >
    A discrete level (PL a–e) specifying the ability of a safety-related control
    system to perform its safety function under foreseeable conditions, as defined
    in ISO 13849-1. PL e provides the highest reliability. Required PL (PLr) is
    determined by risk assessment; achieved PL is calculated from Category, MTTFd,
    and Diagnostic Coverage. PL is the ISO 13849-1 equivalent of SIL in the
    IEC 62061 / IEC 61508 framework.
  standard_pages:
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
  lifecycle_stages:
    - slug: risk-assessment
      label: Risk Assessment
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - SIL
    - Category
    - MTTFd
    - DC

- term: Probability of Dangerous Failure per Hour
  acronym: PFH
  domain: safety
  definition: >
    The average probability of a safety function failing dangerously per hour of
    operation. Used in IEC 62061 and IEC 61508 to quantify SIL compliance for
    high-demand or continuous-demand safety functions. SIL 1 requires PFH < 10⁻⁵;
    SIL 3 requires PFH < 10⁻⁷. Component datasheets from safety device manufacturers
    provide PFH values for use in system calculations.
  standard_pages:
    - url: /standards/functional-safety/iec-62061/
      label: IEC 62061
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - SIL
    - HFT
    - SFF
    - MTTFd

- term: Programmable Logic Controller
  acronym: PLC
  domain: electrical
  definition: >
    An industrial digital computer designed for real-time control of manufacturing
    and automation processes. Standard PLCs are not rated for use in safety functions.
    Safety PLCs (also called safety controllers or FSCs) are designed and certified
    to IEC 61508 / IEC 62061 / ISO 13849-1 and are required for implementing
    safety-rated control functions at SIL 2–3 or PL d–e.
  standard_pages:
    - url: /standards/functional-safety/iec-62061/
      label: IEC 62061
    - url: /standards/functional-safety/iso-13849-1/
      label: ISO 13849-1
  lifecycle_stages:
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - SIL
    - PL
    - SIS

- term: Safe Failure Fraction
  acronym: SFF
  domain: safety
  definition: >
    The proportion of all failures that are either safe failures or dangerous detected
    failures, expressed as a percentage. Defined in IEC 61508. SFF ≥ 90% is typically
    required for SIL 2 subsystems with HFT 0; SFF ≥ 99% for SIL 3. SFF and HFT
    together determine the maximum SIL a subsystem can claim without architectural
    constraints.
  standard_pages:
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
    - url: /standards/functional-safety/iec-62061/
      label: IEC 62061
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - SIL
    - HFT
    - PFH

- term: Short-Circuit Current Rating
  acronym: SCCR
  domain: electrical
  definition: >
    The maximum short-circuit current a panel or assembly can withstand without
    damage, expressed in kA. Required to be marked on industrial control panels
    per NEC 409.110. Panel SCCR is determined by the lowest-rated component in
    the assembly, calculated using UL 508A Supplement SB. The marked SCCR must
    meet or exceed the AFC at the installation point — this is one of the most
    commonly failed NEC inspection points.
  standard_pages:
    - url: /standards/us-electrical/ul-508a/
      label: UL 508A
    - url: /standards/us-electrical/nec/
      label: NEC
  lifecycle_stages:
    - slug: detailed-design
      label: Detailed Design
    - slug: installation
      label: Installation
  related_terms:
    - AFC
    - AIC
    - AHJ

- term: Semiconductor Equipment and Materials International
  acronym: SEMI
  domain: standards-bodies
  definition: >
    An industry association that publishes safety standards for semiconductor
    manufacturing equipment. Key standards include SEMI S2 (environmental, health,
    and safety guidelines), SEMI S8 (ergonomics), and SEMI S14 (fire risk assessment).
    SEMI S2 compliance is required by most semiconductor fabs and is distinct from
    NEC, NFPA 79, and IEC standards, though it references many of them.
  standard_pages: []
  lifecycle_stages: []
  related_terms:
    - IEC
    - NEC

- term: Safety Instrumented Function
  acronym: SIF
  domain: safety
  definition: >
    A specific safety function implemented by a Safety Instrumented System (SIS)
    to bring a process to a safe state on demand. Each SIF has its own SIL target,
    determined by risk assessment (typically LOPA). A SIF consists of a sensor
    subsystem, logic solver, and final element subsystem, each contributing to
    the overall SIF PFD or PFH.
  standard_pages:
    - url: /standards/functional-safety/iec-61511/
      label: IEC 61511
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
    - slug: risk-assessment
      label: Risk Assessment
  related_terms:
    - SIL
    - SIS
    - LOPA
    - PFH

- term: Safety Integrity Level
  acronym: SIL
  domain: safety
  definition: >
    A discrete level (SIL 1–4) specifying the required risk reduction a safety
    function must achieve. Defined in IEC 61508 and applied to machinery in IEC 62061
    and to process safety in IEC 61511. Higher SIL levels require greater reliability,
    stricter architectural constraints, and more rigorous verification. SIL 4 is
    rare in practice; most industrial machinery targets SIL 1–3. SIL is the
    IEC 62061/61508 equivalent of Performance Level (PL) in ISO 13849-1.
  standard_pages:
    - url: /standards/functional-safety/iec-62061/
      label: IEC 62061
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
    - url: /standards/functional-safety/iec-61511/
      label: IEC 61511
  lifecycle_stages:
    - slug: risk-assessment
      label: Risk Assessment
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - PL
    - SL
    - HFT
    - SFF
    - PFH

- term: Safety Instrumented System
  acronym: SIS
  domain: safety
  definition: >
    An instrumented system used to implement one or more Safety Instrumented
    Functions (SIFs). A SIS consists of sensors, logic solvers (safety PLCs),
    and final elements (valves, shutdowns). Governed by IEC 61511 in the process
    industries. A SIS is independent of the Basic Process Control System (BPCS)
    and must be designed, tested, and maintained separately.
  standard_pages:
    - url: /standards/functional-safety/iec-61511/
      label: IEC 61511
    - url: /standards/functional-safety/iec-61508/
      label: IEC 61508
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
  related_terms:
    - SIL
    - SIF
    - LOPA
    - PLC

- term: Security Level
  acronym: SL
  domain: safety
  definition: >
    A discrete level (SL 1–4) defined in IEC 62443 specifying the required
    cybersecurity capability of an Industrial Automation and Control System (IACS).
    SL-T (Target) is determined by risk assessment; SL-C (Capability) is what
    a product or system can achieve. SL is conceptually analogous to SIL in
    functional safety, but addresses intentional cyber threats rather than
    random hardware failures.
  standard_pages:
    - url: /standards/cybersecurity/iec-62443/
      label: IEC 62443
  lifecycle_stages:
    - slug: safety-architecture
      label: Safety Architecture
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - SIL
    - PL

- term: Surge Protective Device
  acronym: SPD
  domain: electrical
  definition: >
    A device designed to protect electrical equipment from voltage transients caused
    by lightning, switching, or other disturbances. NEC 409.70 (2023) addresses SPD
    requirements for industrial control panels. SPDs are particularly important where
    safety relay modules, PLCs, or other sensitive electronics are housed in panels
    exposed to transient voltage events.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
  lifecycle_stages:
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - NEC
    - PLC

- term: Underwriters Laboratories
  acronym: UL
  domain: standards-bodies
  definition: >
    A Nationally Recognized Testing Laboratory (NRTL) that develops safety standards
    and certifies products. UL 508A is the standard for industrial control panels.
    UL listing is required by OSHA for equipment in US workplaces and is typically
    required by AHJs. UL 508A certification involves both the panel construction
    standard and Supplement SB for SCCR determination.
  standard_pages:
    - url: /standards/us-electrical/ul-508a/
      label: UL 508A
  lifecycle_stages:
    - slug: build
      label: Build
  related_terms:
    - SCCR
    - AHJ
    - OSHA

- term: Variable Frequency Drive
  acronym: VFD
  domain: electrical
  definition: >
    A power electronics device that controls AC motor speed by varying the frequency
    and voltage of the motor supply. Also called an adjustable speed drive (ASD) or
    inverter. VFDs introduce considerations for motor branch circuit protection
    (NEC Article 430), drive-rated conductors, and input harmonic filtering.
    Safety-rated stop functions on VFDs (STO, SS1, SS2) are covered in IEC 61800-5-2
    and may be used as part of a functional safety architecture.
  standard_pages:
    - url: /standards/us-electrical/nec/
      label: NEC
  lifecycle_stages:
    - slug: detailed-design
      label: Detailed Design
  related_terms:
    - PL
    - SIL
    - E-stop
```

**Step 2: Verify the file is valid YAML**

```bash
python3 -c "import yaml; data = yaml.safe_load(open('docs/_data/glossary.yml')); print(f'OK — {len(data)} terms loaded')"
```

Run from repository root: `./`

Expected output: `OK — 30 terms loaded`

**Step 3: Commit**

```bash
git add docs/_data/glossary.yml
git commit -m "feat(glossary): add glossary.yml data file with 30 seed terms"
```

---

## Task 2: Create `docs/glossary/index.md`

**Files:**
- Create: `docs/glossary/index.md`

**Step 1: Create the glossary page**

Create `docs/glossary/index.md` with the following content:

````markdown
---
layout: default
title: "Glossary"
description: "Definitions of key terms, acronyms, and abbreviations used in industrial control systems and machine safety standards."
breadcrumb:
  - name: "Reference"
  - name: "Glossary"
last_reviewed: "2026-03-08"
---

<div class="page-header">
  <span class="page-header__label">Reference</span>
  <h1>Glossary</h1>
  <p>Key terms, acronyms, and abbreviations used across industrial control systems, machine safety, and electrical standards.</p>
</div>

{% assign sorted_terms = site.data.glossary | sort: "acronym" %}

{% comment %}Build the set of first letters present{% endcomment %}
{% assign letters_present = "" %}
{% for entry in sorted_terms %}
  {% assign first = entry.acronym | slice: 0 | upcase %}
  {% unless letters_present contains first %}
    {% assign letters_present = letters_present | append: first | append: "," %}
  {% endunless %}
{% endfor %}
{% assign letter_list = letters_present | split: "," %}

<nav class="glossary-az" aria-label="Jump to letter">
{% for letter in letter_list %}{% if letter != "" %}<a href="#letter-{{ letter }}">{{ letter }}</a>{% endif %}{% endfor %}
</nav>

{% assign current_letter = "" %}
{% for entry in sorted_terms %}
{% assign first = entry.acronym | slice: 0 | upcase %}
{% if first != current_letter %}
  {% assign current_letter = first %}
  <h2 class="glossary-letter" id="letter-{{ first }}">{{ first }}</h2>
{% endif %}

<div class="glossary-entry" id="{{ entry.acronym | downcase | replace: ' ', '-' | replace: '/', '-' }}">
  <div class="glossary-entry__header">
    <span class="glossary-entry__acronym">{{ entry.acronym }}</span>
    <span class="glossary-entry__term">{{ entry.term }}</span>
    <span class="badge badge--domain badge--domain-{{ entry.domain }}">{{ entry.domain | replace: "-", " " }}</span>
  </div>
  <p class="glossary-entry__definition">{{ entry.definition }}</p>
  <dl class="glossary-entry__meta">
    {% if entry.standard_pages.size > 0 %}
    <dt>Standard</dt>
    <dd>{% for s in entry.standard_pages %}<a href="{{ s.url | relative_url }}">{{ s.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</dd>
    {% endif %}
    {% if entry.lifecycle_stages.size > 0 %}
    <dt>Lifecycle</dt>
    <dd>{% for stage in entry.lifecycle_stages %}<a href="{{ '/verification/lifecycle/' | append: stage.slug | append: '/' | relative_url }}">{{ stage.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</dd>
    {% endif %}
    {% if entry.related_terms.size > 0 %}
    <dt>See also</dt>
    <dd>{% for rel in entry.related_terms %}<a href="#{{ rel | downcase | replace: ' ', '-' | replace: '/', '-' }}">{{ rel }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</dd>
    {% endif %}
  </dl>
</div>
{% endfor %}
````

**Step 2: Verify Jekyll builds cleanly**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -6
```

Expected: `done in X seconds.` with no errors. Page count should increase by 1 (from 52 to 53).

**Step 3: Commit**

```bash
git add docs/glossary/index.md
git commit -m "feat(glossary): add glossary page with A-Z navigation and cross-links"
```

---

## Task 3: Add CSS for glossary components

**Files:**
- Modify: `docs/assets/css/main.css`

**Step 1: Append glossary styles to `main.css`**

Add the following block at the end of `docs/assets/css/main.css`:

```css
/* --- Glossary ------------------------------------------------------------- */
.glossary-az {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 0.5rem;
  padding: 0.75rem 0;
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
  margin-bottom: 2rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.glossary-az a {
  color: var(--color-accent);
  font-weight: 600;
  text-decoration: none;
  padding: 0.1em 0.3em;
}

.glossary-az a:hover {
  text-decoration: underline;
}

.glossary-letter {
  font-family: var(--font-mono);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-muted);
  border-bottom: 1px solid var(--color-border);
  margin: 2rem 0 1rem;
  padding-bottom: 0.25rem;
}

.glossary-entry {
  margin-bottom: 1.75rem;
  padding: 1rem 1.25rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
}

.glossary-entry__header {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}

.glossary-entry__acronym {
  font-family: var(--font-mono);
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-fg);
}

.glossary-entry__term {
  font-size: 0.9rem;
  color: var(--color-muted);
}

.glossary-entry__definition {
  margin: 0.5rem 0 0.75rem;
  font-size: 0.92rem;
  line-height: 1.6;
}

.glossary-entry__meta {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 0.2rem 1rem;
  font-size: 0.82rem;
  margin: 0;
}

.glossary-entry__meta dt {
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--color-muted);
  white-space: nowrap;
}

.glossary-entry__meta dd {
  margin: 0;
}

.glossary-entry__meta a {
  color: var(--color-accent);
  text-decoration: none;
}

.glossary-entry__meta a:hover {
  text-decoration: underline;
}

/* Domain badge variants */
.badge--domain {
  font-size: 0.62rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.badge--domain-safety {
  color: #1a5c8a;
  border-color: #4a8cba;
  background: #eef5fb;
}

.badge--domain-electrical {
  color: #5a3a00;
  border-color: #8a6a00;
  background: #fdfae8;
}

.badge--domain-standards-bodies {
  color: #1a6b1a;
  border-color: #4a9a4a;
  background: #f0faf0;
}

.badge--domain-regulatory {
  color: #5a1a6b;
  border-color: #8a4a9a;
  background: #faf0fd;
}
```

**Step 2: Verify build is still clean**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -4
```

Expected: clean build, no errors.

**Step 3: Commit**

```bash
git add docs/assets/css/main.css
git commit -m "feat(glossary): add glossary CSS — A-Z strip, entry cards, domain badges"
```

---

## Task 4: Add Glossary to sidebar

**Files:**
- Modify: `docs/_includes/sidebar.html`

**Step 1: Add the Glossary link**

In `docs/_includes/sidebar.html`, find the Reference section:

```html
    <summary>Reference</summary>
    <ul class="sidebar__links">
      <li><a href="{{ '/design/software-stack/' | relative_url }}">Software Stack</a></li>
      <li><a href="{{ '/repository/about/' | relative_url }}">About / Trust Boundary</a></li>
    </ul>
```

Replace with:

```html
    <summary>Reference</summary>
    <ul class="sidebar__links">
      <li><a href="{{ '/design/software-stack/' | relative_url }}">Software Stack</a></li>
      <li><a href="{{ '/tools/glossary/' | relative_url }}">Glossary</a></li>
      <li><a href="{{ '/repository/about/' | relative_url }}">About / Trust Boundary</a></li>
    </ul>
```

**Step 2: Verify build and sidebar renders correctly**

```bash
cd docs && bundle exec jekyll build 2>&1 | tail -4
```

Then confirm the sidebar link appears in the built HTML:

```bash
grep -c "glossary" docs/_site/index.html
```

Expected: `1` or more (link appears in sidebar on every page).

**Step 3: Commit**

```bash
git add docs/_includes/sidebar.html
git commit -m "feat(glossary): add Glossary link to sidebar Reference section"
```

---

## Task 5: Update project state

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

**Step 1: Add Phase 6 to `project_state/project_state.md`**

Add the following section after the Phase 5 scope block:

```markdown
## Phase 6 Scope — Glossary — COMPLETED

**Rationale:** Engineers using the site encounter terms (SIL, PL, SCCR, AHJ, HFT, SFF, MTTFd)
across multiple pages with no single reference point. A cross-linked glossary closes this gap.

- [x] `docs/_data/glossary.yml` — 30 seed terms across Safety, Electrical, Standards Bodies, Regulatory domains
- [x] `docs/glossary/index.md` — rendered page with A-Z anchor strip, domain badges, standard links, lifecycle links, See Also cross-links
- [x] `docs/assets/css/main.css` — glossary entry card styles and domain badge variants
- [x] `docs/_includes/sidebar.html` — Glossary added to Reference section
- [x] Jekyll build clean — 53 pages
```

**Step 2: Add entry to `project_state/change_log.md`**

Add after the most recent change log entry:

```markdown
### 2026-03-08: Glossary Page Added

**Type:** Content / Reference
**Status:** Complete

- Added `docs/_data/glossary.yml` with 30 seed terms (SIL, PL, SL, SCCR, AHJ, HFT, SFF, MTTFd, DC, Category, PFH, PLC, SIS, SIF, LOPA, E-stop, AFC, AIC, VFD, SPD, NEC, NFPA, UL, IEC, ISO, SEMI, AHJ, CE, OSHA)
- Added `docs/glossary/index.md` — A-Z anchor navigation, domain badges, cross-links to standard pages, lifecycle stages, and related terms
- Added glossary card CSS and domain badge color variants to `main.css`
- Added Glossary to Reference section in sidebar
- Build: 53 pages, clean
```

**Step 3: Commit**

```bash
git add project_state/project_state.md project_state/change_log.md
git commit -m "chore(state): update project state for Phase 6 glossary"
```
