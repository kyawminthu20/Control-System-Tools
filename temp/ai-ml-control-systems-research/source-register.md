# Initial Source Register

**Source policy:** Prefer peer-reviewed papers, standards bodies, government
guidance, and official project documentation. Record vendor material only as an
implementation example, not as proof of general capability. Notes below are
paraphrases, not copied source text.

## Foundations and model families

### Physics-informed neural networks

- **Raissi, Perdikaris, and Karniadakis, “Physics-informed neural networks,”
  Journal of Computational Physics 378 (2019), DOI 10.1016/j.jcp.2018.10.045.**
  <https://www.sciencedirect.com/science/article/abs/pii/S0021999118307125>
  - Foundational PINN paper combining neural approximation with governing
    differential-equation residuals for forward and inverse problems.
  - Relevance: foundation for the PINN section; does not by itself establish
    industrial real-time suitability or formal control guarantees.

### Convolutional neural networks

- **Krizhevsky, Sutskever, and Hinton, “ImageNet Classification with Deep
  Convolutional Neural Networks,” NeurIPS 2012.**
  <https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html>
  - Landmark deep-CNN result for visual classification.
  - Relevance: foundation for explaining convolution, learned spatial features,
    and why CNNs became central to machine vision. Industrial validation must be
    researched separately.

## LLMs and industrial automation

- **Fakih et al., “LLM4PLC: Harnessing Large Language Models for Verifiable
  Programming of PLCs in Industrial Control Systems,” 2024 preprint.**
  <https://arxiv.org/abs/2401.05443>
  - Proposes an iterative PLC-code pipeline using compilers, grammar checking,
    and formal verification rather than trusting raw model output.
  - Relevance: useful evidence for an “LLM drafts; tools verify; engineer owns”
    architecture. Treat results as research, not general production proof.

- **Xia et al., “Control Industrial Automation System with Large Language
  Models,” 2024 preprint.**
  <https://arxiv.org/abs/2409.18009>
  - Proof-of-concept architecture using structured events and an LLM agent for
    automation tasks.
  - Relevance: candidate end-to-end architecture to critique for latency,
    authority, determinism, cybersecurity, and safety boundaries.

## Industrial interoperability and edge deployment

- **OPC Foundation, OPC UA Part 1: Overview and Concepts.**
  <https://reference.opcfoundation.org/specs/OPC-10000-1/4>
  - Defines OPC UA as a platform-independent framework for secure, reliable,
    semantically structured industrial information exchange.
  - Relevance: primary source for the interface architecture. OPC UA capability
    to carry commands must be separated from authorization for AI control.

- **OPC Foundation, “OPC UA for AI: Enhancing Automation with Artificial
  Intelligence,” 2024.**
  <https://opcconnect.opcfoundation.org/2024/06/opc-ua-for-ai-enhancing-automation-with-artificial-intelligence/>
  - Describes industry work on exposing standardized automation semantics to AI.
  - Relevance: direction-setting source; claims are not a substitute for
    independent validation or a deployed-system safety case.

- **ONNX Runtime, “Deploy ML Models on IoT and Edge Devices.”**
  <https://onnxruntime.ai/docs/tutorials/iot-edge/>
  - Official deployment documentation covering cross-platform edge inference and
    practical tradeoffs such as latency, offline operation, model size, and
    limited compute.
  - Relevance: implementation option for a later edge-inference walkthrough.

## Risk, security, and governance

- **NIST, Artificial Intelligence Risk Management Framework 1.0.**
  <https://www.nist.gov/itl/ai-risk-management-framework>
  - Organizes AI risk work around govern, map, measure, and manage functions.
  - Relevance: baseline vocabulary for trustworthiness, lifecycle risk, testing,
    and monitoring. It is general guidance rather than control-system design law.

- **NIST SP 800-82 Rev. 3, Guide to Operational Technology Security.**
  <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
  - Covers OT architectures, threats, vulnerabilities, segmentation, and
    countermeasures for PLC, DCS, SCADA, and related systems.
  - Relevance: baseline for placing AI services without bypassing OT security
    zones, conduits, least privilege, or operational availability needs.

## Sources still needed

- Peer-reviewed surveys of CNN/temporal models for industrial fault diagnosis
- PINN reviews emphasizing failure modes, optimization difficulty, uncertainty,
  and comparisons with classical numerical methods
- Hybrid-model and neural state-estimation/control papers with reproducible data
- Constrained/safe learning-control research and explicit stability guarantees
- Current standards or guidance for AI in machinery, functional safety, and
  critical infrastructure
- MQTT Sparkplug primary specifications and secure OT deployment guidance
- Model lifecycle, drift, calibration, uncertainty, and out-of-distribution tests
- Public industrial datasets suitable for reproducible examples

