---
layout: default
title: "Standards Explorer"
description: "Browse industrial automation standards by family: US Electrical, International Machinery, Functional Safety."
breadcrumb:
  - name: "Standards"
repo_path: "control-standards/rag/standards_intelligence/"
related_standards:
  - name: "Standards Applicability Matrix"
    url: "/crosswalks/standards-decision-workflow/"
  - name: "Crosswalks"
    url: "/crosswalks/"
---

<div class="page-header">
  <span class="page-header__label">Standards Explorer</span>
  <h1>Industrial Automation Standards</h1>
  <p>Browse standards by family. Use the <a href="{{ '/crosswalks/standards-decision-workflow/' | relative_url }}">decision workflow</a> if you're unsure which standard applies to your project.</p>
</div>

## Quick Decision

```
US panel / machinery only?   → NEC + NFPA 79 + UL 508A
International / CE marking?  → IEC 60204-1 + ISO 12100 + ISO 13849-1
Safety functions (PL)?       → ISO 13849-1 + IEC 62061
Safety functions (SIL)?      → IEC 62061 (machinery) or IEC 61511 (process)
Process SIS?                 → IEC 61511 + IEC 61508
Global (US + EU)?            → NFPA 79 + IEC 60204-1 + ISO 13849-1 (design to most restrictive)
```

---

## US Electrical Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [NEC (NFPA 70)]({{ '/standards/us-electrical/nec/' | relative_url }}) | 2023 | US electrical installation code, legally enforced | Complete |
| [NFPA 79]({{ '/standards/us-electrical/nfpa-79/' | relative_url }}) | 2024 | Electrical standard for industrial machinery | Complete |
| [UL 508A]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) | 2022 | Industrial control panel construction and listing | Complete |

<p><a href="{{ '/standards/us-electrical/' | relative_url }}">View US Electrical family page &rarr;</a></p>

---

## International Machinery Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) | 2018 | Electrical equipment of machines, global / CE | Complete |

<p><a href="{{ '/standards/machinery/' | relative_url }}">View International Machinery family page &rarr;</a></p>

---

## Functional Safety Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) | 2010 | Risk assessment and risk reduction | Planned <span class="badge badge--verify">TO VERIFY</span> |
| [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) | 2023 | Safety of machinery — PL approach | Planned <span class="badge badge--verify">TO VERIFY</span> |
| [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) | 2021 | Functional safety — machinery SIL approach | Planned <span class="badge badge--verify">TO VERIFY</span> |
| [IEC 61508]({{ '/standards/functional-safety/iec-61508/' | relative_url }}) | 2010 | Functional safety of E/E/PE systems | Planned <span class="badge badge--verify">TO VERIFY</span> |
| [IEC 61511]({{ '/standards/functional-safety/iec-61511/' | relative_url }}) | 2016 | Functional safety — process industry | Planned <span class="badge badge--verify">TO VERIFY</span> |

<p><a href="{{ '/standards/functional-safety/' | relative_url }}">View Functional Safety family page &rarr;</a></p>

---

## Standards Relationship Diagram

<div class="mermaid-wrap">
<pre class="mermaid">
graph TD
    ISO12100[ISO 12100] --> ISO13849[ISO 13849-1]
    ISO12100 --> IEC62061[IEC 62061]
    ISO13849 --> IEC60204[IEC 60204-1]
    IEC62061 --> IEC61508[IEC 61508]
    IEC61511[IEC 61511] --> IEC61508
    NFPA79[NFPA 79] --> NEC[NEC]
    UL508A[UL 508A] --> NEC
    UL508A --> NFPA79
    IEC60204 --> NFPA79
    IEC62443[IEC 62443] --> IEC61508
    IEC62443 --> IEC61511
    IEC61131[IEC 61131-3] --> IEC62061
    IEC61131 --> IEC61508
    IEC60079[IEC 60079 Family] --> IEC61511
</pre>
</div>
