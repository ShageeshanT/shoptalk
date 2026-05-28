from shoptalk.customer_segments import customer_segment_label, customer_segment_priority


def test_customer_segment_labels_vip_by_order_count() -> None:
    assert customer_segment_label(order_count=10, total_spend=0) == "vip"


def test_customer_segment_labels_repeat_by_spend() -> None:
    assert customer_segment_label(order_count=1, total_spend=50_000) == "repeat"


def test_customer_segment_labels_prospect_without_orders() -> None:
    assert customer_segment_label(order_count=0, total_spend=0) == "prospect"


def test_customer_segment_priority_handles_unknown_segment() -> None:
    assert customer_segment_priority("unknown") == 0
