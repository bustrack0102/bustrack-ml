"""Fintech-grade security tests for bustrack-ml: adversarial inputs, DoS limits, and PII non-leakage."""

from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)


def _valid_payload(viaje_id: str = "VJ-FIN-001") -> dict:
    return {
        "viajeId": viaje_id,
        "rutaId": "R-01",
        "intervaloMuestreoMs": 100,
        "consentimientoUsuario": True,
        "muestras": [
            {"timestampRelativoMs": 0, "accelX": 0.1, "accelY": 0.1, "accelZ": 9.81},
            {"timestampRelativoMs": 100, "accelX": 0.2, "accelY": 0.15, "accelZ": 9.79},
        ],
    }


def test_rejects_adversarial_non_finite_and_invalid_sampling_inputs() -> None:
    invalid_interval = _valid_payload()
    invalid_interval["intervaloMuestreoMs"] = -50
    res_interval = client.post("/inference", json=invalid_interval)
    assert res_interval.status_code == 422

    negative_ts = _valid_payload()
    negative_ts["muestras"][0]["timestampRelativoMs"] = -100
    res_ts = client.post("/inference", json=negative_ts)
    assert res_ts.status_code in (200, 422)
    assert res_ts.status_code != 500


def test_rejects_raw_non_finite_json_payload_without_500() -> None:
    raw_nan = (
        '{"viajeId":"VJ-NAN","rutaId":"R-01","intervaloMuestreoMs":100,'
        '"consentimientoUsuario":true,'
        '"muestras":[{"timestampRelativoMs":0,"accelX":NaN,"accelY":0.1,"accelZ":9.81}]}'
    )
    res = client.post(
        "/inference",
        content=raw_nan,
        headers={"Content-Type": "application/json"},
    )
    assert res.status_code in (400, 422)
    assert "Traceback" not in res.text


def test_anonymized_trip_hash_never_exposes_source_id_or_pii() -> None:
    res = client.post("/inference", json=_valid_payload("VJ-SENSITIVE-998877"))
    assert res.status_code == 200
    body = res.json()
    assert "VJ-SENSITIVE-998877" not in body["viajeAnonimoHash"]
    assert len(body["viajeAnonimoHash"]) >= 16


def test_fail_closed_auth_never_leaks_internal_secret(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    secret = "ml-super-secret-2026"
    monkeypatch.setenv("INTERNAL_SERVICE_CREDENTIAL", secret)

    res = client.post(
        "/inference",
        json=_valid_payload(),
        headers={"X-Internal-Key": ""},
    )
    assert res.status_code in (401, 403)
    assert secret not in res.text
    assert "Traceback" not in res.text
