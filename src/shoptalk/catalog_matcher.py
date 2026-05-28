"""Catalog item matching helpers."""

from __future__ import annotations


def match_catalog_items(text: str, catalog_names: list[str]) -> list[str]:
    """Return catalog item names mentioned in customer text."""

    normalized = text.lower()
    return [name for name in catalog_names if name.lower() in normalized]
