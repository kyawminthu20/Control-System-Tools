<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: CONTROL_SYSTEMS
MODULE_ID: pid_drone_control
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["pid", "drone_control", "quadcopter", "rate_loop", "attitude_loop", "altitude_control", "position_control", "motor_mixing", "imu", "anti_windup", "filtering", "tuning"]
  systems: ["drone", "quadcopter", "flight_controller", "motion_axis", "control_loop"]
-->

# PID Drone Control

## 0. Purpose

This note explains how PID control stabilizes and guides a multirotor drone, especially a quadcopter.

Use it to understand:

- why a drone needs very fast feedback loops
- how the nested control structure is organized
- what the rate, attitude, altitude, and position loops each do
- how motor mixing turns loop outputs into real torque and thrust changes
- what tuning, filtering, and anti-windup problems look like in practice

## 1. Why drone control is a useful PID example

A quadcopter is an **inherently unstable system**. Without active control, it flips, drifts, or falls almost immediately.

That makes it a strong teaching example for PID because:

- the plant is fast
- the system is unstable without feedback
- the controller must react continuously
- nested loops are easy to see conceptually
- actuator changes map directly into motion and torque

In most drones, stability is achieved through **fast cascade feedback loops** running inside the flight controller at hundreds or thousands of updates per second.

## 2. What the flight controller must regulate

A drone must regulate several variables at the same time.

| Controlled state | Meaning |
| --- | --- |
| Roll | left-right tilt |
| Pitch | forward-back tilt |
| Yaw | rotation around the vertical axis |
| Altitude | vertical position |
| Vertical speed | climb or descent rate |
| Horizontal velocity | speed over ground |
| Position | horizontal location |

The most critical inner stabilization loops are:

- roll
- pitch
- yaw

Altitude and position control sit on top of those inner loops.

## 3. Sensor feedback sources

A flight controller depends heavily on an **IMU (Inertial Measurement Unit)**.

Typical sensors include:

| Sensor | Main use |
| --- | --- |
| Gyroscope | angular velocity |
| Accelerometer | acceleration and gravity reference |
| Magnetometer | heading reference |
| Barometer | altitude estimate |
| GPS | position and ground velocity |
| Range sensor or lidar | low-altitude height control on some systems |

The **gyroscope is usually the most critical stabilization sensor** because the inner rate loop depends on accurate angular-rate measurement.

Typical practical update rates are:

- IMU readout: roughly 1 kHz to several kHz
- rate loop: hundreds of Hz to a few kHz
- outer loops such as position: slower than the rate loop

The exact numbers depend on the flight controller, sensor filtering, and airframe type.

## 4. Control loop hierarchy

Flight controllers usually use **nested loops** rather than one single PID block.

A typical stack looks like:

```text
Position Loop
        ↓
Velocity Loop
        ↓
Angle / Attitude Loop
        ↓
Angular Rate Loop
        ↓
Motor Mix
        ↓
ESC / Motor / Propeller
```

Not every drone uses every layer.

Examples:

- a racing drone may focus mainly on rate control with little or no GPS position loop
- a camera drone usually uses the full stack
- a simple altitude-hold drone may use a vertical loop without full horizontal position hold

## 5. The most important inner loop: angular rate control

The **angular rate loop** is the core stabilization loop.

It controls:

- roll rate
- pitch rate
- yaw rate

Example:

- desired roll rate = pilot command or outer-loop command
- measured roll rate = gyroscope reading

The error is:

`error = desired_rate - measured_rate`

The PID controller turns that error into a corrective torque demand.

This loop is the reason the drone feels locked-in rather than loose or unstable.

## 6. Angle or attitude loop

Above the rate loop, many drones use an **angle loop** or **attitude loop**.

Its job is different:

- the angle loop controls desired orientation
- the rate loop controls how fast the drone rotates to achieve that orientation

For example:

- pilot stick command asks for 10 degrees of roll
- attitude loop compares commanded roll angle to measured roll angle
- attitude loop generates a desired roll rate
- rate loop then drives the motors to produce that roll rate

This is a common cascade structure:

`attitude error -> desired angular rate -> rate PID -> motor command`

## 7. Altitude and vertical control

Altitude control is usually not handled by the same loop that handles roll and pitch stabilization.

A practical vertical structure often includes:

- altitude loop
- vertical velocity loop
- thrust command output

Typical sensors for this layer include:

- barometer
- accelerometer fusion
- range sensor at low altitude

The vertical plant is different from the attitude plant because:

- gravity creates a constant bias
- thrust margin matters
- battery voltage changes available performance
- propeller efficiency changes with load and airspeed

This is a good place to remember why proportional-only control can leave offset in some systems.

## 8. Position control

Position control is usually an outer loop built on top of stabilized attitude control.

Typical path:

`position error -> desired velocity -> desired angle -> desired angular rate -> motor outputs`

That means a drone does not usually move laterally by directly commanding "go east." Instead, it tilts, which creates a horizontal force component.

Because of that:

- position control depends on accurate attitude control
- attitude control depends on accurate rate control
- poor inner-loop tuning ruins outer-loop behavior

## 9. Rate PID law in practical form

A simplified rate PID law looks like:

`u = Kp*e + Ki*integral(e) + Kd*de/dt`

Where:

- `e` is angular-rate error
- `u` is a control effort that becomes a motor-thrust adjustment after mixing

In practical flight controllers, the implementation often includes:

- filtered gyro signals
- filtered derivative calculation
- actuator limits
- anti-windup
- feedforward or setpoint weighting on some platforms

So the real implementation is always more than the clean textbook equation.

## 10. Motor mixing

A quadcopter has four motors, and the controller does not send the same output to all of them.

A simplified quad layout can be thought of as:

```text
       Front
        M1
     /      \
  M2          M3
     \      /
        M4
```

To create roll:

- motors on one side speed up
- motors on the other side slow down

To create pitch:

- front and rear motors are driven differentially

To create yaw:

- the controller changes the balance of clockwise and counterclockwise reaction torque

That means the PID output is not "the motor command." It is first converted into axis corrections, then mixed across all motors.

Conceptually:

`motor_output = throttle + roll_correction + pitch_correction + yaw_correction`

The exact sign and mixing matrix depend on frame layout and motor spin directions.

## 11. Why P, I, and D are all useful on a drone

### Proportional action

The proportional term responds immediately to the current error.

Effect:

- fast restoring torque
- primary stabilization force

Too much proportional gain can create:

- high-frequency oscillation
- aggressive stick feel
- motor heating from excessive rapid correction

### Integral action

Integral action corrects slow persistent bias.

Examples:

- motor imbalance
- frame asymmetry
- steady wind
- center-of-gravity offset
- imperfect trim

Without enough integral action:

- the drone may slowly drift or lean under constant disturbance

Too much integral action can create:

- slow oscillation
- overshoot after disturbance
- long recovery after saturation

### Derivative action

Derivative reacts to the rate of change of error and adds damping.

Effect:

- reduces overshoot
- improves stopping behavior
- helps prevent rapid oscillation

Derivative matters a lot in drones because:

- the system is fast
- inertia is relatively low
- the airframe responds quickly to motor changes

But derivative is also highly sensitive to sensor noise, so filtering is critical.

## 12. Example: roll stabilization

Suppose wind pushes the drone to the right.

Measured roll rate:

`+20 deg/s`

Desired roll rate:

`0 deg/s`

Then:

`error = desired_rate - measured_rate`

The controller produces a corrective roll torque command.

The motor mixer then adjusts thrust so the drone creates restoring torque in the opposite direction.

In simple terms:

- motors on one side increase thrust
- motors on the other side decrease thrust

That differential thrust fights the disturbance and drives the roll rate back toward zero.

## 13. Why drone loops are usually cascaded

A drone is hard to control well with one single loop because different layers of behavior happen at different speeds.

Examples:

- motor torque and angular rate change very quickly
- attitude changes somewhat more slowly
- position changes more slowly still

A cascade lets each loop do a narrower job:

- outer loop chooses what should happen next
- inner loop makes it happen quickly

This is the same general control idea seen in servo drives:

- outer position loop
- middle velocity loop
- inner current loop

The drone version uses attitude and rate instead of machine-axis position and velocity, but the structure is conceptually similar.

## 14. Filtering and derivative management

Drone controllers almost always filter sensor data because:

- gyros contain high-frequency noise
- vibration from motors and propellers contaminates measurements
- derivative action can amplify that noise badly

Common practical tools include:

- gyro low-pass filtering
- notch filters for frame or propeller vibration
- derivative filtering
- separate filter choices for pilot feel versus loop stability

A drone with poor filtering may show:

- twitchy response
- hot motors
- unexplained oscillation
- poor tuning even when gains seem reasonable

## 15. Integrator management and anti-windup

Anti-windup is important in drones because actuator saturation happens often.

Examples:

- throttle near maximum during aggressive climb
- one side of the motor mix saturating during a fast roll
- large disturbance pushing the controller to its output limits

If the integrator keeps growing during saturation, the drone may:

- overshoot when authority returns
- bounce after sharp maneuvers
- feel sluggish coming out of aggressive commands

Practical anti-windup methods include:

- clamping integral accumulation at a defined bound
- reducing or freezing integral accumulation during saturation
- resetting or decaying integral during certain mode transitions

## 16. Feedforward and pilot feel

Many modern drone controllers use more than pure PID.

A common addition is **feedforward** or setpoint-based boosting.

Its purpose is not mainly disturbance correction. Instead, it helps the drone react more directly to command changes.

That can improve:

- stick responsiveness
- command tracking
- feel in racing or acrobatic flight

In practice:

- PID handles stabilization and disturbance rejection
- feedforward improves how directly the drone responds to pilot input

## 17. Flight modes and loop usage

Different flight modes rely on different parts of the control stack.

Examples:

- **Rate / Acro mode**: pilot commands angular rate directly; the rate loop dominates
- **Angle mode**: pilot commands attitude; the attitude loop sits above the rate loop
- **Altitude hold**: vertical control loop maintains height
- **Position hold**: outer GPS or vision-based loop commands velocity and attitude targets

This means a drone can feel completely different between modes even though the same hardware is used.

## 18. Tuning behavior in practical terms

Common tuning symptoms in drone control include:

| Symptom | Likely issue |
| --- | --- |
| fast oscillation | too much P or too much D noise sensitivity |
| slow bounce or wobble | too much I or poor outer-loop tuning |
| drift under steady disturbance | too little I |
| mushy feel | too little P or too much filtering |
| sharp overshoot at stop | not enough damping or too much P |
| hot motors at hover | noisy D path, excessive oscillation, or overdriven filters/gains |

These are heuristics, not guaranteed diagnoses, but they are useful starting points.

## 19. Typical commissioning or tuning sequence

A practical tuning order often looks like this:

1. verify motor order, spin direction, frame geometry, and sensor orientation
2. confirm gyro health and vibration level before tuning gains
3. tune the inner rate loop first
4. tune the attitude loop after the rate loop is stable
5. tune altitude or position loops only after the inner stabilization loops are solid
6. review actuator saturation, battery sag, and noise effects before chasing gains further

This order matters because poor inner-loop tuning makes every outer loop look worse.

## 20. Practical failure modes

Drone PID problems are often not caused by gains alone.

Common root causes include:

- wrong motor direction
- incorrect propeller installation
- bad sensor orientation
- excessive vibration
- ESC latency or calibration issues
- flexing frame
- poor center-of-gravity placement
- too much weight or too little thrust margin

A badly built airframe can look like a badly tuned controller even when the real problem is mechanical.

## 21. Engineering takeaways

- Drone control is a strong example of PID because the plant is fast and unstable.
- The inner angular-rate loop is the most important stabilization loop.
- Outer loops such as attitude, altitude, and position depend on the inner loop being stable first.
- Derivative action is valuable on drones, but only if filtering and vibration control are handled properly.
- Anti-windup and output saturation matter because aggressive maneuvers regularly push the actuators near their limits.
- A drone controller is usually not a single PID block; it is a stack of nested loops plus motor mixing and filtering.

## Related files

- [PID Control Overview](./pid_control_intuitive_foundation.md)
- [PID Control Intuition](./pid_control_intuition.md)
- [Industrial PID Implementation](./industrial_pid_implementation.md)
- [Industrial Control Loop Architectures](./industrial_control_loop_architectures.md)
