import re


def normalize_whitespace(value: str) -> str:
    """Collapse customer chat spacing without changing the actual words."""
    return re.sub(r"\s+", " ", value).strip()
