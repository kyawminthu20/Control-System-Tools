# Digital Twin Integration with Real-World Control Data

## Working definition

For this research, a digital twin is a maintained digital representation of a
specific physical asset, machine, process, or system. It combines identifiable
asset context and synchronized operational state with one or more behavioral
models capable of estimation, simulation, prediction, diagnosis, or optimization.

A dashboard showing live tags is a connected data view. It becomes more
twin-like as it gains asset identity, relationships, state synchronization,
behavioral models, calibration, lifecycle history, and validated use cases.

## Closed cyber-physical loop

```text
                         PHYSICAL SIDE
 process -> sensors -> PLC/DCS -> actuators -> process
                 |                     ^
                 | telemetry           | approved/bounded action
                 v                     |
        acquisition and context        |
        - timestamps and quality       |
        - units and engineering ranges |
        - asset/tag identity           |
        - operating mode and recipe    |
                 |                     |
                 v                     |
                      DIGITAL SIDE     |
        synchronized digital-twin state|
                 |                     |
     +-----------+-----------+         |
     |           |           |         |
    CNN         PINN        LLM        |
 perception   physics/     knowledge/  |
 features     estimation   interaction |
     |           |           |         |
     +-----------+-----------+         |
                 |                     |
       prediction / diagnosis /        |
       simulation / recommendation     |
                 |                     |
                 v                     |
        validation and authority gate -+
```

## Responsibilities of each model family

### CNNs

CNNs can convert high-dimensional real-world observations into features or
classes used by the twin:

- Images: part identity, defect class, object location, segmentation
- Thermal imagery: hot-region detection and thermal-state features
- One-dimensional signals: vibration, current, acoustic, pressure-wave, or
  other local-pattern classification

The twin should retain the source timestamp, model version, confidence, and
input-quality context. A CNN classification should not silently become a plant
fact or safety decision.

### PINNs and hybrid physics/data models

PINNs can help connect sparse measurements to unmeasured physical state:

- Estimate parameters or fields that cannot be measured directly
- Calibrate a process or equipment model from operating data
- Build a surrogate for expensive simulation
- Combine conservation laws or differential equations with observations

The physics term constrains learning but does not automatically prove accuracy,
stability, real-time performance, or validity outside the calibrated regime.

### LLMs

LLMs can operate over the twin's semantic and historical context:

- Translate an engineering question into bounded read-only queries
- Retrieve manuals, procedures, alarms, changes, and model evidence
- Explain a prediction using identified evidence and uncertainty
- Draft test plans, maintenance actions, or control logic for verification
- Orchestrate approved tools through typed, allow-listed interfaces

An LLM should normally consume curated twin context rather than unrestricted
raw tag streams. Proposed actions need schema validation, authorization, plant
state checks, and—where required—human confirmation.

## Physical-to-digital path

Research and design checks:

1. Identify the asset, sensor, engineering unit, range, and meaning of each input.
2. Preserve source timestamp, acquisition timestamp, quality, and missing-data state.
3. Align data with PLC scan, camera trigger, batch, recipe, mode, and event context.
4. Reject or mark stale, substituted, frozen, impossible, and out-of-sequence data.
5. Estimate twin state and record which values are measured, derived, or predicted.
6. Compare predicted state with observed state and monitor residuals and drift.
7. Recalibrate or retire models through controlled lifecycle procedures.

## Digital-to-physical path

Possible authority levels:

| Level | Twin/AI output | Control-system treatment |
|---|---|---|
| 0 | Offline analysis | No online interface |
| 1 | Monitoring result | Read-only visualization and logging |
| 2 | Advisory recommendation | Operator evaluates and acts separately |
| 3 | Proposed command/setpoint | Operator explicitly confirms through a governed workflow |
| 4 | Bounded supervisory output | PLC independently checks enable, range, rate, mode, freshness, and permissives |
| 5 | Direct learned control | Research/high-assurance case requiring timing, stability, failure, security, and safety evidence |

Regardless of level, independent trips, interlocks, safety functions, equipment
limits, and manual fallback should remain effective when the twin or AI service
is wrong, stale, unavailable, or compromised.

## Data contract between twin and control system

Candidate fields:

- Asset and signal identifier
- Request/correlation ID
- Source and inference timestamps
- Input and output quality
- Value, class, prediction horizon, and uncertainty/confidence
- Model name, version, feature-pipeline version, and calibration version
- Valid-until or maximum-age value
- Twin synchronization state
- Service health and fallback state
- Requested authority level and action type
- Acknowledgment, rejection reason, and audit identity

## Example research cases

1. **Machine-vision twin:** CNN observations update part and quality state;
   the PLC owns trigger timing and reject actuation.
2. **Motor/drive health twin:** vibration and motor-current models update health
   indicators; maintenance planning remains advisory.
3. **Thermal/process PINN twin:** sparse sensors update estimated temperature or
   flow fields; operators compare forecasts before changing operation.
4. **LLM maintenance interface:** an LLM queries twin state, alarms, history, and
   approved documents through read-only tools and produces cited guidance.
5. **Supervisory optimization:** twin simulations evaluate candidate setpoints;
   only bounded, fresh proposals reach PLC validation logic.

## Questions to answer with evidence

- How tightly must the twin synchronize for each use case?
- Which state is measured, inferred, simulated, or manually entered?
- How is mismatch between physical and digital state detected?
- How are startup, shutdown, maintenance, manual, fault, and degraded modes modeled?
- What prediction horizon is useful relative to process dynamics and action time?
- What happens if AI output is late, missing, low-confidence, or contradictory?
- Who owns approval of model changes and changes to its allowed control authority?
- How can a complete decision be reconstructed from data, model, context, and user action?

