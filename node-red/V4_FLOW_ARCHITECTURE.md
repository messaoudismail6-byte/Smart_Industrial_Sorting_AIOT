# Node-RED V4 flow architecture

```text
MQTT INPUT
   |
   +--> Validation
   |
   +--> Telemetry Historian
   |
   +--> AI Prediction
   |       |
   |       +--> Health
   |       +--> Anomaly
   |       +--> RUL
   |
   +--> Alarm Rules
   |
   +--> OEE Calculator
   |
   +--> Dashboard
   |
   +--> Traceability
   |
   +--> Notification Gateway
```

Recommended topics:

```text
factory/cell01/telemetry
factory/cell01/ai
factory/cell01/alarm
factory/cell01/production
factory/cell01/robot
factory/cell01/oee
factory/cell01/trace
```

For production, use MQTT authentication, TLS and ACLs.
