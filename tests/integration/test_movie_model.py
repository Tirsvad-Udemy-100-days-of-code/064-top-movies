"""!
@file test_movie_model.py
@brief The Movie table keeps every field and refuses a duplicate title.
"""

import pytest
from flask import Flask
from sqlalchemy.exc import IntegrityError

from top_movies.infrastructure.database import Movie, db


def _movie(title: str = "Phone Booth") -> Movie:
    return Movie(
        title=title,
        year=2002,
        description="A man is trapped in a phone booth.",
        rating=7.3,
        ranking=10,
        review="Good caller.",
        img_url="https://example.test/poster.jpg",
    )


def test_movie_is_stored_with_all_fields(app: Flask) -> None:
    """!
    @brief Every field written is read back unchanged.
    """
    with app.app_context():
        db.session.add(_movie())
        db.session.commit()
        db.session.expire_all()
        stored = db.session.execute(db.select(Movie)).scalar_one()
        assert stored.id is not None
        assert stored.title == "Phone Booth"
        assert stored.year == 2002
        assert stored.description == "A man is trapped in a phone booth."
        assert stored.rating == 7.3
        assert stored.ranking == 10
        assert stored.review == "Good caller."
        assert stored.img_url == "https://example.test/poster.jpg"


def test_movie_rating_ranking_and_review_are_optional(app: Flask) -> None:
    """!
    @brief A movie without rating, ranking and review is accepted.
    """
    movie = _movie()
    movie.rating = None
    movie.ranking = None
    movie.review = None
    with app.app_context():
        db.session.add(movie)
        db.session.commit()
        assert db.session.execute(db.select(Movie)).scalar_one().rating is None


def test_movie_duplicate_title_raises_integrity_error(app: Flask) -> None:
    """!
    @brief Two movies with the same title violate the unique constraint.
    """
    with app.app_context():
        db.session.add(_movie())
        db.session.commit()
        db.session.add(_movie())
        with pytest.raises(IntegrityError):
            db.session.commit()
        db.session.rollback()
