**English** · [Dansk](Step-1-View-the-movie-list-da) · [Bahasa Melayu](Step-1-View-the-movie-list-ms)

# Step 1: View the movie list

## What was built

The home page lists every movie stored in a SQLite database. Each card shows the poster and ranking on the front, and title, year, review, rating and description on the back. The database holds a `Movie` table with a unique title, and a seed command inserts the two example movies of the lecture.

## What we gained

- A Flask application factory (`create_app`) and a blueprint hold the pages.
- SQLAlchemy 2 style models with `Mapped` and `mapped_column`; a unique title stops duplicates.
- Querying with `db.session.execute(db.select(Movie)).scalars()`.
- Jinja template inheritance with Bootstrap-Flask.
- An idempotent seed: running it twice never raises an integrity error.

## Try it

```bash
python -m flask --app top_movies seed
python -m flask --app top_movies run
```

## Screenshot

![Home page with two movie cards](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r1-home.png)

## Next step

[Step 2: Edit rating and review](Step-2-Edit-rating-and-review)
