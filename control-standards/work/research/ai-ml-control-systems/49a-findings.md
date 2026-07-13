# Phase 49a — Findings and Go/No-Go

**Generated:** 2026-07-13 · **Status:** Work tier — non-authoritative research capture.
**Inputs:** `evidence-table.md` (98 claims) · `authority-ceilings.md` · `adversarial-verdicts.md`
**Spec:** `docs/superpowers/specs/2026-07-12-ai-ml-methods-register-design.md`

---

## 1. The headline

**The register's central column now has a legal and standards basis — and it is more constraining than
"AI is high-risk."**

The primary hypothesis survived verification, with one correction: the document is **ISO/IEC TR
5469:2024** (a joint ISO/IEC JTC 1/SC 42 Technical Report), **not "IEC TR 5469."** Edition 1.0,
published 2024-01-08, 73 pp — verified on the IEC webstore. Critically, it is a **Technical Report:
guidance, not a certifiable requirement set.** The requirement-bearing successor, **ISO/IEC TS 22440**,
is still at committee-draft stage.

So the position as of today is:

> **There is no published normative standard against which a learned closed-loop safety function could
> be certified.** TR 5469 exists *precisely because* compliance with the existing functional-safety
> standards cannot be shown directly for AI.

And the law has moved ahead of the standards. **Regulation (EU) 2023/1230** (Machinery) — verified
against the official OJ text — lists **"safety components with fully or partially self-evolving
behaviour using machine learning"** in Annex I Part A (items 5 and 6). Consequences: mandatory
notified-body conformity assessment, **self-declaration is not available**; and Annex III EHSR 1.2.1
imposes a **statutory authority ceiling** — a self-evolving system shall not act beyond its defined task
and movement space, it must be correctable at all times, and hazardous self-modification of safety rules
(**including during the learning phase**) must be prevented.

That is **level ≤ 4, codified.** The EU AI Act then binds to the same route: Article 6(1) makes an AI
system high-risk where it is a safety component of a product requiring third-party assessment, and the
machinery route applies. The two regimes bite about six months apart (**machinery 20 Jan 2027; AI Act
Art. 6(1) obligations 2 Aug 2027**).

**Bonus for the existing site:** the sprint independently confirmed that Phase 45's **20 January 2027**
Machinery Regulation date is correct — but *only by virtue of the corrigendum*. The uncorrected OJ text
says 14 January. The site is right and the reason it is right is now documented.

---

## 2. Three places the sprint proved the orchestrator wrong

Recorded prominently, because the design was built to survive exactly this.

**(a) "kHz signals cannot be fed through OPC UA" — FALSE as stated, and it must not go on the site in
that form.** OPC UA sampling intervals have no floor in the specification, and OPC UA PubSub/UADP over
TSN has been measured at a **250 µs cycle (4 kHz)** with sub-microsecond jitter. The protocol is not the
bottleneck.

The reasoning still holds, but it rests on **four different constraints**, none of which is "the
protocol is too slow":

1. **Server floor.** OPC UA Part 4 makes sampling *best-effort*, requires the server to return a
   `revisedSamplingInterval` it can actually meet, and Part 5 defines `MinSupportedSampleRate` — the
   spec *anticipates* a server-imposed floor. One mainstream PLC's embedded OPC UA server publishes a
   minimum sampling interval of **10–100 ms** depending on CPU. That is two to three orders of magnitude
   short of kHz.
2. **Decoupled source / aliasing — the killer, and it is spec-level.** Part 4 concedes the server
   *"provides access to a decoupled system and therefore has no knowledge of the data update logic."*
   **You cannot recover a waveform by oversampling a tag whose source updates once per PLC scan.**
3. **The historian is a compressor, not a recorder.** Deadband and swinging-door compression decimate by
   design. A feature pipeline reading archives gets decimated data.
4. **Segmentation.** Pushing kHz across the IT/OT boundary means widening a conduit NIST SP 800-82r3
   tells you to keep narrow.

The conclusion — **inference on kHz signals belongs at the edge; only the result crosses into SCADA** —
survives, and NIST SP 800-82r3 independently supports it. But the *argument* must be rewritten. A
knowledgeable reader would have caught the original claim, and rightly.

**(b) OPC UA has no native way to carry a model result.** A significant negative finding. `DataValue`
has exactly six fields; quality is a **3-class StatusCode**, not a confidence number; there is **no OPC UA
companion specification for AI/ML inference results.** Anyone claiming OPC UA "has" an AI result model is
wrong. What it *does* give you: custom **Structured DataTypes** (the sanctioned way to define a
`ModelResult` struct), `Uncertain_LastUsableValue` / `Uncertain_SubNormal` as an idiomatic "model
degraded / inputs missing" channel, `SourceTimestamp` for freshness, and — under-used in AI-in-OT
writing — **Part 9 Alarms & Conditions**, which is the *correct* construct for an AI advisory requiring
human acknowledgement. **Sparkplug B is better provisioned out of the box** (arbitrary per-metric
properties, plus a first-class STALE quality).

Write-authority separation, by contrast, is **fully spec-backed and is the strongest part of the whole
sprint**: OPC UA separates read from write at three stacked layers, and the well-known **Observer** role
(browse/read/subscribe, *no write*) maps exactly onto an edge inference service that publishes results
and must never write setpoints. **The architecture I proposed is expressible in the standard without
invention.** Sparkplug's equivalent is a *convention you must enforce*, not a guarantee you inherit.

**(c) The accelerometer-vs-drive-current question is answerable — and the answer went against drive
current.** Paderborn genuinely carries synchronously sampled motor phase current **and** vibration, same
rig, same 32 bearings, same 64 kHz. And vibration beat motor-current in **every** case tested: 98.3% vs
93.3% on real damage, and — in the realistic train-on-artificial / test-on-real case — **75.0% vs
45.9%**, i.e. both collapse and current collapses further. Current-only bearing diagnosis is a
**cost-driven degradation, not an equivalent.** This is a genuinely publishable result and no vendor
whitepaper will state it.

---

## 3. Go / No-Go by domain

| Domain | Verdict | Conditions |
|---|---|---|
| **Core AI/ML (CNN, PINN, LLM, RL)** | **GO** | Strongest-evidenced domain, and the evidence is mostly *negative* — which is exactly what makes the register worth publishing. Ceilings per `authority-ceilings.md`. |
| **Interfaces & edge (SCADA/OPC UA/MQTT)** | **GO, with a mandatory rewrite** | The kHz claim must be reworded per §2(a). Cite NIST SP 800-82r3, never a 62443 clause number. Do not assert a general "SCADA poll rate". |
| **Classical & deterministic baselines** | **GO** | Well-sourced, and they win most head-to-head comparisons. This is the column against which every ML row is judged. |
| **Chemical / process models** | **PARTIAL — proceed with the structure, not the ceilings** | The conservation-law-vs-kinetic-closure split is well sourced and should be the spine. But **no adversarial coverage**, and the equilibrium/thermodynamics family has **no verified source at all** (publisher 403). |
| **Biological / microbiological** | **PARTIAL — reality check only** | What industry *actually does* (PID + open-loop feed profiles; Raman/PLS the narrow exception) is verified and worth publishing. **No adversarial coverage**; no authority claims may be made. |

**No domain is blocked outright.** Two are constrained to structure-and-reality rather than
authority-and-ceilings, which is a weaker but honest posture.

---

## 4. The highest-value next actions

1. **Buy ISO/IEC TR 5469:2024** (73 pp, ISO/IEC). Its **Usage Level × Technology Class matrix** is the
   single most directly relevant artefact for setting authority ceilings, and the free preview truncates
   immediately before it. Everything in the register's `authority_basis` column would be stronger for it.
2. **Check IEC 62061** for ML/self-evolving content. It was not examined, and no page may claim "no
   machinery functional-safety standard addresses learned components" until it is.
3. **Obtain the four paywalled papers** that carry load-bearing numbers: Smith & Randall 2015 (the
   >40 kHz criterion and the CWRU data-quality critique); Hendriks et al. 2022 (the 95%→53% leakage
   result); Naser 2025 (the only source attacking PINNs in an *engineering-systems* framing); the
   lab-to-field transfer-learning assessment.
4. **Resolve the FP64 question.** A 2025 preprint reportedly argues that some canonical PINN failure
   modes are **artefacts of FP32 arithmetic**, rescued by double precision. If true it weakens the
   framing — and it has a sharp control-systems implication, since embedded targets run FP32 or
   fixed-point: *a PINN well-behaved on an FP64 workstation could fail on the deployment hardware.*
5. **Re-run the adversarial pass for chemical and biological.** They have none.

---

## 5. Open gaps carried forward

Full per-workstream detail is in `evidence-table.md`. The ones that constrain what may be written:

- **TR 5469's body is unread** (paywalled). Nothing may imply knowledge of its internal clauses.
- **IEC 61508-3 Table A.2 ratings: UNVERIFIED.** Do not publish.
- **No ISO-derived vibration sample-rate figure may be asserted** — ISO's platform refused retrieval, so
  the kHz-bandwidth requirement is engineering judgement only. This gap sits *directly underneath* the
  motivating example, which is uncomfortable and should be said out loud.
- **Licences.** Paderborn is **CC BY-NC 4.0 — NonCommercial**, redistributable with attribution.
  **CWRU has no licence, no terms of use, and no redistribution statement of any kind**; third-party
  mirrors assert CC terms that trace to no grant by CWRU. **Cite and link CWRU; never redistribute it.**
- **No source measures learned fault diagnosis on a real industrial fleet.** Every number in the field
  comes from a lab rig.
- **No standard says how good an ML model must be** to hold any safety authority. The void is the
  finding.

---

## 6. Recommendation

**Proceed to Phase 49b** for the core AI/ML, interface, and classical-baseline domains — the evidence is
strong, and it is *strong in the negative direction*, which is precisely the register's value. A
catalogue whose honest conclusion is usually "the deterministic method wins, and no learned method may
hold the safety function" is worth far more than one that enumerates capabilities.

**Hold the chemical and biological authority columns** until they have adversarial coverage. Their
*structure* (conservation laws as hard constraints; kinetic closures as the soft, fitted layer where
data-driven models earn their place) and their *reality check* (industrial bioprocess still runs on PID)
can be written now.

**Still outstanding and unchanged:** the owner has not confirmed the `/design/ai-integration/` placement.
That remains a precondition for 49b.
