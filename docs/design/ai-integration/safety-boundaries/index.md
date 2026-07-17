---
layout: default
title: "AI Safety & Security Boundaries"
description: "Why a learned component cannot hold a machine's safety function today — the deterministic functional-safety standards, the AI-specific documents that are only guidance or draft, and the EU law that already caps self-evolving safety components."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "AI & ML Integration"
    url: "/design/ai-integration/"
  - name: "Safety & Security Boundaries"
review:
  standard: "ISO/IEC TR 5469:2024; IEC 62061:2021; Reg (EU) 2023/1230; Reg (EU) 2024/1689; NIST SP 800-82r3"
  edition: "TR 5469 Ed. 1.0 (2024); IEC 62061 Ed. 2.0 (2021); TS 22440 Committee Draft (Feb 2026)"
  status: "Review pending"
  coverage: "Functional-safety and EU-law boundary for learned components; cybersecurity placement at overview level. TR 5469 body is paywalled and unread."
  last_reviewed: "July 2026"
repo_path: "control-standards/rag/design_framework/ai_integration/safety_boundary.md"
related_standards:
  - name: "AI & ML Integration (gate)"
    url: "/design/ai-integration/"
  - name: "ISO 13849-1 — safety functions"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061 — safety functions"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61508 — E/E/PE lifecycle"
    url: "/standards/functional-safety/iec-61508/"
  - name: "IEC 62443 — OT cybersecurity"
    url: "/standards/cybersecurity/iec-62443/"
lifecycle_stage:
  - name: "Risk Assessment"
    slug: "risk-assessment"
  - name: "Safety Architecture"
    slug: "safety-architecture"
---

<div class="page-header">
  <span class="page-header__label">Authority-first design</span>
  <h1>AI Safety &amp; Security Boundaries</h1>
  <p>A learned component may inform or propose; an independent, verifiable layer decides and protects. This page explains why that boundary is not a preference but the current state of the standards and the law.</p>
</div>

> **The one-sentence position:** there is **no published normative standard against which a learned
> closed-loop safety function could be certified today** — and EU product law already treats a
> self-evolving safety component as high-risk and caps what it may do. Both point the same way: the
> safety function stays in a verified, non-learned layer.

This page is part of the [AI &amp; ML Integration]({{ '/design/ai-integration/' | relative_url }})
section; read the [authority gate]({{ '/design/ai-integration/' | relative_url }}) first for the
ladder and the envelope architecture. It is Review pending and does not replace hazard analysis or
the applicable safety and cybersecurity lifecycle.

## Why there is no certification route

The functional-safety standards a machine builder uses are **deterministic methodologies**. They
assume behaviour that can be analysed in advance — and none of them provides a way to demonstrate that
a component whose behaviour comes from training data meets a safety integrity target.

<div class="table-scroll" markdown="1">

| Document | What it is | Status for a learned safety function |
|---|---|---|
| **ISO 13849-1:2023** | Machinery safety functions; PLr from the Annex A risk graph | Deterministic; no route for a learned component |
| **IEC 62061:2021 (Ed. 2.0)** | Functional safety of safety-related control systems, within the IEC 61508 framework | Scope makes **no mention** of AI/ML/self-evolving components |
| **IEC 61508:2010 (Ed. 2.0)** | Base E/E/PE functional-safety lifecycle | Systematic + random-failure methodology; no learned-component route |
| **ISO/IEC TR 5469:2024 (Ed. 1.0)** | AI + functional safety — a Technical **Report** | **Guidance, not certifiable.** Exists *because* the above cannot be shown for AI |
| **ISO/IEC TS 22440 (Parts 1–3)** | The requirement-bearing successor | **Committee Draft (Feb 2026) — not yet published**; no certification route today |
| **ISO/IEC 42001:2023 · 23894:2023** | AI management system · AI risk guidance | Published, but confer **no** technical permission for AI in a safety function |

</div>

The presence of ISO/IEC TR 5469 *is* the argument: a Technical Report was needed precisely because
compliance with the existing functional-safety standards cannot be shown directly for AI. Its
requirement-bearing successor, ISO/IEC TS 22440, is still a Committee Draft. Until it publishes, there
is nothing to certify a learned safety function against. *(TR 5469's body is paywalled and was not
read; this page relies on its existence and scope, both verified at the IEC webstore, not on its
internal clauses.)*

## The law already caps it

EU product law has moved ahead of the standards, and it does not wait for TS 22440.

- **Regulation (EU) 2023/1230 (Machinery Regulation), Annex I Part A items 5–6** list *safety
  components with fully or partially self-evolving behaviour using machine learning*. For these,
  **notified-body conformity assessment is mandatory — self-declaration is not available.**
- **Annex III EHSR 1.2.1** imposes a **statutory authority ceiling**: a self-evolving system shall not
  act beyond its **defined task and movement space**, must be **correctable at all times**, and must
  **prevent hazardous self-modification of safety rules — including during the learning phase.**
- **Regulation (EU) 2024/1689 (AI Act), Article 6(1)** makes such a system high-risk where it is a
  safety component of a product needing third-party assessment.

Annex III EHSR 1.2.1 is, in effect, **authority level ≤ 4 written into law**. The two regimes bite
about six months apart.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    subgraph STD["Standards track — no certification route yet"]
      direction TB
      A["ISO 13849-1 · IEC 62061 · IEC 61508<br/>deterministic — no learned-component route"]
      B["ISO/IEC TR 5469:2024<br/>guidance (a Report), not certifiable"]
      C["ISO/IEC TS 22440<br/>Committee Draft, Feb 2026 — unpublished"]
      A --> B --> C
    end
    subgraph LAW["Law track — binding ceiling, dated"]
      direction TB
      D["Machinery Reg (EU) 2023/1230<br/>self-evolving safety component =<br/>mandatory notified body;<br/>bounded, correctable, no self-modification"]
      E["applies 20 Jan 2027"]
      F["AI Act (EU) 2024/1689 Art 6(1)<br/>applies 2 Aug 2027"]
      D --> E --> F
    end
    STD --> CONC["Conclusion: the safety function stays in a<br/>verified, non-learned layer; the learned policy<br/>acts only inside an independent envelope"]
    LAW --> CONC
    classDef std fill:#e8eff8,stroke:#2b5797,color:#1e1e1e
    classDef law fill:#faeeec,stroke:#a33327,color:#1e1e1e
    classDef conc fill:#eef4ed,stroke:#3a6b35,color:#1e1e1e,stroke-width:2px
    class A,B,C std
    class D,E,F law
    class CONC conc
</pre>
</div>

## The architecture that follows

Every documented real deployment the research reviewed — tokamak coil control, an 840-hour
reinforcement-learning distillation-column run, a learned road-vehicle motion planner — **keeps a
non-learned layer holding the veto.** The safe-learning-control literature is candid that its
guarantees "rely on a set of assumptions … difficult to verify prior to operation" (Brunke et al.,
2022) — a proof conditioned on an unverifiable premise is a conditional theorem, not a safety case.
The strictest sector position found, EASA's AI Concept Paper (Issue 02), permits **offline learning
only**, with the model frozen at approval.

The convergent pattern, and the rule this whole section is built on:

> The learned policy holds operational authority **inside an envelope**. A verified, non-learned layer
> holds the safety function and the veto. The safety-function path never routes through the learned
> layer, and the plant stays safe when the model is wrong, stale, unavailable, or compromised.

See the [envelope architecture]({{ '/design/ai-integration/' | relative_url }}#the-envelope-architecture)
on the gate page for how that separation is implemented in code.

## The cybersecurity boundary

An AI service is also an OT asset. **NIST SP 800-82 Rev. 3** (Guide to Operational Technology
Security) supports edge-local computation and read-only monitoring as a distinct, lower-impact class,
and its segmentation guidance is why a learned service should be **read-only by default,
least-privilege, and inside the existing zone/conduit structure**. An edge inference service publishes
results; it should not hold write access to setpoints. OPC UA's well-known **Observer** role
(browse/read/subscribe, no write) maps exactly onto a publish-only inference service and expresses
that separation in the transport standard without invention. *(This page cites NIST SP 800-82r3 for OT
placement; specific IEC 62443 clause numbers were not verified and are not asserted here — see the
[IEC 62443 page]({{ '/standards/cybersecurity/iec-62443/' | relative_url }}) for that standard.)*

## Design takeaways

- A learned component may **inform or propose**; an independent, verifiable layer **decides and
  protects**. Design the two separately.
- Do **not** attempt to certify a learned component to a safety integrity target against ISO 13849-1,
  IEC 62061, or IEC 61508 — there is no route, and TS 22440 is not yet published.
- For EU-market machinery with a self-evolving safety component, expect **mandatory notified-body
  assessment**; keep the system **correctable at all times**; prevent hazardous self-modification
  **including during learning** (Machinery Regulation Annex III EHSR 1.2.1).
- Keep the AI service **read-only and least-privilege** inside the OT security zones; publish a result
  contract, never a raw stream, across a conduit.

## Review status

This page is distilled from a corpus-owned Draft note and is **Review pending**. Editions and dates
are recorded as verified at the publisher in July 2026; confirm against the governing text before
relying on them. Return to the [authority gate]({{ '/design/ai-integration/' | relative_url }}) or the
[method register]({{ '/design/ai-integration/method-register/' | relative_url }}) for the rest of the
section.
