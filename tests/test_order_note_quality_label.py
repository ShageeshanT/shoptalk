from shoptalk.order_note_quality_label import classify_order_note_quality


def test_classify_order_note_quality_labels_key_states():
    assert classify_order_note_quality(-1) == 'Missing'
    assert classify_order_note_quality(1) == 'Brief'
    assert classify_order_note_quality(40) == 'Detailed'
