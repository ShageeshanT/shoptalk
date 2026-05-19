from uuid import uuid4

from shoptalk.message_tagging import detect_message_tags, tag_messages
from shoptalk.schemas import ConversationMessageOut


def test_detect_message_tags_finds_commercial_topics() -> None:
    tags = detect_message_tags("How much is delivery? I can pay a deposit today")

    assert "price" in tags
    assert "delivery" in tags
    assert "payment" in tags
    assert "urgent" in tags


def test_tag_messages_filters_by_business() -> None:
    business_id = uuid4()
    other_business_id = uuid4()
    tags = tag_messages(
        [
            ConversationMessageOut(business_id=business_id, text="Need delivery asap"),
            ConversationMessageOut(business_id=other_business_id, text="Need a refund"),
        ],
        business_id=business_id,
    )

    assert len(tags) == 1
    assert tags[0].tags == ["delivery", "urgent"]
