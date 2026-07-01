from shoptalk.lead_decay_score import lead_decay_score


def test_lead_decay_score_bounds():
    assert 0 <= lead_decay_score(80, 0, False) <= 100


def test_lead_decay_score_separates_strong_and_weak_signal():
    assert lead_decay_score(80, 0, False) > lead_decay_score(1, 2, True)
