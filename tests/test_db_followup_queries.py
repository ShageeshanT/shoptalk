from datetime import timedelta
from uuid import uuid4

from shoptalk.date_utils import utc_now
from shoptalk.db_followup_queries import filter_followups_due_before, filter_followups_by_status
from shoptalk.db_mappers import followup_to_record
from shoptalk.db_models import FollowUpRecord
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import FollowUp


def test_followup_query_filters_by_status_and_due_date():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    session.add(followup_to_record(FollowUp(business_id=uuid4(), title="Call", due_at=utc_now())))
    session.commit()
    query = filter_followups_due_before(filter_followups_by_status(session.query(FollowUpRecord), "open"), utc_now() + timedelta(days=1))
    assert query.count() == 1
    session.close()
