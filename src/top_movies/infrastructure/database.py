"""!
@file database.py
@brief The SQLAlchemy extension and the Movie table.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """!
    @brief Declarative base class of every table.
    """


## The database extension, bound to the Flask application by the composition root.
db = SQLAlchemy(model_class=Base)


class Movie(db.Model):  # type: ignore[name-defined]
    """!
    @brief One movie of the top list.
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float | None] = mapped_column(Float, nullable=True)
    ranking: Mapped[int | None] = mapped_column(Integer, nullable=True)
    review: Mapped[str | None] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
