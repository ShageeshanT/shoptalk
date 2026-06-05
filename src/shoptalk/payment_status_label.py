from __future__ import annotations

def payment_status_label(status: str) -> str:
    return status.replace("_", " ").strip().title() if status else "Unknown"