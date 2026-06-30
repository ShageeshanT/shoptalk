from shoptalk.pickup_window_label import pickup_window_label

def test_pickup_window_label():
    assert pickup_window_label(0) == "now"
    assert pickup_window_label(45) == "within the hour"
    assert pickup_window_label(600) == "today"
