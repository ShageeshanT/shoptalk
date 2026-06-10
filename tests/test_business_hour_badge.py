from shoptalk.business_hour_badge import business_hour_badge

def test_business_hour_badge_thresholds():
    assert business_hour_badge(1) == 'Open now'
    assert business_hour_badge(0) == 'Closed now'
    assert business_hour_badge(2) == 'Special hours'

def test_business_hour_badge_invalid_value():
    assert business_hour_badge("bad") == 'Hours unknown'
