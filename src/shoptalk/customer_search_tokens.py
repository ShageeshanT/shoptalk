"""Search token helpers for customer lookup."""

from __future__ import annotations


def customer_search_tokens(name: str, phone: str | None = None) -> set[str]:
    """Build simple lowercase search tokens for customer records."""

    tokens = {part.lower() for part in name.split() if part.strip()}
    if phone:
        digits = "".join(ch for ch in phone if ch.isdigit())
        if digits:
            tokens.add(digits)
            tokens.add(digits[-4:])
    return tokens
