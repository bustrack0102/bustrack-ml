"""Anonymization and integrity helpers for telemetry batches (spec-04)."""

import hashlib
import re

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


class IntegrityViolationError(ValueError):
    """Raised when a batch fails anonymization or integrity constraints."""


def anonymize_trip_identifier(viaje_id: str) -> str:
    """Create a one-way SHA-256 truncated hash for non-PII observability."""
    cleaned = viaje_id.strip()
    if EMAIL_PATTERN.search(cleaned):
        raise IntegrityViolationError(
            "El identificador de viaje no debe contener datos personales."
        )
    digest = hashlib.sha256(cleaned.encode("utf-8")).hexdigest()
    return digest[:16]
