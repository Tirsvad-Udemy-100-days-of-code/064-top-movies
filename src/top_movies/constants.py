"""!
@file constants.py
@brief Constants shared by the Top Movies application.
"""

## Name of the application, shown in page titles.
APP_NAME = "Top Movies"

## File name of the SQLite database inside the Flask instance folder.
DATABASE_FILE = "movies.db"

## Name of the environment variable that holds the Flask secret key.
ENV_SECRET_KEY = "SECRET_KEY"  # noqa: S105 - name of a variable, not a secret

## Secret key used when the environment does not set one (development only).
DEFAULT_SECRET_KEY = "development-only-change-me"  # noqa: S105 - documented dev default

## Name of the environment variable that holds the TMDB API key.
ENV_TMDB_API_KEY = "TMDB_API_KEY"
