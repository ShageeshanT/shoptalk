from shoptalk.inbox_backlog_score import inbox_backlog_score


def test_inbox_backlog_score_bounds():
    assert 0 <= inbox_backlog_score(9, 4, 3) <= 100


def test_inbox_backlog_score_separates_strong_and_weak_signal():
    assert inbox_backlog_score(9, 4, 3) > inbox_backlog_score(0, 0, 0)
