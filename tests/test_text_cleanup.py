from shoptalk.text_cleanup import clean_customer_text, preview_customer_text


def test_clean_customer_text_collapses_spacing_and_punctuation() -> None:
    assert clean_customer_text("  Hi\n\ncan   I order????  ") == "Hi can I order??"


def test_preview_customer_text_truncates_clean_text() -> None:
    assert preview_customer_text("hello   world from shoptalk", limit=12) == "hello world…"
