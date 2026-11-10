"""!
@file tmdb_client.py
@brief The movie catalogue port implemented with The Movie Database (TMDB) API, version 3.
"""

from typing import Any

import requests

from top_movies import constants
from top_movies.application.dto import MovieDetails, MovieSearchResult
from top_movies.application.errors import CatalogueError, CatalogueNotConfiguredError


def _year_of(release_date: object) -> int | None:
    """!
    @brief Read the year from a TMDB release date such as 1999-03-31.
    @param release_date The release_date value of a TMDB payload.
    @return The year, or None when the date is missing or malformed.
    """
    if not isinstance(release_date, str) or not release_date[:4].isdigit():
        return None
    return int(release_date[:4])


class TmdbClient:
    """!
    @brief Movie catalogue that asks the TMDB web API.
    """

    def __init__(self, api_key: str, session: requests.Session | None = None) -> None:
        """!
        @brief Create the client.
        @param api_key TMDB API key (v3 auth).
        @param session HTTP session to use; a new one is made when None.
        """
        self._api_key = api_key
        self._session = session if session is not None else requests.Session()

    def search_movies(self, title: str) -> list[MovieSearchResult]:
        """!
        @brief Find the movies whose title matches.
        @param title Text to search for.
        @return The matches, in the order TMDB gives them.
        @throws CatalogueError When TMDB cannot be reached or answers badly.
        """
        payload = self._get("/search/movie", {"query": title})
        try:
            return [
                MovieSearchResult(
                    id=int(item["id"]),
                    title=str(item["title"]),
                    year=_year_of(item.get("release_date")),
                )
                for item in payload["results"]
            ]
        except (KeyError, TypeError, ValueError, AttributeError) as error:
            raise CatalogueError("TMDB sent an unexpected search answer.") from error

    def get_movie(self, movie_id: int) -> MovieDetails:
        """!
        @brief Read the facts of one movie.
        @param movie_id TMDB identifier of the movie.
        @return The details; the year is 0 and the poster a placeholder when TMDB has none.
        @throws CatalogueError When TMDB cannot be reached or answers badly.
        """
        payload = self._get(f"/movie/{movie_id}", {})
        try:
            year = _year_of(payload.get("release_date"))
            poster_path = payload.get("poster_path")
            return MovieDetails(
                title=str(payload["title"]),
                year=constants.TMDB_UNKNOWN_YEAR if year is None else year,
                description=str(payload.get("overview") or ""),
                img_url=(
                    f"{constants.TMDB_IMAGE_BASE_URL}{poster_path}"
                    if poster_path
                    else constants.TMDB_PLACEHOLDER_IMAGE_URL
                ),
            )
        except (KeyError, TypeError, AttributeError) as error:
            raise CatalogueError("TMDB sent an unexpected movie answer.") from error

    def _get(self, path: str, params: dict[str, str]) -> dict[str, Any]:
        """!
        @brief Send one GET request and decode the JSON answer.
        @param path Path under the API base URL.
        @param params Query parameters; the API key is added.
        @return The decoded JSON object.
        @throws CatalogueError On a network error, an HTTP error or a body that is not an object.
        """
        try:
            response = self._session.get(
                constants.TMDB_API_BASE + path,
                params={"api_key": self._api_key, **params},
                timeout=constants.TMDB_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            payload = response.json()
        except (requests.RequestException, ValueError) as error:
            # The message names the failure kind only: the request URL holds the API key.
            raise CatalogueError(f"TMDB request failed: {type(error).__name__}.") from error
        if not isinstance(payload, dict):
            raise CatalogueError("TMDB sent an unexpected answer.")
        return payload


class MissingKeyCatalogue:
    """!
    @brief Movie catalogue used when no API key is set; every call says so.
    """

    def search_movies(self, title: str) -> list[MovieSearchResult]:
        """!
        @brief Always fail, because there is no API key.
        @param title Ignored.
        @return Never returns.
        @throws CatalogueNotConfiguredError Always.
        """
        raise CatalogueNotConfiguredError(constants.MSG_CATALOGUE_NOT_CONFIGURED)

    def get_movie(self, movie_id: int) -> MovieDetails:
        """!
        @brief Always fail, because there is no API key.
        @param movie_id Ignored.
        @return Never returns.
        @throws CatalogueNotConfiguredError Always.
        """
        raise CatalogueNotConfiguredError(constants.MSG_CATALOGUE_NOT_CONFIGURED)
