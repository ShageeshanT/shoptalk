from shoptalk.queue_focus_score import queue_focus_score

def test_queue_focus_score_stays_in_bounds():
    assert 0 <= queue_focus_score(0, 0, 0) <= 100
    assert 0 <= queue_focus_score(5, 5, 5) <= 100

def test_queue_focus_score_responds_to_stronger_signal():
    assert queue_focus_score(5, 5, 5) >= queue_focus_score(0, 0, 0)
