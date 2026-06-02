def lead_temperature(intent: str, urgency: str, asks_price: bool = False) -> str:
    if intent == "new_order" and urgency == "high":
        return "hot"
    if intent in {"new_order", "product_inquiry"} or asks_price:
        return "warm"
    return "cold"
