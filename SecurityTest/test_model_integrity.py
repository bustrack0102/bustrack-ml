"""Model integrity and anti-RCE security checks for bustrack-ml."""

import os
from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_source_contains_no_dynamic_code_execution() -> None:
    """Ensure application source contains no obvious dynamic code execution."""
    src_dir = Path(__file__).resolve().parents[1] / "src"

    for py_file in src_dir.rglob("*.py"):
        content = py_file.read_text(encoding="utf-8")

        assert "pickle.load(" not in content
        assert "pickle.loads(" not in content
        assert "eval(" not in content
        assert "exec(" not in content
        assert "joblib.load(" not in content


def test_classifier_remains_bounded_under_extreme_values() -> None:
    """Extreme accelerometer values must be validated, not cause a 500 error."""
        payload = {
        "viajeId": "VJ-BURST-01",
        "rutaId": "R-01",
        "intervaloMuestreoMs": 100,
        "consentimientoUsuario": True,
        "muestras": [
            {
                "timestampRelativoMs": 0,
                "accelX": 50.0,
                "accelY": -50.0,
                "accelZ": 80.0,
            },
            {
                "timestampRelativoMs": 100,
                "accelX": -40.0,
                "accelY": 40.0,
                "accelZ": -30.0,
            },
        ],
    }

    credential = os.getenv("INTERNAL_SERVICE_CREDENTIAL", "")
    headers = {"X-Internal-Key": credential} if credential else {}

    response = client.post("/inference", json=payload, headers=headers)

    assert response.status_code in (200, 422)
    assert response.status_code != 500
