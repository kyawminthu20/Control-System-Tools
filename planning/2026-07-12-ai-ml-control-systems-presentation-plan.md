# AI/ML for Control Systems — Presentation Plan (Phase 49)

**Recorded:** 2026-07-12
**Status:** **Plan only. No site or corpus content is authorised by this document.**
**Source material:** `control-standards/work/research/ai-ml-control-systems/`
(relocated 2026-07-12 from `temp/`; work tier = non-authoritative capture)

The owner's research workspace is self-labelled *"Research staging only … Nothing
here is authoritative site or RAG content"* and carries an explicit
do-not-build-yet posture. **This plan honours that.** It decides *how the material
would be presented if and when it is promoted*, and what must be true before a
single page ships. It does not promote anything.

---

## 1. The one structural change I would make

The research file `research-map.md` §5 proposes a provisional site shape,
**topic-first**:

```text
├── Foundations and model-selection guide
├── CNNs for machine vision and industrial signals
├── PINNs and hybrid physics/data models
├── LLMs, RAG, copilots, and agents
├── Industrial data and interface architectures
├── Edge deployment and model serving
├── Verification, monitoring, and model lifecycle
├── Safety and cybersecurity boundaries          <-- 8th of 9
└── Worked architectures and decision matrices
```

**The ordering is the problem, not the content.** A topic-first tree lets a reader
arrive at "LLMs, RAG, copilots and agents", read it, and leave — having never
encountered the authority ladder or the safety boundary, which sit seven and eight
entries down. On a site whose entire premise is that safety functions are designed,
justified, and kept independent, that is the one failure mode we cannot ship.
People do not read reference sites front-to-back; they land mid-tree from search.

The research itself already contains the correct organising principle. From the
workspace README:

> Start with the least operational authority needed:
> `offline analysis -> read-only monitoring -> advisory recommendation ->
> operator-approved action -> bounded supervisory action -> direct closed-loop action`
> …Safety functions and basic equipment protection remain independent unless an
> applicable high-assurance engineering case explicitly establishes otherwise.

**Proposal: make the authority ladder the spine of the section, and hang the model
families off it — rather than making the model families the spine and appending
safety at the end.** Every page then inherits the gate instead of pointing at it.

This is the same editorial instinct the site already applies elsewhere: the wiring
guides lead with the safety notice, and the standards pages lead with the edition
and status. The reader meets the constraint before the capability.

---

## 2. Where it belongs in the taxonomy

**Recommendation: one new subsection under Design — `/design/ai-integration/`.**
Do **not** split it across Fundamentals and Design.

| Option | Verdict |
|---|---|
| **Design → `/design/ai-integration/`** | **Recommended.** The material's value is architectural: where a model sits in a control architecture, what authority it holds, how it hands off to a PLC, and what stays independent of it. That is a design question, and Design is where the site already answers "how do I build this correctly". |
| Fundamentals → `/fundamentals/ai-ml/` | Rejected as the primary home. Fundamentals explains *how a thing works* (motors, control theory, PLC software). A model-family explainer would fit — but placing it there separates the capability from the authority gate, which is exactly the failure mode in §1. |
| Split across both | **Rejected, and this is the load-bearing call.** A reader who lands on "CNNs" in Fundamentals from a search engine would meet the capability with no gate attached. Co-location is a safety property here, not a filing preference. |
| New top-level section | Rejected. The 9-section taxonomy is governed (CONTENT_STANDARDS); a tenth section for a research track that has not yet been validated would overstate its standing. |

**Consequence to accept:** the model-family explainer lives under Design even
though it reads like Fundamentals. That is a deliberate trade — one slightly
misfiled explainer is cheaper than an ungated capability page.

---

## 3. Proposed page structure

Authority-first. Seven pages, in reading order, each earning its place:

| # | Page | What it does | Why it exists |
|---|---|---|---|
| 1 | `/design/ai-integration/` (index) | **The authority ladder, and when *not* to use ML.** Opens with the six rungs (offline → read-only → advisory → operator-approved → bounded supervisory → closed-loop) and the rule that evidence, validation, monitoring and rollback requirements increase at every rung. Carries the decision matrix: deterministic logic, classical estimation, statistics, or MPC first — ML only when those genuinely cannot do the job. | The gate. Nothing else in the section is reachable without passing through it. |
| 2 | Safety and security boundaries | **AI does not implement a safety function.** Safety functions stay independent of any AI path, designed under ISO 13849-1 / IEC 62061 / IEC 61511. AI services sit inside IEC 62443 zones and conduits with least privilege; they do not get write access by default. Cross-links the functional-safety and 62443 pages. | Promoted from 8th to 2nd. This is the page the section exists to make unavoidable. |
| 3 | Model families and fit | CNNs (vision + 1-D signals), PINNs and hybrid physics/data models, LLMs, and the classical alternatives. **Structured as capability *and* poor-fit** — where each is wrong, not only where it is right. | The explainer, arriving *after* the gate. |
| 4 | The digital twin as integration spine | The working architecture is not "AI wired to a PLC" — it is physical process ↔ sensors/PLC → governed data interface → synchronised twin state → models → validation and authority gate → operator or bounded action. Physical-to-digital and digital-to-physical treated as **separate problems**, per the research. Includes the distinction the research is careful about: a live data mirror is not a behavioural digital twin. | The architectural centrepiece; the thing that makes the rest coherent. |
| 5 | Interfaces and handshakes | OPC UA information models, MQTT/Sparkplug, historians and REST; edge IPCs and model runtimes. The **PLC handshake contract**: valid, ready, result, confidence, timeout, health. The key separation the research already names — *OPC UA's capability to carry a command is not authorisation for AI to command*. | Where the abstraction meets real hardware. Strong tie-in to the existing Communications section. |
| 6 | Validation, drift, and model lifecycle | Data lineage, test sets, uncertainty, drift detection, out-of-distribution behaviour, fail-safe on model failure, human review, rollback, change control. The **model-evidence ledger** from `scientific-domain-integration.md` becomes a downloadable template under `/tools/templates/`. | The part vendors skip. Also the natural home for NIST AI RMF vocabulary. |
| 7 | Worked architectures | Vision inspection cell · predictive-maintenance pipeline · PINN soft sensor · LLM maintenance copilot on read-only plant context. Each worked through the ladder: *which rung, what evidence, what stays independent.* | The site's established habit — one worked example beats three abstractions. |

**Deferred:** the scientific-domain track (physics/chemistry/biology/microbiology/
space) in `scientific-domain-integration.md` is genuinely interesting and genuinely
enormous. It is **not** in the seven pages. It only earns a page once the
coupled-interface and time/length-scale questions have real sources behind them;
otherwise it becomes a taxonomy of things we have not verified.

---

## 4. Promotion gates — ALL must pass before any page ships

Carried over from the roadmap, plus the Phase 45 lessons:

- [ ] **The `source-register.md` "Sources still needed" list is filled.** It is
      currently eight items long and includes the load-bearing ones: peer-reviewed
      CNN fault-diagnosis surveys, PINN reviews covering *failure modes*,
      safe-learning-control research with explicit stability guarantees, and
      current standards/guidance for AI in machinery and functional safety.
      **Writing the safety page without that last item would be inventing a
      position.**
- [ ] **The two arXiv preprints are re-checked against the publisher.**
      LLM4PLC (arXiv 2401.05443) and Xia et al. (arXiv 2409.18009) are 2024
      preprints. Confirm whether each was peer-reviewed, superseded, or withdrawn
      before citing. *Phase 45 is the precedent: an unverified claim propagated
      into published content is exactly how the IEC 61511 "SIL 1–3" error and the
      fabricated 25 V AC threshold got onto the live site.*
- [ ] **Peer-reviewed claims are separated from vendor claims, visibly.** The
      research's own source policy already says this: vendor material is an
      implementation example, never proof of general capability. The pages must
      show which is which, not merge them into one confident voice.
- [ ] **Corpus first.** A corpus module
      (`control-standards/rag/standards_intelligence/…/ai_ml_control_systems/`)
      is written and passes the promotion checklist **before** any site page.
      Site pages present the corpus; they do not invent technical content.
      Then `python3 tools/generate_rag_tree.py`.
- [ ] **The least-authority framing survives into every page**, not just the index.
- [ ] **Every page states that safety functions remain independent of the AI path.**
- [ ] **Status: Review pending.** No AI-drafted page is ever marked *Reviewed* —
      only the author does that (CONTENT_STANDARDS §3).
- [ ] **Copyright:** original diagrams only. No vendor screenshots, no copied
      figures from papers. (The Phase 46 withheld-photograph decision is the
      standing precedent.)

**Owner decision still outstanding:** confirm the `/design/ai-integration/`
placement above, or overrule it. Nothing proceeds without that.

---

## 5. What is deliberately *not* being planned

- **No `cst` toolkit code.** No inference, no model serving, no ML dependencies in
  the Python package. This is a content track.
- **No closed-loop learned control content beyond describing it as the
  high-assurance research boundary it is.** The research names it as the far end of
  the ladder; the site should not read as a how-to for it.
- **No claim that any of this is standards-backed** until the "current standards or
  guidance for AI in machinery, functional safety, and critical infrastructure"
  source gap is actually closed. Right now the honest position is that this is
  emerging practice with a thin standards base, and the site should say so plainly
  rather than borrowing authority it has not got.

---

## 6. Sequencing

Phase 49, **after** Phases 47 (PLC software) and 48 (PLC/IPC hardware + vendor
index). Those two are ready to build from verified sources; this one is gated on
research the owner has not finished. Building it earlier would mean building it
on the "sources still needed" list — which is the thing this plan exists to
prevent.
