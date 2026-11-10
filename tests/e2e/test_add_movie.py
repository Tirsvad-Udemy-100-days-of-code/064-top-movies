"""!
@file test_add_movie.py
@brief Add a movie: search the catalogue, select a match, land on its edit page.
"""

import html

from flask import Flask
from flask.testing import FlaskClient

from conftest import FakeCatalogue
from top_movies import constants
from top_movies.application.errors import CatalogueError, CatalogueNotConfiguredError
from top_movies.infrastructure.database import Movie, db


def _stored(app: Flask) -> list[tuple[int, str, int, float | None]]:
    """!
    @brief Read id, title, year and rating of every stored movie.
    @param app The application, for the app context.
    @return The rows, in id order.
    """
    with app.app_context():
        movies = db.session.execute(db.select(Movie).order_by(Movie.id)).scalars().all()
        return [(m.id, m.title, m.year, m.rating) for m in movies]


def test_home_add_link_points_to_add_route(client: FlaskClient) -> None:
    """!
    @brief The Add Movie button links to /add.
    """
    assert 'href="/add"' in client.get("/").get_data(as_text=True)


def test_add_page_shows_one_title_field(client: FlaskClient) -> None:
    """!
    @brief GET /add renders a form with a title field and the Add Movie button.
    """
    response = client.get("/add")
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'id="title"' in body
    assert 'id="submit"' in body
    assert constants.ADD_SUBMIT_LABEL in body
    assert body.count("<input") == 2


def test_add_post_lists_titles_and_years(client: FlaskClient, catalogue: FakeCatalogue) -> None:
    """!
    @brief A valid title lists the matches with their years and select links.
    """
    response = client.post("/add", data={"title": "matrix"})
    body = html.unescape(response.get_data(as_text=True))
    assert response.status_code == 200
    assert catalogue.queries == ["matrix"]
    assert "The Matrix</a> - 1999" in body
    assert 'href="/select?id=603"' in body
    assert "The Matrix Reloaded" in body
    assert 'href="/select?id=604"' in body


def test_add_post_with_empty_title_shows_form_again(
    client: FlaskClient, catalogue: FakeCatalogue
) -> None:
    """!
    @brief An empty title does not search.
    """
    response = client.post("/add", data={"title": ""})
    assert 'id="title"' in response.get_data(as_text=True)
    assert catalogue.queries == []


def test_select_stores_movie_and_redirects_to_edit(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Selecting a match stores it without rating and redirects to its edit page.
    """
    response = client.get("/select?id=603")
    stored = _stored(app)
    assert stored == [(stored[0][0], "The Matrix", 1999, None)]
    assert response.status_code == 302
    assert response.headers["Location"] == f"/edit?id={stored[0][0]}"
    with app.app_context():
        movie = db.session.execute(db.select(Movie)).scalar_one()
        assert movie.description == "A hacker learns the truth."
        assert movie.img_url == "https://img.test/603.jpg"
        assert movie.review is None
        assert movie.ranking is None


def test_select_existing_title_does_not_duplicate(app: Flask, client: FlaskClient) -> None:
    """!
    @brief Selecting a stored title again redirects to the same edit page.
    """
    first = client.get("/select?id=603")
    second = client.get("/select?id=603")
    assert len(_stored(app)) == 1
    assert second.headers["Location"] == first.headers["Location"]


def test_select_without_id_returns_400(client: FlaskClient) -> None:
    """!
    @brief A missing id is a bad request.
    """
    assert client.get("/select").status_code == 400


def test_select_non_numeric_id_returns_400(client: FlaskClient) -> None:
    """!
    @brief An id that is not a number is a bad request.
    """
    assert client.get("/select?id=abc").status_code == 400


def test_missing_key_gives_503_with_hint(client: FlaskClient, catalogue: FakeCatalogue) -> None:
    """!
    @brief A catalogue without a key answers 503 and tells how to set the variable.
    """
    catalogue.error = CatalogueNotConfiguredError("no key")
    response = client.post("/add", data={"title": "matrix"})
    assert response.status_code == constants.HTTP_SERVICE_UNAVAILABLE
    assert constants.ENV_TMDB_API_KEY in response.get_data(as_text=True)
    assert client.get("/select?id=603").status_code == constants.HTTP_SERVICE_UNAVAILABLE


def test_catalogue_failure_gives_502_and_stores_nothing(
    app: Flask, client: FlaskClient, catalogue: FakeCatalogue
) -> None:
    """!
    @brief A failing catalogue answers 502 on search and on select, and nothing is stored.
    """
    catalogue.error = CatalogueError("down")
    assert client.post("/add", data={"title": "matrix"}).status_code == constants.HTTP_BAD_GATEWAY
    assert client.get("/select?id=603").status_code == constants.HTTP_BAD_GATEWAY
    assert _stored(app) == []
