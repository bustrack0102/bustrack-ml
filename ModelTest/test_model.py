"""Model evaluation tests for determinism, sensitivity, and confidence bounds."""

from src.core.schemas import AccelerometerSample, InferenceRequest
from src.models.classifier import MODEL_VERSION, run_inference


def _make_batch(
    viaje_id: str, triples: list[tuple[float, float, float]]
) -> InferenceRequest:
    samples = [
        AccelerometerSample(
            timestampRelativoMs=idx * 100,
            accelX=x,
            accelY=y,
            accelZ=z,
        )
        for idx, (x, y, z) in enumerate(triples)
    ]
    return InferenceRequest(
        viajeId=viaje_id,
        rutaId="R-01",
        intervaloMuestreoMs=100,
        consentimientoUsuario=True,
        muestras=samples,
    )


def test_model_detects_severe_pothole_accurately() -> None:
    req = _make_batch(
        "VJ-BACHE-01",
        [
            (0.1, 0.1, 9.8),
            (0.2, 0.1, 9.9),
            (2.8, 3.2, 20.5),
            (0.3, 0.2, 10.1),
            (0.1, 0.1, 9.8),
        ],
    )
    res = run_inference(req)
    assert res.modeloVersion == MODEL_VERSION
    assert res.clasificacionPrincipal == "BACHE_SEVERO"
    assert res.severidadMaxima == 3
    assert 0.85 <= res.confianzaGlobal <= 1.0


def test_model_detects_stationary_bus_stop() -> None:
    req = _make_batch(
        "VJ-PARADA-01",
        [(0.02, 0.01, 9.81) for _ in range(6)],
    )
    res = run_inference(req)
    assert res.clasificacionPrincipal == "PARADA_DETECTADA"
    assert res.severidadMaxima == 1


def test_model_detects_moderate_vibration_and_smooth_road() -> None:
    vib_req = _make_batch(
        "VJ-VIB-01",
        [
            (1.5, 2.0, 14.5),
            (0.2, 0.4, 9.8),
            (1.1, 1.4, 14.0),
            (0.2, 0.1, 9.9),
            (0.1, 0.2, 9.8),
        ],
    )
    vib_res = run_inference(vib_req)
    assert vib_res.clasificacionPrincipal == "ANOMALIA_VIBRACION_MODERADA"
    assert vib_res.severidadMaxima == 2

    smooth_req = _make_batch(
        "VJ-SMOOTH-01",
        [
            (0.4, 0.3, 9.6),
            (0.7, 0.5, 10.2),
            (0.2, 0.3, 9.3),
            (0.6, 0.4, 10.0),
            (0.5, 0.3, 9.5),
        ],
    )
    smooth_res = run_inference(smooth_req)
    assert smooth_res.clasificacionPrincipal == "VIA_REGULAR_OPTIMA"
    assert smooth_res.severidadMaxima == 0


def test_model_predictions_are_deterministic_and_within_confidence_bounds() -> None:
    req = _make_batch("VJ-DET-01", [(0.1, 0.2, 9.8), (1.5, 1.8, 19.2), (0.2, 0.1, 9.7)])
    first = run_inference(req)
    second = run_inference(req)
    assert first.clasificacionPrincipal == second.clasificacionPrincipal
    assert first.confianzaGlobal == second.confianzaGlobal
    assert first.viajeAnonimoHash == second.viajeAnonimoHash
    assert 0.0 <= first.confianzaGlobal <= 1.0
