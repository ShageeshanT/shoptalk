from datetime import datetime
from sqlalchemy.orm import Query

from shoptalk.db_models import FollowUpRecord


def filter_followups_by_status(query: Query, status: str | None):
    if not status:
        return query
    return query.filter(FollowUpRecord.status == status)


def filter_followups_due_before(query: Query, due_before: datetime | None):
    if due_before is None:
        return query
    return query.filter(FollowUpRecord.due_at <= due_before)
