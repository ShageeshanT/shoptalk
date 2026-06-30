from shoptalk.order_priority_label import order_priority_label

def test_order_priority_label():
    assert order_priority_label(1) == "urgent"
    assert order_priority_label(8) == "today"
