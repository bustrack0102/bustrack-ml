"""HTTP endpoints for BusTrack ML service (GET /health, POST /inference)."""

from fastapi import APIRouter, Depends, HTTPException, status
from src.core.config import load_config
from src.core.schemas import HealthResponse, InferenceRequest, InferenceResponse
from src.core.security import verify_internal_caller
from src.data.anonymizer import IntegrityViolationError
from src.models.classifier import run_inference

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
def get_health() -> HealthResponse:
    """Return internal service health status without exposing internals."""
    cfg = load_config()
    return HealthResponse(
        status="healthy",
        service=cfg.service_name,
        version=cfg.service_version,
        modeloVersion=cfg.model_version,
    )


@router.post(
    "/inference",
    response_model=InferenceResponse,
    dependencies=[Depends(verify_internal_caller)],
    tags=["Inference"],
)
def post_inference(payload: InferenceRequest) -> InferenceResponse:
    """Classify an anonymized accelerometer batch from the central API."""
    cfg = load_config()
    if len(payload.muestras) > cfg.max_batch_samples:
        raise HTTPException(
            status_code=status.HTTP_413_CONTENT_TOO_LARGE,
            detail=(
                f"El lote excede el limite maximo permitido de "
                f"{cfg.max_batch_samples} muestras."
            ),
        )

    try:
        return run_inference(payload)
    except IntegrityViolationError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
