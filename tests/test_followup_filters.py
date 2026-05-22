from datetime import timedelta
from uuid import uuid4

from shoptalk.date_utils import utc_now
from shoptalk.followup_filters import overdue_followups
from shoptalk.schemas import FollowUp


def test_overdue_followups_returns_open_items_before_now() -> None:
    now = utc_now()
    old = FollowUp(business_id=uuid4(), title="Call", due_at=now - timedelta(hours=1))
    future = FollowUp(business_id=uuid4(), title="Later", due_at=now + timedelta(hours=1))
    assert overdue_followups([old, future], now) == [old]
