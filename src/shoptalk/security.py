SENSITIVE_MARKERS = ['password', 'otp', 'one time password', 'api key', 'secret']


def contains_sensitive_marker(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in SENSITIVE_MARKERS)
