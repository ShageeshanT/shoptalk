from shoptalk.channels import normalize_channel


def test_normalize_channel_maps_common_aliases() -> None:
    assert normalize_channel("WA") == "whatsapp"
    assert normalize_channel("ig") == "instagram"
