from __future__ import annotations

def sla_minutes_label(minutes: int | None) -> str:
    if minutes is None: return "No SLA"
    if minutes < 60: return f"{minutes} min"
    return f"{minutes//60}h {minutes%60}m"