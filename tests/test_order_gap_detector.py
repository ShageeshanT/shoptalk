from shoptalk.order_gap_detector import order_gaps


def test_order_gaps_lists_missing_fields():
    assert order_gaps({"customer": "A", "items": ["cake"]}) == ["delivery", "payment"]


def test_order_gaps_empty_when_complete():
    assert order_gaps({"customer": "A", "items": ["cake"], "delivery": "Friday", "payment": "paid"}) == []
