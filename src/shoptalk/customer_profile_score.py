from __future__ import annotations


def customer_profile_score(has_name, has_phone, has_address, has_notes) -> int:
    score = 0
    for present in (has_name, has_phone, has_address, has_notes):
        if present:
            score += 25
    return min(score, 100)
