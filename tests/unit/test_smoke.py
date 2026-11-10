"""!
@file test_smoke.py
@brief Smoke tests that prove the package imports and its constants are set.
"""

import sys

import top_movies
from top_movies import constants


def test_python_version_is_supported() -> None:
    """!
    @brief The project requires Python 3.13 or later.
    """
    assert sys.version_info >= (3, 13)


def test_package_has_version() -> None:
    """!
    @brief The package exposes a version string.
    """
    assert top_movies.__version__


def test_constants_are_defined() -> None:
    """!
    @brief The shared constants exist and are not empty.
    """
    assert constants.APP_NAME
    assert constants.DATABASE_FILE.endswith(".db")
