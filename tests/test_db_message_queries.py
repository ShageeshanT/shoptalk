from uuid import uuid4

from shoptalk.db_mappers import message_to_record
from shoptalk.db_message_queries import filter_messages_by_channel, filter_messages_by_customer
from shoptalk.db_models import MessageRecord
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import ConversationMessageOut


def test_message_query_filters_by_customer_and_channel():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    customer_id = uuid4()
    session.add(message_to_record(ConversationMessageOut(business_id=uuid4(), customer_id=customer_id, channel="whatsapp", text="Hi")))
    session.commit()
    query = filter_messages_by_channel(filter_messages_by_customer(session.query(MessageRecord), customer_id), "whatsapp")
    assert query.count() == 1
    session.close()
