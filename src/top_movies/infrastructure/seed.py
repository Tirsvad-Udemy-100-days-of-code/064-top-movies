"""!
@file seed.py
@brief Insert the example movies of the lecture into the database.
"""

from collections.abc import Iterable, Mapping
from typing import Any

from top_movies.constants import SEED_MOVIES
from top_movies.infrastructure.database import Movie, db


def seed_movies(movies: Iterable[Mapping[str, Any]] = SEED_MOVIES) -> int:
    """!
    @brief Insert the movies whose title is not stored yet; running it twice is safe.
    @param movies Field values of the movies to insert.
    @return The number of movies inserted.
    """
    inserted = 0
    for fields in movies:
        exists = db.session.execute(db.select(Movie).filter_by(title=fields["title"])).scalar()
        if exists is None:
            db.session.add(Movie(**fields))
            inserted += 1
    db.session.commit()
    return inserted
