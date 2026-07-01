from shoptalk.customer_engagement_score import customer_engagement_score

def test_customer_engagement_score_stays_in_bounds():
    assert 0 <= customer_engagement_score(0, 0, 0) <= 100
    assert 0 <= customer_engagement_score(5, 5, 5) <= 100

def test_customer_engagement_score_responds_to_stronger_signal():
    assert customer_engagement_score(5, 5, 5) >= customer_engagement_score(0, 0, 0)
