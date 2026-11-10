[English](Step-4-Add-movies-through-TMDB) · **Dansk** · [Bahasa Melayu](Step-4-Add-movies-through-TMDB-ms)

# Trin 4: Tilføj film via TMDB

## Hvad blev bygget

Add Movie åbner en formular med ét felt (`FindMovieForm`). Titlen søges på The Movie Database (TMDB); træffene vises med årstal. Når du vælger en, hentes detaljerne, og titel, år, beskrivelse og plakat gemmes, hvorefter redigeringssiden åbnes, så du kan tilføje rating og anmeldelse.

## Hvad vi lærte

- Kald af et web-API med `requests`: altid timeout, `raise_for_status` og tydelige fejl.
- API-nøglen ligger i miljøet (`TMDB_API_KEY`), aldrig i koden.
- Porte og adaptere: visningerne afhænger af en lille `MovieCatalogue`-grænseflade, så test og skærmbilleder bruger en falsk udgave og kræver hverken netværk eller nøgle.
- Venlige fejlsider: 503 når nøglen mangler, 502 når TMDB fejler.
- Et flertrinsforløb: søg, vælg, gem, redigér.

## Prøv det

```powershell
$env:TMDB_API_KEY = "your-key-here"
python -m flask --app top_movies run
```

## Skærmbillede

![Tilføj-siden med titelfeltet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-add.png)

![Vælg-siden med søgeresultaterne](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-select.png)

![Redigeringssiden for den nye film](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-edit-new.png)

## Næste trin

[Trin 5: Rangér efter rating](Step-5-Rank-by-rating-da)
