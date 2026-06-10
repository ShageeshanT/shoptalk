from __future__ import annotations

def order_issue_label(issue: str) -> str:
    normalized = (issue or "").strip().lower().replace(" ", "_")
    labels = {
        'missing_item': 'Missing item',
        'wrong_address': 'Wrong address',
        'late_delivery': 'Late delivery',
    }
    return labels.get(normalized, 'General issue')
