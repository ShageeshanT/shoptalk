from shoptalk.draft_safety import draft_safety_warnings, is_draft_safe


def test_draft_safety_warnings_flag_risky_content() -> None:
    warnings = draft_safety_warnings(
        "This is guaranteed, send your OTP here!!!! http://example.com"
    )

    assert warnings == [
        "risky_claim_or_sensitive_request",
        "insecure_link",
        "too_many_exclamations",
    ]


def test_draft_safety_warnings_flag_long_reply() -> None:
    assert draft_safety_warnings("x" * 601) == ["long_reply"]


def test_is_draft_safe() -> None:
    assert is_draft_safe("Thanks, your order is confirmed.")
    assert not is_draft_safe("Send your bank password")
