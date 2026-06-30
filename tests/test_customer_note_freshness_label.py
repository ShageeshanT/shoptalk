from shoptalk.customer_note_freshness_label import classify_customer_note_freshness


def test_classify_customer_note_freshness_labels_key_states():
    assert classify_customer_note_freshness(13) == "Fresh note"
    assert classify_customer_note_freshness(14) == "Review note"
    assert classify_customer_note_freshness(45) == "Stale note"
