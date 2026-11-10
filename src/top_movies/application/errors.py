"""!
@file errors.py
@brief Errors raised by a movie catalogue.
"""


class CatalogueError(Exception):
    """!
    @brief The movie catalogue could not answer.
    """


class CatalogueNotConfiguredError(CatalogueError):
    """!
    @brief The movie catalogue has no credentials, so it cannot be used.
    """
