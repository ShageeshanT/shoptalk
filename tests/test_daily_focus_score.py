from shoptalk.daily_focus_score import daily_focus_score


def test_daily_focus_score_bounds():
    assert 0 <= daily_focus_score(4, 4, 3) <= 100


def test_daily_focus_score_separates_strong_and_weak_signal():
    assert daily_focus_score(4, 4, 3) > daily_focus_score(0, 0, 0)
