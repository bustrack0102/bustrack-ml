"""Train, evaluate, and persist the RandomForest inertial telemetry classifier."""

from pathlib import Path
from typing import Any, Dict, List, Tuple
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from src.pipelines.signal_pipeline import WindowFeatures

MODEL_ARTIFACT_PATH = (
    Path(__file__).resolve().parents[2] / "models" / "stop_detector_v1.joblib"
)

LABELS: Tuple[str, ...] = (
    "VIA_REGULAR_OPTIMA",
    "PARADA_DETECTADA",
    "ANOMALIA_VIBRACION_MODERADA",
    "BACHE_SEVERO",
)

SEVERITY_BY_LABEL: Dict[str, int] = {
    "VIA_REGULAR_OPTIMA": 0,
    "PARADA_DETECTADA": 1,
    "ANOMALIA_VIBRACION_MODERADA": 2,
    "BACHE_SEVERO": 3,
}


def features_to_vector(features: WindowFeatures) -> List[float]:
    """Convert WindowFeatures dataclass into ordered numeric vector."""
    return [
        features.mean_mag,
        features.std_mag,
        features.rms_mag,
        features.peak_mag,
        features.max_abs_z,
        float(features.zero_crossings),
    ]


def generate_training_dataset(seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """Generate physics-calibrated accelerometer feature windows across 4 classes."""
    rng = np.random.default_rng(seed)
    rows: List[List[float]] = []
    targets: List[int] = []
    samples_per_class = 400

    # Class 0: VIA_REGULAR_OPTIMA (cruising oscillation around 1g without big spikes)
    for _ in range(samples_per_class):
        mean_m = rng.uniform(9.45, 10.15)
        std_m = rng.uniform(0.18, 1.35)
        peak_m = rng.uniform(max(mean_m + 0.3, 10.45), 13.0)
        rms_m = float(np.sqrt(mean_m**2 + std_m**2))
        max_z = rng.uniform(9.5, min(12.8, peak_m))
        zc = float(rng.integers(2, 6))
        rows.append([mean_m, std_m, rms_m, peak_m, max_z, zc])
        targets.append(0)

    # Class 1: PARADA_DETECTADA (stationary bus: tight 9.81 m/s^2 flatline)
    for _ in range(samples_per_class):
        mean_m = rng.uniform(9.55, 10.05)
        std_m = rng.uniform(0.0, 0.11)
        peak_m = rng.uniform(mean_m, min(10.28, mean_m + 0.22))
        rms_m = float(np.sqrt(mean_m**2 + std_m**2))
        max_z = rng.uniform(9.5, 10.15)
        zc = float(rng.integers(0, 2))
        rows.append([mean_m, std_m, rms_m, peak_m, max_z, zc])
        targets.append(1)

    # Class 2: ANOMALIA_VIBRACION_MODERADA (rough pavement / speed bump)
    for _ in range(samples_per_class):
        mean_m = rng.uniform(10.2, 12.1)
        std_m = rng.uniform(1.5, 3.2)
        peak_m = rng.uniform(13.5, 17.2)
        rms_m = float(np.sqrt(mean_m**2 + std_m**2))
        max_z = rng.uniform(12.5, min(17.1, peak_m))
        zc = float(rng.integers(1, 5))
        rows.append([mean_m, std_m, rms_m, peak_m, max_z, zc])
        targets.append(2)

    # Class 3: BACHE_SEVERO (high-G impact peak >= 18.0 m/s^2)
    for _ in range(samples_per_class):
        mean_m = rng.uniform(11.0, 14.5)
        std_m = rng.uniform(3.3, 6.8)
        peak_m = rng.uniform(18.0, 29.0)
        rms_m = float(np.sqrt(mean_m**2 + std_m**2))
        max_z = rng.uniform(18.0, peak_m)
        zc = float(rng.integers(1, 5))
        rows.append([mean_m, std_m, rms_m, peak_m, max_z, zc])
        targets.append(3)

    return np.array(rows, dtype=float), np.array(targets, dtype=int)


def train_and_evaluate(seed: int = 42) -> Dict[str, Any]:
    """Train RandomForest model and compute holdout F1 & ROC-AUC metrics."""
    x_data, y_data = generate_training_dataset(seed=seed)
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.25, stratify=y_data, random_state=seed
    )

    clf = RandomForestClassifier(
        n_estimators=80,
        max_depth=8,
        min_samples_leaf=2,
        random_state=seed,
    )
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    y_prob = clf.predict_proba(x_test)
    f1_macro = float(f1_score(y_test, y_pred, average="macro"))
    roc_auc = float(
        roc_auc_score(y_test, y_prob, multi_class="ovr", average="weighted")
    )

    return {
        "model": clf,
        "classes": LABELS,
        "version": "1.0.0",
        "metrics": {
            "f1_macro": round(f1_macro, 4),
            "roc_auc_ovr": round(roc_auc, 4),
        },
    }


def save_model_artifact(output_path: Path = MODEL_ARTIFACT_PATH) -> Dict[str, Any]:
    """Train and serialize the joblib model bundle cleanly."""
    bundle = train_and_evaluate(seed=42)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(bundle, output_path, compress=3)
    return bundle


if __name__ == "__main__":
    artifact = save_model_artifact()
    print(f"Saved {MODEL_ARTIFACT_PATH}: {artifact['metrics']}")
