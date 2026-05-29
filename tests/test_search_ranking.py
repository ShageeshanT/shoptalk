from shoptalk.search_ranking import search_rank_score, sort_by_search_rank


def test_search_rank_score_prioritizes_exact_prefix_and_contains() -> None:
    assert search_rank_score("Chocolate Cake", "chocolate cake") == 100
    assert search_rank_score("Chocolate Cake Large", "chocolate") == 80
    assert search_rank_score("Large Chocolate Cake", "chocolate") == 60
    assert search_rank_score("Large Vanilla Cake", "chocolate cake") == 25


def test_sort_by_search_rank() -> None:
    items = ["Vanilla cake", "Chocolate cake", "Cake topper"]

    assert sort_by_search_rank(items, "cake") == [
        "Cake topper",
        "Chocolate cake",
        "Vanilla cake",
    ]
