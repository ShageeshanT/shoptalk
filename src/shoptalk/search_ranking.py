from __future__ import annotations


def search_rank_score(text: str, query: str) -> int:
    """Small deterministic ranker for seller dashboard search results."""
    normalized_text = text.lower()
    normalized_query = query.strip().lower()
    if not normalized_query:
        return 0
    if normalized_text == normalized_query:
        return 100
    if normalized_text.startswith(normalized_query):
        return 80
    if normalized_query in normalized_text:
        return 60

    terms = [term for term in normalized_query.split() if term]
    matched_terms = sum(1 for term in terms if term in normalized_text)
    if not terms:
        return 0
    return int((matched_terms / len(terms)) * 50)


def sort_by_search_rank(items: list[str], query: str) -> list[str]:
    return sorted(items, key=lambda item: (-search_rank_score(item, query), item.lower()))
