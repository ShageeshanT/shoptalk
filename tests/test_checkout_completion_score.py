from shoptalk.checkout_completion_score import checkout_completion_score

def test_checkout_completion_score_stays_in_bounds():
    assert 0 <= checkout_completion_score(0, 0, 0) <= 100
    assert 0 <= checkout_completion_score(5, 5, 5) <= 100

def test_checkout_completion_score_responds_to_stronger_signal():
    assert checkout_completion_score(5, 5, 5) >= checkout_completion_score(0, 0, 0)
