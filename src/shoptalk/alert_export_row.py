"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_export_row(level: str, title: str) -> dict[str, str]:
    return {"level": level, "title": title}
