"""Integration tests for GET /health and POST /inference endpoints."""

from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)


def test_health_endpoint_returns_healthy_and_correlation_id() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert body["service"] == "bustrack-ml"
    assert "X-Correlation-ID" in response.headers


def test_inference_endpoint_processes_valid_batch() -> None:
    payload = {
        "viajeId": "VJ-INT-001",
        "rutaId": "R-01",
        "intervaloMuestreoMs": 100,
        "consentimientoUsuario": True,
        "muestras": [
            {"timestampRelativoMs": 0, "accelX": 0.1, "accelY": 0.2, "accelZ": 9.81},
            {"timestampRelativoMs": 100, "accelX": 2.4, "accelY": 3.1, "accelZ": 19.5},
        ],
    }
    response = client.post("/inference", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["rutaId"] == "R-01"
    assert data["clasificacionPrincipal"] == "BACHE_SEVERO"
    assert data["totalMuestrasProcesadas"] == 2
    assert "VJ-INT-001" not in data["viajeAnonimoHash"]


def test_inference_rejects_empty_batch_with_422() -> None:
    response = client.post(
        "/inference",
        json={"viajeId": "VJ-01", "rutaId": "R-01", "muestras": []},
    )
    assert response.status_code == 422


def test_inference_rejects_oversized_batch_with_413(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("MAX_BATCH_SAMPLES", "3")
    payload = {
        "viajeId": "VJ-LARGE-01",
        "rutaId": "R-01",
        "muestras": [
            {
                "timestampRelativoMs": i * 100,
                "accelX": 0.1,
                "accelY": 0.1,
                "accelZ": 9.8,
            }
            for i in range(4)
        ],
    }
    response = client.post("/inference", json=payload)
    assert response.status_code == 413
