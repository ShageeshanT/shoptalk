from shoptalk.daily_sales_label import daily_sales_label

def test_daily_sales_label_thresholds():
    assert daily_sales_label(100000) == 'Strong sales day'
    assert daily_sales_label(25000) == 'Good sales day'
    assert daily_sales_label(1) == 'Sales recorded'

def test_daily_sales_label_invalid_value():
    assert daily_sales_label("bad") == 'No sales'
