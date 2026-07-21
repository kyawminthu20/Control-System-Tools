---
layout: default
title: "Standards Comparison"
description: "Select any two standards to view their overlap and relationship."
breadcrumb:
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
  - name: "Compare"
related_standards:
  - name: "NFPA 79 vs IEC 60204-1"
    url: "/tools/crosswalks/nfpa79-iec60204/"
  - name: "UL 508A / NEC / NFPA 79"
    url: "/tools/crosswalks/ul508a-nec-nfpa79/"
  - name: "Standards Decision Workflow"
    url: "/tools/crosswalks/standards-decision-workflow/"
redirect_from:
  - /crosswalks/compare/
  - /crosswalks/compare/index.html
review:
  standard: "Pairwise standards relationships (site data)"
  edition: "n/a — relationship summaries derived from the standards pages"
  status: "Review pending"
  coverage: "Interactive side-by-side of editorial relationship summaries; not clause-level equivalence."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Crosswalks</span>
  <h1>Standards Comparison</h1>
  <p>Select two standards to view their overlap matrix. Only pairs with documented crosswalk data are shown.</p>
</div>

<div class="compare-selector">
  <select id="compare-a" aria-label="First standard">
    <option value="">— Select standard A —</option>
    <option value="nec">NEC (NFPA 70)</option>
    <option value="nfpa79">NFPA 79</option>
    <option value="ul508a">UL 508A</option>
    <option value="iec60204">IEC 60204-1</option>
    <option value="iso12100">ISO 12100</option>
    <option value="iso13849">ISO 13849-1</option>
    <option value="iec62061">IEC 62061</option>
    <option value="iec61508">IEC 61508</option>
    <option value="iec61511">IEC 61511</option>
  </select>
  <span class="compare-selector__vs">vs</span>
  <select id="compare-b" aria-label="Second standard">
    <option value="">— Select standard B —</option>
    <option value="nec">NEC (NFPA 70)</option>
    <option value="nfpa79">NFPA 79</option>
    <option value="ul508a">UL 508A</option>
    <option value="iec60204">IEC 60204-1</option>
    <option value="iso12100">ISO 12100</option>
    <option value="iso13849">ISO 13849-1</option>
    <option value="iec62061">IEC 62061</option>
    <option value="iec61508">IEC 61508</option>
    <option value="iec61511">IEC 61511</option>
  </select>
</div>

<p class="compare-no-data" id="compare-no-data" hidden>
  No documented crosswalk exists for this pair in the reference library.
  See the <a href="{{ '/tools/crosswalks/' | relative_url }}">Crosswalks index</a> for available comparisons,
  or consult <a href="{{ '/standards/' | relative_url }}">individual standard pages</a> for relationship context.
</p>

<!-- Pair: NFPA 79 vs IEC 60204-1 -->
<div class="compare-result" id="pair-nfpa79-iec60204" hidden>

## NFPA 79:2024 vs IEC 60204-1:2016+AMD1:2021

Both cover electrical equipment of machines. Use when designing for US + EU markets. Design to the **most restrictive** requirement from each standard.

[View full crosswalk →](../nfpa79-iec60204/)

| Topic Area | NFPA 79 | IEC 60204-1 | Equivalence |
|------------|---------|-------------|-------------|
| Scope boundary | Ch. 1 | Clause 1 | High |
| Incoming supply / Disconnect | Ch. 5 | Clause 5 | Very High |
| Protection against electric shock | Ch. 7 | Clause 6 | High |
| Equipment protection (overcurrent) | Ch. 6 | Clause 7 | High |
| Grounding / Bonding | Ch. 8 | Clause 8 | Very High |
| Control circuits / E-stop | Ch. 9 | Clause 9 | Very High |
| Operator interface | Ch. 10 | Clause 10 | High |
| Control equipment / Enclosures | Ch. 11 | Clause 11 | High |
| Motors and drives | Ch. 12 | Clause 12 | High |
| Wiring / Conductors | Ch. 14 | Clause 12 | Medium |
| Marking and documentation | Ch. 19 | Clause 17 | High |
| Verification and testing | Ch. 20 | Clause 15 | High |

**Key difference — wire colors:**

| Conductor | NFPA 79 | IEC 60204-1 |
|-----------|---------|-------------|
| Protective Earth | Green or bare | Yellow-green (required) |
| Neutral | White or gray | Blue |
| Phase conductors | Black, red, blue | Brown, black, gray |

</div>

<!-- Pair: US Electrical family (UL 508A / NEC / NFPA 79) -->
<div class="compare-result" id="pair-us-electrical" hidden>

## US Electrical Standards: UL 508A / NEC / NFPA 79

These three standards form the US electrical compliance stack. They overlap but have distinct scopes.

[View full crosswalk →](../ul508a-nec-nfpa79/)

| Standard | Primary Scope | When It Applies |
|----------|---------------|-----------------|
| NEC (NFPA 70) | Electrical wiring in buildings | Always — governs supply wiring to the panel |
| NFPA 79 | Electrical equipment on industrial machinery | Machinery with motors, actuators, control circuits |
| UL 508A | Industrial control panel construction | When UL listing is required (most US installations) |

| Topic | NEC | NFPA 79 | UL 508A |
|-------|-----|---------|---------|
| Scope | Premises wiring | Machine electrical equipment | Control panel construction |
| Branch circuit protection | Governs | References NEC | References both |
| Wire sizing | NEC tables | Follows NEC inside enclosure | Follows NEC |
| Grounding | Art. 250 | Ch. 8 references NEC | Follows NFPA 79 / NEC |
| E-stop / Safety | Not covered | Ch. 9 | Not covered |
| Listing / Marking | Not a listing std | Not a listing std | UL listing mark |
| Panel enclosure | Not covered | Ch. 11 | Detailed requirements |

</div>

<script>
(function () {
  var selA = document.getElementById('compare-a');
  var selB = document.getElementById('compare-b');
  var noData = document.getElementById('compare-no-data');

  var pairs = {
    'nfpa79+iec60204':  'pair-nfpa79-iec60204',
    'iec60204+nfpa79':  'pair-nfpa79-iec60204',
    'nec+nfpa79':       'pair-us-electrical',
    'nfpa79+nec':       'pair-us-electrical',
    'nec+ul508a':       'pair-us-electrical',
    'ul508a+nec':       'pair-us-electrical',
    'nfpa79+ul508a':    'pair-us-electrical',
    'ul508a+nfpa79':    'pair-us-electrical'
  };

  function update() {
    var a = selA.value;
    var b = selB.value;

    document.querySelectorAll('.compare-result').forEach(function (el) {
      el.hidden = true;
    });
    noData.hidden = true;

    if (!a || !b || a === b) return;

    var pairId = pairs[a + '+' + b];
    if (pairId) {
      var result = document.getElementById(pairId);
      if (result) result.hidden = false;
    } else {
      noData.hidden = false;
    }
  }

  selA.addEventListener('change', update);
  selB.addEventListener('change', update);
})();
</script>
