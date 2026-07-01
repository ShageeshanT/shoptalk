from shoptalk.conversation_priority_score import conversation_priority_score

def test_conversation_priority_score_bounds():
    assert 0 <= conversation_priority_score(0, 0, 0) <= 100

def test_conversation_priority_score_increases_for_riskier_input():
    assert conversation_priority_score(20, 60, 5000) > conversation_priority_score(20, 0, 0)
