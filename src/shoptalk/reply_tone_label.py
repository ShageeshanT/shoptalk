from __future__ import annotations

def reply_tone_label(tone: str) -> str:
    normalized = (tone or "").strip().lower().replace(" ", "_")
    labels = {
        'friendly': 'Friendly',
        'formal': 'Formal',
        'urgent': 'Urgent',
    }
    return labels.get(normalized, 'Neutral')
