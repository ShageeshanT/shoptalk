from __future__ import annotations

def customer_segment_label(segment: str) -> str:
    normalized = (segment or "").strip().lower().replace(" ", "_")
    labels = {
        'vip': 'VIP',
        'repeat': 'Repeat customer',
        'new': 'New customer',
    }
    return labels.get(normalized, 'Unsegmented')
