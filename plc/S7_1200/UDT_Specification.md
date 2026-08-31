# UDT specification

## UDT_Product

```text
ID              : DINT
Weight_kg       : REAL
WeightClass     : INT
Destination     : INT
CycleTime_s     : REAL
Timestamp       : DATE_AND_TIME
```

## UDT_RobotHandshake

```text
PLC_PickRequest  : BOOL
PLC_TargetA      : BOOL
PLC_TargetB      : BOOL
PLC_TargetC      : BOOL
PLC_Reject       : BOOL
RobotReady       : BOOL
RobotBusy        : BOOL
RobotDone        : BOOL
RobotFault       : BOOL
```

## UDT_AIHealth

```text
HealthScore      : REAL
Confidence       : REAL
AnomalyScore     : REAL
RUL_HoursProxy   : REAL
RiskLevel        : INT
PredictionValid  : BOOL
```
