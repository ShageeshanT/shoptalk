from __future__ import annotations

def delivery_status_badge(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    if normalized == "delivered":
        return "Delivered"
    if normalized in {"out_for_delivery", "on_the_way"}:
        return "Out for delivery"
    if normalized == "delayed":
        return "Delayed"
    if normalized in {"cancelled", "canceled"}:
        return "Cancelled"
    return "Preparing"
