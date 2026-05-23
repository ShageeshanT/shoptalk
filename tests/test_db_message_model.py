from shoptalk.db_models import Base, MessageRecord


def test_message_table_is_registered():
    assert "messages" in Base.metadata.tables
    assert MessageRecord.__tablename__ == "messages"
