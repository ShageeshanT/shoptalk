from shoptalk.delivery_fee_badge import delivery_fee_badge

def test_delivery_fee_badge_thresholds():
    assert delivery_fee_badge(0) == 'Free delivery'
    assert delivery_fee_badge(500) == 'Standard delivery fee'
    assert delivery_fee_badge(1500) == 'High delivery fee'

def test_delivery_fee_badge_invalid_value():
    assert delivery_fee_badge("bad") == 'Custom delivery fee'
