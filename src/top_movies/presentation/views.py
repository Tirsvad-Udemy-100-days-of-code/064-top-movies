"""!
@file views.py
@brief The pages of the website. View names follow the lecture.
"""

from flask import Blueprint, abort, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

from top_movies import constants
from top_movies.infrastructure.database import Movie, db
from top_movies.presentation.forms import RateMovieForm

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


@main.route("/edit", methods=["GET", "POST"])
def edit() -> str | Response:
    """!
    @brief Change the rating and the review of the movie named by the id query parameter.

    A missing or non-numeric id answers 400, an id with no movie answers 404.
    @return The edit form, or a redirect to the home page after a valid submit.
    """
    movie_id = request.args.get("id", type=int)
    if movie_id is None:
        abort(400)
    movie = db.get_or_404(Movie, movie_id)
    form = RateMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template(
        "edit.html", movie=movie, form=form, subheading=constants.EDIT_SUBHEADING
    )


@main.route("/delete")
def delete() -> Response:
    """!
    @brief Delete the movie named by the id query parameter.

    This changes state on GET, as the lecture does, so the Delete button can be a plain link.
    A missing or non-numeric id answers 400, an id with no movie answers 404.
    @return A redirect to the home page.
    """
    movie_id = request.args.get("id", type=int)
    if movie_id is None:
        abort(400)
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("main.home"))
