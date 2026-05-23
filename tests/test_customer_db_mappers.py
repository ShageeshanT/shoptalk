from uuid import uuid4

from shoptalk.db_mappers import customer_from_record, customer_to_record
from shoptalk.schemas import Customer


def test_customer_mapper_preserves_contact_fields_and_tags():
    customer = Customer(
        business_id=uuid4(),
        name="Ama",
        phone="0771234567",
        email="ama@example.com",
        tags=["vip", "cakes"],
        notes="Prefers WhatsApp",
    )
    restored = customer_from_record(customer_to_record(customer))
    assert restored.phone == "0771234567"
    assert restored.email == "ama@example.com"
    assert restored.tags == ["vip", "cakes"]
    assert restored.notes == "Prefers WhatsApp"
