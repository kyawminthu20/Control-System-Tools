# Science-Informed AI, Digital Twins, and Control Systems — Research Workspace

**Status:** Research staging only  
**Started:** 2026-07-11  
**Destination:** Not yet decided. Nothing here is authoritative site or RAG content.

## Research question

How should digital twins combine real-world control-system data with scientific
models from physics, chemistry, biology, microbiology, and space/environmental
science, alongside CNNs, physics-informed neural networks (PINNs), large
language models (LLMs), and related model families—and how should the resulting
cyber-physical system be selected, deployed, interfaced, validated, and governed?

The intended result is practical guidance answering:

- **What** each model family is good at and where it is a poor fit.
- **Where** it belongs in a control architecture: device, edge, supervisory,
  historian/analytics, engineering workstation, or enterprise/cloud layer.
- **When** it is justified relative to deterministic logic, classical
  estimation, statistics, model-predictive control, or rules.
- **How** it exchanges data with PLC, DCS, SCADA, historian, vision, and asset
  systems without weakening segmentation or safety boundaries.
- **How to validate it:** data lineage, test sets, uncertainty, drift,
  fail-safe behavior, human review, rollback, and change control.

## Working taxonomy

1. **Foundations and model selection**
   - Supervised, unsupervised, self-supervised, reinforcement, and generative AI
   - Training versus inference
   - Deterministic algorithms versus learned models
   - Accuracy, latency, uncertainty, explainability, and lifecycle cost
2. **CNNs and perception models**
   - Machine vision: inspection, classification, detection, segmentation
   - One-dimensional CNNs for vibration, current, acoustic, and process signals
   - Edge inference, camera triggering, reject timing, and confidence handling
3. **PINNs and hybrid physics/data models**
   - State and parameter estimation
   - System identification and inverse problems
   - Soft sensors, digital twins, reduced-order and surrogate models
   - Limits: training difficulty, scaling, mismatch, and weak guarantees
4. **LLMs and language-centered models**
   - Documentation search and retrieval-augmented generation
   - Alarm and maintenance assistance
   - Requirements-to-control-logic assistance with independent verification
   - Natural-language interfaces and agent/tool architectures
   - Hallucination, prompt injection, authority, and write-access boundaries
5. **Control-system interfaces**
   - OPC UA information models and subscriptions
   - MQTT/Sparkplug and controlled publish/subscribe gateways
   - Historians, databases, REST services, and file/batch exchange
   - Edge IPCs, inference servers, accelerators, and model runtimes
   - PLC handshake patterns: valid, ready, result, confidence, timeout, health
6. **Deployment patterns**
   - Advisory/offline analytics
   - Supervisory read-only inference
   - Bounded recommendation with operator confirmation
   - Guarded setpoint optimization
   - Closed-loop learned control (research/high-assurance boundary)
7. **Safety, security, and governance**
   - AI must not silently replace safety-rated or deterministic protection
   - OT/IT segmentation and least privilege
   - Model/data provenance and versioning
   - Verification, validation, monitoring, drift detection, and rollback
   - Human factors and operational responsibility
8. **Worked architectures and decision guides**
   - Vision inspection cell
   - Predictive-maintenance pipeline
   - PINN soft sensor or process surrogate
   - LLM maintenance copilot using read-only plant context
   - Decision matrix: when not to use ML
9. **Digital-twin integration**
   - Physical asset, control system, data pipeline, twin state, and AI models
   - State synchronization, model calibration, simulation, and prediction
   - Difference between a live data mirror and a behavioral digital twin
   - Twin-to-control feedback authority and independent safety constraints
10. **Scientific domains and coupled interfaces**
   - Physics: mechanics, fluids, heat, electromagnetics, acoustics, radiation
   - Chemistry: kinetics, equilibrium, transport, electrochemistry, combustion
   - Biology: growth, metabolism, physiology, ecological and cellular response
   - Microbiology: populations, contamination, fermentation, biofilms, inhibition
   - Space/cosmic environment: radiation, vacuum, plasma, orbital and solar effects
   - Coupled multiphysics and multiscale boundary conditions

## Initial architecture principle

Start with the least operational authority needed:

```text
offline analysis
    -> read-only monitoring
    -> advisory recommendation
    -> operator-approved action
    -> bounded supervisory action
    -> direct closed-loop action
```

Evidence, validation rigor, deterministic constraints, monitoring, and rollback
requirements increase at every step to the right. Safety functions and basic
equipment protection remain independent unless an applicable high-assurance
engineering case explicitly establishes otherwise.

## Digital twin as the integration spine

The working architecture is not “AI connected directly to a PLC.” It is:

```text
physical process
    <-> sensors, actuators, PLC/DCS
    -> governed real-world data interface
    -> synchronized digital-twin state
    -> scientific + CNN / PINN / LLM / analytical models
    -> prediction, diagnosis, simulation, or recommendation
    -> validation and authority gate
    -> operator or bounded control-system action
```

The research will examine both directions separately:

- **Physical-to-digital:** acquisition, time alignment, quality, context, state
  estimation, twin calibration, and drift detection.
- **Digital-to-physical:** recommendation or command validation, constraints,
  ownership, timeout, fallback, audit, and independent protection.

## Files

- `research-map.md` — questions, use cases, architecture, and research backlog
- `source-register.md` — primary and authoritative sources with relevance notes
- `digital-twin-integration.md` — cyber-physical loop and model responsibilities
- `scientific-domain-integration.md` — scientific models and coupled interfaces
