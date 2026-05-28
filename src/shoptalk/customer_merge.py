"""Customer merge helpers."""

from __future__ import annotations


def normalized_phone(phone: str) -> str:
    """Normalize a phone number to digits for duplicate checks."""

    return "".join(ch for ch in phone if ch.isdigit())


def likely_same_customer(name_a: str, phone_a: str, name_b: str, phone_b: str) -> bool:
    """Return whether two customer records are likely duplicates."""

    if normalized_phone(phone_a) and normalized_phone(phone_a) == normalized_phone(phone_b):
        return True
    return name_a.strip().lower() == name_b.strip().lower()
