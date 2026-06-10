from __future__ import annotations

def fulfillment_mode_label(mode: str) -> str:
    normalized = (mode or "").strip().lower().replace(" ", "_")
    labels = {
        'delivery': 'Delivery',
        'pickup': 'Pickup',
        'digital': 'Digital',
    }
    return labels.get(normalized, 'Manual fulfillment')
