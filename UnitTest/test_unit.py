"""Unit tests for anonymization, sliding windowing, feature extraction, and contracts."""

import math
import pytest
from pydantic import ValidationError
from src.core.schemas import AccelerometerSample, InferenceRequest
from src.data.anonymizer import IntegrityViolationError, anonymize_trip_identifier
from src.pipelines.signal_pipeline import (
    build_sliding_windows,
    extract_window_features,
    sort_and_clean_samples,
)


def _sample_reading(ts: int, x: float, y: float, z: float) -> AccelerometerSample:
    return AccelerometerSample(timestampRelativoMs=ts, accelX=x, accelY=y, accelZ=z)


def test_anonymize_trip_identifier_hashes_deterministically() -> None:
    first = anonymize_trip_identifier("VIAJE-TULA-2026")
    second = anonymize_trip_identifier("VIAJE-TULA-2026")
    assert first == second
    assert len(first) == 16
    assert "VIAJE-TULA" not in first


def test_anonymizer_rejects_email_pii() -> None:
    with pytest.raises(IntegrityViolationError):
        anonymize_trip_identifier("chofer@bustrack.mx")


def test_sliding_windows_and_chronological_sort() -> None:
    unsorted = [
        _sample_reading(ts, 0.1, 0.1, 9.81) for ts in [300, 0, 200, 100, 400, 500, 600]
    ]
    ordered = sort_and_clean_samples(unsorted)
    assert [s.timestampRelativoMs for s in ordered] == [0, 100, 200, 300, 400, 500, 600]

    windows = build_sliding_windows(ordered, window_size=5, step=2)
    assert len(windows) == 2
    assert len(windows[0]) == 5
    assert windows[0][0].timestampRelativoMs == 0
    assert windows[1][0].timestampRelativoMs == 200


def test_extract_window_features_computes_rms_and_peak() -> None:
    samples = [
        _sample_reading(0, 0.0, 0.0, 9.81),
        _sample_reading(100, 3.0, 4.0, 19.0),
    ]
    feats = extract_window_features(samples)
    assert feats.start_ms == 0
    assert feats.end_ms == 100
    assert feats.peak_mag == pytest.approx(
        math.sqrt(3.0**2 + 4.0**2 + 19.0**2), rel=1e-4
    )
    assert feats.rms_mag > 10.0


def test_schema_requires_explicit_consent_and_finite_axes() -> None:
    with pytest.raises(ValidationError):
        InferenceRequest(
            viajeId="VJ-001",
            rutaId="R-01",
            consentimientoUsuario=False,
            muestras=[_sample_reading(0, 0.0, 0.0, 9.81)],
        )

    with pytest.raises(ValidationError):
        _sample_reading(0, float("nan"), 0.0, 9.81)
