from shoptalk.upsell_window_label import classify_upsell_window


def test_classify_upsell_window_labels_key_states():
    assert classify_upsell_window(2499) == "No upsell"
    assert classify_upsell_window(2500) == "Soft upsell"
    assert classify_upsell_window(7500) == "Prime upsell"
