from shoptalk.chat_digest import chat_digest


def test_chat_digest_uses_latest_messages():
    assert chat_digest(["one", "two", "three"], 2) == "two | three"


def test_chat_digest_handles_zero_limit():
    assert chat_digest(["one"], 0) == ""
