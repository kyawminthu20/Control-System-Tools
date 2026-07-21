---
layout: home
title: "Home"
description: "Route from your project, lifecycle stage, or market to the standards, workflows, and training that apply."
review_exempt: "navigation hub (home layout) — decision claims link to the reviewed source pages that hold the governed metadata"
---

<section class="home-hero">
  <span class="home-hero__label">Control Systems Engineering Field Guide</span>
  <h1 class="home-hero__title">Find the right standards path for your machine, panel, or safety system.</h1>
  <p class="home-hero__subtitle">
    Practical standards guidance, design workflows, commissioning references, and engineering
    tools for industrial automation. Start from your project type, lifecycle stage, or market —
    an independent educational reference, not a substitute for the published standards or your
    authority having jurisdiction.
  </p>
  <div class="home-hero__ctas">
    <a href="{{ '/tools/standards-finder/' | relative_url }}" class="hero__cta">Find applicable standards &rarr;</a>
    <a href="{{ '/tools/scenarios/' | relative_url }}" class="hero__cta hero__cta--secondary">Start with a scenario &rarr;</a>
    <a href="{{ '/fundamentals/' | relative_url }}" class="hero__cta hero__cta--secondary">Learn fundamentals &rarr;</a>
  </div>
</section>

<section class="home-section">
  <h2>Start here</h2>
  <p class="home-section__intro">Pick the card that best describes what you are doing right now. Each one routes to the right reference, workflow, or module.</p>

  <div class="start-grid">
    <a class="start-card" href="{{ '/tools/standards-finder/' | relative_url }}">
      <span class="start-card__label">Decision</span>
      <span class="start-card__title">I need applicable standards</span>
      <span class="start-card__desc">Pick the scenario closest to your project — region, equipment class, and risk profile already mapped to a standards stack.</span>
      <span class="start-card__next">Open the Standards Finder &rarr;</span>
    </a>

    <a class="start-card" href="{{ '/tools/scenarios/us-industrial-control-panel/' | relative_url }}">
      <span class="start-card__label">Scenario 01</span>
      <span class="start-card__title">I'm building a US control panel</span>
      <span class="start-card__desc">UL 508A + NEC Article 409 + NFPA 79. Construction, listing, and legal baseline in one walk-through.</span>
      <span class="start-card__next">Open the scenario &rarr;</span>
    </a>

    <a class="start-card" href="{{ '/tools/scenarios/global-machine/' | relative_url }}">
      <span class="start-card__label">Scenario 02</span>
      <span class="start-card__title">I'm designing a machine for US + EU</span>
      <span class="start-card__desc">NFPA 79 for the US, IEC 60204-1 for the EU, ISO 12100 as the risk-assessment foundation. Where they overlap and where they don't.</span>
      <span class="start-card__next">Open the scenario &rarr;</span>
    </a>

    <a class="start-card" href="{{ '/lifecycle/safety-architecture/' | relative_url }}">
      <span class="start-card__label">Safety</span>
      <span class="start-card__title">I need safety architecture guidance</span>
      <span class="start-card__desc">PL (ISO 13849-1) vs SIL (IEC 62061 / 61511), dual-channel patterns, STO/SS1/SLS, category selection.</span>
      <span class="start-card__next">Open the safety architecture stage &rarr;</span>
    </a>

    <a class="start-card" href="{{ '/tools/troubleshooting/' | relative_url }}">
      <span class="start-card__label">Field</span>
      <span class="start-card__title">I'm troubleshooting or commissioning</span>
      <span class="start-card__desc">Motor, VFD, and servo troubleshooting trees; commissioning checklists; field-engineering references.</span>
      <span class="start-card__next">Open troubleshooting &rarr;</span>
    </a>

    <a class="start-card" href="{{ '/fundamentals/' | relative_url }}">
      <span class="start-card__label">Learning</span>
      <span class="start-card__title">I want training and fundamentals</span>
      <span class="start-card__desc">50+ modules across electrical fundamentals, motors and drives, NEC application, control systems, and safety.</span>
      <span class="start-card__next">Open training &rarr;</span>
    </a>
  </div>
</section>

<section class="home-section">
  <h2>Common engineering scenarios</h2>
  <p class="home-section__intro">The quickest route into the atlas is an end-to-end worked example. Each scenario names the standards stack, the rationale, and the lifecycle path.</p>

  <div class="scenario-grid">
    <div class="scenario-card">
      <span class="scenario-card__num">Scenario 01</span>
      <span class="scenario-card__title">US Industrial Control Panel</span>
      <p class="scenario-card__start"><strong>Start with:</strong> UL 508A + NEC Article 409 + NFPA 79</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">US market, UL listing required. NEC is the legal baseline, UL 508A governs panel construction and listing, NFPA 79 applies when the panel sits on a machine.</p>
      <a href="{{ '/tools/scenarios/us-industrial-control-panel/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
    </div>

    <div class="scenario-card">
      <span class="scenario-card__num">Scenario 02</span>
      <span class="scenario-card__title">Global Machine (US + EU)</span>
      <p class="scenario-card__start"><strong>Start with:</strong> NFPA 79 (US) + IEC 60204-1 (EU) + ISO 12100</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Machine sold in both markets — design to the most restrictive rule from each. EU machinery law requires a documented risk assessment and compliance with the applicable essential health and safety requirements. EN ISO 12100 is the harmonized methodology commonly used to perform and document it — voluntary, but conferring presumption of conformity for the requirements it covers.</p>
      <a href="{{ '/tools/scenarios/global-machine/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
    </div>

    <div class="scenario-card">
      <span class="scenario-card__num">Scenario 03</span>
      <span class="scenario-card__title">Process Skid Shutdown System</span>
      <p class="scenario-card__start"><strong>Start with:</strong> IEC 61511 + IEC 61508 foundation</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">SIS / ESD for process industry. IEC 61511 is the application standard; IEC 61508 is the lifecycle foundation. <span class="badge badge--reviewed">Reviewed</span></p>
      <a href="{{ '/tools/scenarios/process-skid/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
    </div>

    <div class="scenario-card">
      <span class="scenario-card__num">Scenario 04</span>
      <span class="scenario-card__title">Networked Safety PLC Architecture</span>
      <p class="scenario-card__start"><strong>Start with:</strong> ISO 13849-1 or IEC 62061 + IEC 62443</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Safety PLC with network connectivity. Safety function design per PL or SIL path; cybersecurity overlay per IEC 62443.</p>
      <a href="{{ '/tools/scenarios/networked-safety-plc/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
    </div>

    <div class="scenario-card">
      <span class="scenario-card__num">Scenario 05</span>
      <span class="scenario-card__title">Semiconductor Equipment Compliance</span>
      <p class="scenario-card__start"><strong>Start with:</strong> 15-Standard Minimum Compliance Stack</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Complex compliance stack for fab equipment. SEMI S2/S8/S14 in the reference library alongside the industry overlay.</p>
      <a href="{{ '/tools/scenarios/semiconductor-equipment/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
    </div>
  </div>

  <p style="margin-top:1rem;"><a href="{{ '/tools/scenarios/' | relative_url }}">All scenarios &rarr;</a></p>
</section>

<section class="home-section">
  <h2>Browse by lifecycle stage</h2>
  <p class="home-section__intro">A structured lifecycle from concept through operation and management of change — each page lists the standards and outputs that apply.</p>

  <div class="lifecycle-ribbon">
    <a href="{{ '/lifecycle/concept/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">01</span>
      <span class="lifecycle-stage__name">Concept</span>
      <span class="lifecycle-stage__std">ISO 12100</span>
    </a>
    <a href="{{ '/lifecycle/standards-selection/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">02</span>
      <span class="lifecycle-stage__name">Standards Selection</span>
      <span class="lifecycle-stage__std">Decision map</span>
    </a>
    <a href="{{ '/lifecycle/risk-assessment/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">03</span>
      <span class="lifecycle-stage__name">Risk Assessment</span>
      <span class="lifecycle-stage__std">ISO 12100 · 61511</span>
    </a>
    <a href="{{ '/lifecycle/safety-architecture/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">04</span>
      <span class="lifecycle-stage__name">Safety Architecture</span>
      <span class="lifecycle-stage__std">13849 · 62061</span>
    </a>
    <a href="{{ '/lifecycle/detailed-design/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">05</span>
      <span class="lifecycle-stage__name">Detailed Design</span>
      <span class="lifecycle-stage__std">NFPA 79 · UL 508A</span>
    </a>
    <a href="{{ '/lifecycle/draft-documentation/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">06</span>
      <span class="lifecycle-stage__name">Documentation</span>
      <span class="lifecycle-stage__std">All applicable</span>
    </a>
    <a href="{{ '/lifecycle/build/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">07</span>
      <span class="lifecycle-stage__name">Build</span>
      <span class="lifecycle-stage__std">UL 508A · NFPA 79</span>
    </a>
    <a href="{{ '/lifecycle/installation/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">08</span>
      <span class="lifecycle-stage__name">Installation</span>
      <span class="lifecycle-stage__std">NEC · NFPA 79</span>
    </a>
    <a href="{{ '/lifecycle/pre-commissioning/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">09</span>
      <span class="lifecycle-stage__name">Pre-Commissioning</span>
      <span class="lifecycle-stage__std">13849 Annex K</span>
    </a>
    <a href="{{ '/lifecycle/commissioning/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">10</span>
      <span class="lifecycle-stage__name">Commissioning</span>
      <span class="lifecycle-stage__std">FAT / SAT / V&amp;V</span>
    </a>
    <a href="{{ '/lifecycle/maintenance/' | relative_url }}" class="lifecycle-stage">
      <span class="lifecycle-stage__num">11</span>
      <span class="lifecycle-stage__name">Maintenance</span>
      <span class="lifecycle-stage__std">13849 §10</span>
    </a>
  </div>
</section>

<section class="home-section home-explore">
  <h2>Explore the field guide</h2>
  <p class="home-section__intro">Beyond the entry routes above: browse by standards family or
  industry overlay, or open the power-user views of the underlying reference library.</p>

<div class="home-explore__block">
  <h3>Browse by standards family</h3>
  <p class="home-section__intro">Already know which family applies? Jump straight in.</p>

  <div class="card-grid">
    <div class="card">
      <span class="card__label">US Electrical</span>
      <span class="card__title">NEC · NFPA 79 · UL 508A</span>
      <p class="card__desc">US-market rules for industrial control panels and machinery electrical design. NEC is legally enforced; UL 508A covers panel listing.</p>
      <a href="{{ '/standards/us-electrical/' | relative_url }}" class="card__link">View family &rarr;</a>
    </div>

    <div class="card">
      <span class="card__label">International Machinery</span>
      <span class="card__title">IEC 60204-1</span>
      <p class="card__desc">Electrical equipment of machines for CE-marked and global markets. Equivalent scope to NFPA 79 outside the US.</p>
      <a href="{{ '/standards/machinery/' | relative_url }}" class="card__link">View family &rarr;</a>
    </div>

    <div class="card">
      <span class="card__label">Functional Safety</span>
      <span class="card__title">ISO 12100 · 13849-1 · IEC 62061 · 61508 · 61511</span>
      <p class="card__desc">Risk assessment and safety function design. PL path via ISO 13849-1; SIL path via IEC 62061 or IEC 61511 for process.</p>
      <a href="{{ '/standards/functional-safety/' | relative_url }}" class="card__link">View family &rarr;</a>
      <span class="badge badge--reviewed">Reviewed</span>
    </div>

    <div class="card">
      <span class="card__label">Software &amp; Cybersecurity</span>
      <span class="card__title">IEC 61131-3 · IEC 62443</span>
      <p class="card__desc">PLC programming languages and safety software lifecycle. Industrial cybersecurity series for networked control systems.</p>
      <a href="{{ '/design/software-stack/' | relative_url }}" class="card__link">Routing guide &rarr;</a>
    </div>

    <div class="card">
      <span class="card__label">Crosswalks</span>
      <span class="card__title">NFPA 79 ↔ IEC 60204-1 · UL 508A / NEC overlap</span>
      <p class="card__desc">Side-by-side comparison tables mapping clause equivalencies between US and international standards.</p>
      <a href="{{ '/tools/crosswalks/' | relative_url }}" class="card__link">View crosswalks &rarr;</a>
    </div>

    <div class="card">
      <span class="card__label">Reference Models</span>
      <span class="card__title">7-Layer Architecture · Safety Architecture · 15-Standard Stack</span>
      <p class="card__desc">Cross-cutting reference models: machine architecture layers, universal safety architecture, semiconductor compliance stack.</p>
      <a href="{{ '/design/software-stack/' | relative_url }}" class="card__link">View reference &rarr;</a>
    </div>
  </div>
</div>

<div class="home-explore__block">
  <h3>Browse by industry</h3>
  <p class="home-section__intro">Every industry has an overlay that narrows the general standards. Six of the most common — see the full list on the industries page.</p>

  <div class="industry-tiles">
    <a class="industry-tile" href="{{ '/industries/semiconductor/' | relative_url }}">
      <span class="industry-tile__name">Semiconductor</span>
      <span class="industry-tile__meta">SEMI S2/S8/S14 · fab facility reference</span>
    </a>
    <a class="industry-tile" href="{{ '/industries/petroleum/' | relative_url }}">
      <span class="industry-tile__name">Oil &amp; Gas</span>
      <span class="industry-tile__meta">IEC 61511 · IEC 60079 hazardous area</span>
    </a>
    <a class="industry-tile" href="{{ '/industries/energy/' | relative_url }}">
      <span class="industry-tile__name">Energy</span>
      <span class="industry-tile__meta">SIL · IEC 62443 cybersecurity</span>
    </a>
    <a class="industry-tile" href="{{ '/industries/food-and-beverage/' | relative_url }}">
      <span class="industry-tile__name">Food &amp; Beverage</span>
      <span class="industry-tile__meta">Hygienic design · washdown</span>
    </a>
    <a class="industry-tile" href="{{ '/industries/water-wastewater/' | relative_url }}">
      <span class="industry-tile__name">Water &amp; Wastewater</span>
      <span class="industry-tile__meta">IEC 61511 · AWWA · ISA-18.2</span>
    </a>
    <a class="industry-tile" href="{{ '/industries/offshore/' | relative_url }}">
      <span class="industry-tile__name">Offshore &amp; Marine</span>
      <span class="industry-tile__meta">Class rules · IEC 61511</span>
    </a>
  </div>

  <p style="margin-top:1rem;"><a href="{{ '/industries/' | relative_url }}">All 9 industry overlays &rarr;</a></p>
</div>

<details class="home-deep-dive">
  <summary>For power users — standards graph and source browser</summary>

  <div class="home-explore__block" style="margin-top:1.5rem;">
    <h3 style="font-size:1.1rem;">Standards relationship graph</h3>
    <p class="home-section__intro">Interactive map of how standards reference and depend on each other.</p>
    <p><a href="{{ '/standards/graph/' | relative_url }}">Open the full graph &rarr;</a></p>
  </div>

  <div class="home-explore__block">
    <h3 style="font-size:1.1rem;">Source material</h3>
    <p class="home-section__intro">
      Every page is backed by the project's reference library of clause-level source notes.
      Browse the raw notes in the <a href="{{ '/tools/rag-browser/' | relative_url }}">source browser</a>,
      or read how content is produced and reviewed on the
      <a href="{{ '/about/' | relative_url }}">About &amp; methodology page</a>.
    </p>
  </div>

</details>

</section>
