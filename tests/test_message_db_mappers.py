from uuid import uuid4

from shoptalk.db_mappers import message_from_record, message_to_record
from shoptalk.schemas import ConversationMessageOut


def test_message_mapper_preserves_external_id_and_text():
    message = ConversationMessageOut(business_id=uuid4(), text="Hi", external_message_id="wa-1")
    restored = message_from_record(message_to_record(message))
    assert restored.text == "Hi"
    assert restored.external_message_id == "wa-1"
    assert restored.sender == message.sender
