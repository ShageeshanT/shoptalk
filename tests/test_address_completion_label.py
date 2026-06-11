from shoptalk.address_completion_label import classify_address_completion


def test_classify_address_completion_labels_key_states():
    assert classify_address_completion(-1) == 'Missing'
    assert classify_address_completion(2) == 'Partial'
    assert classify_address_completion(5) == 'Complete'
