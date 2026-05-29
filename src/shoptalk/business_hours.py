from __future__ import annotations

from datetime import datetime, time
from zoneinfo import ZoneInfo

COLOMBO_TZ = ZoneInfo("Asia/Colombo")


def is_within_business_hours(
    now: datetime,
    *,
    opens_at: time = time(9, 0),
    closes_at: time = time(18, 0),
) -> bool:
    """Check whether a message falls inside the seller's reply window."""
    local_now = now.astimezone(COLOMBO_TZ) if now.tzinfo else now.replace(tzinfo=COLOMBO_TZ)
    if local_now.weekday() >= 6:
        return False
    current_time = local_now.time()
    return opens_at <= current_time < closes_at


def reply_window_label(now: datetime) -> str:
    return "business_hours" if is_within_business_hours(now) else "after_hours"
