from shoptalk.deposits import deposit_due


def test_deposit_due_uses_default_half_payment() -> None:
    assert deposit_due(4500) == 2250


def test_deposit_due_clamps_percent() -> None:
    assert deposit_due(1000, 150) == 1000
