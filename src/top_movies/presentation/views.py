"""!
@file views.py
@brief The pages of the website. View names follow the lecture.
"""

from flask import Blueprint, render_template

from top_movies import constants
from top_movies.infrastructure.database import Movie, db

## Blueprint that holds every page.
main = Blueprint("main", __name__)


@main.route("/")
def home() -> str:
    """!
    @brief Show every movie as a card.
    @return The rendered home page.
    """
    result = db.session.execute(db.select(Movie).order_by(Movie.id))
    movies = result.scalars().all()
    return render_template(
        "index.html",
        movies=movies,
        heading=constants.HOME_HEADING,
        subheading=constants.HOME_SUBHEADING,
    )
