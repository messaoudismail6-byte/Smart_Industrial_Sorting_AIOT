# PLC sequence

## State machine

0. IDLE
1. STARTUP CHECK
2. CONVEYOR FEED
3. PRODUCT DETECTED
4. WEIGH
5. CLASSIFY
6. MOVE TO ROBOT PICK POSITION
7. ROBOT PICK
8. ROBOT PLACE
9. CONFIRM DROP
10. PRODUCTION COUNT
11. RETURN TO FEED

Fault state: 900

## Weight classification

```text
Weight < 1.0 kg        => Class 1 / Bin A
1.0 <= Weight < 3.0 kg => Class 2 / Bin B
3.0 <= Weight <= 5.0 kg=> Class 3 / Bin C
Weight > 5.0 kg        => Class 4 / Reject
```

## Interlocks

Robot pick request requires:
- EStop_OK
- RobotReady
- product present
- conveyor stopped
- valid weight

Conveyor run requires:
- EStop_OK
- no critical alarm
- robot not inside conveyor danger zone
