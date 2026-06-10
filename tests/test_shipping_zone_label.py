from shoptalk.shipping_zone_label import shipping_zone_label

def test_shipping_zone_label_known_values():
    assert shipping_zone_label('local') == 'Local delivery'
    assert shipping_zone_label('regional') == 'Regional delivery'
    assert shipping_zone_label('international') == 'International delivery'

def test_shipping_zone_label_unknown_value():
    assert shipping_zone_label("") == 'Unknown zone'
