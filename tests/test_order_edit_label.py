from shoptalk.order_edit_label import classify_order_edit


def test_classify_order_edit_labels_key_states():
    assert classify_order_edit(-1) == 'Stable'
    assert classify_order_edit(1) == 'Changed'
    assert classify_order_edit(4) == 'Messy'
