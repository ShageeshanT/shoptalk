from shoptalk.product_visibility_label import product_visibility_label

def test_product_visibility_label_thresholds():
    assert product_visibility_label(1000) == 'Hot product'
    assert product_visibility_label(100) == 'Visible product'
    assert product_visibility_label(1) == 'Low visibility'

def test_product_visibility_label_invalid_value():
    assert product_visibility_label("bad") == 'Unseen product'
