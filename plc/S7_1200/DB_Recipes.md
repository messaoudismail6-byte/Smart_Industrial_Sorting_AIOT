# Recipe DB

Recommended PLC DB: `DB300_Recipes`

| Parameter | Type | Example |
|---|---|---:|
| RecipeID | INT | 1 |
| Limit_A_kg | REAL | 1.0 |
| Limit_B_kg | REAL | 3.0 |
| Limit_C_kg | REAL | 5.0 |
| ConveyorSpeedPct | REAL | 55.0 |
| MaxCycleTime_s | REAL | 10.0 |

Classification pseudocode:

```text
IF Weight_kg < Limit_A_kg THEN
    WeightClass := 1;
ELSIF Weight_kg < Limit_B_kg THEN
    WeightClass := 2;
ELSIF Weight_kg <= Limit_C_kg THEN
    WeightClass := 3;
ELSE
    WeightClass := 4;
END_IF;
```

Validate recipe values before allowing them into AUTO mode.
