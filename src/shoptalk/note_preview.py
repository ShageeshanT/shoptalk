from __future__ import annotations

def note_preview(text: str | None, limit: int=40) -> str:
    text=(text or "").strip()
    return text if len(text)<=limit else text[:limit-1].rstrip()+"…"