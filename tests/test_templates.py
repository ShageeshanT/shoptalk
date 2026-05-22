from shoptalk.templates import catalog_reply, delivery_confirmation, payment_reminder


def test_catalog_reply_mentions_product_hint() -> None:
    assert "cupcakes" in catalog_reply("cupcakes")


def test_payment_reminder_formats_amount() -> None:
    assert "LKR 2,500" in payment_reminder(2500)


def test_delivery_confirmation_uses_window() -> None:
    assert "evening" in delivery_confirmation("evening")
