<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Servo Commissioning Workflow

## 0. Purpose

Use this workflow to structure staged commissioning for a servo axis.

Servo systems should be commissioned with tighter control over mechanical risk, feedback correctness, and tuning than a basic induction-motor drive.

## 1. Confirm axis readiness

Before enabling the axis, confirm:

- the correct motor/drive pairing is installed
- the axis is mechanically safe to move
- hard limits, stops, and safety-related functions are understood
- the feedback device and motor-cable terminations are complete

## 2. Enter motor and feedback data

Confirm the drive is using the correct:

- motor model or rated data
- encoder or resolver type
- feedback resolution
- commutation or alignment method

Configuration mismatch should be treated as a blocking issue, not a tuning issue.

## 3. Verify feedback before motion

Check that the drive sees feedback cleanly and in the expected direction.

Review:

- signal health
- direction sense
- reference or homing assumptions
- any warnings about feedback loss or mismatch

## 4. Controlled enable and commutation check

Enable the axis only in a controlled state and verify that:

- the motor holds or responds as expected
- no unexpected jump or runaway behavior occurs
- commutation/alignment completes correctly if the OEM process requires it

## 5. Stage the tuning work

Tuning should be staged:

1. current or torque loop stability
2. velocity response
3. position response

Do not jump directly to aggressive position tuning before lower-level behavior is confirmed.

## 6. Functional motion review

After basic tuning, confirm:

- commanded direction matches actual motion
- overshoot and oscillation are acceptable
- following error stays within expected limits
- the mechanical system does not introduce resonance or backlash problems that were misdiagnosed as electrical issues

## Related files

- [Servo Drive Fundamentals](../../training_modules/electrical_machines/servo_drive_fundamentals.md)
- [Motor Troubleshooting Decision Tree](./motor_troubleshooting_decision_tree.md)
