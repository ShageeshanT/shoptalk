from shoptalk.pickup_queue_label import classify_pickup_queue


def test_classify_pickup_queue_labels_key_states():
    assert classify_pickup_queue(2) == "Quiet pickup"
    assert classify_pickup_queue(3) == "Pickup building"
    assert classify_pickup_queue(8) == "Pickup crowded"
