from __future__ import annotations

def shipping_zone_label(zone: str) -> str:
    normalized = (zone or "").strip().lower().replace(" ", "_")
    labels = {
        'local': 'Local delivery',
        'regional': 'Regional delivery',
        'international': 'International delivery',
    }
    return labels.get(normalized, 'Unknown zone')
