from shoptalk.reply_length_guard import reply_length_guard


def test_reply_length_guard_cleans_spaces():
    assert reply_length_guard("hi   there") == "hi there"


def test_reply_length_guard_truncates():
    assert reply_length_guard("a" * 10, 5) == "aaaa…"
