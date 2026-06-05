from __future__ import annotations

def followup_status_label(status) -> str:
    return str(status).replace("_", " ").title()