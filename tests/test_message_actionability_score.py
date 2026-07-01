from shoptalk.message_actionability_score import message_actionability_score

def test_message_actionability_score_stays_in_bounds():
    assert 0 <= message_actionability_score(0, 0, 0) <= 100
    assert 0 <= message_actionability_score(5, 5, 5) <= 100

def test_message_actionability_score_responds_to_stronger_signal():
    assert message_actionability_score(5, 5, 5) >= message_actionability_score(0, 0, 0)
