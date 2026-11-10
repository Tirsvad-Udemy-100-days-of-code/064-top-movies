"""!
@file test_seed_movies.py
@brief The seed inserts the two example movies once and the CLI command runs it.
"""

from flask import Flask

from top_movies.infrastructure.database import Movie, db
from top_movies.infrastructure.seed import seed_movies


def _titles() -> dict[str, Movie]:
    movies = db.session.execute(db.select(Movie)).scalars().all()
    return {movie.title: movie for movie in movies}


def test_seed_movies_inserts_the_two_lecture_movies(app: Flask) -> None:
    """!
    @brief The stored values match the assignment.
    """
    with app.app_context():
        assert seed_movies() == 2
        stored = _titles()
        phone = stored["Phone Booth"]
        avatar = stored["Avatar The Way of Water"]
        assert (phone.year, phone.rating, phone.ranking) == (2002, 7.3, 10)
        assert (avatar.year, avatar.rating, avatar.ranking) == (2022, 7.3, 9)


def test_seed_movies_twice_leaves_two_rows(app: Flask) -> None:
    """!
    @brief The second call inserts nothing.
    """
    with app.app_context():
        seed_movies()
        assert seed_movies() == 0
        assert len(_titles()) == 2


def test_seed_cli_command_inserts_movies_and_is_repeatable(app: Flask) -> None:
    """!
    @brief `flask seed` reports the inserted count, then zero.
    """
    runner = app.test_cli_runner()
    first = runner.invoke(args=["seed"])
    second = runner.invoke(args=["seed"])
    assert first.exit_code == 0
    assert "Inserted 2 movie(s)." in first.output
    assert "Inserted 0 movie(s)." in second.output
