from shoptalk.customer_reorder_score import customer_reorder_score

def test_customer_reorder_score_stays_in_bounds():
    assert 0 <= customer_reorder_score(0, 0, 0) <= 100
    assert 0 <= customer_reorder_score(5, 5, 5) <= 100

def test_customer_reorder_score_responds_to_stronger_signal():
    assert customer_reorder_score(5, 5, 5) >= customer_reorder_score(0, 0, 0)
