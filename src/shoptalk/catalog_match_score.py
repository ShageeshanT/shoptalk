from __future__ import annotations

def catalog_match_score(query: str, product: str) -> int:
    query_words = set(query.lower().split())
    product_words = set(product.lower().split())
    return len(query_words & product_words)
