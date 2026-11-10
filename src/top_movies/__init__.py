"""!
@file __init__.py
@brief Top Movies: a Flask website that ranks your favourite movies.
"""

from typing import Any

## Package version, kept in step with pyproject.toml.
__version__ = "0.1.0"


def create_app(
    config: dict[str, Any] | None = None,
    catalogue: Any = None,  # noqa: ANN401 - a MovieCatalogue; typed loosely to keep Flask lazy
) -> Any:  # noqa: ANN401 - Flask is imported lazily
    """!
    @brief Build the Flask application; this is the entry point of `flask --app top_movies`.
    @param config Optional settings that override the defaults, used by the tests.
    @param catalogue Optional movie catalogue; built from the environment when None.
    @return The configured Flask application.
    """
    from top_movies.presentation.app import create_app as build_app

    return build_app(config, catalogue)
