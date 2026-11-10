[English](Step-1-View-the-movie-list) · **Dansk** · [Bahasa Melayu](Step-1-View-the-movie-list-ms)

# Trin 1: Se filmlisten

## Hvad blev bygget

Forsiden viser alle film i en SQLite-database. Hvert kort viser plakat og placering på forsiden, og titel, år, anmeldelse, rating og beskrivelse på bagsiden. Databasen har en `Movie`-tabel med unik titel, og en seed-kommando indsætter lektionens to eksempelfilm.

## Hvad vi lærte

- En Flask-applikationsfabrik (`create_app`) og et blueprint samler siderne.
- SQLAlchemy 2-modeller med `Mapped` og `mapped_column`; en unik titel forhindrer dubletter.
- Forespørgsler med `db.session.execute(db.select(Movie)).scalars()`.
- Jinja-skabelonarv med Bootstrap-Flask.
- Et idempotent seed: kørt to gange giver det aldrig en integritetsfejl.

## Prøv det

```bash
python -m flask --app top_movies seed
python -m flask --app top_movies run
```

## Skærmbillede

![Forsiden med to filmkort](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r1-home.png)

## Næste trin

[Trin 2: Redigér rating og anmeldelse](Step-2-Edit-rating-and-review-da)
