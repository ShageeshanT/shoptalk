from __future__ import annotations

RISKY_TERMS = {
    "guaranteed",
    "free forever",
    "no refund",
    "bank password",
    "otp",
    "one-time password",
}


def draft_safety_warnings(text: str) -> list[str]:
    """Flag risky phrases before a seller approves an outbound reply."""
    normalized = text.lower()
    warnings: list[str] = []

    if len(text) > 600:
        warnings.append("long_reply")
    if any(term in normalized for term in RISKY_TERMS):
        warnings.append("risky_claim_or_sensitive_request")
    if "http://" in normalized:
        warnings.append("insecure_link")
    if text.count("!") >= 4:
        warnings.append("too_many_exclamations")

    return warnings


def is_draft_safe(text: str) -> bool:
    return not draft_safety_warnings(text)
