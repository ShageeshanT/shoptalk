"""Small helper for seller alert UI."""

from __future__ import annotations


def filter_alert_levels(levels: list[str], selected: str) -> list[str]:
    return levels if selected == "all" else [level for level in levels if level == selected]
