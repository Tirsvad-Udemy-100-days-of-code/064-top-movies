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

## Base URL of version 3 of the TMDB API.
TMDB_API_BASE = "https://api.themoviedb.org/3"

## Base URL of TMDB poster images, at the w500 size.
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

## Poster used when TMDB has no poster for a movie.
TMDB_PLACEHOLDER_IMAGE_URL = "https://placehold.co/500x750?text=No+poster"

## Seconds to wait for TMDB before a request fails.
TMDB_TIMEOUT_SECONDS = 10

## Year stored when TMDB gives no release date; a movie must have a year, 0 means unknown.
TMDB_UNKNOWN_YEAR = 0

## Longest movie title the add form accepts, equal to the size of the title column.
TITLE_MAX_LENGTH = 250

## Label of the title field of the add form.
TITLE_LABEL = "Movie Title"

## Label of the submit button of the add form.
ADD_SUBMIT_LABEL = "Add Movie"

## Name under which the movie catalogue is kept in the Flask extensions.
EXTENSION_MOVIE_CATALOGUE = "movie_catalogue"

## Message shown when the TMDB API key is not set.
MSG_CATALOGUE_NOT_CONFIGURED = (
    "The movie database is not configured. Set the environment variable "
    f"{ENV_TMDB_API_KEY} to your TMDB API key and restart the website."
)

## Message shown when the movie database cannot be reached or answers badly.
MSG_CATALOGUE_FAILED = "The movie database could not be reached. Please try again later."

## HTTP status when the catalogue is not configured.
HTTP_SERVICE_UNAVAILABLE = 503

## HTTP status when the catalogue fails.
HTTP_BAD_GATEWAY = 502
