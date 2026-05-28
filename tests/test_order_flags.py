from shoptalk.order_flags import order_flags


def test_order_flags_combined():
    assert order_flags(60000, True, False) == ["same_day", "high_value", "payment_pending"]


def test_order_flags_empty_for_normal_paid_order():
    assert order_flags(1000, False, True) == []
