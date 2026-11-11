"""Validated Pydantic contracts for BusTrack ML service (no PII allowed)."""

import math
from typing import List, Literal
from pydantic import BaseModel, Field, field_validator

ClassificationLabel = Literal[
    "BACHE_SEVERO",
    "ANOMALIA_VIBRACION_MODERADA",
    "PARADA_DETECTADA",
    "VIA_REGULAR_OPTIMA",
]


class AccelerometerSample(BaseModel):
    """Single triaxial inertial reading in m/s^2 relative to trip start."""

    timestampRelativoMs: int = Field(..., ge=0, le=86_400_000)
    accelX: float = Field(..., ge=-100.0, le=100.0)
    accelY: float = Field(..., ge=-100.0, le=100.0)
    accelZ: float = Field(..., ge=-100.0, le=100.0)

    @field_validator("accelX", "accelY", "accelZ")
    @classmethod
    def ensure_finite(cls, value: float) -> float:
        if not math.isfinite(value):
            raise ValueError("La lectura inercial debe ser finita.")
        return value


class InferenceRequest(BaseModel):
    """Anonymized batch payload for POST /inference."""

    viajeId: str = Field(..., min_length=2, max_length=64)
    rutaId: str = Field(..., min_length=2, max_length=64)
    intervaloMuestreoMs: int = Field(default=100, ge=10, le=5000)
    consentimientoUsuario: bool = Field(default=True)
    muestras: List[AccelerometerSample] = Field(..., min_length=1)

    @field_validator("consentimientoUsuario")
    @classmethod
    def require_explicit_consent(cls, consent: bool) -> bool:
        if not consent:
            raise ValueError(
                "Se requiere consentimiento explicito para procesar telemetria."
            )
        return consent


class DetectedEvent(BaseModel):
    """Window-level inertial event classified by the versioned ML pipeline."""

    tipoEvento: ClassificationLabel
    severidad: int = Field(..., ge=0, le=3)
    confianza: float = Field(..., ge=0.0, le=1.0)
    ventanaInicioMs: int = Field(..., ge=0)
    ventanaFinMs: int = Field(..., ge=0)
    rmsMagnitud: float = Field(..., ge=0.0)


class InferenceResponse(BaseModel):
    """Output payload returned to central BusTrack API."""

    inferenciaId: str
    viajeAnonimoHash: str
    rutaId: str
    modeloVersion: str
    clasificacionPrincipal: ClassificationLabel
    confianzaGlobal: float = Field(..., ge=0.0, le=1.0)
    severidadMaxima: int = Field(..., ge=0, le=3)
    totalMuestrasProcesadas: int = Field(..., ge=1)
    ventanasAnalizadas: int = Field(..., ge=1)
    eventosDetectados: List[DetectedEvent]
    procesadoEnMs: int = Field(..., ge=0)


class HealthResponse(BaseModel):
    """Output payload for GET /health."""

    status: Literal["healthy", "unhealthy"]
    service: str
    version: str
    modeloVersion: str
