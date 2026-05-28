from shoptalk.whatsapp_formatting import (
    compact_whatsapp_text,
    format_order_update,
    format_payment_instruction,
)


def test_compact_whatsapp_text_removes_extra_spacing() -> None:
    assert compact_whatsapp_text("two   dozen\n cupcakes") == "two dozen cupcakes"


def test_format_order_update_uses_fallback_customer_name() -> None:
    assert format_order_update("", "birthday cake", "confirmed") == (
        "Hi there, quick update: your birthday cake order is now confirmed."
    )


def test_format_payment_instruction_includes_amount_and_method() -> None:
    assert format_payment_instruction(2500, "bank transfer") == (
        "Please pay LKR 2,500 via bank transfer. Send the receipt here once done."
    )
