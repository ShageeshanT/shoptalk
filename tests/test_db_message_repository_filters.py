from uuid import uuid4

from shoptalk.db_message_repository import SqlMessageRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import ConversationMessage


def test_sql_message_repository_filters_by_customer_and_channel():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlMessageRepository(session)
    business_id = uuid4(); customer_id = uuid4()
    repo.create(ConversationMessage(business_id=business_id, customer_id=customer_id, channel="whatsapp", text="Hi"))
    repo.create(ConversationMessage(business_id=business_id, channel="manual", text="Note"))
    assert [message.text for message in repo.search_for_business(business_id, customer_id=customer_id, channel="whatsapp")] == ["Hi"]
    session.close()
