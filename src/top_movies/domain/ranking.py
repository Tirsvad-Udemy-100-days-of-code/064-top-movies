"""!
@file ranking.py
@brief The rule that ranks movies by rating.
"""

from collections.abc import Sequence
from typing import Protocol


class Rankable(Protocol):
    """!
    @brief Anything with a rating and a ranking that can be ranked.
    """

    rating: float | None
    ranking: int | None


def _rating_sort_key(movie: Rankable) -> tuple[bool, float]:
    """!
    @brief Sort key that puts the best rating first and an unrated movie last.
    @param movie The movie to key.
    @return A tuple that sorts unrated last and higher ratings first.
    """
    if movie.rating is None:
        return (True, 0.0)
    return (False, -movie.rating)


def rank_by_rating[R: Rankable](movies: Sequence[R]) -> list[R]:
    """!
    @brief Order movies best rating first and set their ranking to 1..N in that order.

    An unrated movie comes last. Movies with the same rating keep their input order.
    @param movies The movies to rank; each one has its ranking overwritten.
    @return A new list of the same movies, in rank order.
    """
    ranked = sorted(movies, key=_rating_sort_key)
    for position, movie in enumerate(ranked, start=1):
        movie.ranking = position
    return ranked
