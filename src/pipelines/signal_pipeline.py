"""Signal cleaning, sliding windowing, and statistical feature extraction (spec-05/06)."""

from dataclasses import dataclass
from typing import List, Sequence
import numpy as np
from src.core.schemas import AccelerometerSample

GRAVITY_MPS2 = 9.81


@dataclass(frozen=True)
class WindowFeatures:
    """Statistical features extracted from a fixed inertial time window."""

    start_ms: int
    end_ms: int
    mean_mag: float
    std_mag: float
    rms_mag: float
    peak_mag: float
    max_abs_z: float
    zero_crossings: int


def sort_and_clean_samples(
    samples: Sequence[AccelerometerSample],
) -> List[AccelerometerSample]:
    """Sort readings chronologically by relative timestamp without silent drops."""
    return sorted(samples, key=lambda item: item.timestampRelativoMs)


def build_sliding_windows(
    samples: Sequence[AccelerometerSample],
    window_size: int = 5,
    step: int = 3,
) -> List[List[AccelerometerSample]]:
    """Split samples into overlapping reproducible windows."""
    if not samples:
        return []
    ordered = sort_and_clean_samples(samples)
    if len(ordered) <= window_size:
        return [list(ordered)]

    windows: List[List[AccelerometerSample]] = []
    idx = 0
    while idx < len(ordered):
        end = idx + window_size
        chunk = list(ordered[idx:end])
        if chunk:
            windows.append(chunk)
        if end >= len(ordered):
            break
        idx += step
    return windows


def extract_window_features(window: Sequence[AccelerometerSample]) -> WindowFeatures:
    """Compute magnitude statistics and gravity-centered zero crossings."""
    accel_x = np.array([s.accelX for s in window], dtype=float)
    accel_y = np.array([s.accelY for s in window], dtype=float)
    accel_z = np.array([s.accelZ for s in window], dtype=float)

    magnitudes = np.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
    centered = magnitudes - GRAVITY_MPS2

    crossings = 0
    if len(centered) > 1:
        signs = np.sign(centered)
        signs[signs == 0] = 1
        crossings = int(np.sum(signs[1:] != signs[:-1]))

    return WindowFeatures(
        start_ms=window[0].timestampRelativoMs,
        end_ms=window[-1].timestampRelativoMs,
        mean_mag=float(np.mean(magnitudes)),
        std_mag=float(np.std(magnitudes)),
        rms_mag=float(np.sqrt(np.mean(magnitudes**2))),
        peak_mag=float(np.max(magnitudes)),
        max_abs_z=float(np.max(np.abs(accel_z))),
        zero_crossings=crossings,
    )
