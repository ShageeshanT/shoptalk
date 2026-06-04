KEYWORDS = {
    "buy": "purchase",
    "order": "purchase",
    "price": "pricing",
    "cost": "pricing",
    "available": "availability",
    "deliver": "delivery",
}


def buyer_intent(text: str) -> str:
    normalized = text.lower()
    for keyword, intent in KEYWORDS.items():
        if keyword in normalized:
            return intent
    return "general"
