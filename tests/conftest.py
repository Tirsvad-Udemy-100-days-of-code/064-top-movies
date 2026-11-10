"""!
@file conftest.py
@brief Shared fixtures: a fake movie catalogue, an in-memory application and its client.
"""

from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from top_movies import create_app
from top_movies.application.dto import MovieDetails, MovieSearchResult
from top_movies.application.errors import CatalogueError
from top_movies.infrastructure.database import db

## Details the fake catalogue knows, by catalogue id.
FAKE_DETAILS = {
    603: MovieDetails("The Matrix", 1999, "A hacker learns the truth.", "https://img.test/603.jpg"),
    604: MovieDetails("The Matrix Reloaded", 2003, "The war goes on.", "https://img.test/604.jpg"),
}


class FakeCatalogue:
    """!
    @brief In-memory movie catalogue; set `error` to make every call fail.
    """

    def __init__(self) -> None:
        """!
        @brief Create a catalogue that knows two Matrix movies and does not fail.
        """
        self.error: CatalogueError | None = None
        self.queries: list[str] = []

    def search_movies(self, title: str) -> list[MovieSearchResult]:
        """!
        @brief Return both known movies for any title, one of them without a year.
        @param title Text searched for; recorded in `queries`.
        @return The matches.
        """
        self.queries.append(title)
        if self.error is not None:
            raise self.error
        return [
            MovieSearchResult(603, "The Matrix", 1999),
            MovieSearchResult(604, "The Matrix Reloaded", None),
        ]

    def get_movie(self, movie_id: int) -> MovieDetails:
        """!
        @brief Return the known details of a movie.
        @param movie_id Catalogue id of the movie.
        @return The details.
        """
        if self.error is not None:
            raise self.error
        try:
            return FAKE_DETAILS[movie_id]
        except KeyError as error:
            raise CatalogueError("unknown movie") from error


@pytest.fixture
def catalogue() -> FakeCatalogue:
    """!
    @brief Fake movie catalogue injected into the application.
    @return A catalogue that does not fail.
    """
    return FakeCatalogue()


@pytest.fixture
def app(catalogue: FakeCatalogue) -> Iterator[Flask]:
    """!
    @brief Application bound to a fresh in-memory SQLite database and the fake catalogue.
    @param catalogue The fake catalogue fixture.
    @return The application, with its tables created.
    """
    application = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite://", "WTF_CSRF_ENABLED": False},
        catalogue,
    )
    yield application
    with application.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """!
    @brief Test client of the application.
    @param app The application fixture.
    @return A client that sends requests without a server.
    """
    return app.test_client()
