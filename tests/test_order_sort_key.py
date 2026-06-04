from shoptalk.order_sort_key import order_sort_key


def test_order_sort_key_prioritizes_urgent():
    assert order_sort_key("urgent", 5) < order_sort_key("normal", 1)


def test_order_sort_key_unknown_normal():
    assert order_sort_key("weird", 2) == (2, 2)
