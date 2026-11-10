"""!
@file fake_catalogue.py
@brief A small canned movie catalogue so the screenshot demo needs no TMDB key or network.
"""

from top_movies.application.dto import MovieDetails, MovieSearchResult

## Poster images are loaded by the browser from TMDB, so the demo shows real posters.
_POSTER_BASE = "https://image.tmdb.org/t/p/w500"

## The movies of the demo, by catalogue id.
MOVIES = {
    603: MovieDetails(
        "The Matrix",
        1999,
        "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a "
        "group of underground insurgents fighting the vast and powerful computers who now rule "
        "the earth.",
        f"{_POSTER_BASE}/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    ),
    604: MovieDetails(
        "The Matrix Reloaded",
        2003,
        "Six months after the events depicted in The Matrix, Neo has proved to be a good "
        "omen for the free humans, as more and more humans are being freed from the matrix.",
        f"{_POSTER_BASE}/9TGHDvWrqKBzwDxDodHYXEmOE6J.jpg",
    ),
    605: MovieDetails(
        "The Matrix Revolutions",
        2003,
        "The human city of Zion defends itself against the massive invasion of the machines "
        "as Neo fights to end the war at another front while also opposing the rogue Agent Smith.",
        f"{_POSTER_BASE}/sKogjhfs5q3azmpW7DFKKAeLEG8.jpg",
    ),
}


class FakeCatalogue:
    """!
    @brief Movie catalogue that answers from the canned MOVIES.
    """

    def search_movies(self, title: str) -> list[MovieSearchResult]:
        """!
        @brief Find the canned movies whose title contains the text, ignoring case.
        @param title Text to search for.
        @return The matches, in id order.
        """
        needle = title.casefold()
        return [
            MovieSearchResult(movie_id, movie.title, movie.year)
            for movie_id, movie in MOVIES.items()
            if needle in movie.title.casefold()
        ]

    def get_movie(self, movie_id: int) -> MovieDetails:
        """!
        @brief Read one canned movie.
        @param movie_id Catalogue id of the movie.
        @return The details.
        @throws KeyError When the id is not canned.
        """
        return MOVIES[movie_id]
