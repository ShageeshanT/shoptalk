from uuid import uuid4

from shoptalk.enums import MessageDirection
from shoptalk.schemas import ConversationMessageOut
from shoptalk.storage import InMemoryRepository


def test_repository_filters_by_multiple_fields() -> None:
    repository = InMemoryRepository[ConversationMessageOut]()
    business_id = uuid4()
    matching_customer_id = uuid4()
    other_customer_id = uuid4()

    matching = ConversationMessageOut(
        business_id=business_id,
        customer_id=matching_customer_id,
        sender=MessageDirection.CUSTOMER,
        text="I need cupcakes",
    )
    other = ConversationMessageOut(
        business_id=business_id,
        customer_id=other_customer_id,
        sender=MessageDirection.CUSTOMER,
        text="I need brownies",
    )
    repository.extend([matching, other])

    results = repository.filter_by(business_id=business_id, customer_id=matching_customer_id)

    assert results == [matching]
