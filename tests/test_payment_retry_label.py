from shoptalk.payment_retry_label import classify_payment_retry


def test_classify_payment_retry_labels_key_states():
    assert classify_payment_retry(0) == "No retry"
    assert classify_payment_retry(1) == "Retry gently"
    assert classify_payment_retry(3) == "Escalate payment"
