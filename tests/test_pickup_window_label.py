from shoptalk.pickup_window_label import label_pickup_window


def test_pickup_window_label():
    assert label_pickup_window(24) == "today"
