from shoptalk.idempotency import make_idempotency_key


def test_make_idempotency_key_is_stable_for_same_message() -> None:
    first = make_idempotency_key("whatsapp", "abc", "Hello")
    second = make_idempotency_key("whatsapp", "abc", "Different body")
    assert first == second
