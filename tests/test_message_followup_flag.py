from shoptalk.message_followup_flag import message_followup_flag


def test_message_followup_flag():
    assert message_followup_flag("please remind me later") == True
