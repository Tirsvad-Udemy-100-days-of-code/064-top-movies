"""!
@file serve_demo.py
@brief Serve the application on a temporary, seeded database for the screenshot tool.

Runs inside the Docker container of this folder (see entrypoint.sh), bound to the
loopback address only and never in debug mode. Movies come from a canned catalogue
(fake_catalogue.py), so the demo needs no TMDB key and no network for searches.
"""

import logging
import tempfile
from pathlib import Path

from fake_catalogue import FakeCatalogue

from top_movies import create_app
from top_movies.infrastructure.seed import seed_movies

## Address the demo listens on; loopback only.
HOST = "127.0.0.1"

## Port the demo listens on.
PORT = 5000

## Logger of this tool.
LOG = logging.getLogger("serve_demo")


def main() -> None:
    """!
    @brief Seed a temporary SQLite file with the example movies and serve it.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    with tempfile.TemporaryDirectory() as folder:
        database = Path(folder) / "demo.db"
        app = create_app(
            {"SQLALCHEMY_DATABASE_URI": f"sqlite:///{database.as_posix()}"}, FakeCatalogue()
        )
        with app.app_context():
            LOG.info("seeded %d movie(s)", seed_movies())
        app.run(host=HOST, port=PORT, debug=False)


if __name__ == "__main__":
    main()
