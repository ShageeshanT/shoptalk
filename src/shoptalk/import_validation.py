from __future__ import annotations

REQUIRED_CUSTOMER_FIELDS = ("channel", "name")
OPTIONAL_CUSTOMER_FIELDS = {"phone", "email", "notes"}


def validate_customer_import_row(row: dict[str, str | None]) -> list[str]:
    """Return field-level validation errors for simple customer CSV imports."""
    errors: list[str] = []
    for field in REQUIRED_CUSTOMER_FIELDS:
        if not (row.get(field) or "").strip():
            errors.append(f"missing_{field}")

    unknown_fields = sorted(set(row) - set(REQUIRED_CUSTOMER_FIELDS) - OPTIONAL_CUSTOMER_FIELDS)
    if unknown_fields:
        errors.append("unknown_fields:" + ",".join(unknown_fields))

    email = (row.get("email") or "").strip()
    if email and "@" not in email:
        errors.append("invalid_email")

    return errors
