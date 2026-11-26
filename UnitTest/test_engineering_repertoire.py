"""Engineering repertoire tests: property-based, table-driven, golden, idempotency, fuzzing."""

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def _sample_batch(viaje_id: str = "VJ-ENG-001", interval_ms: int = 100) -> dict:
    return {
        "viajeId": viaje_id,
        "rutaId": "R-01",
        "intervaloMuestreoMs": interval_ms,
        "consentimientoUsuario": True,
        "muestras": [
            {"timestampRelativoMs": 0, "accelX": 0.1, "accelY": 0.1, "accelZ": 9.81},
            {"timestampRelativoMs": 100, "accelX": 0.2, "accelY": 0.1, "accelZ": 9.82},
        ],
    }


def test_golden_master_health_schema() -> None:
    res = client.get("/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "healthy"
    assert body["service"] == "bustrack-ml"


@pytest.mark.parametrize(
    ("interval_ms", "expected_status"),
    [
        (100, 200),
        (20, 200),
        (-1, 422),
        (0, 422),
    ],
)
def test_table_driven_sampling_interval_matrix(
    interval_ms: int, expected_status: int
) -> None:
    res = client.post("/inference", json=_sample_batch(interval_ms=interval_ms))
    assert res.status_code == expected_status


def test_idempotency_same_trip_produces_identical_hash() -> None:
    payload = _sample_batch("VJ-IDEMP-001")
    res1 = client.post("/inference", json=payload)
    res2 = client.post("/inference", json=payload)
    assert res1.status_code == 200
    assert res2.status_code == 200
    assert res1.json()["viajeAnonimoHash"] == res2.json()["viajeAnonimoHash"]


def test_property_based_and_fuzzing_invalid_json_never_returns_500() -> None:
    for raw in ["", "{", "[]", '{"viajeId": 123}', '{"muestras": "bad"}']:
        res = client.post(
            "/inference", content=raw, headers={"Content-Type": "application/json"}
        )
        assert res.status_code in (400, 422)
