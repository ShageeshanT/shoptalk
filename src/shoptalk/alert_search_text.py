"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_search_text(title: str, message: str) -> str:
    return f"{title} {message}".strip().lower()
