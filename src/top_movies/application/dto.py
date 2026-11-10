"""!
@file dto.py
@brief Plain data that crosses the boundary of the application layer.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MovieSearchResult:
    """!
    @brief One match of a title search.
    """

    ## Identifier of the movie in the catalogue.
    id: int
    ## Title of the movie.
    title: str
    ## Release year, or None when the catalogue has no release date.
    year: int | None


@dataclass(frozen=True, slots=True)
class MovieDetails:
    """!
    @brief The facts about one movie that the website stores.
    """

    ## Title of the movie.
    title: str
    ## Release year.
    year: int
    ## Short description of the plot.
    description: str
    ## Address of the poster image.
    img_url: str
