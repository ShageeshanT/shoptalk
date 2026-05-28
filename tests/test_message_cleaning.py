from shoptalk.message_cleaning import clean_message_text, is_empty_message


def test_clean_message_text_normalizes_whitespace():
    assert clean_message_text("Hi\n\n I need   cake") == "Hi I need cake"


def test_is_empty_message():
    assert is_empty_message("   \n ")
    assert not is_empty_message("hi")
