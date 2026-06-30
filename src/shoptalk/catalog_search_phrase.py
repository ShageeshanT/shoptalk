def catalog_search_phrase(query):
    return " ".join(str(query).lower().strip().split())
