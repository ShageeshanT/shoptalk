import re


def detect_time_window(text: str) -> str | None:
    lowered = text.lower()
    for marker in ['morning', 'afternoon', 'evening', 'night']:
        if marker in lowered:
            return marker
    match = re.search(r"\b(\d{1,2})(?::\d{2})?\s?(am|pm)\b", lowered)
    if match:
        return match.group(0)
    return None
