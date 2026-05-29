from shoptalk.contact_format import display_contact, mask_phone


def test_display_contact_prefers_available_routes() -> None:
    assert display_contact("+94700000000", "a@example.com") == "+94700000000 · a@example.com"
    assert display_contact(phone="+94700000000") == "+94700000000"
    assert display_contact(email="a@example.com") == "a@example.com"
    assert display_contact() == "No contact route"


def test_mask_phone_keeps_last_four_digits() -> None:
    assert mask_phone("+94 70 123 4567") == "••••4567"
    assert mask_phone("123") == "••••"
