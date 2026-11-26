"""Model integrity and anti-RCE security checks for bustrack-ml."""

from pathlib import Path
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_source_contains_no_unsafe_pickle_eval_or_exec() -> None:
    src_dir = Path(__file__).resolve().parents[1] / "src"
    for py_file in src_dir.rglob("*.py"):
        content = py_file.read_text(encoding="utf-8")
        assert "pickle.load(" not in content
        assert "pickle.loads(" not in content
        assert "eval(" not in content
        assert "exec(" not in content


def test_classifier_remains_bounded_under_extreme_adversarial_burst() -> None:
    payload = {
        "viajeId": "VJ-BURST-01",
        "rutaId": "R-01",
        "intervaloMuestreoMs": 100,
        "consentimientoUsuario": True,
        "muestras": [
            {"timestampRelativoMs": 0, "accelX": 50.0, "accelY": -50.0, "accelZ": 80.0},
            {"timestampRelativoMs": 100, "accelX": -40.0, "accelY": 40.0, "accelZ": -30.0},
        ],
    }
    res = client.post("/inference", json=payload)
    assert res.status_code in (200, 422)
    assert res.status_code != 500
