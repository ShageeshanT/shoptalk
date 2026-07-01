from shoptalk.customer_lifetime_value_score import customer_lifetime_value_score

def test_customer_lifetime_value_score_stays_in_bounds():
    assert 0 <= customer_lifetime_value_score(0, 0, 0) <= 100
    assert 0 <= customer_lifetime_value_score(5, 5, 5) <= 100

def test_customer_lifetime_value_score_responds_to_stronger_signal():
    assert customer_lifetime_value_score(5, 5, 5) >= customer_lifetime_value_score(0, 0, 0)
