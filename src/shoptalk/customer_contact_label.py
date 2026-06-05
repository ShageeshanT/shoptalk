from __future__ import annotations


def customer_contact_label(phone: str | None = None, email: str | None = None) -> str:
    if phone and phone.strip():
        return "Phone available"
    if email and email.strip():
        return "Email available"
    return "No contact details"