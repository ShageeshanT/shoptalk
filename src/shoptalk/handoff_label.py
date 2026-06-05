from __future__ import annotations

def handoff_label(required: bool) -> str:
    return "Human review needed" if required else "Assistant can draft"