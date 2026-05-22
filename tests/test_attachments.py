from shoptalk.attachments import MessageAttachment, has_voice_note


def test_has_voice_note_detects_audio_attachment() -> None:
    attachments = [MessageAttachment(kind="audio", url="https://example.com/a.ogg")]
    assert has_voice_note(attachments) is True
