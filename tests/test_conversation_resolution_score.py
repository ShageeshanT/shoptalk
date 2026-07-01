from shoptalk.conversation_resolution_score import conversation_resolution_score

def test_conversation_resolution_score_stays_in_bounds():
    assert 0 <= conversation_resolution_score(0, 0, 0) <= 100
    assert 0 <= conversation_resolution_score(5, 5, 5) <= 100

def test_conversation_resolution_score_responds_to_stronger_signal():
    assert conversation_resolution_score(5, 5, 5) >= conversation_resolution_score(0, 0, 0)
