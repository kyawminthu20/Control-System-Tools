<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_TOOL_INTERFACE
-->

# Tool and Facility Interface

## Purpose

This note defines the engineering boundary between facility utilities and semiconductor process tools.

## Why this boundary matters

Many startup problems come from unclear ownership at the hookup point. A tool may assume the facility proves one condition, while the facility assumes the tool handles it internally.

## Interface categories

- utility supply availability
- permit-to-run and ready signals
- exhaust and cooling prove
- fault and shutdown exchange
- communication or status integration
- maintenance and lockout coordination

## Minimum questions for every utility interface

- Where is the physical battery limit?
- Who owns final isolation for abnormal events?
- What signals are hardwired versus networked?
- Which faults are advisory only and which must remove permit-to-run?
- What is the startup order between facility package and tool controller?
- What states are allowed after a communications loss?

## Typical handshake objects

- facility ready
- tool request
- utility available
- utility degraded
- local shutdown active
- emergency shutdown active
- reset permitted

## Documentation outputs worth building

- interface control document
- handshake truth table
- signal ownership matrix
- startup and shutdown sequence between facility and tool
- fault escalation path

## Standards anchors

- SEMI E5, E30, and E37 when host or equipment communications become part of the interface
- SEMI S2 and related safety guidance when the boundary changes shutdown behavior
- facility electrical and control standards already in the local corpus
