"""Seller alert helpers for surfacing risky or urgent conversations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SellerAlert:
    """Small alert object shown in a seller workspace."""

    level: str
    title: str
    message: str


NEGATIVE_MARKERS = ("angry", "refund", "cancel", "late", "wrong", "bad")
URGENT_MARKERS = ("urgent", "today", "now", "asap", "immediately")


def build_seller_alert(text: str) -> SellerAlert | None:
    """Create a lightweight seller alert from message text."""

    normalized = text.lower()
    if any(marker in normalized for marker in NEGATIVE_MARKERS):
        return SellerAlert("danger", "Customer needs attention", text)
    if any(marker in normalized for marker in URGENT_MARKERS):
        return SellerAlert("warning", "Time sensitive chat", text)
    return None
