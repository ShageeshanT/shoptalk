from shoptalk.business_settings import default_settings


def test_default_settings_keep_human_approval_enabled() -> None:
    settings = default_settings()
    assert settings.require_human_approval is True
    assert settings.default_deposit_percent == 50
