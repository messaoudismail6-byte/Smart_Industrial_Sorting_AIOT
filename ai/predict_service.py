"""FastAPI service for advisory machine-health predictions."""

from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

try:
    from .feature_engineering import build_features
except ImportError:
    from feature_engineering import build_features

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "health_model.pkl"

if not MODEL_PATH.exists():
    try:
        from . import train_model
    except ImportError:
        import train_model
    train_model.main()

model = joblib.load(MODEL_PATH)
app = FastAPI(
    title="Smart Industrial Edge AI",
    description="Predictive maintenance and machine-health API",
    version="2.1",
)


class Telemetry(BaseModel):
    vibration_rms: float = Field(ge=0.0, le=10.0)
    temperature_c: float = Field(ge=-40.0, le=150.0)
    current_a: float = Field(ge=0.0, le=100.0)
    cycle_time_s: float = Field(gt=0.0, le=3600.0)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model": "RandomForest", "version": "2.1"}


@app.post("/predict")
def predict(x: Telemetry) -> dict[str, float | int | str]:
    features = build_features(
        x.vibration_rms,
        x.temperature_c,
        x.current_a,
        x.cycle_time_s,
    )
    predicted_class = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    confidence = float(np.max(probabilities))

    health_score = 100.0 - (
        min(x.vibration_rms / 2.0, 1.0) * 35.0
        + min(max(x.temperature_c - 40.0, 0.0) / 50.0, 1.0) * 25.0
        + min(max(x.current_a - 4.0, 0.0) / 8.0, 1.0) * 20.0
        + min(max(x.cycle_time_s - 6.0, 0.0) / 8.0, 1.0) * 20.0
    )
    health_score = float(np.clip(health_score, 0.0, 100.0))
    labels = {
        0: ("NORMAL", "Continue monitoring"),
        1: ("WARNING", "Inspect vibration and temperature trend"),
        2: ("CRITICAL", "Follow validated stop/isolation procedure"),
    }
    level, recommendation = labels.get(
        predicted_class, ("UNKNOWN", "Review model output")
    )
    return {
        "health_score": round(health_score, 1),
        "risk_level": level,
        "confidence": round(confidence, 3),
        "predicted_fault_class": predicted_class,
        "recommendation": recommendation,
    }
