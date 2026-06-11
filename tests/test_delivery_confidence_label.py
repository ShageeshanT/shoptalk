from shoptalk.delivery_confidence_label import classify_delivery_confidence


def test_classify_delivery_confidence_labels_key_states():
    assert classify_delivery_confidence(-1) == 'Low'
    assert classify_delivery_confidence(40) == 'Medium'
    assert classify_delivery_confidence(80) == 'High'
