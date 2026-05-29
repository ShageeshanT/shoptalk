from __future__ import annotations

import re

_WHITESPACE_RE = re.compile(r"\s+")
_REPEATED_PUNCTUATION_RE = re.compile(r"([!?])\1{2,}")


def clean_customer_text(text: str) -> str:
    """Normalize noisy incoming customer text without changing meaning."""
    cleaned = _WHITESPACE_RE.sub(" ", text).strip()
    return _REPEATED_PUNCTUATION_RE.sub(r"\1\1", cleaned)


def preview_customer_text(text: str, *, limit: int = 80) -> str:
    cleaned = clean_customer_text(text)
    if len(cleaned) <= limit:
        return cleaned
    return f"{cleaned[: limit - 1].rstrip()}…"
