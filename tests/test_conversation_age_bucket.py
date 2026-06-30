from shoptalk.conversation_age_bucket import conversation_age_bucket


def test_conversation_age_bucket():
    assert conversation_age_bucket(12) == "same_day"
