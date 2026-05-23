from uuid import uuid4

from shoptalk.db_followup_repository import SqlFollowUpRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import FollowUpCreate


def test_sql_followup_repository_lists_open_items():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlFollowUpRepository(session)
    business_id = uuid4()
    follow_up = repo.create(FollowUpCreate(business_id=business_id, title="Check payment"))
    assert [item.id for item in repo.list_open_for_business(business_id)] == [follow_up.id]
    session.close()
