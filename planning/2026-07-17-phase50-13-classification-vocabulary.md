# Phase 50.13 — Classification Vocabulary for the Interactive Method Selector

**Status:** DRAFT — owner approval required before any canonical-schema change.
**Date:** 2026-07-17
**Scope:** proposal only. No `methods.yml` row, generator, or site data is changed by
this document. Implementation of 50.13 is gated on sign-off here.

## Why this exists

50.13 adds a dependency-light selector above the AI/ML method register that filters the
42 canonical rows by eight axes. The Phase 50 plan is explicit: **do not infer missing
classifications in page JavaScript.** Every filter must read a *validated canonical field*.
Four of the eight axes already exist; four are new and must be added to the schema, filled
on all 42 rows, and validated in `generate_ai_method_register.py`.

Two of the new fields (`safety_relevance`, `decision_type`) encode safety-significant
judgements across the whole register, which is why this is an owner decision and not an
autonomous edit.

## The eight filter axes

| Selector axis | Field | Status |
|---|---|---|
| Decision type | `decision_type` | **NEW** |
| Authority required | `max_authority` | exists (0–5 / Planned) |
| Deployment layer | `layer` | exists |
| Learned / deterministic class | `method_class` | **NEW** |
| Maturity | `maturity` | exists |
| Evidence strength | `evidence_strength` | exists |
| Data availability | `data_availability` | **NEW** |
| Safety relevance | `safety_relevance` | **NEW** |

## Proposed controlled vocabularies (new fields)

### `method_class` — is this machine learning or not?

| Value | Definition (inclusion test) |
|---|---|
| `deterministic` | Output is a fixed function of inputs once configured — physics, rules, or tuned gains. No parameters are fitted from a training dataset at deploy time. Repeatable: same input → same output. Classical estimators (Kalman/observers), MPC, SPC, and first-principles models are deterministic even where tuning uses measured data. |
| `learned` | Parameters are fitted from a training dataset (supervised, unsupervised, or reinforcement). Behaviour depends on that dataset. Includes pretrained foundation models used via prompting. |
| `hybrid` | A fixed physical/structural model **plus** a learned component (residual, closure, or embedded network). Neither part alone describes it. |

### `decision_type` — what kind of decision it supports

| Value | Definition |
|---|---|
| `regulatory-control` | Computes or commands a control action in a loop (including protective/limiting action). |
| `state-estimation` | Infers an unmeasured state, parameter, or quality variable (observers, soft sensors, reconciliation). |
| `monitoring-detection` | Flags anomalies, faults, or quality excursions for a human or downstream logic. |
| `prediction-simulation` | Predicts future values or what-if behaviour (forecasting, first-principles/physics simulation, prognostics). |
| `perception` | Interprets images or raw signals into labels/features. |
| `engineering-support` | Assists engineering work off the live control path (copilots, code drafting, model identification, agentic workflows). |
| `data-transport` | Moves or publishes results between systems (OPC UA/Sparkplug publication, historian pipelines, inference substrate, state sync). |

*(`optimization-scheduling` was considered and dropped — no current row is a pure planner/scheduler;
MPC and flux-balance are classed by primary intent, control and prediction respectively. Add the
value if a scheduling method is introduced.)*

### `data_availability` — measured-plant-data burden to deploy

Ordered by acquisition burden. This axis is specifically about **measured plant data**; a
method's dependence on physical constants / property data is already captured in the free-text
`data_requirement` and does not raise this level.

| Value | Definition |
|---|---|
| `none-or-spec` | Configured from equations, rules, datasheets, or known physical constants. No measured dataset. |
| `commissioning-tests` | Step/bump tests or short operating records for tuning or identification. No training corpus. |
| `operating-history` | A body of (unlabelled) normal operating history. |
| `labelled-examples` | Paired input→target data — classification labels, annotated images, or regression targets (e.g. lab reference assays). |
| `pretrained-plus-context` | An external pretrained model plus local prompt/context; no local training set. |

### `safety_relevance` — role the output may play relative to safety

Conservative three-level scheme that encodes the register's governing architecture: **the
verified non-learned layer holds the safety function and the veto; the learned policy only
holds operational authority inside an envelope.**

| Value | Definition |
|---|---|
| `safety-related` | May sit in the protective layer or act as the verified veto/limit. **Must be deterministic and verifiable.** |
| `safety-adjacent` | Can inform or drive an operational decision on the live plant (advisory included — operators act on advice), but must **not** be the safety function; an independent protective layer is required. |
| `non-safety` | Off-line or engineering-only, output reviewed/verified by a person before use, with no path to a hazardous action. |

## Cross-field invariants (enforced by the generator)

1. **`safety_relevance == "safety-related"` ⟹ `method_class == "deterministic"`.**
   No learned or hybrid method may be classed safety-related. This is the single most
   important guardrail and directly encodes the Phase 49a finding.
2. **`safety_relevance == "safety-related"` ⟹ `max_authority != "Planned"`.**
   A protective-layer claim cannot ride on an undetermined authority ceiling.
3. **`data_availability == "pretrained-plus-context"` ⟹ `method_class == "learned"`
   and `safety_relevance != "safety-related"`.**
4. Every value must be a member of its controlled set (membership check per row).

Under the proposed assignments below, exactly two rows are `safety-related` — `rule_engine`
and `robust_mpc_safety_filter` — both deterministic, both with a real authority value.
Invariants 1–3 hold for all 42 rows.

## Proposed per-row assignments (for review)

Chemical/biological rows carry `max_authority: Planned` and received no adversarial authority
coverage (Phase 49a hit a session limit). Their `safety_relevance` below is therefore marked
**provisional** and must not be treated as a cleared claim until the deferred adversarial review
runs — the same posture as their Planned authority.

### classical-deterministic

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| pid_control | deterministic | regulatory-control | commissioning-tests | safety-adjacent |
| feedforward_control | deterministic | regulatory-control | commissioning-tests | safety-adjacent |
| rule_engine | deterministic | regulatory-control | none-or-spec | **safety-related** |
| system_identification | deterministic | engineering-support | commissioning-tests | non-safety |
| statistical_process_control | deterministic | monitoring-detection | operating-history | safety-adjacent |
| first_principles_solver | deterministic | prediction-simulation | none-or-spec | safety-adjacent |

### estimation

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| kalman_filter | deterministic | state-estimation | commissioning-tests | safety-adjacent |
| nonlinear_state_estimator | deterministic | state-estimation | commissioning-tests | safety-adjacent |
| pca_pls | learned | monitoring-detection | operating-history | safety-adjacent |
| gradient_boosted_trees | learned | prediction-simulation | labelled-examples | safety-adjacent |
| gaussian_process | learned | state-estimation | labelled-examples | safety-adjacent |
| learned_soft_sensor | learned | state-estimation | labelled-examples | safety-adjacent |
| online_adaptive_learning | learned | state-estimation | operating-history | safety-adjacent |

### optimisation

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| moving_horizon_estimation | deterministic | state-estimation | commissioning-tests | safety-adjacent |
| model_predictive_control | deterministic | regulatory-control | commissioning-tests | safety-adjacent |
| robust_mpc_safety_filter | deterministic | regulatory-control | none-or-spec | **safety-related** |
| reinforcement_learning_policy | learned | regulatory-control | operating-history | safety-adjacent |

### perception

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| one_dimensional_cnn | learned | perception | labelled-examples | safety-adjacent |
| two_dimensional_cnn | learned | perception | labelled-examples | safety-adjacent |
| temporal_transformer | learned | prediction-simulation | operating-history | safety-adjacent |
| autoencoder_anomaly_detection | learned | monitoring-detection | operating-history | safety-adjacent |

### physics-informed

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| pinn_forward_model | hybrid | prediction-simulation | none-or-spec | non-safety |
| pinn_inverse_model | hybrid | state-estimation | operating-history | non-safety |
| hybrid_residual_model | hybrid | prediction-simulation | operating-history | safety-adjacent |
| hybrid_chemical_closure | hybrid | prediction-simulation | operating-history | safety-adjacent *(provisional)* |

### language/agentic

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| llm_engineering_copilot | learned | engineering-support | pretrained-plus-context | non-safety |
| llm_plc_code_draft | learned | engineering-support | pretrained-plus-context | non-safety |
| agentic_engineering_workflow | learned | engineering-support | pretrained-plus-context | non-safety |

### interface

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| edge_inference | deterministic | data-transport | none-or-spec | safety-adjacent |
| opcua_ai_result_publication | deterministic | data-transport | none-or-spec | safety-adjacent |
| sparkplug_ai_result_publication | deterministic | data-transport | none-or-spec | safety-adjacent |
| historian_feature_pipeline | deterministic | data-transport | none-or-spec | non-safety |
| digital_twin_state_sync | deterministic | data-transport | none-or-spec | safety-adjacent |

### chemical-kinetic *(safety_relevance provisional — Planned authority)*

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| mass_energy_balance | deterministic | state-estimation | none-or-spec | safety-adjacent *(prov.)* |
| arrhenius_kinetics | deterministic | prediction-simulation | commissioning-tests | non-safety *(prov.)* |
| equilibrium_thermodynamics | deterministic | prediction-simulation | none-or-spec | non-safety *(prov.)* |
| transport_pde_model | deterministic | prediction-simulation | none-or-spec | non-safety *(prov.)* |

### biological *(safety_relevance provisional — Planned authority)*

| id | method_class | decision_type | data_availability | safety_relevance |
|---|---|---|---|---|
| monod_growth_model | deterministic | prediction-simulation | commissioning-tests | non-safety *(prov.)* |
| fed_batch_feed_profile | deterministic | regulatory-control | commissioning-tests | safety-adjacent *(prov.)* |
| raman_pls_soft_sensor | learned | state-estimation | labelled-examples | safety-adjacent *(prov.)* |
| metabolic_flux_balance | deterministic | prediction-simulation | none-or-spec | non-safety *(prov.)* |
| advanced_bioprocess_control | hybrid | regulatory-control | operating-history | safety-adjacent *(prov.)* |

## Rows I want you to confirm (genuine judgement calls)

1. **`safety-related` set = {rule_engine, robust_mpc_safety_filter} only.** Everything else that
   touches live control is `safety-adjacent`, including basic PID and MPC (they are BPCS, not the
   safety function). Confirm this conservative boundary.
2. **Advisory (auth 2) methods are `safety-adjacent`, not `non-safety`.** Rationale: operators act
   on advice, so a wrong soft-sensor/anomaly output has a live-plant consequence. Alternative: treat
   auth ≤ 2 with a human in the loop as `non-safety`. Your call on which risk posture the field encodes.
3. **`gradient_boosted_trees` decision_type** = `prediction-simulation` vs `state-estimation`
   (it is generic; classed by typical soft-sensing use it would be state-estimation).
4. **`advanced_bioprocess_control` method_class** = `hybrid` (assumed MPC+ML); confirm or set to
   `learned`/`deterministic` per the intended definition.
5. **`historian_feature_pipeline` = `non-safety`** (offline analytics prep) vs `safety-adjacent`
   (if features later feed online models).

## Implementation once approved (50.13)

1. Add `method_class`, `decision_type`, `data_availability`, `safety_relevance` to
   `REQUIRED_METHOD_FIELDS` and add the four `ALLOWED_*` sets in
   `tools/generate_ai_method_register.py`; enforce membership + the four invariants above; extend
   `tests/tools/test_generate_ai_method_register.py` (vocabulary membership + each invariant, incl.
   a failing fixture where a learned row is marked safety-related).
2. Backfill the four fields on all 42 rows in
   `control-standards/rag/design_framework/ai_integration/methods.yml` per the approved table;
   regenerate `docs/_data/ai_methods/`.
3. Build the selector on `/design/ai-integration/`: filters derive only from these validated
   fields; state preserved in query parameters (linkable/reviewable); a fully usable no-JavaScript
   register and deep method anchors retained; accessible keyboard/screen-reader behaviour.
4. Test the filter vocabulary and the URL round-trip; site + full release gates green.
