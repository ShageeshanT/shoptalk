from __future__ import annotations

from datetime import datetime


def delivery_slot_label(delivery_at: datetime | None) -> str:
    if delivery_at is None:
        return "delivery_not_set"
    hour = delivery_at.hour
    if 5 <= hour < 12:
        return "morning_delivery"
    if 12 <= hour < 17:
        return "afternoon_delivery"
    if 17 <= hour < 22:
        return "evening_delivery"
    return "late_delivery"


def delivery_slot_summary(delivery_at: datetime | None) -> str:
    label = delivery_slot_label(delivery_at)
    return label.replace("_", " ")
