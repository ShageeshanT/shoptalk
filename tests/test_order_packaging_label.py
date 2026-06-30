from shoptalk.order_packaging_label import classify_order_packaging


def test_classify_order_packaging_labels_key_states():
    assert classify_order_packaging(2) == "Small pack"
    assert classify_order_packaging(3) == "Medium pack"
    assert classify_order_packaging(10) == "Bulk pack"
