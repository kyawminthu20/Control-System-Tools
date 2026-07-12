---
layout: default
title: "Standards Explorer"
description: "Browse industrial automation standards by family: US Electrical, Machinery, Functional Safety, Cybersecurity, Hazardous Area, and Semiconductor."
breadcrumb:
  - name: "Standards"
repo_path: "control-standards/rag/standards_intelligence/"
related_standards:
  - name: "Standards Applicability Matrix"
    url: "/tools/crosswalks/standards-decision-workflow/"
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
---

<div class="page-header">
  <span class="page-header__label">Standards Explorer</span>
  <h1>Industrial Automation Standards</h1>
  <p>Browse standards by family. Use the <a href="{{ '/tools/crosswalks/standards-decision-workflow/' | relative_url }}">decision workflow</a> if you're unsure which standard applies to your project.</p>
</div>

## Quick Decision

```
US panel / machinery only?   → NEC + NFPA 79 + UL 508A
International / CE marking?  → IEC 60204-1 + ISO 12100 + ISO 13849-1
Safety functions (PL)?       → ISO 13849-1 + IEC 62061
Safety functions (SIL)?      → IEC 62061 (machinery) or IEC 61511 (process)
Process SIS?                 → IEC 61511 + IEC 61508
Hazardous-area / Ex?         → IEC 60079 + NEC Art. 500/504/505
Semiconductor tool / fab?    → SEMI S2/S8/S14 + IEC 60204-1 + NFPA 79
Global (US + EU)?            → NFPA 79 + IEC 60204-1 + ISO 13849-1 (design to most restrictive)
```

> **Applicability note:** these are common starting points, not complete determinations.
> Actual applicability also depends on the authority having jurisdiction, listing
> requirements, state/local code adoption, hazardous-location classification,
> customer specifications, product-specific standards, and where the equipment
> boundary ends and the installation begins. Confirm the governing editions for
> your project before relying on any row above.

---

## US Electrical Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [NEC (NFPA 70)]({{ '/standards/us-electrical/nec/' | relative_url }}) | 2023 covered; 2026 latest published — AHJ adoption governs | US electrical installation code, legally enforced | <span class="badge badge--pending">Review pending</span> |
| [NFPA 79]({{ '/standards/us-electrical/nfpa-79/' | relative_url }}) | 2024 | Electrical standard for industrial machinery | <span class="badge badge--pending">Review pending</span> |
| [UL 508A]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) | 3rd Ed. (2018), rev. through 2025-06-26 | Industrial control panel construction and listing | <span class="badge badge--pending">Review pending</span> |

<p><a href="{{ '/standards/us-electrical/' | relative_url }}">View US Electrical family page &rarr;</a></p>

---

## International Machinery Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) | 2016+AMD1:2021 | Electrical equipment of machines, global / CE | <span class="badge badge--pending">Review pending</span> |

<p><a href="{{ '/standards/machinery/' | relative_url }}">View International Machinery family page &rarr;</a></p>

---

## Functional Safety Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) | 2010 | Risk assessment and risk reduction | <span class="badge badge--pending">Review pending</span> |
| [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) | 2023 | Safety of machinery — PL approach | <span class="badge badge--pending">Review pending</span> |
| [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}) | 2021+AMD1:2024+AMD2:2026 | Functional safety — machinery SIL approach | <span class="badge badge--revalidate">Needs revalidation</span> |
| [IEC 61508]({{ '/standards/functional-safety/iec-61508/' | relative_url }}) | 2010 | Functional safety of E/E/PE systems | <span class="badge badge--reviewed">Reviewed</span> |
| [IEC 61511]({{ '/standards/functional-safety/iec-61511/' | relative_url }}) | 2016 | Functional safety — process industry | <span class="badge badge--pending">Review pending</span> |

<p><a href="{{ '/standards/functional-safety/' | relative_url }}">View Functional Safety family page &rarr;</a></p>

---

## Cybersecurity Standards

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [IEC 62443]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}) | Series | IACS security — Zone/Conduit, Security Levels, FRs, lifecycle | <span class="badge badge--pending">Review pending</span> |

<p><a href="{{ '/standards/cybersecurity/' | relative_url }}">View Cybersecurity family page &rarr;</a></p>

---

## Hazardous Area Standards

| Standard | Publisher | Scope | Status |
|----------|-----------|-------|--------|
| [IEC 60079 (6 parts)]({{ '/standards/hazardous-area/iec-60079/' | relative_url }}) | IEC | Explosive atmosphere equipment and installation | <span class="badge badge--reviewed">Reviewed</span> |

<p><a href="{{ '/standards/hazardous-area/' | relative_url }}">View Hazardous Area family page &rarr;</a></p>

---

## Semiconductor Equipment Standards

| Standard | Publisher | Scope | Status |
|----------|-----------|-------|--------|
| [SEMI S2 / S8 / S14]({{ '/standards/semiconductor/semi/' | relative_url }}) | SEMI | Semiconductor equipment safety, ergonomics, fire risk | <span class="badge badge--reviewed">Reviewed</span> |

<p><a href="{{ '/standards/semiconductor/' | relative_url }}">View Semiconductor family page &rarr;</a></p>

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
    SEMI[SEMI S2/S8/S14] --> IEC60204
    SEMI --> ISO12100
</pre>
</div>
