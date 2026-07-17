<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# The digital twin as integration spine

This note is the corpus source for the site's Digital Twin page. It records what a digital twin is (and
is not), why the physical-to-digital and digital-to-physical directions are separate engineering
problems, and how the authority gate still governs anything the twin's models feed back to the plant.
It is a decision aid, not permission to deploy. Where a claim rests on a published framework it is
cited; where it is engineering judgement, it says so. The twin does not relax any ceiling in the
[method register](README.md) or any boundary in the [safety note](safety_boundary.md): a learned model
inside a twin holds exactly the authority the register assigns it, and no safety function routes
through the twin.

## 1. What a digital twin is — and the distinction that matters

A published framework already defines the term. **ISO 23247 (Digital Twin Framework for Manufacturing)**
defines a digital twin as a *"fit for purpose digital representation of an observable manufacturing
element with synchronization between the element and its digital representation."* Two words in that
definition carry the weight: **synchronization** (the digital side is kept current with the physical
side) and **fit for purpose** (the twin is scoped to a use case, not a general-purpose replica).

The distinction the rest of this note turns on is the direction and richness of that synchronization:

- **A live data mirror** is a connected view — dashboards, tags, historian trends. It has *one-way*
  synchronization: it receives data from the physical asset and shows it. It is useful and it is not a
  behavioural twin. (The reference literature makes the same point: long-standing jet-engine
  monitoring "twins" *"receive data from the physical object but do not provide control feedback"* —
  one-way synchronization.)
- **A behavioural twin** adds asset identity and relationships, calibrated behavioural models
  (estimation, simulation, prediction, diagnosis, optimisation), lifecycle history, and validated use
  cases on top of the synchronized state. It can answer "what is happening that I cannot measure" and
  "what happens next," not only "what does the sensor read."

A dashboard becomes more twin-like as it gains asset identity, state synchronization, behavioural
models, calibration, lifecycle history, and validated use cases — it is a spectrum, not a badge.
**Honest caveat:** the field has no single agreed definition; ISO 23247 is a *manufacturing* framework
and a reference architecture, **not** a functional-safety or model-validation standard. Synchronization
is not authority — being current says nothing about being correct, and nothing in ISO 23247 lets a
learned model hold a safety function.

## 2. The framework's shape — a reference architecture, not a product

ISO 23247 is a **four-part series (2021)** — Part 1 overview and general principles, Part 2 reference
architecture, Part 3 digital representation, Part 4 information exchange — extended by Part 5:2026
(digital thread). Its reference model is organised as **four domains**:

- **Observable manufacturing domain** — the physical Observable Manufacturing Elements (OMEs):
  equipment, material, process, personnel — the thing being twinned.
- **Device communication domain** — the layer between the OMEs and their twins that carries data
  exchange **and synchronization**, and (the standard is explicit) also transfers commands and signals
  for control and actuation. This is the layer where the authority question lives.
- **Digital twin domain** — the twin's own state, models, and services.
- **User domain** — applications and people consuming the twin.
- A **cross-system entity** spans the domains for data translation, data assurance, and security.

The value of citing the framework is not that a site must adopt it verbatim — it is that the twin is a
**reference architecture with named seams**, and the seam that matters for AI safety is the device
communication domain, because that is where a digital output can become a physical action.

## 3. Physical-to-digital and digital-to-physical are separate problems

Treating "the twin" as one bidirectional pipe hides the two hardest questions. Split it.

**Physical-to-digital (getting the twin honest).** The engineering here is data integrity, not
modelling flair:

1. Identify the asset, sensor, engineering unit, range, and meaning of every input.
2. Preserve source timestamp, acquisition timestamp, quality, and missing-data state.
3. Align data with PLC scan, camera trigger, batch, recipe, mode, and event context.
4. Reject or mark stale, substituted, frozen, impossible, and out-of-sequence data.
5. Estimate twin state and record which values are **measured, derived, or predicted** — never let a
   prediction silently read as a measurement.
6. Compare predicted state with observed state; monitor residuals and drift.
7. Recalibrate or retire models through controlled lifecycle procedures.

**Digital-to-physical (letting the twin act — carefully).** This direction is governed by the same
authority ladder as every other learned output. A twin's model output is not privileged by living in a
twin; it is capped at the register ceiling for that model family, and an independent non-learned layer
holds the veto:

| Level | Twin / model output | Control-system treatment |
|---|---|---|
| 0 | Offline analysis | No online interface |
| 1 | Monitoring result | Read-only visualisation and logging |
| 2 | Advisory recommendation | Operator evaluates and acts separately |
| 3 | Proposed command / setpoint | Operator confirms through a governed workflow |
| 4 | Bounded supervisory output | A non-learned layer independently checks enable, range, rate, mode, freshness, permissives |
| 5 | Direct learned control | Not assigned to any learned twin output here |

Regardless of level, independent trips, interlocks, safety functions, equipment limits, and manual
fallback stay effective when the twin or its models are **wrong, stale, unavailable, or compromised**.
This is the same envelope architecture as the gate page — the twin is where the models live; the
envelope is still what protects the plant.

## 4. The data contract between twin and control system

Because the device-communication seam can carry an action, the payload crossing it must be
self-describing enough to be *gated*. Candidate fields:

- Asset and signal identifier; request / correlation ID.
- Source and inference timestamps; input and output quality.
- Value, class, prediction horizon, and uncertainty / confidence.
- Model name, version, feature-pipeline version, calibration version.
- Valid-until / maximum-age; twin synchronization state.
- Service health and fallback state.
- Requested authority level and action type.
- Acknowledgment, rejection reason, and audit identity.

The last three lines are what let the non-learned gate do its job: a proposal that names its requested
authority, carries a freshness bound, and records why it was accepted or rejected is one a verifiable
layer can accept, clamp, or veto — and one an audit can reconstruct after the fact.

## 5. The model families inside the twin

The twin is a spine; the models hanging off it are the same families the register scores, at the same
ceilings (see [Model Families & Fit](model_families.md)):

- **CNN / perception** turns images, thermal frames, and 1-D signals into features or classes for the
  twin — advisory only; a classification must not silently become a plant fact.
- **PINN / physics models** connect sparse measurements to unmeasured state (parameter/field estimation,
  calibration, surrogates) — the physics term constrains learning but does not prove accuracy,
  stability, real-time performance, or validity outside the calibrated regime; never close a loop on it.
- **LLM / knowledge** operates over the twin's semantic and historical context through read-only,
  allow-listed tools — it consumes curated twin context, not raw tag streams, and its proposals need
  schema validation, authorization, and (where required) human confirmation.

## 6. What this means for design

- **Say which state is measured, inferred, simulated, or manually entered** — and keep predictions
  visibly distinct from measurements in the twin's own state.
- **Design the two directions separately.** Physical-to-digital is a data-integrity problem; solve
  staleness, aliasing, and provenance before trusting any model output.
- **The twin grants no authority.** A model's placement on the ladder comes from the register and the
  safety boundary, not from the fact that it now lives in a twin. The device-communication seam is
  gated by the non-learned envelope.
- **Match synchronization tightness and prediction horizon to the process.** Ask how tightly each use
  case must synchronize, what horizon is useful relative to process dynamics and action time, and what
  happens when the AI output is late, missing, low-confidence, or contradictory.
- **Own model change control.** Who approves a model change, and who approves a change to its allowed
  authority, must be defined before either happens.

## Sources

- **ISO 23247, Digital Twin Framework for Manufacturing** — Parts 1–4 (2021: overview, reference
  architecture, digital representation, information exchange), Part 5 (2026, digital thread). Definition
  and four-domain reference model as summarised by the NIST analysis below; the ISO body was not read
  (ISO catalogue blocks automated retrieval), so nothing here implies knowledge of its clause text.
- **NIST, "Digital Twins for Advanced Manufacturing: The Standardized Approach"** (government
  publication) — source for the verified ISO 23247 definition (*"fit for purpose digital representation
  of an observable manufacturing element with synchronization between the element and its digital
  representation"*), the four-domain reference model, and the one-way-vs-two-way synchronization
  distinction (jet-engine monitoring twins receive data but give no control feedback).
- **NIST SP 800-82 Rev. 3** — OT security placement for the device-communication seam (read-only by
  default, least privilege, inside the existing zones/conduits).
- Cross-references: [method register](README.md), [safety boundary](safety_boundary.md),
  [model families](model_families.md), [interfaces & edge](interfaces_edge.md) for the transport and
  result-contract mechanics of the device-communication seam.

## Changelog

- 2026-07-17 — Slice E corpus note drafted from the Phase 49a research note
  `digital-twin-integration.md`, re-verified before promotion. The twin **definition and four-domain
  reference model were grounded in ISO 23247** (verified via a NIST government publication citing the
  standard; the ISO body itself was not read), replacing the note's unsourced working definition. The
  mirror-vs-behavioural distinction is now anchored on ISO 23247's *synchronization* and the
  one-way/two-way sync distinction. No authority ceiling was changed; the digital-to-physical ladder is
  the register's. Review pending.
