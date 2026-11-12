"""Versioned inertial classifier backed by serialized RandomForest (.joblib)."""

from functools import lru_cache
import time
from typing import Any, Dict, List, Tuple, cast
import uuid
import joblib
import numpy as np
from src.core.config import load_config
from src.core.schemas import (
    ClassificationLabel,
    DetectedEvent,
    InferenceRequest,
    InferenceResponse,
)
from src.data.anonymizer import anonymize_trip_identifier
from src.models.train_classifier import (
    LABELS,
    MODEL_ARTIFACT_PATH,
    SEVERITY_BY_LABEL,
    features_to_vector,
    save_model_artifact,
)
from src.pipelines.signal_pipeline import (
    WindowFeatures,
    build_sliding_windows,
    extract_window_features,
)

MODEL_VERSION = "1.0.0"


@lru_cache(maxsize=1)
def load_model_bundle() -> Dict[str, Any]:
    """Load trained joblib artifact or regenerate deterministically if mismatched."""
    if MODEL_ARTIFACT_PATH.exists():
        try:
            return cast(Dict[str, Any], joblib.load(MODEL_ARTIFACT_PATH))
        except (OSError, ValueError, AttributeError, KeyError, ModuleNotFoundError):
            return save_model_artifact(MODEL_ARTIFACT_PATH)
    return save_model_artifact(MODEL_ARTIFACT_PATH)


def classify_window(
    features: WindowFeatures,
) -> Tuple[ClassificationLabel, int, float]:
    """Classify a feature window via RandomForest (.joblib) probabilities."""
    bundle = load_model_bundle()
    model = bundle["model"]
    classes = bundle.get("classes", LABELS)

    vec = np.array([features_to_vector(features)], dtype=float)
    probs = model.predict_proba(vec)[0]
    best_idx = int(np.argmax(probs))
    label = cast(ClassificationLabel, classes[best_idx])
    severity = SEVERITY_BY_LABEL[label]
    confidence = round(float(probs[best_idx]), 4)
    return (label, severity, max(0.5, min(0.9999, confidence)))


def run_inference(payload: InferenceRequest) -> InferenceResponse:
    """Execute full anonymization, windowing, feature extraction, and ML."""
    started = time.perf_counter()
    cfg = load_config()
    viaje_hash = anonymize_trip_identifier(payload.viajeId)

    windows = build_sliding_windows(payload.muestras)
    events: List[DetectedEvent] = []
    for window in windows:
        features = extract_window_features(window)
        label, severity, confidence = classify_window(features)
        events.append(
            DetectedEvent(
                tipoEvento=label,
                severidad=severity,
                confianza=confidence,
                ventanaInicioMs=features.start_ms,
                ventanaFinMs=features.end_ms,
                rmsMagnitud=round(features.rms_mag, 4),
            )
        )

    primary = max(events, key=lambda evt: (evt.severidad, evt.confianza))
    avg_confidence = round(sum(e.confianza for e in events) / len(events), 4)
    elapsed_ms = max(1, int((time.perf_counter() - started) * 1000))

    return InferenceResponse(
        inferenciaId=str(uuid.uuid4()),
        viajeAnonimoHash=viaje_hash,
        rutaId=payload.rutaId,
        modeloVersion=cfg.model_version or MODEL_VERSION,
        clasificacionPrincipal=primary.tipoEvento,
        confianzaGlobal=avg_confidence,
        severidadMaxima=primary.severidad,
        totalMuestrasProcesadas=len(payload.muestras),
        ventanasAnalizadas=len(events),
        eventosDetectados=events,
        procesadoEnMs=elapsed_ms,
    )
