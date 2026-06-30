from shoptalk.order_margin_label import classify_order_margin


def test_classify_order_margin_labels_key_states():
    assert classify_order_margin(9) == "Thin margin"
    assert classify_order_margin(10) == "Healthy margin"
    assert classify_order_margin(30) == "Great margin"
