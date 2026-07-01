from shoptalk.daily_sales_health_score import daily_sales_health_score

def test_daily_sales_health_score_stays_in_bounds():
    assert 0 <= daily_sales_health_score(0, 0, 0) <= 100
    assert 0 <= daily_sales_health_score(5, 5, 5) <= 100

def test_daily_sales_health_score_responds_to_stronger_signal():
    assert daily_sales_health_score(5, 5, 5) >= daily_sales_health_score(0, 0, 0)
