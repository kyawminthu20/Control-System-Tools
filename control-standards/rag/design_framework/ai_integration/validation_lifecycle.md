<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Validation, drift, and the model lifecycle

This note is the corpus source for the site's Validation & Lifecycle page. It records what has to be
true *over time* for a learned component to keep whatever authority the register grants it — data
lineage, honest test sets, uncertainty, drift and out-of-distribution detection, a defined failure
response, human review, rollback, and change control — and how the NIST AI Risk Management Framework
supplies the vocabulary for that work. It is a decision aid, not permission to deploy. Where a claim
rests on a published framework it is cited; the frameworks named here are **process guidance, not
functional-safety permission** — none of them lets a learned component hold a safety function (see the
[safety boundary](safety_boundary.md)).

## 1. Why the lifecycle is the point

A learned component is not validated once and finished. Its behaviour comes from training data, so it
degrades as the plant, the sensors, the product, and the environment drift away from the conditions it
learned. Everything on the [gate page](README.md) — the authority a method may hold — is conditional on
this ongoing work: **the authority is only as current as the last evidence that the model still
behaves.** A model that was advisory-grade in commissioning can silently become worse than useless a
year later, and nothing about its output announces the change. The lifecycle is the mechanism that
keeps the authority claim honest.

## 2. The vocabulary: NIST AI Risk Management Framework

Two published NIST documents give this work a shared, non-proprietary vocabulary:

- **NIST AI RMF 1.0 (NIST AI 100-1, January 2023)** organises AI risk work around four functions —
  **Govern, Map, Measure, Manage** — and a set of trustworthiness characteristics (valid and reliable,
  safe, secure and resilient, accountable and transparent, explainable and interpretable,
  privacy-enhanced, fair). It is **voluntary guidance**, not a control-system standard and not a
  certification.
- **NIST AI RMF: Generative AI Profile (NIST AI 600-1, 26 July 2024)** is a *"cross-sectoral profile of
  and companion resource for the AI RMF 1.0"* — it does not replace it. It adds generative-AI-specific
  risks (for example **confabulation** — plausible, fluent, wrong output — and information integrity,
  data privacy, and information security concerns) and suggested actions organised under the same four
  functions. It is the relevant companion whenever an **LLM** appears in the architecture (draft-then-
  verify code, a read-only copilot).

Use these for **vocabulary and process structure** — what to govern, what to measure, what to manage —
not as evidence that a model may hold authority. That evidence comes from the register and the safety
boundary. (The base framework is `nist_ai_rmf`; the generative companion is `nist_genai_profile`.)

## 3. The lifecycle demands, mapped to the RMF functions

### Govern — who owns the model and its authority

- A named owner for each model, its allowed authority level, and any change to that authority.
- Management of change: a model update, a retrain, or an authority change goes through the same MoC
  discipline as a control-logic change — reviewed, approved, recorded, reversible.
- An audit trail sufficient to **reconstruct a decision** from data, model version, context, and the
  human action taken.

### Map — know what the model is for and where it breaks

- Data lineage: the provenance of every training and calibration input — asset, sensor, unit, range,
  licence, and collection conditions. (The dataset-licence discipline from
  [model families](model_families.md) lives here: a NonCommercial or unlicensed dataset constrains what
  may be shipped.)
- The **operating envelope**: the regime the model was validated in, and the known-invalid regimes
  where its output must be distrusted.
- Coupling and interface ownership when the model is one component of a larger twin.

### Measure — prove it works, honestly

- **Leakage-free test sets.** Split by held-out *components/assets*, not by held-out windows —
  window-level or by-load splits inflate accuracy to near-100% while the honest, component-wise number
  can be near chance (the fault-diagnosis result on the [model families](model_families.md) page).
  Assume any accuracy figure is leaky until the split protocol is disclosed.
- **Uncertainty, not just a point estimate.** A usable model output carries a confidence or an error
  band; a bare number invites misplaced trust.
- **Validate at the deployment conditions** — including numerical precision (the FP32/FP64 trap for
  PINNs) and the real sensor/actuator hardware, not only the bench.

### Manage — keep it honest in service, and fail safe

- **Drift and out-of-distribution detection.** Monitor input distribution and prediction residuals
  against the validated envelope; flag when the live regime has moved. A residual monitor is necessary
  but not sufficient — some failures (a PINN relaxing to a plausible wrong state) keep the residual low
  while the answer is wrong, so cross-checks against independent measurements matter.
- **A defined failure response.** When the model is stale, low-confidence, out-of-distribution,
  unavailable, or contradicted, the non-learned envelope applies the **hazard-analysis-derived**
  `on_fail` response — bumpless transfer to a base controller, a bounded-lifetime hold, manual takeover,
  a defined safe state, or shutdown — never a universal default. This is the same envelope as the gate.
- **Rollback.** Every deployed model version is retained and re-deployable; a bad update must be
  reversible to the last known-good version quickly, without a rebuild.
- **Human review** of advisories and of any proposed action above read-only, on a defined cadence and
  on every anomaly.

## 4. The model-evidence ledger

The durable artefact of all of the above is a per-component record — a **model-evidence ledger** — that
makes a learned component's evidence auditable in one place. Each twin/model component should record:

- Scientific domain and modelled phenomenon.
- Governing equations or causal assumptions; boundary and initial conditions.
- Material/chemical/biological parameters and their sources.
- Empirical correlations and their valid ranges.
- Learned components, datasets (with licence and provenance), and feature definitions.
- Calibration state and uncertainty.
- Spatial and temporal resolution.
- Coupling variables and interface ownership.
- Numerical solver and convergence criteria (and deployment precision).
- Validation experiments and acceptance limits.
- Known invalid regimes and the fallback behaviour when they are entered.
- Model version, authority level, owner, and change history.

A blank, fill-in version of this ledger is published as a downloadable template
(`ai_model_evidence_ledger.md`) so the record can be started at design time and maintained across the
model's life, not reconstructed after an incident.

## 5. What this means for design

- **Treat authority as perishable.** Re-earn it: schedule revalidation, monitor drift, and drop the
  authority when the evidence lapses.
- **Split test sets by component, carry uncertainty, and validate at deployment conditions** — bench
  accuracy is not field accuracy.
- **Wire the failure response into the non-learned envelope**, hazard-analysis-derived, and keep every
  model version rollback-ready.
- **Keep a model-evidence ledger from day one**, and put model changes through management of change.
- **Use NIST AI RMF for structure and vocabulary** (and the GenAI Profile for any LLM component) — and
  remember it is process guidance, not a route to safety authority.

## Sources

- **NIST AI RMF 1.0 (NIST AI 100-1, January 2023)** — the Govern/Map/Measure/Manage functions and
  trustworthiness characteristics; voluntary guidance, not a control-system standard.
- **NIST AI RMF: Generative AI Profile (NIST AI 600-1, 26 July 2024)** — verified at NIST as a
  cross-sectoral profile of and companion resource for the AI RMF 1.0 (not a replacement); adds
  generative-AI-specific risks and suggested actions under the same four functions.
- **NIST SP 800-82 Rev. 3** — OT security placement for any model service (read-only by default,
  least-privilege, inside existing zones/conduits).
- Model-evidence ledger fields adapted from the Phase 49a research note
  `scientific-domain-integration.md` (work tier).
- Cross-references: [method register](README.md), [safety boundary](safety_boundary.md),
  [model families](model_families.md), [digital twin](digital_twin.md).

## Changelog

- 2026-07-17 — Slice F corpus note drafted. The **NIST AI RMF Generative AI Profile (NIST AI 600-1)**
  was verified at the publisher (designation, 2024-07-26 date, companion-not-replacement status) —
  closing the item deferred from Phase 50.12 — and added as the LLM-relevant companion to the base
  framework. The model-evidence ledger from the research note was promoted to a downloadable template.
  No authority ceiling changed; NIST AI RMF is framed as process vocabulary, not safety permission.
  Review pending.
