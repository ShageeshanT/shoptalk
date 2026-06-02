from shoptalk.whatsapp_sanitizer import is_voice_note_placeholder, sanitize_whatsapp_text


def test_sanitize_whatsapp_text_removes_direction_marks_and_extra_space():
    assert sanitize_whatsapp_text(" hi\u200f   there ") == "hi there"


def test_voice_note_placeholder_detection():
    assert is_voice_note_placeholder(" <audio> ") is True
