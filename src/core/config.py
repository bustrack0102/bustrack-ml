"""Environment-based configuration for BusTrack ML service."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceConfig:
    """Immutable configuration loaded from environment variables."""

    service_name: str
    service_version: str
    model_version: str
    environment: str
    internal_credential: str
    max_batch_samples: int
    min_confidence: float


def load_config() -> ServiceConfig:
    """Load configuration from environment without hardcoded credentials."""
    return ServiceConfig(
        service_name=os.getenv("SERVICE_NAME", "bustrack-ml"),
        service_version=os.getenv("SERVICE_VERSION", "1.0.0"),
        model_version=os.getenv("MODEL_VERSION", "1.0.0"),
        environment=os.getenv("ENVIRONMENT", "production"),
        internal_credential=os.getenv("INTERNAL_SERVICE_CREDENTIAL", ""),
        max_batch_samples=int(os.getenv("MAX_BATCH_SAMPLES", "1000")),
        min_confidence=float(os.getenv("MIN_CONFIDENCE", "0.60")),
    )
