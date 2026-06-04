from shoptalk.seller_focus_score import seller_focus_score


def test_seller_focus_score_weights_workload():
    assert seller_focus_score(2, 3, 4) == 19


def test_seller_focus_score_caps():
    assert seller_focus_score(200, 100, 100) == 100
