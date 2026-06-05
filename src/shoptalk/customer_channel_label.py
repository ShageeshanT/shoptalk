from __future__ import annotations

def customer_channel_label(channel: str) -> str:
    return channel.replace("_", " ").title() if channel else "Manual"