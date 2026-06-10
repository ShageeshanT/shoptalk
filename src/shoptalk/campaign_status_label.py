from __future__ import annotations

def campaign_status_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'active': 'Active campaign',
        'paused': 'Paused campaign',
        'ended': 'Ended campaign',
    }
    return labels.get(normalized, 'Draft campaign')
