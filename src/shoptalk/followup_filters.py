from datetime import datetime

from shoptalk.enums import FollowUpStatus
from shoptalk.schemas import FollowUp


def overdue_followups(followups: list[FollowUp], now: datetime) -> list[FollowUp]:
    return [item for item in followups if item.status == FollowUpStatus.OPEN and item.due_at is not None and item.due_at < now]
