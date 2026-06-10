from shoptalk.customer_age_label import customer_age_label

def test_customer_age_label_thresholds():
    assert customer_age_label(365) == 'Long-term customer'
    assert customer_age_label(90) == 'Returning customer'
    assert customer_age_label(7) == 'New customer'

def test_customer_age_label_invalid_value():
    assert customer_age_label("bad") == 'Fresh lead'
