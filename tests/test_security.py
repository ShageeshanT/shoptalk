from shoptalk.security import contains_sensitive_marker


def test_contains_sensitive_marker_flags_otp_messages() -> None:
    assert contains_sensitive_marker("my OTP is 123456") is True
    assert contains_sensitive_marker("cake order please") is False
