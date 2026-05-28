from shoptalk.order_totals import order_subtotal, order_total


def test_order_subtotal():
    assert order_subtotal([100, 250.5]) == 350.5


def test_order_total_with_fee_and_discount():
    assert order_total([1000], delivery_fee=200, discount=100) == 1100


def test_order_total_never_negative():
    assert order_total([100], discount=500) == 0
