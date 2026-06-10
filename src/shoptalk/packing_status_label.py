from __future__ import annotations

def packing_status_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'packed': 'Packed',
        'packing': 'Packing',
        'blocked': 'Packing blocked',
    }
    return labels.get(normalized, 'Not packed')
