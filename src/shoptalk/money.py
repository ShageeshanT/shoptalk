import re

_AMOUNT_RE = re.compile(r"(?:rs\.?|lkr)?\s*(\d[\d,]*(?:\.\d{1,2})?)", re.IGNORECASE)


def parse_lkr_amount(text: str) -> float | None:
    """Extract the first rupee amount from a casual customer message."""
    match = _AMOUNT_RE.search(text)
    if not match:
        return None
    return float(match.group(1).replace(',', ''))
