---
layout: default
title: "AI Interfaces & Handshakes"
description: "Where a learned service sits on the network: why high-rate inference belongs at the edge, why neither OPC UA nor Sparkplug gives an AI result a standard meaning, and the publish-only result contract that crosses into the control system."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Interfaces & Handshakes"
review:
  standard: "OPC UA Parts 1/3/4/5/9/18; MQTT Sparkplug; NIST SP 800-82r3"
  edition: "OPC UA parts retrieved 2026-07 (Phase 49a); NIST SP 800-82 Rev. 3"
  status: "Review pending"
  coverage: "Edge-inference rationale, transport semantics, write-authority separation, result contract, OT placement. Version-dependent details flagged verify-against-your-version."
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/interfaces_edge.md"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "Safety & Security Boundaries"
    url: "/design/ai-integration/safety-boundaries/"
  - name: "IEC 62443 — OT cybersecurity"
    url: "/standards/cybersecurity/iec-62443/"
  - name: "Software Stack & Cybersecurity"
    url: "/design/software-stack/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design"
---

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>AI Interfaces &amp; Handshakes</h1>
  <p>Analyse the fast signal where it is measured; send the verdict, not the waveform. Neither OPC UA nor Sparkplug assigns an AI result a standard meaning or authority — you define and test the contract, and the inference service stays publish-only.</p>
</div>

This page is part of the [AI &amp; ML Integration]({{ '/design/ai-integration/' | relative_url }})
section; read the [authority gate]({{ '/design/ai-integration/' | relative_url }}) first, and the
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }})
page for why the service stays read-only. Review pending.

## The rule

Perform high-rate acquisition and inference at the source, then publish the lower-rate result with its
class or estimate, confidence or uncertainty, model version, timestamp, quality, and freshness. OPC UA
PubSub/TSN can support many architectures; the limitation below is the chosen *acquisition path*, not
OPC UA as a whole.

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

## Why the edge, in four constraints

"kHz signals cannot go through OPC UA" is **false as a protocol claim** — OPC UA PubSub/UADP over TSN
has been measured at a 250 µs (4 kHz) cycle. The edge-inference conclusion rests on four different
constraints:

1. **Server sampling floor.** OPC UA Part 4 makes sampling *best-effort* (the server returns a
   `revisedSamplingInterval` it can meet); Part 5 defines `MinSupportedSampleRate`. Some embedded OPC
   UA servers impose a floor of tens to hundreds of milliseconds — orders of magnitude short of kHz.
   *Verify the floor for your device.*
2. **Decoupled source and aliasing — the decisive one.** Part 4 states the server "has no knowledge of
   the data update logic" of the decoupled source. You cannot reconstruct a waveform by oversampling a
   tag that updates once per PLC scan; you alias it.
3. **The historian is a compressor, not a recorder.** Deadband and swinging-door compression decimate
   by design; a pipeline reading archives gets decimated data.
4. **Segmentation.** A kHz stream across the IT/OT boundary widens a conduit that NIST SP 800-82 Rev. 3
   guidance says to keep narrow.

## Neither transport gives an AI result a standard meaning

Define and test the application contract explicitly — the transport carries bytes, not semantics.

| Transport | What it does **not** give | What you can build on |
|---|---|---|
| **OPC UA** | No AI/ML companion specification; `DataValue` quality is a coarse `StatusCode`, not a confidence number | Custom **Structured DataTypes** to define a `ModelResult`; `Uncertain_*` status for "model degraded"; `SourceTimestamp` for freshness; **Part 9 Alarms & Conditions** for an advisory needing human acknowledgement |
| **MQTT Sparkplug B** | No standard AI-result meaning or authority | **Arbitrary per-metric properties** (carry confidence / model version / freshness); **birth/death certificates** (NBIRTH/NDEATH) so a subscriber detects a dead publisher |

*(Companion specifications and payload conventions evolve — verify against the OPC UA companion-spec
list and the Sparkplug version you deploy.)*

## Write-authority separation

The strongest, fully spec-backed part of the interface story. OPC UA separates read from write, and its
well-known **Observer** role — browse / read / subscribe, **no write** — maps exactly onto an edge
inference service that publishes results and must never write setpoints. Sparkplug B has no equivalent
role construct: the same separation is a **convention you enforce** with broker ACLs and topic
namespacing, not a guarantee you inherit.

So the inference service is **publish-only** with respect to control. It emits a result; a separate,
verifiable layer — the [envelope]({{ '/design/ai-integration/' | relative_url }}#the-envelope-architecture)
— decides whether to act on it.

## The result contract

Publish a compact, self-describing result, not a raw stream:

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

Two optional fields strengthen it: a **training-set identifier** makes drift auditable, and an explicit
**authority tag** lets the consumer enforce the register's ceiling at the point of use. Publishing a
compact result also crosses zone boundaries on terms a raw waveform stream does not.

## The cybersecurity boundary

Place the AI service inside the existing OT security zones and conduits. **NIST SP 800-82 Rev. 3**
supports edge-local computation and read-only monitoring as a distinct, lower-impact class; keep the
service **read-only by default and least-privilege**, and do not widen a conduit to carry a raw stream.
*(This page cites NIST SP 800-82r3 for OT placement; specific IEC 62443 clause numbers are not asserted
— see the [IEC 62443 page]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}).)*

## Review status

Distilled from a corpus-owned Draft note and **Review pending**. Version-dependent details (server
sampling floors, companion specifications, Sparkplug payload conventions) are flagged
verify-against-your-version. Return to the [authority gate]({{ '/design/ai-integration/' | relative_url }}),
the [method register]({{ '/design/ai-integration/method-register/' | relative_url }}), or
[Safety &amp; Security Boundaries]({{ '/design/ai-integration/safety-boundaries/' | relative_url }}).
