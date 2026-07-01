from shoptalk.customer_patience_score import customer_patience_score

def test_customer_patience_score_stays_in_bounds():
    assert 0 <= customer_patience_score(0, 0, 0) <= 100
    assert 0 <= customer_patience_score(5, 5, 5) <= 100

def test_customer_patience_score_penalizes_long_waits():
    assert customer_patience_score(5, 5, 0) <= customer_patience_score(0, 0, 0)
