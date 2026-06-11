from shoptalk.support_load_label import classify_support_load


def test_classify_support_load_labels_key_states():
    assert classify_support_load(-1) == 'Clear'
    assert classify_support_load(1) == 'Normal'
    assert classify_support_load(6) == 'Heavy'
