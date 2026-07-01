"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_safe_title(title: str) -> str:
    return title.strip() or "Untitled alert"
