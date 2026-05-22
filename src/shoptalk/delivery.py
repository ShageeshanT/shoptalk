def detect_delivery_preference(text: str) -> str:
    lowered = text.lower()
    if 'pickup' in lowered or 'pick up' in lowered or 'collect' in lowered:
        return 'pickup'
    if 'deliver' in lowered or 'delivery' in lowered or 'courier' in lowered:
        return 'delivery'
    return 'unknown'
