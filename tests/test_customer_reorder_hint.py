from shoptalk.customer_reorder_hint import customer_reorder_hint


def test_customer_reorder_hint():
    assert customer_reorder_hint(30) == "good_time"
