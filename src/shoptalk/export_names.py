"""Export filename helpers."""

from __future__ import annotations


def safe_export_name(name: str) -> str:
    """Return a simple safe filename stem."""

    cleaned = "".join(ch.lower() if ch.isalnum() else "_" for ch in name.strip())
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_") or "export"
