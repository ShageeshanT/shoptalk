from shoptalk.conversation_health_label import conversation_health_label

def test_conversation_health_label_thresholds():
    assert conversation_health_label(80) == 'Healthy conversation'
    assert conversation_health_label(50) == 'Needs follow-up'
    assert conversation_health_label(20) == 'At risk'

def test_conversation_health_label_invalid_value():
    assert conversation_health_label("bad") == 'Cold conversation'
