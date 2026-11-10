"""!
@file test_home_ranking.py
@brief The home page ranks the movies by rating, best first, and stores the rankings.
"""

import re

from flask import Flask
from flask.testing import FlaskClient

from top_movies.infrastructure.database import Movie, db


def _add(app: Flask, title: str, rating: float | None) -> int:
    """!
    @brief Store a movie with a rating and no ranking.
    @param app The application, for the app context.
    @param title Title of the movie.
    @param rating Rating of the movie, or None.
    @return The id of the movie.
    """
    movie = Movie(title=title, year=2000, description="d", img_url="https://img.test/x.jpg")
    movie.rating = rating
    with app.app_context():
        db.session.add(movie)
        db.session.commit()
        return movie.id


def _cards(client: FlaskClient) -> list[tuple[str, str]]:
    """!
    @brief Read the displayed ranking and title of each card, in page order.
    @param client The test client.
    @return Pairs of ranking text and title.
    """
    body = client.get("/").get_data(as_text=True)
    rankings = re.findall(r'class="large-number">([^<]*)</p>', body)
    titles = re.findall(r'<div class="title">(.*?) <span', body)
    return list(zip(rankings, titles, strict=True))


def _stored(app: Flask) -> dict[str, int | None]:
    """!
    @brief Read the stored ranking of each movie by title.
    @param app The application, for the app context.
    @return Title to ranking.
    """
    with app.app_context():
        movies = db.session.execute(db.select(Movie)).scalars().all()
        return {movie.title: movie.ranking for movie in movies}


def _three_movies(app: Flask) -> int:
    """!
    @brief Store the lecture examples.
    @param app The application, for the app context.
    @return The id of Parasite.
    """
    _add(app, "Matrix", 9.3)
    _add(app, "Spirited Away", 9.5)
    return _add(app, "Parasite", 9.9)


def test_home_ranks_lecture_examples_best_first(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Matrix 9.3, Spirited Away 9.5, Parasite 9.9 rank 3, 2, 1 and Parasite is first.
    """
    _three_movies(app)
    assert _cards(client) == [("1", "Parasite"), ("2", "Spirited Away"), ("3", "Matrix")]


def test_home_reranks_after_rating_is_lowered(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Editing Parasite to 8.9 moves it to the last rank.
    """
    parasite_id = _three_movies(app)
    client.get("/")
    client.post(f"/edit?id={parasite_id}", data={"rating": "8.9", "review": "ok"})
    assert _cards(client) == [("1", "Spirited Away"), ("2", "Matrix"), ("3", "Parasite")]


def test_added_movie_is_placed_by_its_rating(app: Flask, client: FlaskClient) -> None:
    """!
    @brief A movie added through the add flow goes last until rated, then by its rating.
    """
    _add(app, "Matrix", 9.3)
    _add(app, "Spirited Away", 9.5)
    client.get("/select?id=604")
    assert _cards(client)[-1] == ("3", "The Matrix Reloaded")
    with app.app_context():
        added = db.session.execute(db.select(Movie).filter_by(title="The Matrix Reloaded"))
        added_id = added.scalar_one().id
    client.post(f"/edit?id={added_id}", data={"rating": "9.4", "review": "good"})
    assert [title for _, title in _cards(client)] == [
        "Spirited Away",
        "The Matrix Reloaded",
        "Matrix",
    ]


def test_unrated_movies_are_last_with_a_ranking(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Unrated movies follow the rated ones and still show a number.
    """
    _add(app, "Unrated", None)
    _add(app, "Rated", 1.0)
    assert _cards(client) == [("1", "Rated"), ("2", "Unrated")]


def test_home_persists_rankings(app: Flask, client: FlaskClient) -> None:
    """!
    @brief After visiting the home page the rankings are in the database.
    """
    _three_movies(app)
    assert set(_stored(app).values()) == {None}
    client.get("/")
    assert _stored(app) == {"Parasite": 1, "Spirited Away": 2, "Matrix": 3}
