"""Badge payloads for seller alert resolution states."""

from __future__ import annotations

from shoptalk.alert_resolution_copy import alert_resolution_copy

_BADGE_TONES = {
    "resolved": "success",
    "waiting_on_customer": "muted",
    "needs_seller_reply": "attention",
}


def alert_status_badge(status: str) -> dict[str, str]:
    """Return a small badge payload for an alert status."""

    normalized = status if status in _BADGE_TONES else "needs_seller_reply"
    return {
        "status": normalized,
        "tone": _BADGE_TONES[normalized],
        "label": alert_resolution_copy(normalized),
    }
