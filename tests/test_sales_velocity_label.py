from shoptalk.sales_velocity_label import classify_sales_velocity


def test_classify_sales_velocity_labels_key_states():
    assert classify_sales_velocity(-1) == 'Quiet'
    assert classify_sales_velocity(1) == 'Moving'
    assert classify_sales_velocity(6) == 'Hot'
