"""Train the deterministic demo health classifier."""

from __future__ import annotations

import os

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def main() -> None:
    rng = np.random.default_rng(42)
    n = 2500
    vibration = rng.normal(0.45, 0.25, n).clip(0, 2.5)
    temperature = rng.normal(48, 10, n).clip(20, 100)
    current = rng.normal(5.5, 1.2, n).clip(1, 12)
    cycle = rng.normal(7.0, 1.0, n).clip(3, 15)
    risk = (
        (vibration > 0.9).astype(int)
        + (temperature > 70).astype(int)
        + (current > 8).astype(int)
        + (cycle > 9).astype(int)
    )
    labels = np.where(risk >= 3, 2, np.where(risk >= 1, 1, 0))
    X = np.column_stack([vibration, temperature, current, cycle])
    model = RandomForestClassifier(
        n_estimators=120,
        max_depth=8,
        random_state=42,
    )
    model.fit(X, labels)
    model_path = os.path.join(os.path.dirname(__file__), "models", "health_model.pkl")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Saved {model_path}")


if __name__ == "__main__":
    main()
