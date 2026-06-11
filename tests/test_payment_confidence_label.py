from shoptalk.payment_confidence_label import classify_payment_confidence


def test_classify_payment_confidence_labels_key_states():
    assert classify_payment_confidence(-1) == 'Unclear'
    assert classify_payment_confidence(40) == 'Likely'
    assert classify_payment_confidence(80) == 'Confirmed'
