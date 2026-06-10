from __future__ import annotations

def approval_status_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'approved': 'Approved',
        'pending': 'Pending approval',
        'rejected': 'Rejected',
    }
    return labels.get(normalized, 'Draft')
