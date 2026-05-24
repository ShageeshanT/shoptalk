from uuid import uuid4

from shoptalk.db_counts import business_record_counts
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database


def test_business_record_counts_default_to_zero():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    assert business_record_counts(session, uuid4()) == {"customers": 0, "orders": 0, "messages": 0, "follow_ups": 0}
    session.close()
