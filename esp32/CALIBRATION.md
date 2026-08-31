# Weight and sensor calibration

## Load cell

1. Empty platform -> tare.
2. Place a certified reference mass.
3. Adjust `calibration_factor`.
4. Repeat with at least two reference points.
5. Record calibration date and operator.

Do not use the example factor as a certified calibration value.

## Vibration

Record a baseline while the motor is healthy. Calculate:
- RMS
- peak
- rolling average
- deviation from baseline

## Reliability

Recommended additions for an industrial prototype:
- MQTT Last Will
- reconnect backoff
- sensor timeout flag
- local buffering if network is unavailable
- CRC/checksum where supported
- watchdog reset
