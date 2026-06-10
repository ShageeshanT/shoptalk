from shoptalk.delivery_status_badge import delivery_status_badge

def test_delivery_status_badge_known_states():
    assert delivery_status_badge("delivered") == "Delivered"
    assert delivery_status_badge("out for delivery") == "Out for delivery"
    assert delivery_status_badge("delayed") == "Delayed"

def test_delivery_status_badge_default():
    assert delivery_status_badge(None) == "Preparing"
