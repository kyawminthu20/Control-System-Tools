<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# AI and the safety boundary — functional safety, law, and independence

This note is the corpus source for the site's Safety & Security Boundaries page. It records the
verified position on where a learned component may sit relative to a machine's safety functions, and
why. It is a decision aid, not permission to deploy a learned component in a safety role. Claims here
trace to the publisher or official text; where evidence is guidance or a preprint, it says so.

## 1. The core position

**There is no published normative standard against which a learned closed-loop safety function could
be certified today.** The functional-safety standards that machine builders use are deterministic
methodologies; the AI-specific functional-safety documents that exist are either guidance (a Technical
Report) or still in draft. Meanwhile, EU product law already treats a self-evolving safety component
as high-risk and caps what it may do. So the honest position is: the *law* has moved ahead of the
*standards*, and both point the same way — a learned policy may hold operational authority inside an
envelope, but a verified non-learned layer must hold the safety function and the veto.

## 2. The functional-safety standards are deterministic

- **ISO 13849-1:2023** — a deterministic methodology. Performance Level (PLr) is derived from the
  S/F/P risk graph in Annex A; the architecture, diagnostic coverage, and MTTFD accounting all assume
  behaviour that can be analysed in advance.
- **IEC 62061:2021 (Edition 2.0, 2021-03-22)** — "Safety of machinery — Functional safety of
  safety-related control systems." Verified at the IEC webstore (publication 59927): its scope covers
  the design, integration, and validation of safety-related control systems for machines within the
  **IEC 61508 framework**, and **makes no mention of artificial intelligence, machine learning, or
  self-evolving/adaptive components**.
- **IEC 61508:2010 (Ed. 2.0)** — the base E/E/PE functional-safety lifecycle. A systematic-capability
  and random-hardware-failure methodology; it provides no validation route for a component whose
  behaviour comes from training data.

None of these standards provides a way to demonstrate that a learned component meets a safety
integrity target. That is not an oversight to be worked around — it is the reason the AI-specific
documents below exist. (IEC's own AI-safety communications state that existing functional-safety
standards do not recommend the use of AI, including statistical machine learning.)

## 3. The AI-specific documents are guidance or draft — not a certification route

- **ISO/IEC TR 5469:2024**, "Artificial intelligence — Functional safety and AI systems." Edition 1.0,
  published 2024-01-08, 73 pp, joint ISO/IEC JTC 1/SC 42. Verified at the IEC webstore. **It is a
  Technical *Report* — guidance, not a certifiable requirement set.** Its existence is itself the
  argument: it was written because compliance with the existing functional-safety standards cannot be
  shown directly for AI. (Its body is paywalled and was not read; nothing here implies knowledge of
  its internal clauses. Note the identifier is **ISO/IEC** TR 5469, not "IEC TR 5469.")
- **ISO/IEC TS 22440** — the requirement-bearing successor, in three parts (Part 1 Requirements,
  Part 2 Guidance, Part 3 Examples of application). As of **February 2026** all three parts are at
  **Committee Draft (CD)** stage (ISO catalogue 89535/89536/89537). **Not yet published; it confers no
  certification route today.**
- **ISO/IEC 42001:2023** (AI management systems) and **ISO/IEC 23894:2023** (AI risk guidance) are
  both published, but **neither confers any technical permission for AI to participate in a safety
  function**, and neither is harmonised for machinery.

## 4. The law leads the standards — and codifies the ceiling

- **Regulation (EU) 2023/1230 (Machinery Regulation).** Verified against the official OJ text.
  - **Annex I Part A, items 5 and 6** list *safety components with fully or partially self-evolving
    behaviour using machine learning*. Consequence: **mandatory notified-body conformity assessment —
    self-declaration is not available** for such components.
  - **Annex III EHSR 1.2.1** imposes a **statutory authority ceiling**: a self-evolving system shall
    not act beyond its defined task and movement space, it must be correctable at all times, and
    hazardous self-modification of safety rules must be prevented **including during the learning phase**.
  - **Date of application: 20 January 2027** — correct only by virtue of the Corrigendum of 4 July 2023
    (the uncorrected OJ text says 14 January).
- **Regulation (EU) 2024/1689 (AI Act).** Article 6(1) makes an AI system high-risk where it is a
  safety component of a product that requires third-party conformity assessment — the machinery route
  applies. Article 6(1) obligations apply **2 August 2027**, about six months after the Machinery
  Regulation.

Annex III EHSR 1.2.1 is, in effect, **authority level ≤ 4 written into law**: bounded task space,
always correctable, no hazardous self-modification. It is not a design preference; it is a legal
requirement for machinery placed on the EU market.

## 5. The architectural consequence

Every documented real deployment that the research reviewed — tokamak coil control, an 840-hour
reinforcement-learning distillation-column run, a learned road-vehicle motion planner — **keeps a
non-learned layer holding the veto.** The safe-learning-control literature (Brunke et al., *Annual
Review of Control, Robotics, and Autonomous Systems*, 2022) is candid that its guarantees "rely on a
set of assumptions … difficult to verify prior to operation" — a proof conditioned on an unverifiable
premise is a conditional theorem, not a safety case. The strictest sector position found is EASA's AI
Concept Paper (Issue 02): supervised, **offline learning only**, model frozen at approval, no adaptive
learning capability in operation.

The convergent pattern across standards, law, and deployment:

> The learned policy holds operational authority **inside an envelope**. A verified, non-learned layer
> holds the safety function and the veto. The safety-function path never routes through the learned
> layer, and the plant stays safe when the model is wrong, stale, unavailable, or compromised.

## 6. The cybersecurity boundary

An AI service is also an OT asset and must be placed accordingly. **NIST SP 800-82 Rev. 3** (Guide to
Operational Technology Security) supports edge-local computation and read-only monitoring as a
distinct, lower-impact class, and its segmentation guidance is the reason a learned service should be
**read-only by default, least-privilege, and inside the existing zone/conduit structure** — an edge
inference service publishes results and must not hold write access to setpoints. (Cite NIST SP
800-82r3 for this; specific IEC 62443 clause numbers were not verified and are not asserted.) OPC UA's
well-known **Observer** role — browse/read/subscribe, no write — maps exactly onto a publish-only
inference service and expresses this separation in the transport standard without invention.

## 7. What this means for design

- A learned component may **inform or propose**; an independent, verifiable layer **decides and
  protects**. Design the two separately.
- Do not attempt to certify a learned component to a safety integrity target against ISO 13849-1,
  IEC 62061, or IEC 61508 — there is no route, and TS 22440 is not yet published.
- For EU-market machinery with a self-evolving safety component: expect **mandatory notified-body
  assessment**, keep the system **correctable at all times**, and prevent hazardous self-modification
  **including during learning** (MR Annex III EHSR 1.2.1).
- Keep the AI service **read-only and least-privilege** inside the OT security zones; publish a result
  contract, never a raw stream, across a conduit.

## Sources

- IEC 62061:2021 Ed. 2.0 — IEC webstore, publication 59927 (verified: scope, edition, date; no AI/ML content).
- ISO/IEC TR 5469:2024 Ed. 1.0 — IEC webstore (verified existence/scope; body paywalled, unread).
- ISO/IEC TS 22440 Parts 1–3 — ISO catalogue 89535/89536/89537 (Committee Draft, Feb 2026).
- ISO/IEC 42001:2023; ISO/IEC 23894:2023 — IEC webstore (verified).
- ISO 13849-1:2023; IEC 61508:2010 Ed. 2.0 — deterministic functional-safety methodologies.
- Regulation (EU) 2023/1230 (Machinery) — official OJ text incl. Corrigendum of 4 July 2023.
- Regulation (EU) 2024/1689 (AI Act) — official text, Article 6(1).
- NIST SP 800-82 Rev. 3 — Guide to Operational Technology Security.
- EASA AI Concept Paper, Issue 02 — offline-learning-only position.
- Brunke et al., *Annual Review of Control, Robotics, and Autonomous Systems* 5 (2022) — safe-learning survey.

## Changelog

- 2026-07-17 — Slice B corpus note drafted from the Phase 49a evidence findings; the IEC 62061 ML-content
  gap was closed and the ISO/IEC TS 22440 status updated at the publisher during Slice B. Review pending.
