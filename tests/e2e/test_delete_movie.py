"""!
@file test_delete_movie.py
@brief The delete link removes one movie from the database.
"""

from flask import Flask
from flask.testing import FlaskClient

from top_movies.constants import SEED_MOVIES
from top_movies.infrastructure.database import Movie, db
from top_movies.infrastructure.seed import seed_movies


def _seed(app: Flask) -> list[int]:
    """!
    @brief Store the seed movies.
    @param app The application, for the app context.
    @return The ids of the stored movies, in order.
    """
    with app.app_context():
        seed_movies()
        movies = db.session.execute(db.select(Movie).order_by(Movie.id)).scalars().all()
        return [movie.id for movie in movies]


def _stored_ids(app: Flask) -> list[int]:
    """!
    @brief Read the ids of every stored movie.
    @param app The application, for the app context.
    @return The ids, in order.
    """
    with app.app_context():
        return list(db.session.execute(db.select(Movie.id).order_by(Movie.id)).scalars().all())


def test_delete_removes_only_that_movie_and_redirects_home(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Deleting one movie keeps the others and redirects to the home page.
    """
    ids = _seed(app)
    assert len(ids) >= 2
    response = client.get(f"/delete?id={ids[0]}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert _stored_ids(app) == ids[1:]


def test_delete_unknown_id_returns_404_and_removes_nothing(app: Flask, client: FlaskClient) -> None:
    """!
    @brief An id with no movie is not found and the movies stay.
    """
    ids = _seed(app)
    assert client.get("/delete?id=999").status_code == 404
    assert _stored_ids(app) == ids


def test_delete_without_id_returns_400_and_removes_nothing(app: Flask, client: FlaskClient) -> None:
    """!
    @brief A request with no id is a bad request and the movies stay.
    """
    ids = _seed(app)
    assert client.get("/delete").status_code == 400
    assert _stored_ids(app) == ids


def test_delete_non_numeric_id_returns_400(client: FlaskClient) -> None:
    """!
    @brief An id that is not a number is a bad request.
    """
    assert client.get("/delete?id=abc").status_code == 400


def test_home_delete_link_points_to_delete_route(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Each Delete button links to the delete route of its movie.
    """
    ids = _seed(app)
    body = client.get("/").get_data(as_text=True)
    for movie_id in ids:
        assert f'href="/delete?id={movie_id}"' in body


def test_home_no_longer_shows_deleted_title(app: Flask, client: FlaskClient) -> None:
    """!
    @brief After a delete the home page omits the title but keeps the other movies.
    """
    ids = _seed(app)
    client.get(f"/delete?id={ids[0]}")
    body = client.get("/").get_data(as_text=True)
    assert SEED_MOVIES[0]["title"] not in body
    assert SEED_MOVIES[1]["title"] in body
