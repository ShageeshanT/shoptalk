from shoptalk.money import parse_lkr_amount


def test_parse_lkr_amount_handles_rupee_prefixes() -> None:
    assert parse_lkr_amount("deposit Rs. 2,500 please") == 2500


def test_parse_lkr_amount_returns_none_without_number() -> None:
    assert parse_lkr_amount("payment pending") is None
