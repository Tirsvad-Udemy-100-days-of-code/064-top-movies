"""!
@file app.py
@brief Composition root: builds the Flask application and wires the layers together.
"""

import os
from pathlib import Path
from typing import Any

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_bootstrap import Bootstrap5

from top_movies import constants
from top_movies.infrastructure.database import db
from top_movies.infrastructure.seed import seed_movies
from top_movies.presentation.views import main


@click.command("seed")
@with_appcontext
def seed_command() -> None:
    """!
    @brief Insert the example movies; safe to run more than once.
    """
    click.echo(f"Inserted {seed_movies()} movie(s).")


def create_app(config: dict[str, Any] | None = None) -> Flask:
    """!
    @brief Create and configure the application.
    @param config Optional settings that override the defaults, used by the tests.
    @return The configured Flask application.
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get(
        constants.ENV_SECRET_KEY, constants.DEFAULT_SECRET_KEY
    )
    default_uri = f"sqlite:///{constants.DATABASE_FILE}"
    app.config["SQLALCHEMY_DATABASE_URI"] = default_uri
    app.config.update(config or {})
    app.jinja_env.globals["APP_NAME"] = constants.APP_NAME

    if app.config["SQLALCHEMY_DATABASE_URI"] == default_uri:
        # The default database lives in the instance folder, which must exist.
        Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    Bootstrap5(app)
    db.init_app(app)
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()

    app.cli.add_command(seed_command)
    return app
