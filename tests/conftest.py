"""!
@file conftest.py
@brief Shared fixtures: an application on an in-memory database and its test client.
"""

from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from top_movies import create_app
from top_movies.infrastructure.database import db


@pytest.fixture
def app() -> Iterator[Flask]:
    """!
    @brief Application bound to a fresh in-memory SQLite database.
    @return The application, with its tables created.
    """
    application = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite://", "WTF_CSRF_ENABLED": False}
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
