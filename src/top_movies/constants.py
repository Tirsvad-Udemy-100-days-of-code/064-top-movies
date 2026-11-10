"""!
@file constants.py
@brief Constants shared by the Top Movies application.
"""

## Name of the application, shown in page titles.
APP_NAME = "Top Movies"

## File name of the SQLite database inside the Flask instance folder.
DATABASE_FILE = "movies.db"

## Name of the environment variable that holds the Flask secret key.
ENV_SECRET_KEY = "SECRET_KEY"  # noqa: S105 - name of a variable, not a secret

## Secret key used when the environment does not set one (development only).
DEFAULT_SECRET_KEY = "development-only-change-me"  # noqa: S105 - documented dev default

## Name of the environment variable that holds the TMDB API key.
ENV_TMDB_API_KEY = "TMDB_API_KEY"

## Title shown at the top of the home page.
HOME_HEADING = "My Top 10 Movies"

## Sub title shown under the heading of the home page.
HOME_SUBHEADING = "These are my all time favourite movies."

## Sub title shown under the movie title on the edit page.
EDIT_SUBHEADING = "Edit Movie Rating"

## Lowest rating a movie can get.
RATING_MIN = 0

## Highest rating a movie can get.
RATING_MAX = 10

## Longest review, equal to the size of the review column.
REVIEW_MAX_LENGTH = 250

## Label of the rating field of the edit form.
RATING_LABEL = "Your Rating Out of 10 e.g. 7.5"

## Label of the review field of the edit form.
REVIEW_LABEL = "Your Review"

## Label of the submit button of the edit form.
SUBMIT_LABEL = "Done"

## Movies stored by the seed command: the two examples of the lecture.
SEED_MOVIES = (
    {
        "title": "Phone Booth",
        "year": 2002,
        "description": (
            "Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by "
            "an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's "
            "negotiation with the caller leads to a jaw-dropping climax."
        ),
        "rating": 7.3,
        "ranking": 10,
        "review": "My favourite character was the caller.",
        "img_url": "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
    },
    {
        "title": "Avatar The Way of Water",
        "year": 2022,
        "description": (
            "Set more than a decade after the events of the first film, learn the story of the "
            "Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the "
            "lengths they go to keep each other safe, the battles they fight to stay alive, and "
            "the tragedies they endure."
        ),
        "rating": 7.3,
        "ranking": 9,
        "review": "I liked the water.",
        "img_url": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
    },
)
