import hashlib


def make_idempotency_key(channel: str, external_message_id: str | None, text: str) -> str:
    base = f"{channel}:{external_message_id or text.strip().lower()}"
    return hashlib.sha256(base.encode('utf-8')).hexdigest()
