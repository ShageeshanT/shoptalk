from shoptalk.text_utils import normalize_whitespace


def test_normalize_whitespace_collapses_chat_spacing() -> None:
    assert normalize_whitespace("  Hi   can\nI order?  ") == "Hi can I order?"
