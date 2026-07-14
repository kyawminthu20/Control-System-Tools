# Research Map

## 1. Model-family map

| Family | Strong candidate uses | Weak or hazardous uses without further controls | Typical placement |
|---|---|---|---|
| CNN / vision network | Surface inspection, object detection, segmentation, reading gauges, PPE/zone monitoring | Sole safety sensor, unbounded motion decision, use outside validated image conditions | Camera/vision controller, edge IPC, GPU appliance |
| 1D CNN / temporal network | Vibration, acoustic, motor-current and waveform classification; anomaly signatures | Replacing trips/interlocks; diagnosis without representative fault data | Edge IPC or historian analytics layer |
| PINN / science-informed hybrid model | Parameter estimation, soft sensors, inverse problems, coupled process surrogates, digital-twin calibration | Assuming a scientific loss term creates formal correctness; hard real-time control without timing and stability evidence | Engineering/simulation platform or supervisory edge server |
| LLM | Search, summarization, engineering assistance, alarm context, maintenance guidance, draft logic and tests | Direct unverified PLC writes, autonomous safety decisions, treating generated explanations as plant truth | Engineering workstation, secured server, read-only OT gateway |
| Classical ML | Regression, classification, clustering, forecasting, anomaly detection | Using a complex model when limits/rules or first-principles models are sufficient | Edge, historian, MES/analytics |
| Reinforcement learning | Simulation-based optimization and research into constrained control | Online exploration on production equipment; unconstrained reward optimization | Simulator/digital twin first; tightly bounded supervisory layer only after validation |

## 2. “Where does it go?” digital-twin architecture

```text
Physical process and equipment
          |
Sensors / cameras / drives
          |
          v
PLC / DCS / safety controller  <--- deterministic control and protection
          |
          | controlled, authenticated, minimum necessary data
          v
OT data and synchronization    <--- time, quality, units, operating mode
          |
          v
Digital twin state/model       <--- synchronized cyber-physical representation
          |
          +---- first-principles scientific models
          +---- coupled physical/chemical/biological interfaces
          +---- CNN: perception and signal features
          +---- PINN: physics-constrained estimation/surrogate
          +---- LLM: language, retrieval, explanation, orchestration
          +---- classical model: simulation, observer, optimization
          |
          v
Validation and authority gate  <--- bounds, confidence, version, timeout
          |
          v
SCADA / historian / operator   <--- display, trend, confirm, audit, action
          |
          v
DMZ / governed data service    <--- broker/API/OPC UA aggregation
          |
          v
Engineering or enterprise AI   <--- LLM/RAG, training, fleet analytics
```

Research must distinguish **data flow** from **control authority**. A protocol
that can carry a command does not imply that an AI service should be authorized
to issue one.

It must also distinguish a **live data mirror** from a **digital twin**. A useful
twin normally combines synchronized asset state with a behavioral, physics,
statistical, or hybrid model that can estimate, simulate, predict, or test
counterfactual conditions.

## 3. Interface pattern to investigate

For online inference, evaluate a PLC-facing contract containing at least:

- Request ID and input timestamp
- Input-valid and inference-request handshake
- Result value/class and confidence or uncertainty measure
- Result-valid, model version, and inference timestamp
- Service health, stale-data indication, timeout, and quality status
- PLC-side range/rate/sequence checks
- Explicit fallback state when the service, network, or model is unavailable
- Audit record for recommendations or actions

Candidate transports and their proper roles:

- **OPC UA:** structured, typed plant information with security and semantics
- **MQTT/Sparkplug:** event and telemetry distribution through governed brokers
- **Historian/database:** delayed analytics, training data, and fleet comparison
- **REST/gRPC:** bounded service interfaces behind an OT gateway; not a substitute
  for a deterministic fieldbus or safety network
- **Files/batches:** offline training, model promotion, and controlled exchange

## 4. Core research questions

### Use-case justification

- Is the problem perception, estimation, diagnosis, forecasting, optimization,
  language interaction, or direct control?
- Is there a simpler rule, signal-processing method, observer, or physics model?
- Is enough representative data available, including abnormal and changing states?
- What is the economic or safety consequence of false positive, false negative,
  stale output, or confident error?

### Real-time behavior

- Required scan/inference period, jitter, deadline, and maximum age?
- What happens during model startup, overload, network loss, or failover?
- Can the PLC reject late, implausible, or low-confidence output?
- Is the model advisory, permissive, supervisory, or directly actuating?

### Validation and lifecycle

- How are training, validation, and operational datasets separated?
- Which operating modes, products, environments, faults, and edge cases are covered?
- How are calibration, uncertainty, drift, and out-of-distribution inputs measured?
- How are model, feature pipeline, configuration, and data-schema versions tied?
- What regression tests, shadow deployment, acceptance criteria, rollback, and
  management-of-change process apply?

### Safety and cybersecurity

- Does AI failure remain outside the safety function and basic protection layers?
- What network zone hosts inference and training?
- Is access read-only by default, with allow-listed actions and independent checks?
- How are model files, prompts, retrieval documents, and updates authenticated?
- For LLMs, can untrusted plant text or documents inject instructions?

## 5. Proposed future site shape — provisional

Do not create these pages until the research is validated and the owner chooses
where this category belongs in the established site taxonomy.

```text
AI & Machine Learning for Control Systems
├── Foundations and model-selection guide
├── CNNs for machine vision and industrial signals
├── PINNs and hybrid physics/data models
├── LLMs, RAG, copilots, and agents
├── Industrial data and interface architectures
├── Edge deployment and model serving
├── Verification, monitoring, and model lifecycle
├── Safety and cybersecurity boundaries
└── Worked architectures and decision matrices
```

## 6. Research backlog

- [ ] Establish vocabulary: AI, ML, deep learning, foundation model, CNN, PINN,
      transformer, LLM, RAG, agent, digital twin, soft sensor, inference
- [ ] Review CNN use cases for vision and one-dimensional industrial signals
- [ ] Review PINN evidence, limitations, and control/estimation applications
- [ ] Review LLM applications in PLC/DCS engineering and operator assistance
- [ ] Compare OPC UA, MQTT/Sparkplug, APIs, historians, and file exchange
- [ ] Define reference architectures for offline, advisory, and bounded online use
- [ ] Define digital-twin maturity levels: offline model, connected shadow,
      synchronized twin, predictive twin, and bounded closed-loop twin
- [ ] Research state synchronization, time alignment, data quality, and model
      calibration between physical asset and twin
- [ ] Assign CNN, PINN, LLM, and classical-model responsibilities inside the twin
- [ ] Map physics, chemistry, biology, microbiology, and space/environmental
      science to control-system measurements, manipulated variables, constraints,
      models, time scales, and validation methods
- [ ] Research coupled interfaces: thermal-fluid, electrochemical, biochemical,
      reaction-transport, organism-environment, radiation-material, and plasma-field
- [ ] Separate governing laws, empirical correlations, learned residuals, and
      operator knowledge in every hybrid model
- [ ] Build a “when not to use ML” decision tree
- [ ] Develop validation and model-change checklists
- [ ] Map relevant OT security, AI risk, functional-safety, and machinery standards
- [ ] Identify public datasets and reproducible teaching examples
- [ ] Separate peer-reviewed results from vendor claims and proof-of-concepts
- [ ] Decide whether the eventual site content is a top-level category or fits under
      Fundamentals, Design, Communications, and Tools without adding a new top level
