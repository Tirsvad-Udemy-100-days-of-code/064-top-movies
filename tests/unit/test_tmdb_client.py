"""!
@file test_tmdb_client.py
@brief TmdbClient parses TMDB answers and maps failures to CatalogueError, with a fake session.
"""

from typing import Any

import pytest
import requests

from top_movies import constants
from top_movies.application.errors import CatalogueError, CatalogueNotConfiguredError
from top_movies.infrastructure.tmdb_client import MissingKeyCatalogue, TmdbClient


class FakeResponse:
    """!
    @brief Minimal stand-in for requests.Response.
    """

    def __init__(self, payload: Any = None, status: int = 200, bad_json: bool = False) -> None:
        """!
        @brief Create the response.
        @param payload Value that json() returns.
        @param status HTTP status code.
        @param bad_json When True, json() raises as for a body that is not JSON.
        """
        self.payload = payload
        self.status = status
        self.bad_json = bad_json

    def raise_for_status(self) -> None:
        """!
        @brief Raise HTTPError for a 4xx or 5xx status.
        """
        if self.status >= 400:
            raise requests.HTTPError(f"status {self.status}")

    def json(self) -> Any:
        """!
        @brief Return the payload, or fail when the body is not JSON.
        @return The payload.
        """
        if self.bad_json:
            raise requests.JSONDecodeError("not json", "", 0)
        return self.payload


class FakeSession:
    """!
    @brief Records every get call and answers with a prepared response or error.
    """

    def __init__(
        self, response: FakeResponse | None = None, error: Exception | None = None
    ) -> None:
        """!
        @brief Create the session.
        @param response Response to return.
        @param error Exception to raise instead.
        """
        self.response = response
        self.error = error
        self.calls: list[dict[str, Any]] = []

    def get(self, url: str, **kwargs: Any) -> FakeResponse:
        """!
        @brief Record the call and answer.
        @param url Requested URL.
        @param kwargs Keyword arguments of the call (params, timeout).
        @return The prepared response.
        """
        self.calls.append({"url": url, **kwargs})
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _client(session: FakeSession) -> TmdbClient:
    """!
    @brief Build a client on a fake session.
    @param session The fake session.
    @return The client.
    """
    return TmdbClient("secret-key", session)  # type: ignore[arg-type]


def test_search_movies_parses_results_and_sends_key_and_query() -> None:
    """!
    @brief Ids, titles and years are read, and the request carries the key, query and timeout.
    """
    payload = {"results": [{"id": 603, "title": "The Matrix", "release_date": "1999-03-31"}]}
    session = FakeSession(FakeResponse(payload))
    results = _client(session).search_movies("matrix")
    assert [(r.id, r.title, r.year) for r in results] == [(603, "The Matrix", 1999)]
    call = session.calls[0]
    assert call["url"] == f"{constants.TMDB_API_BASE}/search/movie"
    assert call["params"] == {"api_key": "secret-key", "query": "matrix"}
    assert call["timeout"] == constants.TMDB_TIMEOUT_SECONDS


@pytest.mark.parametrize("release_date", [None, "", "unknown"])
def test_search_movies_gives_no_year_without_release_date(release_date: str | None) -> None:
    """!
    @brief A missing, empty or malformed release date gives year None.
    """
    item: dict[str, Any] = {"id": 1, "title": "X"}
    if release_date is not None:
        item["release_date"] = release_date
    results = _client(FakeSession(FakeResponse({"results": [item]}))).search_movies("x")
    assert results[0].year is None


def test_search_movies_returns_empty_list_for_no_results() -> None:
    """!
    @brief No match is an empty list, not an error.
    """
    assert _client(FakeSession(FakeResponse({"results": []}))).search_movies("zzz") == []


def test_get_movie_parses_details_and_builds_poster_url() -> None:
    """!
    @brief Title, year, overview and poster URL are read, with the timeout on the call.
    """
    payload = {
        "title": "The Matrix",
        "release_date": "1999-03-31",
        "overview": "A hacker learns the truth.",
        "poster_path": "/abc.jpg",
    }
    session = FakeSession(FakeResponse(payload))
    details = _client(session).get_movie(603)
    assert details.title == "The Matrix"
    assert details.year == 1999
    assert details.description == "A hacker learns the truth."
    assert details.img_url == f"{constants.TMDB_IMAGE_BASE_URL}/abc.jpg"
    call = session.calls[0]
    assert call["url"] == f"{constants.TMDB_API_BASE}/movie/603"
    assert call["params"] == {"api_key": "secret-key"}
    assert call["timeout"] == constants.TMDB_TIMEOUT_SECONDS


def test_get_movie_uses_placeholders_for_missing_poster_and_date() -> None:
    """!
    @brief Missing poster, release date and overview fall back to documented defaults.
    """
    payload = {"title": "Obscure", "poster_path": None, "overview": None}
    details = _client(FakeSession(FakeResponse(payload))).get_movie(1)
    assert details.img_url == constants.TMDB_PLACEHOLDER_IMAGE_URL
    assert details.year == constants.TMDB_UNKNOWN_YEAR
    assert details.description == ""


def test_get_movie_without_title_raises_catalogue_error() -> None:
    """!
    @brief A payload that lacks the title is a bad answer.
    """
    with pytest.raises(CatalogueError):
        _client(FakeSession(FakeResponse({"overview": "x"}))).get_movie(1)


def test_search_movies_with_malformed_results_raises_catalogue_error() -> None:
    """!
    @brief A results entry without an id is a bad answer.
    """
    with pytest.raises(CatalogueError):
        _client(FakeSession(FakeResponse({"results": [{"title": "X"}]}))).search_movies("x")


def test_http_error_raises_catalogue_error_without_leaking_key() -> None:
    """!
    @brief An HTTP error status becomes CatalogueError, and the message hides the key.
    """
    session = FakeSession(FakeResponse({}, status=401))
    with pytest.raises(CatalogueError) as caught:
        _client(session).search_movies("x")
    assert "secret-key" not in str(caught.value)
    assert isinstance(caught.value.__cause__, requests.HTTPError)


def test_invalid_json_raises_catalogue_error() -> None:
    """!
    @brief A body that is not JSON becomes CatalogueError.
    """
    with pytest.raises(CatalogueError):
        _client(FakeSession(FakeResponse(bad_json=True))).get_movie(1)


def test_non_object_json_raises_catalogue_error() -> None:
    """!
    @brief JSON that is not an object becomes CatalogueError.
    """
    with pytest.raises(CatalogueError):
        _client(FakeSession(FakeResponse([1, 2]))).search_movies("x")


@pytest.mark.parametrize("error", [requests.Timeout("slow"), requests.ConnectionError("down")])
def test_network_failure_raises_catalogue_error(error: Exception) -> None:
    """!
    @brief A timeout or connection failure becomes CatalogueError.
    """
    with pytest.raises(CatalogueError):
        _client(FakeSession(error=error)).search_movies("x")


def test_missing_key_catalogue_raises_not_configured_error() -> None:
    """!
    @brief Both operations report the missing key with the hint to set the variable.
    """
    catalogue = MissingKeyCatalogue()
    with pytest.raises(CatalogueNotConfiguredError, match=constants.ENV_TMDB_API_KEY):
        catalogue.search_movies("x")
    with pytest.raises(CatalogueNotConfiguredError):
        catalogue.get_movie(1)
