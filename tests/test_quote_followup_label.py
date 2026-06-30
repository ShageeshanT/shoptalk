from shoptalk.quote_followup_label import classify_quote_followup


def test_classify_quote_followup_labels_key_states():
    assert classify_quote_followup(5) == "Fresh quote"
    assert classify_quote_followup(6) == "Follow up soon"
    assert classify_quote_followup(24) == "Quote going cold"
