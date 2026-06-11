from shoptalk.payment_method_label import classify_payment_method


def test_classify_payment_method_labels_key_states():
    assert classify_payment_method(False) == 'Manual'
    assert classify_payment_method(True) == 'Digital'
