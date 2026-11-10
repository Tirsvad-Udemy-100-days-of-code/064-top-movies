**English** · [Dansk](Step-3-Delete-movies-da) · [Bahasa Melayu](Step-3-Delete-movies-ms)

# Step 3: Delete movies

## What was built

The Delete button on a card removes that movie from the database and returns to the home page. The screenshot shows the list after Avatar was deleted.

## What we gained

- Deleting a row with `db.session.delete` and `commit`.
- Reading a query-string parameter with `request.args` and rejecting a missing or non-numeric id with 400.
- An unknown id gives 404 and removes nothing.
- The lecture uses a GET link for deletion. It is simple, but a state change on GET is not safe in production; a POST with a CSRF token is the better choice.

## Try it

`/delete?id=2`

## Screenshot

![Home page after deleting a movie](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r3-delete.png)

## Next step

[Step 4: Add movies through TMDB](Step-4-Add-movies-through-TMDB)
