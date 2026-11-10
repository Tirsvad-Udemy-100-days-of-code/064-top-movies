"""!
@file test_rate_movie_form.py
@brief Validation rules of the RateMovieForm.
"""

import pytest
from flask import Flask

from top_movies import constants
from top_movies.presentation.forms import RateMovieForm


def _validate(app: Flask, data: dict[str, str]) -> RateMovieForm:
    """!
    @brief Validate the form against the given submitted data.
    @param app The application, for the request context.
    @param data The submitted fields.
    @return The validated form.
    """
    with app.test_request_context("/edit?id=1", method="POST", data=data):
        form = RateMovieForm()
        form.validate()
        return form


def test_form_is_valid_with_rating_and_review(app: Flask) -> None:
    """!
    @brief A rating in range and a review pass.
    """
    form = _validate(app, {"rating": "7.5", "review": "Great"})
    assert not form.errors
    assert form.rating.data == 7.5


@pytest.mark.parametrize("rating", [constants.RATING_MIN, constants.RATING_MAX])
def test_form_accepts_rating_at_the_limits(app: Flask, rating: int) -> None:
    """!
    @brief The lowest and highest rating are valid, including 0.
    @param app The application fixture.
    @param rating The rating at a limit.
    """
    form = _validate(app, {"rating": str(rating), "review": "ok"})
    assert not form.errors


@pytest.mark.parametrize("rating", ["-0.1", "10.1"])
def test_form_rejects_rating_outside_range(app: Flask, rating: str) -> None:
    """!
    @brief A rating just below 0 or just above 10 is refused.
    @param app The application fixture.
    @param rating The out of range rating.
    """
    form = _validate(app, {"rating": rating, "review": "ok"})
    assert "rating" in form.errors


def test_form_rejects_non_numeric_rating(app: Flask) -> None:
    """!
    @brief Text in the rating field is refused.
    """
    form = _validate(app, {"rating": "abc", "review": "ok"})
    assert "rating" in form.errors


def test_form_rejects_empty_review(app: Flask) -> None:
    """!
    @brief A missing review is refused.
    """
    form = _validate(app, {"rating": "5", "review": ""})
    assert "review" in form.errors


def test_form_accepts_review_of_maximum_length(app: Flask) -> None:
    """!
    @brief A review of exactly 250 characters is valid.
    """
    form = _validate(app, {"rating": "5", "review": "a" * constants.REVIEW_MAX_LENGTH})
    assert not form.errors


def test_form_rejects_review_longer_than_maximum(app: Flask) -> None:
    """!
    @brief A review of 251 characters is refused.
    """
    form = _validate(app, {"rating": "5", "review": "a" * (constants.REVIEW_MAX_LENGTH + 1)})
    assert "review" in form.errors
