from __future__ import annotations

def pickup_status_badge(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'ready': 'Ready for pickup',
        'collected': 'Collected',
        'delayed': 'Pickup delayed',
    }
    return labels.get(normalized, 'Not ready')
