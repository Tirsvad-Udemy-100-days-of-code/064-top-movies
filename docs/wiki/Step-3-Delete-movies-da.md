[English](Step-3-Delete-movies) · **Dansk** · [Bahasa Melayu](Step-3-Delete-movies-ms)

# Trin 3: Slet film

## Hvad blev bygget

Knappen Delete på et kort fjerner filmen fra databasen og vender tilbage til forsiden. Skærmbilledet viser listen efter Avatar blev slettet.

## Hvad vi lærte

- Sletning af en række med `db.session.delete` og `commit`.
- Læsning af en query-string-parameter med `request.args` og afvisning af manglende eller ikke-numerisk id med 400.
- Et ukendt id giver 404 og sletter intet.
- Lektionen bruger et GET-link til sletning. Det er enkelt, men en tilstandsændring på GET er ikke sikker i produktion; en POST med CSRF-token er bedre.

## Prøv det

`/delete?id=2`

## Skærmbillede

![Forsiden efter sletning af en film](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r3-delete.png)

## Næste trin

[Trin 4: Tilføj film via TMDB](Step-4-Add-movies-through-TMDB-da)
