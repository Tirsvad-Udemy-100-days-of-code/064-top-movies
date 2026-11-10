**English** · [Dansk](Step-4-Add-movies-through-TMDB-da) · [Bahasa Melayu](Step-4-Add-movies-through-TMDB-ms)

# Step 4: Add movies through TMDB

## What was built

Add Movie opens a one-field form (`FindMovieForm`). The title is searched on The Movie Database (TMDB); the matches are listed with their year. Choosing one fetches its details, stores title, year, description and poster, and opens the edit page so you can add a rating and a review.

## What we gained

- Calling a web API with `requests`: always a timeout, `raise_for_status`, and clear errors.
- Keeping the API key in the environment (`TMDB_API_KEY`), never in code.
- Ports and adapters: the views depend on a small `MovieCatalogue` interface, so tests and screenshots use a fake and need no network and no key.
- Friendly error pages: 503 when the key is missing, 502 when TMDB fails.
- A multi-step flow: search, select, store, edit.

## Try it

```powershell
$env:TMDB_API_KEY = "your-key-here"
python -m flask --app top_movies run
```

## Screenshot

![Add page with the title field](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-add.png)

![Select page with the search results](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-select.png)

![Edit page of the new movie](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-edit-new.png)

## Next step

[Step 5: Rank by rating](Step-5-Rank-by-rating)
