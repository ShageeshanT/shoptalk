from uuid import uuid4

import pytest

from shoptalk.db_message_repository import SqlMessageRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.persistence_errors import DuplicateRecordError
from shoptalk.schemas import ConversationMessage


def test_sql_message_repository_rejects_duplicate_external_id():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlMessageRepository(session)
    business_id = uuid4()
    repo.create(ConversationMessage(business_id=business_id, text="Hi", external_message_id="wa-1"))
    with pytest.raises(DuplicateRecordError):
        repo.create(ConversationMessage(business_id=business_id, text="Again", external_message_id="wa-1"))
    session.close()
