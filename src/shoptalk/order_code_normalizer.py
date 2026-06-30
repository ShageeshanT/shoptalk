from __future__ import annotations

def order_code_normalizer(code: str) -> str:
    return code.strip().replace(" ", "-").upper()
