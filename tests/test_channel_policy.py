from shoptalk.channel_policy import (
    can_send_automated_reply,
    channel_policy_label,
    normalize_channel,
)


def test_normalize_channel_defaults_to_manual() -> None:
    assert normalize_channel(None) == "manual"
    assert normalize_channel(" Whats App ") == "whats_app"


def test_channel_policy_labels_supported_modes() -> None:
    assert channel_policy_label("whatsapp") == "automated_with_approval"
    assert channel_policy_label("manual") == "manual_approval_only"
    assert channel_policy_label("fax") == "unsupported_channel"


def test_can_send_automated_reply() -> None:
    assert can_send_automated_reply("telegram")
    assert not can_send_automated_reply("manual")
