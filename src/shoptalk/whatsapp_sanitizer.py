def sanitize_whatsapp_text(text: str) -> str:
    cleaned = " ".join(text.replace("\u200f", "").replace("\u200e", "").split())
    return cleaned.strip()


def is_voice_note_placeholder(text: str) -> bool:
    return sanitize_whatsapp_text(text).lower() in {"voice note", "audio", "<audio>"}
