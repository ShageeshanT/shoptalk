"""Compact seller dashboard helper for batch preparation size."""

from __future__ import annotations


def classify_batch_prep(orders_in_batch: int | float) -> str:
    """Return a short seller-facing label for batch preparation size."""
    return "Single prep" if orders_in_batch < 2 else "Batch prep" if orders_in_batch < 7 else "Large batch prep"
