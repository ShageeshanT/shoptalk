from shoptalk.phone import normalize_lk_phone


def test_normalize_lk_phone_converts_local_mobile() -> None:
    assert normalize_lk_phone("077 123 4567") == "94771234567"


def test_normalize_lk_phone_keeps_international_digits() -> None:
    assert normalize_lk_phone("+94 77 123 4567") == "94771234567"
