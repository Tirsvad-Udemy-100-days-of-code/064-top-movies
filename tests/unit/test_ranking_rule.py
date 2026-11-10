"""!
@file test_ranking_rule.py
@brief The rule that ranks movies by rating, tested without Flask or a database.
"""

from dataclasses import dataclass

from top_movies.domain.ranking import rank_by_rating


@dataclass
class FakeMovie:
    """!
    @brief Plain object that satisfies the Rankable protocol.
    """

    name: str
    rating: float | None
    ranking: int | None = None


def _names(movies: list[FakeMovie]) -> list[str]:
    """!
    @brief Get the names of the movies in order.
    @param movies The movies.
    @return Their names.
    """
    return [movie.name for movie in movies]


def test_rank_orders_best_rating_first_and_numbers_from_one() -> None:
    """!
    @brief Ratings 9.3, 9.5, 9.9 give the order 9.9, 9.5, 9.3 and rankings 1, 2, 3.
    """
    matrix, spirited, parasite = FakeMovie("a", 9.3), FakeMovie("b", 9.5), FakeMovie("c", 9.9)
    ranked = rank_by_rating([matrix, spirited, parasite])
    assert _names(ranked) == ["c", "b", "a"]
    assert [m.ranking for m in ranked] == [1, 2, 3]
    assert (matrix.ranking, spirited.ranking, parasite.ranking) == (3, 2, 1)


def test_rank_puts_unrated_movies_last() -> None:
    """!
    @brief A movie with no rating gets the last rankings.
    """
    ranked = rank_by_rating(
        [FakeMovie("none", None), FakeMovie("low", 1.0), FakeMovie("zero", 0.0)]
    )
    assert _names(ranked) == ["low", "zero", "none"]
    assert ranked[-1].ranking == 3


def test_rank_keeps_input_order_for_equal_ratings() -> None:
    """!
    @brief Ties, rated or unrated, keep the order of the input.
    """
    movies = [
        FakeMovie("n1", None),
        FakeMovie("t1", 7.0),
        FakeMovie("n2", None),
        FakeMovie("t2", 7.0),
        FakeMovie("t3", 7.0),
    ]
    assert _names(rank_by_rating(movies)) == ["t1", "t2", "t3", "n1", "n2"]


def test_rank_empty_list_returns_empty_list() -> None:
    """!
    @brief No movies give no movies.
    """
    assert rank_by_rating([]) == []


def test_rank_single_movie_gets_ranking_one() -> None:
    """!
    @brief One movie, rated or not, is number 1.
    """
    rated, unrated = FakeMovie("a", 5.0), FakeMovie("b", None)
    rank_by_rating([rated])
    rank_by_rating([unrated])
    assert (rated.ranking, unrated.ranking) == (1, 1)


def test_rank_overwrites_existing_rankings() -> None:
    """!
    @brief A wrong stored ranking is replaced by the calculated one.
    """
    movies = [FakeMovie("a", 2.0, ranking=10), FakeMovie("b", 8.0, ranking=9)]
    rank_by_rating(movies)
    assert [m.ranking for m in movies] == [2, 1]


def test_rank_does_not_change_the_input_list_order() -> None:
    """!
    @brief The input sequence keeps its order; the result is a new list.
    """
    movies = [FakeMovie("a", 1.0), FakeMovie("b", 2.0)]
    rank_by_rating(movies)
    assert _names(movies) == ["a", "b"]
