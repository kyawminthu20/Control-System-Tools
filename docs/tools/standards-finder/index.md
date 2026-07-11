---
layout: default
title: "Standards Finder"
description: "Pick the scenario closest to what you're building and jump to the standards stack that applies — region, equipment class, and risk profile already mapped."
breadcrumb:
  - name: "Tools"
    url: "/tools/"
  - name: "Standards Finder"
---

<div class="page-header">
  <span class="page-header__label">Standards Finder</span>
  <h1>Find the standards that apply to what you're building</h1>
  <p>Each card below is a real engineering scenario with its standards stack already mapped — region, equipment class, and risk profile. Pick the one closest to your project and open the full walk-through. If nothing fits, the escape hatch at the bottom routes to the comparison crosswalks.</p>
</div>

<div class="finder-filters" data-finder-filters aria-label="Filter scenarios">
  <div class="finder-filters__row">
    <span class="finder-filters__label">Market:</span>
    <button type="button" class="finder-chip" data-facet="region" data-value="us">US-market</button>
    <button type="button" class="finder-chip" data-facet="region" data-value="global">Global / EU</button>
    <button type="button" class="finder-chip" data-facet="region" data-value="industry">Industry-bound</button>
  </div>
  <div class="finder-filters__row">
    <span class="finder-filters__label">What you're building:</span>
    <button type="button" class="finder-chip" data-facet="domain" data-value="machinery">Machinery / panel</button>
    <button type="button" class="finder-chip" data-facet="domain" data-value="process">Process safety (SIS)</button>
    <button type="button" class="finder-chip" data-facet="domain" data-value="hazloc">Hazardous area</button>
    <button type="button" class="finder-chip" data-facet="domain" data-value="cyber">Cybersecurity</button>
    <button type="button" class="finder-chip" data-facet="domain" data-value="industry-overlay">Industry overlay (SEMI / DNV)</button>
  </div>
  <div class="finder-filters__meta">
    <span class="finder-filters__count" data-finder-count>Showing all 9 scenarios</span>
    <button type="button" class="finder-filters__clear" data-finder-clear hidden>Clear filters</button>
  </div>
</div>

<nav class="finder-jump" aria-label="Jump to scenario group">
  <span class="finder-jump__label">Jump to:</span>
  <a href="#us-machines">US-market machines &amp; panels</a>
  <a href="#global-machines">Global / EU machines</a>
  <a href="#process-safety">Process safety (SIS / ESD)</a>
  <a href="#networked-safety">Networked &amp; cyber-physical safety</a>
  <a href="#industry">Industry-specific stacks</a>
</nav>

<p class="finder-empty" data-finder-empty hidden>No scenarios match the current filter combination. Try removing a chip or use the <a href="#escape-hatch">comparison crosswalks</a> below.</p>

<section class="home-section" data-finder-section id="us-machines">
  <h2>US-market machines &amp; control panels</h2>
  <p class="home-section__intro">Built for sale or installation in the United States. NEC is the legal baseline; UL listing and NFPA 79 layer on top depending on whether you ship a panel, a machine, or both.</p>
  <div class="scenario-grid">
    <div class="scenario-card" data-finder-region="us" data-finder-domain="machinery">
      <span class="scenario-card__num">Scenario 01</span>
      <span class="scenario-card__title">US Industrial Control Panel</span>
      <p class="scenario-card__start"><strong>Stack:</strong> UL 508A + NEC Article 409 + NFPA 79</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">UL listing required. NEC is the legal baseline, UL 508A governs panel construction, NFPA 79 applies once the panel sits on a machine.</p>
      <a href="{{ '/tools/scenarios/us-industrial-control-panel/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
    <div class="scenario-card" data-finder-region="us global" data-finder-domain="machinery">
      <span class="scenario-card__num">Scenario 06</span>
      <span class="scenario-card__title">Practical Machine Safety Implementation</span>
      <p class="scenario-card__start"><strong>Stack:</strong> ISO 13849-1 / IEC 62061 — 10-step SIL/PL workflow</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Safety-function design path applicable to US machines too. Pick PL (ISO 13849-1) or SIL (IEC 62061) depending on the safety lifecycle you're already inside.</p>
      <a href="{{ '/tools/scenarios/machine-safety-implementation/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
  </div>
</section>

<section class="home-section" data-finder-section id="global-machines">
  <h2>Global / EU-market machines</h2>
  <p class="home-section__intro">CE-marked or sold into both US and EU markets. ISO 12100 is the risk-assessment foundation; design to the more restrictive rule between NFPA 79 and IEC 60204-1 where they disagree.</p>
  <div class="scenario-grid">
    <div class="scenario-card" data-finder-region="us global" data-finder-domain="machinery">
      <span class="scenario-card__num">Scenario 02</span>
      <span class="scenario-card__title">Global Machine (US + EU)</span>
      <p class="scenario-card__start"><strong>Stack:</strong> NFPA 79 (US) + IEC 60204-1 (EU) + ISO 12100</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Same machine for both markets. CE marking requires an ISO 12100 risk assessment as the foundation; the rest layers on top.</p>
      <a href="{{ '/tools/scenarios/global-machine/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
  </div>
</section>

<section class="home-section" data-finder-section id="process-safety">
  <h2>Process safety — SIS / ESD</h2>
  <p class="home-section__intro">Continuous-process plants (refining, chemicals, oil &amp; gas, water). IEC 61511 is the application standard; IEC 61508 is the lifecycle foundation.</p>
  <div class="scenario-grid">
    <div class="scenario-card" data-finder-region="us global" data-finder-domain="process">
      <span class="scenario-card__num">Scenario 03</span>
      <span class="scenario-card__title">Process Skid Shutdown System</span>
      <p class="scenario-card__start"><strong>Stack:</strong> IEC 61511 + IEC 61508 foundation</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">SIS / ESD for general process industry. <span class="badge badge--complete">REVIEWED</span></p>
      <a href="{{ '/tools/scenarios/process-skid/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
    <div class="scenario-card" data-finder-region="us" data-finder-domain="process hazloc">
      <span class="scenario-card__num">Scenario 07</span>
      <span class="scenario-card__title">O&amp;G Onshore Process Skid (ESD / F&amp;G)</span>
      <p class="scenario-card__start"><strong>Stack:</strong> IEC 61511 + IEC 60079 + NEC Art. 500–505</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Hazardous-area onshore skid. Adds explosive-atmosphere classification and area marking on top of the SIS path.</p>
      <a href="{{ '/tools/scenarios/oil-gas-process-skid/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
  </div>
</section>

<section class="home-section" data-finder-section id="networked-safety">
  <h2>Networked &amp; cyber-physical safety</h2>
  <p class="home-section__intro">Safety functions over a network. The safety standard is unchanged (ISO 13849-1 or IEC 62061); the cybersecurity overlay is IEC 62443.</p>
  <div class="scenario-grid">
    <div class="scenario-card" data-finder-region="us global" data-finder-domain="machinery cyber">
      <span class="scenario-card__num">Scenario 04</span>
      <span class="scenario-card__title">Networked Safety PLC Architecture</span>
      <p class="scenario-card__start"><strong>Stack:</strong> ISO 13849-1 or IEC 62061 + IEC 62443</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Safety PLC with network connectivity. Pick the safety-function path you're already on; layer cybersecurity per IEC 62443 zones &amp; conduits.</p>
      <a href="{{ '/tools/scenarios/networked-safety-plc/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
  </div>
</section>

<section class="home-section" data-finder-section id="industry">
  <h2>Industry-specific stacks</h2>
  <p class="home-section__intro">When the industry overlay is non-negotiable: semiconductor SEMI standards, offshore DNV, etc. These layer over the general control-panel and safety stacks.</p>
  <div class="scenario-grid">
    <div class="scenario-card" data-finder-region="industry" data-finder-domain="industry-overlay">
      <span class="scenario-card__num">Scenario 05</span>
      <span class="scenario-card__title">Semiconductor Equipment Compliance</span>
      <p class="scenario-card__start"><strong>Stack:</strong> 15-Standard Minimum Compliance Stack</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">SEMI S2/S8/S14 + the general machinery and electrical stacks. Use this when the buyer is a fab.</p>
      <a href="{{ '/tools/scenarios/semiconductor-equipment/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
    <div class="scenario-card" data-finder-region="industry" data-finder-domain="industry-overlay machinery">
      <span class="scenario-card__num">Scenario 08</span>
      <span class="scenario-card__title">Semiconductor Fab Tool (Etch / CVD)</span>
      <p class="scenario-card__start"><strong>Stack:</strong> SEMI S2/S8/S14 + IEC 60204-1 + ISO 12100</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Specific to etch and CVD process tools — narrower scope than the general SEMI compliance stack.</p>
      <a href="{{ '/tools/scenarios/semiconductor-fab-tool/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
    <div class="scenario-card" data-finder-region="industry" data-finder-domain="process hazloc industry-overlay">
      <span class="scenario-card__num">Scenario 09</span>
      <span class="scenario-card__title">Offshore Platform ESD / F&amp;G</span>
      <p class="scenario-card__start"><strong>Stack:</strong> DNV-OS-D201 + IEC 61511 + IEC 60079</p>
      <p style="font-size:0.78rem;color:var(--color-text-muted);">Offshore-specific control and safety. DNV is non-negotiable; IEC 61511 carries the SIS lifecycle; IEC 60079 covers hazardous-area equipment.</p>
      <a href="{{ '/tools/scenarios/offshore-platform-control/' | relative_url }}" style="font-size:0.8rem;">Open scenario &rarr;</a>
    </div>
  </div>
</section>

<section class="home-section" id="escape-hatch">
  <h2>None of these fit?</h2>
  <p class="home-section__intro">If your project doesn't map cleanly to a scenario, jump straight into the comparison crosswalks or browse the full standards atlas.</p>
  <div class="card-grid">
    <div class="card">
      <span class="card__label">Comparison</span>
      <span class="card__title">Standards Crosswalks</span>
      <p class="card__desc">Side-by-side comparison between US and IEC standards (NFPA 79 ↔ IEC 60204-1, UL 508A / NEC / NFPA 79, IEC 61511 ↔ IEC 61508, IEC 60079 ↔ NEC 500/505).</p>
      <a href="{{ '/tools/crosswalks/' | relative_url }}" class="card__link">Open crosswalks &rarr;</a>
    </div>
    <div class="card">
      <span class="card__label">Browse</span>
      <span class="card__title">Standards Atlas</span>
      <p class="card__desc">Every standards family in the corpus, organized by region and topic. Use this when you already know which standard you need.</p>
      <a href="{{ '/standards/' | relative_url }}" class="card__link">Open atlas &rarr;</a>
    </div>
  </div>
</section>
