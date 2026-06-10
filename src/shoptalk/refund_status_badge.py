from __future__ import annotations

def refund_status_badge(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'approved': 'Refund approved',
        'requested': 'Refund requested',
        'rejected': 'Refund rejected',
    }
    return labels.get(normalized, 'No refund')
