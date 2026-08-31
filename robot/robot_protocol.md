# Robot protocol

The robot controller can be connected through Ethernet/TCP, digital I/O, or the manufacturer's fieldbus.

## Command model

```text
READY
PICK
PLACE_A
PLACE_B
PLACE_C
REJECT
DONE
FAULT
```

Recommended handshake:

PLC -> Robot:
- PickRequest
- TargetA
- TargetB
- TargetC
- Reject

Robot -> PLC:
- Ready
- Busy
- PickComplete
- PlaceComplete
- Fault

Never use the portfolio protocol as a substitute for the robot manufacturer's safety interface.
