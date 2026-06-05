from __future__ import annotations

def email_display(email: str | None) -> str:
    return email.strip().lower() if email and email.strip() else "No email"