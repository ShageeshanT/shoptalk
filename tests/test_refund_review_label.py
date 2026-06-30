from shoptalk.refund_review_label import classify_refund_review


def test_classify_refund_review_labels_key_states():
    assert classify_refund_review(2) == "Simple refund"
    assert classify_refund_review(3) == "Review refund"
    assert classify_refund_review(7) == "Manager review"
