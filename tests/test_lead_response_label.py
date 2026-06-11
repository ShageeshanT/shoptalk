from shoptalk.lead_response_label import classify_lead_response


def test_classify_lead_response_labels_key_states():
    assert classify_lead_response(-1) == 'Instant'
    assert classify_lead_response(6) == 'Fast'
    assert classify_lead_response(40) == 'Warm'
