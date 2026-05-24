from datetime import timedelta
from uuid import uuid4

from shoptalk.date_utils import utc_now
from shoptalk.db_followup_repository import SqlFollowUpRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import FollowUpCreate


def test_sql_followup_repository_filters_due_items():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlFollowUpRepository(session)
    business_id = uuid4()
    repo.create(FollowUpCreate(business_id=business_id, title="Call", due_at=utc_now()))
    assert len(repo.search_for_business(business_id, status="open", due_before=utc_now() + timedelta(days=1))) == 1
    session.close()
