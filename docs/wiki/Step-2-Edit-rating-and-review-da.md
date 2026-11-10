[English](Step-2-Edit-rating-and-review) · **Dansk** · [Bahasa Melayu](Step-2-Edit-rating-and-review-ms)

# Trin 2: Redigér rating og anmeldelse

## Hvad blev bygget

Knappen Update på et kort åbner en formular, hvor du ændrer rating og anmeldelse. `RateMovieForm` er en WTForms-formular, som Bootstrap-Flask tegner med `render_form`. En gyldig indsendelse opdaterer filmen og vender tilbage til forsiden.

## Hvad vi lærte

- Formularer med Flask-WTF og WTForms, inklusive CSRF-beskyttelse.
- Validatorer: `NumberRange(0, 10)` til rating og en længdegrænse til anmeldelsen. `InputRequired` bruges i stedet for `DataRequired`, fordi en rating på 0 er gyldig.
- GET viser formularen udfyldt med de nuværende værdier; POST validerer og gemmer.
- `db.get_or_404` svarer på en ukendt film med en 404-side.
- Redirect efter POST, så en genindlæsning ikke sender to gange.

## Prøv det

`/edit?id=1`

## Skærmbillede

![Redigeringsformular for Phone Booth](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r2-edit.png)

## Næste trin

[Trin 3: Slet film](Step-3-Delete-movies-da)
