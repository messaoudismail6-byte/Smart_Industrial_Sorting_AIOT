# Factory I/O fault-injection scenarios

Use simulation to demonstrate predictive and diagnostic capabilities.

## Scenario A — Conveyor overload
Increase simulated motor load/current.
Expected:
- current increases
- AI health decreases
- WARNING/CRITICAL appears

## Scenario B — Bearing vibration
Increase vibration signal gradually.
Expected:
- vibration RMS trend rises
- AI warning
- maintenance recommendation

## Scenario C — Sensor failure
Freeze or remove product sensor.
Expected:
- PLC timeout alarm
- production stops safely
- diagnostic message

## Scenario D — Robot not ready
Robot Ready remains FALSE.
Expected:
- conveyor sequence pauses at robot handshake
- no unsafe pick command

## Scenario E — Overweight product
Weight > recipe limit.
Expected:
- RejectRequest
- reject counter increment
- traceability event
