from shoptalk.promo_strength_label import promo_strength_label

def test_promo_strength_label_thresholds():
    assert promo_strength_label(80) == 'Strong promo'
    assert promo_strength_label(50) == 'Good promo'
    assert promo_strength_label(20) == 'Weak promo'

def test_promo_strength_label_invalid_value():
    assert promo_strength_label("bad") == 'No promo'
