[English](Step-5-Rank-by-rating) · **Dansk** · [Bahasa Melayu](Step-5-Rank-by-rating-ms)

# Trin 5: Rangér efter rating

## Hvad blev bygget

Forsiden rangerer filmene efter rating, bedst først, og gemmer placeringen. På skærmbilledet bliver en ny film med rating 9,2 nummer 1, og de andre rykker ned. Når en rating redigeres, rangeres listen igen ved næste besøg. Film uden rating kommer sidst.

## Hvad vi lærte

- En ren forretningsregel i `domain`-laget (`rank_by_rating`) uden Flask- eller databasekode.
- En stabil sortering: ens ratings beholder rækkefølgen; film uden rating kommer sidst.
- Forespørgselsresultater bliver til en Python-liste, og den beregnede placering skrives tilbage.
- Regelen testes alene med almindelige objekter, og siden testes med lektionens eksempler (Matrix 9,3, Spirited Away 9,5, Parasite 9,9).
- Clean architecture i praksis: reglerne i midten, frameworket i kanten.

## Prøv det

`/`

## Skærmbillede

![Forsiden rangeret efter rating](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r5-ranking.png)
