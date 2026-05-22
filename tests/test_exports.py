from uuid import uuid4

from shoptalk.exports import order_export_row
from shoptalk.schemas import Order


def test_order_export_row_serializes_business_fields() -> None:
    order = Order(business_id=uuid4(), title="Cake", total_amount=4500)
    row = order_export_row(order)
    assert row["title"] == "Cake"
    assert row["total_amount"] == "4500.0"
