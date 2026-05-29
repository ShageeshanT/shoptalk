from __future__ import annotations

from datetime import datetime, timezone

from shoptalk.schemas import FollowUp


def followup_priority(follow_up: FollowUp, *, now: datetime | None = None) -> str:
    now = now or datetime.now(timezone.utc)
    if follow_up.due_at is None:
        return "unscheduled"
    due_at = follow_up.due_at if follow_up.due_at.tzinfo else follow_up.due_at.replace(tzinfo=timezone.utc)
    if due_at <= now:
        return "overdue"
    hours_until_due = (due_at - now).total_seconds() / 3600
    if hours_until_due <= 24:
        return "due_today"
    return "scheduled"
