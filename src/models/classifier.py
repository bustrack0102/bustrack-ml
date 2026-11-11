"""Versioned inertial classifier for road anomalies and transit stops (spec-10/11)."""

import time
import uuid
from typing import List, Tuple
from src.core.config import load_config
from src.core.schemas import (
    ClassificationLabel,
    DetectedEvent,
    InferenceRequest,
    InferenceResponse,
)
from src.data.anonymizer import anonymize_trip_identifier
from src.pipelines.signal_pipeline import (
    WindowFeatures,
    build_sliding_windows,
    extract_window_features,
)

MODEL_VERSION = "1.0.0"


def classify_window(
    features: WindowFeatures,
) -> Tuple[ClassificationLabel, int, float]:
    """Classify a single feature window into road anomaly or transit stop states."""
    if features.peak_mag >= 18.0 or features.max_abs_z >= 18.0:
        margin = min(0.05, (features.peak_mag - 18.0) * 0.005)
        return ("BACHE_SEVERO", 3, round(min(0.99, 0.92 + max(0.0, margin)), 4))

    if features.peak_mag >= 13.5 or features.std_mag >= 1.8:
        return ("ANOMALIA_VIBRACION_MODERADA", 2, 0.88)

    if (
        features.std_mag <= 0.12
        and 9.3 <= features.mean_mag <= 10.3
        and features.zero_crossings <= 1
    ):
        return ("PARADA_DETECTADA", 1, 0.86)

    return ("VIA_REGULAR_OPTIMA", 0, 0.95)


def run_inference(payload: InferenceRequest) -> InferenceResponse:
    """Execute full anonymization, windowing, feature extraction, and classification."""
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

    # Select highest-severity event as primary batch outcome without inventing data
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
