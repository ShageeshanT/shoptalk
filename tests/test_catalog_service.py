"""Tests for CatalogService product matching."""

from shoptalk.services.catalog_service import CatalogItem, CatalogService


def make_catalog():
    return [
        CatalogItem(id="1", name="chocolate cake", description="Rich chocolate layer cake", price=25.0),
        CatalogItem(id="2", name="vanilla cupcake", description="Classic vanilla cupcake", price=3.5),
        CatalogItem(id="3", name="red velvet cake", description="Red velvet with cream cheese", price=30.0),
    ]


def test_exact_match():
    svc = CatalogService()
    result = svc.match("chocolate cake", make_catalog())
    assert result.item is not None
    assert result.item.id == "1"
    assert result.score == 1.0


def test_partial_match():
    svc = CatalogService()
    result = svc.match("chocolate", make_catalog())
    assert result.item is not None
    assert result.item.id == "1"
    assert 0 < result.score < 1.0


def test_no_match_empty_catalog():
    svc = CatalogService()
    result = svc.match("anything", [])
    assert result.item is None
    assert result.score == 0.0


def test_unavailable_items_excluded():
    catalog = [
        CatalogItem(id="1", name="chocolate cake", description="", price=None, available=False),
        CatalogItem(id="2", name="vanilla cupcake", description="", price=3.5, available=True),
    ]
    svc = CatalogService()
    result = svc.match("chocolate cake", catalog)
    # Should not match the unavailable item
    assert result.item is None or result.item.id != "1"
