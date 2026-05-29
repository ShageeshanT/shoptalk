from shoptalk.import_validation import validate_customer_import_row


def test_validate_customer_import_row_accepts_valid_row() -> None:
    row = {"name": "Amani", "channel": "whatsapp", "email": "a@example.com"}

    assert validate_customer_import_row(row) == []


def test_validate_customer_import_row_reports_missing_and_invalid_fields() -> None:
    row = {"name": "", "channel": "", "email": "bad", "extra": "x"}

    assert validate_customer_import_row(row) == [
        "missing_channel",
        "missing_name",
        "unknown_fields:extra",
        "invalid_email",
    ]
