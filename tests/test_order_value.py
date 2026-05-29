from uuid import uuid4

from shoptalk.order_value import order_value_band, order_value_summary
from shoptalk.schemas import Order


def _order(total_amount: float | None) -> Order:
    return Order(business_id=uuid4(), title="Order", total_amount=total_amount)


def test_order_value_band_thresholds() -> None:
    assert order_value_band(_order(None)) == "unknown"
    assert order_value_band(_order(25000)) == "high"
    assert order_value_band(_order(7500)) == "medium"
    assert order_value_band(_order(1200)) == "low"


def test_order_value_summary_counts_bands() -> None:
    summary = order_value_summary([_order(30000), _order(12000), _order(1000), _order(None)])

    assert summary == {"high": 1, "medium": 1, "low": 1, "unknown": 1}
