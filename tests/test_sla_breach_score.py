from shoptalk.sla_breach_score import sla_breach_score


def test_sla_breach_score_bounds():
    assert 0 <= sla_breach_score(180, 3, True) <= 100


def test_sla_breach_score_separates_strong_and_weak_signal():
    assert sla_breach_score(180, 3, True) > sla_breach_score(0, 1, False)
