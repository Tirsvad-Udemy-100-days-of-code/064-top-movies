"""!
@file ports.py
@brief Interfaces the application needs from the outside world.
"""

from typing import Protocol

from top_movies.application.dto import MovieDetails, MovieSearchResult


class MovieCatalogue(Protocol):
    """!
    @brief A source of movie facts, such as The Movie Database.
    """

    def search_movies(self, title: str) -> list[MovieSearchResult]:
        """!
        @brief Find the movies whose title matches.
        @param title Text to search for.
        @return The matches, best first.
        @throws CatalogueError When the catalogue cannot answer.
        """
        ...

    def get_movie(self, movie_id: int) -> MovieDetails:
        """!
        @brief Read the facts of one movie.
        @param movie_id Identifier of the movie in the catalogue.
        @return The details of the movie.
        @throws CatalogueError When the catalogue cannot answer.
        """
        ...
