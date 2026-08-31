from pathlib import Path
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from feature_engineering import build_features

MODEL_PATH = Path("models/health_model.pkl")
if not MODEL_PATH.exists():
    import train_model
model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Smart Industrial Edge AI",
    description="Predictive maintenance and machine-health API",
    version="2.0"
)

class Telemetry(BaseModel):
    vibration_rms: float
    temperature_c: float
    current_a: float
    cycle_time_s: float

@app.get("/health")
def health():
    return {"status": "ok", "model": "RandomForest", "version": "2.0"}

@app.post("/predict")
def predict(x: Telemetry):
    X = build_features(
        x.vibration_rms,
        x.temperature_c,
        x.current_a,
        x.cycle_time_s
    )

    cls = int(model.predict(X)[0])
    proba = model.predict_proba(X)[0]
    confidence = float(np.max(proba))

    # Advisory health index.
    health = 100.0 - (
        min(x.vibration_rms / 2.0, 1.0) * 35.0 +
        min(max(x.temperature_c - 40.0, 0.0) / 50.0, 1.0) * 25.0 +
        min(max(x.current_a - 4.0, 0.0) / 8.0, 1.0) * 20.0 +
        min(max(x.cycle_time_s - 6.0, 0.0) / 8.0, 1.0) * 20.0
    )
    health = float(np.clip(health, 0, 100))

    labels = {
        0: ("NORMAL", "Continue monitoring"),
        1: ("WARNING", "Inspect vibration and temperature trend"),
        2: ("CRITICAL", "Follow validated stop/isolation procedure")
    }
    level, recommendation = labels[cls]

    return {
        "health_score": round(health, 1),
        "risk_level": level,
        "confidence": round(confidence, 3),
        "predicted_fault_class": cls,
        "recommendation": recommendation
    }
