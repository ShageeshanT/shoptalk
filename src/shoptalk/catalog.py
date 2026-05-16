from pydantic import BaseModel, Field


class CatalogItem(BaseModel):
    name: str = Field(..., min_length=1)
    price: float | None = Field(default=None, ge=0)
    tags: list[str] = Field(default_factory=list)


class CatalogMatch(BaseModel):
    item: CatalogItem
    score: int


def match_catalog_items(message: str, catalog: list[CatalogItem]) -> list[CatalogMatch]:
    words = {word.strip(".,!?;:").lower() for word in message.split()}
    matches: list[CatalogMatch] = []
    for item in catalog:
        item_terms = {item.name.lower(), *[tag.lower() for tag in item.tags]}
        score = sum(term in message.lower() or term in words for term in item_terms)
        if score > 0:
            matches.append(CatalogMatch(item=item, score=score))
    return sorted(matches, key=lambda match: match.score, reverse=True)
