from datetime import datetime, timezone

from shoptalk.enums import FollowUpStatus
from shoptalk.schemas import FollowUp


def is_open_follow_up(follow_up: FollowUp) -> bool:
    return follow_up.status == FollowUpStatus.OPEN


def follow_up_priority(follow_up: FollowUp) -> int:
    if not is_open_follow_up(follow_up):
        return 0
    if follow_up.due_at is None:
        return 1

    due_at = follow_up.due_at
    if due_at.tzinfo is None:
        due_at = due_at.replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    return 3 if due_at <= now else 2
