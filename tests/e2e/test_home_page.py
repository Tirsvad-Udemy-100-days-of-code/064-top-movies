"""!
@file test_home_page.py
@brief The home page lists the movies stored in the database.
"""

import html

from flask import Flask
from flask.testing import FlaskClient

from top_movies.constants import SEED_MOVIES
from top_movies.infrastructure.seed import seed_movies


def test_home_page_shows_every_seeded_movie(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Title, year, review, description and poster of each movie are on the page.
    """
    with app.app_context():
        seed_movies()
    response = client.get("/")
    body = html.unescape(response.get_data(as_text=True))
    assert response.status_code == 200
    for movie in SEED_MOVIES:
        assert movie["title"] in body
        assert f"({movie['year']})" in body
        assert movie["review"] in body
        assert movie["description"] in body
        assert movie["img_url"] in body


def test_home_page_with_no_movies_returns_ok(client: FlaskClient) -> None:
    """!
    @brief An empty database gives an empty list, not an error.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "movie-card" not in response.get_data(as_text=True)
