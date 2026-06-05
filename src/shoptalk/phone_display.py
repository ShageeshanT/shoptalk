from __future__ import annotations

def phone_display(phone: str | None) -> str:
    if not phone: return "No phone"
    cleaned="".join(ch for ch in phone if ch.isdigit() or ch=="+")
    return cleaned or "No phone"