"""!
@file views.py
@brief The pages of the website. View names follow the lecture.
"""

from flask import Blueprint, abort, current_app, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

from top_movies import constants
from top_movies.application.errors import CatalogueError, CatalogueNotConfiguredError
from top_movies.application.ports import MovieCatalogue
from top_movies.infrastructure.database import Movie, db
from top_movies.presentation.forms import FindMovieForm, RateMovieForm

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


def _catalogue() -> MovieCatalogue:
    """!
    @brief Get the movie catalogue that the composition root registered.
    @return The movie catalogue of the running application.
    """
    catalogue: MovieCatalogue = current_app.extensions[constants.EXTENSION_MOVIE_CATALOGUE]
    return catalogue


def _catalogue_error_page(error: CatalogueError) -> tuple[str, int]:
    """!
    @brief Render the error page for a failed catalogue call.
    @param error The failure; a missing key answers 503, any other failure 502.
    @return The page and its HTTP status.
    """
    if isinstance(error, CatalogueNotConfiguredError):
        status = constants.HTTP_SERVICE_UNAVAILABLE
        message = constants.MSG_CATALOGUE_NOT_CONFIGURED
    else:
        status = constants.HTTP_BAD_GATEWAY
        message = constants.MSG_CATALOGUE_FAILED
    return render_template("error.html", message=message), status


@main.route("/add", methods=["GET", "POST"])
def add() -> str | tuple[str, int]:
    """!
    @brief Ask for a movie title and list the matching movies of the catalogue.
    @return The add form, the list of matches after a valid submit, or an error page.
    """
    form = FindMovieForm()
    if not form.validate_on_submit():
        return render_template("add.html", form=form)
    try:
        options = _catalogue().search_movies(form.title.data)
    except CatalogueError as error:
        return _catalogue_error_page(error)
    return render_template("select.html", options=options)


@main.route("/select")
def select() -> str | Response | tuple[str, int]:
    """!
    @brief Store the catalogue movie named by the id query parameter and open its edit page.

    A missing or non-numeric id answers 400. A movie whose title is already stored is not
    stored twice; its edit page opens instead.
    @return A redirect to the edit page, or an error page.
    """
    catalogue_id = request.args.get("id", type=int)
    if catalogue_id is None:
        abort(400)
    try:
        details = _catalogue().get_movie(catalogue_id)
    except CatalogueError as error:
        return _catalogue_error_page(error)
    movie = db.session.execute(db.select(Movie).filter_by(title=details.title)).scalar()
    if movie is None:
        movie = Movie(
            title=details.title,
            year=details.year,
            description=details.description,
            img_url=details.img_url,
        )
        db.session.add(movie)
        db.session.commit()
    return redirect(url_for("main.edit", id=movie.id))
