"""!
@file test_edit_page.py
@brief The edit page changes the rating and the review of one movie.
"""

import html

from flask import Flask
from flask.testing import FlaskClient

from top_movies.constants import SEED_MOVIES
from top_movies.infrastructure.database import Movie, db
from top_movies.infrastructure.seed import seed_movies


def _seed(app: Flask) -> int:
    """!
    @brief Store the seed movies.
    @param app The application, for the app context.
    @return The id of the first stored movie.
    """
    with app.app_context():
        seed_movies()
        return db.session.execute(db.select(Movie).order_by(Movie.id)).scalars().first().id  # type: ignore[union-attr]


def _stored(app: Flask, movie_id: int) -> tuple[float | None, str | None]:
    """!
    @brief Read the rating and review of a stored movie.
    @param app The application, for the app context.
    @param movie_id The id of the movie.
    @return The rating and the review.
    """
    with app.app_context():
        movie = db.session.get(Movie, movie_id)
        assert movie is not None
        return movie.rating, movie.review


def test_edit_page_shows_title_and_current_values(app: Flask, client: FlaskClient) -> None:
    """!
    @brief The form is prefilled with the stored rating and review.
    """
    movie_id = _seed(app)
    response = client.get(f"/edit?id={movie_id}")
    body = html.unescape(response.get_data(as_text=True))
    assert response.status_code == 200
    assert SEED_MOVIES[0]["title"] in body
    assert f'value="{SEED_MOVIES[0]["rating"]}"' in body
    assert f'value="{SEED_MOVIES[0]["review"]}"' in body


def test_edit_valid_submit_updates_movie_and_redirects_home(
    app: Flask, client: FlaskClient
) -> None:
    """!
    @brief A valid post stores the values and redirects to the home page.
    """
    movie_id = _seed(app)
    response = client.post(f"/edit?id={movie_id}", data={"rating": "9.1", "review": "Better now"})
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert _stored(app, movie_id) == (9.1, "Better now")


def test_edit_invalid_rating_shows_error_and_stores_nothing(
    app: Flask, client: FlaskClient
) -> None:
    """!
    @brief A rating above 10 gives the form back with an error, and the movie is unchanged.
    """
    movie_id = _seed(app)
    response = client.post(f"/edit?id={movie_id}", data={"rating": "11", "review": "Nope"})
    assert response.status_code == 200
    assert "invalid-feedback" in response.get_data(as_text=True)
    assert _stored(app, movie_id) == (SEED_MOVIES[0]["rating"], SEED_MOVIES[0]["review"])


def test_edit_unknown_id_returns_404(client: FlaskClient) -> None:
    """!
    @brief An id with no movie is not found.
    """
    assert client.get("/edit?id=999").status_code == 404


def test_edit_without_id_returns_400(client: FlaskClient) -> None:
    """!
    @brief A request with no id is a bad request.
    """
    assert client.get("/edit").status_code == 400


def test_home_update_link_points_to_edit_page(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Each Update button links to the edit page of its movie.
    """
    movie_id = _seed(app)
    body = client.get("/").get_data(as_text=True)
    assert f'href="/edit?id={movie_id}"' in body
