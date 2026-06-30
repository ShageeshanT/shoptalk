from __future__ import annotations

def followup_age_label(hours_old: float) -> str:
    if hours_old >= 48: return "stale"
    if hours_old >= 12: return "aging"
    return "fresh"
