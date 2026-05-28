"""Seller note cleanup helpers."""

from __future__ import annotations


def normalize_seller_note(note: str) -> str:
    """Normalize a note before saving it."""

    return " ".join(note.strip().split())


def note_preview(note: str, limit: int = 60) -> str:
    """Build a short note preview."""

    normalized = normalize_seller_note(note)
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 1].rstrip() + "…"
