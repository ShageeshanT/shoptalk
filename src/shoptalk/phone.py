import re


def normalize_lk_phone(value: str) -> str:
    """Normalize Sri Lankan phone numbers into a WhatsApp friendly international form."""
    digits = re.sub(r"\D+", "", value)
    if digits.startswith('0') and len(digits) == 10:
        return '94' + digits[1:]
    if digits.startswith('94'):
        return digits
    if len(digits) == 9:
        return '94' + digits
    return digits
