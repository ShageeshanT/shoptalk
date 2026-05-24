from shoptalk.db_mappers import business_to_record
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.db_snapshot import business_snapshot
from shoptalk.schemas import Business


def test_business_snapshot_includes_business_and_counts():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    business = Business(name="Kavi Bakes")
    session.add(business_to_record(business)); session.commit()
    snapshot = business_snapshot(session, business.id)
    assert snapshot["business"]["name"] == "Kavi Bakes"
    assert snapshot["counts"]["orders"] == 0
    session.close()
