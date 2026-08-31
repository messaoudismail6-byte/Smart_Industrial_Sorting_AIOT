# Commissioning / Test Matrix

| Test | Input | Expected result |
|---|---|---|
| T01 | Start | Conveyor starts after permissives |
| T02 | Product detected | Conveyor stops at weighing station |
| T03 | 0.8 kg | Bin A |
| T04 | 2.0 kg | Bin B |
| T05 | 4.0 kg | Bin C |
| T06 | 6.0 kg | Reject |
| T07 | Robot not ready | Sequence waits |
| T08 | E-stop status false | Outputs go to safe state |
| T09 | High vibration | AI warning/critical trend |
| T10 | Sensor timeout | Diagnostic alarm |
| T11 | MQTT loss | Communication diagnostic |
| T12 | Recipe change | New limits applied after validation |
