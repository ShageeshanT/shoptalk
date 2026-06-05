from __future__ import annotations

def business_timezone_label(timezone: str) -> str:
    return timezone.replace("_", " ") or "Asia/Colombo"