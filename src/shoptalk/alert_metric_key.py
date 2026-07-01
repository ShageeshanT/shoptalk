"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_metric_key(level: str) -> str:
    return f"seller_alerts.{level if level in {"danger", "warning", "info"} else "unknown"}"
