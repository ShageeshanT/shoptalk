from shoptalk.pickup_status_badge import pickup_status_badge

def test_pickup_status_badge_known_values():
    assert pickup_status_badge('ready') == 'Ready for pickup'
    assert pickup_status_badge('collected') == 'Collected'
    assert pickup_status_badge('delayed') == 'Pickup delayed'

def test_pickup_status_badge_unknown_value():
    assert pickup_status_badge("") == 'Not ready'
