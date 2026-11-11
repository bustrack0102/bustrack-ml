"""Security tests for internal authentication and PII protection."""

from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)


def _valid_payload(viaje_id: str = "VJ-SEC-001") -> dict:
    return {
        "viajeId": viaje_id,
        "rutaId": "R-01",
        "intervaloMuestreoMs": 100,
        "consentimientoUsuario": True,
        "muestras": [
            {"timestampRelativoMs": 0, "accelX": 0.1, "accelY": 0.1, "accelZ": 9.81}
        ],
    }


def test_rejects_missing_or_invalid_internal_credential(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("INTERNAL_SERVICE_CREDENTIAL", "bustrack-ml-internal-2026")

    res_missing = client.post("/inference", json=_valid_payload())
    assert res_missing.status_code == 401

    res_wrong = client.post(
        "/inference",
        json=_valid_payload(),
        headers={"X-Internal-Key": "invalid-header-val"},
    )
    assert res_wrong.status_code == 403

    res_valid = client.post(
        "/inference",
        json=_valid_payload(),
        headers={"X-Internal-Key": "bustrack-ml-internal-2026"},
    )
    assert res_valid.status_code == 200


def test_rejects_pii_in_trip_identifier() -> None:
    response = client.post(
        "/inference",
        json=_valid_payload("conductor@uttt.edu.mx"),
    )
    assert response.status_code == 422


def test_rejects_missing_user_consent_with_422() -> None:
    payload = _valid_payload()
    payload["consentimientoUsuario"] = False
    response = client.post("/inference", json=payload)
    assert response.status_code == 422
