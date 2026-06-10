from shoptalk.address_quality_label import address_quality_label

def test_address_quality_label_thresholds():
    assert address_quality_label(80) == 'Clear address'
    assert address_quality_label(50) == 'Needs landmark'
    assert address_quality_label(20) == 'Needs confirmation'

def test_address_quality_label_invalid_value():
    assert address_quality_label("bad") == 'Missing address'
