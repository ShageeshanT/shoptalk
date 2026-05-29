from datetime import datetime, timedelta, timezone
from uuid import uuid4

from shoptalk.followup_priority import followup_priority
from shoptalk.schemas import FollowUp


def _followup(due_at: datetime | None) -> FollowUp:
    return FollowUp(business_id=uuid4(), title="Check payment", due_at=due_at)


def test_followup_priority_labels_schedule_state() -> None:
    now = datetime(2026, 5, 29, 9, tzinfo=timezone.utc)

    assert followup_priority(_followup(None), now=now) == "unscheduled"
    assert followup_priority(_followup(now - timedelta(minutes=1)), now=now) == "overdue"
    assert followup_priority(_followup(now + timedelta(hours=6)), now=now) == "due_today"
    assert followup_priority(_followup(now + timedelta(days=3)), now=now) == "scheduled"
