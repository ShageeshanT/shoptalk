from shoptalk.checkout_dropoff_label import classify_checkout_dropoff


def test_classify_checkout_dropoff_labels_key_states():
    assert classify_checkout_dropoff(19) == "Active checkout"
    assert classify_checkout_dropoff(20) == "Nudge checkout"
    assert classify_checkout_dropoff(90) == "Rescue checkout"
