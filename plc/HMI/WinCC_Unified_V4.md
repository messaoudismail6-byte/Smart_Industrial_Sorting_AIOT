# WinCC Unified HMI — V4 Portfolio Design

## Global navigation

```text
HOME
PRODUCTION
AI / MAINTENANCE
ROBOT
RECIPES
ALARMS
DIAGNOSTICS
TRACEABILITY
```

## Home
- AUTO/MANUAL state
- PLC / Robot / AI connection state
- current weight
- destination
- OEE
- health score
- alarm banner

## AI / Maintenance
- Health score gauge
- anomaly score
- RUL proxy
- vibration trend
- temperature trend
- current trend
- maintenance recommendation

## Recipe
Editable:
- Recipe ID
- A limit
- B limit
- C limit
- conveyor speed
- max cycle time

Use authorization for engineering parameters.

## Alarm philosophy

Severity:
- INFO
- WARNING
- CRITICAL

Every alarm should include:
- timestamp
- source
- text
- acknowledgement
- reset condition

## Diagnostic screen

Show:
- PLC heartbeat
- ESP32 heartbeat
- MQTT state
- AI API state
- Robot handshake
- Factory I/O simulation mode
