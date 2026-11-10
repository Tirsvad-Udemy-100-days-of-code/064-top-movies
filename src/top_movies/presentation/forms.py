"""!
@file forms.py
@brief The web forms of the website. Form names follow the lecture.
"""

from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange

from top_movies import constants


class RateMovieForm(FlaskForm):  # type: ignore[misc]
    """!
    @brief Form that changes the rating and the review of one movie.
    """

    rating = FloatField(
        constants.RATING_LABEL,
        # InputRequired, not DataRequired: DataRequired would reject the valid rating 0.
        validators=[InputRequired(), NumberRange(constants.RATING_MIN, constants.RATING_MAX)],
    )
    review = StringField(
        constants.REVIEW_LABEL,
        validators=[DataRequired(), Length(max=constants.REVIEW_MAX_LENGTH)],
    )
    submit = SubmitField(constants.SUBMIT_LABEL)


class FindMovieForm(FlaskForm):  # type: ignore[misc]
    """!
    @brief Form that asks for the title of a movie to look up.
    """

    title = StringField(
        constants.TITLE_LABEL,
        validators=[DataRequired(), Length(max=constants.TITLE_MAX_LENGTH)],
    )
    submit = SubmitField(constants.ADD_SUBMIT_LABEL)
