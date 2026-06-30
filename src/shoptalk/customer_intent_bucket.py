from __future__ import annotations

def customer_intent_bucket(text: str) -> str:
    lowered = text.lower()
    if "price" in lowered or "cost" in lowered: return "pricing"
    if "deliver" in lowered: return "delivery"
    return "general"
