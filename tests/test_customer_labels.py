from uuid import uuid4

from shoptalk.customer_labels import customer_display_label
from shoptalk.schemas import Customer


def test_customer_display_label_prefers_phone() -> None:
    customer = Customer(business_id=uuid4(), name="Nimali", phone="94770000000")
    assert customer_display_label(customer) == "Nimali (94770000000)"
