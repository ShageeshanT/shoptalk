from shoptalk.thread_heat_score import thread_heat_score


def test_thread_heat_score_bounds():
    assert 0 <= thread_heat_score(8, 90, 2) <= 100


def test_thread_heat_score_separates_strong_and_weak_signal():
    assert thread_heat_score(8, 90, 2) > thread_heat_score(1, 0, 0)
