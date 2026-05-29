from __future__ import annotations


def display_contact(phone: str | None = None, email: str | None = None) -> str:
    if phone and email:
        return f"{phone} · {email}"
    if phone:
        return phone
    if email:
        return email
    return "No contact route"


def mask_phone(phone: str) -> str:
    digits = "".join(char for char in phone if char.isdigit())
    if len(digits) <= 4:
        return "••••"
    return f"••••{digits[-4:]}"
