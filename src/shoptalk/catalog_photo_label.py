"""Compact seller dashboard helper for catalog photo completeness."""

from __future__ import annotations


def classify_catalog_photo(missing_photos: int | float) -> str:
    """Return a short seller-facing label for catalog photo completeness."""
    return "Photos ready" if missing_photos < 1 else "Add photos" if missing_photos < 5 else "Photo gap"
