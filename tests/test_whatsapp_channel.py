"""Tests for the WhatsApp channel adapter."""

from shoptalk.channels.whatsapp import WhatsAppChannel


SAMPLE_PAYLOAD = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [{
                    "from": "94771234567",
                    "type": "text",
                    "timestamp": "1700000000",
                    "text": {"body": "I want to order a cake"}
                }]
            }
        }]
    }]
}


def test_parse_text_message():
    channel = WhatsAppChannel(verify_token="test-token")
    messages = channel.parse_webhook(SAMPLE_PAYLOAD)
    assert len(messages) == 1
    assert messages[0].text == "I want to order a cake"
    assert messages[0].sender_phone == "94771234567"
    assert messages[0].channel == "whatsapp"


def test_parse_empty_payload():
    channel = WhatsAppChannel(verify_token="test-token")
    messages = channel.parse_webhook({})
    assert messages == []


def test_verify_webhook_success():
    channel = WhatsAppChannel(verify_token="my-secret")
    result = channel.verify_webhook("subscribe", "my-secret", "abc123")
    assert result == "abc123"


def test_verify_webhook_wrong_token():
    channel = WhatsAppChannel(verify_token="my-secret")
    result = channel.verify_webhook("subscribe", "wrong-token", "abc123")
    assert result is None


def test_non_text_messages_ignored():
    payload = {
        "entry": [{"changes": [{"value": {"messages": [
            {"from": "123", "type": "image", "timestamp": "1700000000"}
        ]}}]}]
    }
    channel = WhatsAppChannel(verify_token="tok")
    assert channel.parse_webhook(payload) == []
