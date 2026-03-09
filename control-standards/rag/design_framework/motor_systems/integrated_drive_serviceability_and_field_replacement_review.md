<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Integrated Drive Serviceability and Field Replacement Review

## 0. Purpose

Use this note to review how integrated drive-on-motor architecture changes service strategy, diagnostics, spare holding, and field replacement.

## 1. Why serviceability changes

With separate motor and drive hardware, the maintenance team can often isolate and replace one element at a time.

With integrated packaging, replacement may occur at the assembly level instead:

- motor plus drive
- axis package
- propulsion module
- traction subsystem

## 2. Comparison table

| Architecture | Typical service model | Main service advantage | Main service drawback |
| --- | --- | --- | --- |
| Industrial VFD on motor | replace decentralized module or motor-drive assembly | fast modular swap in distributed systems | larger field-replacement unit |
| Industrial servo on motor | replace axis package or integrated servo assembly | compact motion package | more expensive replacement per unit |
| EV integrated traction unit | service at subsystem level | tight vehicle integration | less field-level separation of components |
| Drone propulsion unit | replace ESC/motor pair or propulsion module | quick propulsion-module replacement | limited repair granularity |

## 3. Service review questions

1. Can the technician diagnose motor faults and electronics faults separately?
2. Is the spare strategy based on subcomponents or integrated assemblies?
3. Does field replacement require special alignment, tuning, or parameter restore?
4. Will downtime be lower or higher in the real maintenance model?
5. Does the environment allow safe access to the integrated hardware?

## 4. Industrial machinery implications

For industrial machinery, integrated drives can be attractive when:

- modular swap time matters
- decentralized architecture is intentional
- separate cabinet space is expensive

They are less attractive when:

- separate motor and drive replacement is operationally important
- field conditions are harsh
- diagnostics are weak
- spare cost per assembly is too high

## 5. Practical conclusion

Integration may simplify installation but complicate maintenance economics. Service strategy should be part of the architecture decision, not an afterthought.

## Related files

- [Integrated Motor-Drive Architecture Comparison](./integrated_motor_drive_architecture_comparison.md)
- [Integrated Drive Failure Modes and Tradeoffs](./integrated_drive_failure_modes_and_tradeoffs.md)
