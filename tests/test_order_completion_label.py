from shoptalk.order_completion_label import classify_order_completion


def test_classify_order_completion_labels_key_states():
    assert classify_order_completion(-1) == 'Started'
    assert classify_order_completion(40) == 'Halfway'
    assert classify_order_completion(100) == 'Ready'
