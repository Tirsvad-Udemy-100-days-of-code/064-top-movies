**English** · [Dansk](Step-2-Edit-rating-and-review-da) · [Bahasa Melayu](Step-2-Edit-rating-and-review-ms)

# Step 2: Edit rating and review

## What was built

The Update button on a card opens a form where you change the rating and the review. `RateMovieForm` is a WTForms form; Bootstrap-Flask renders it with `render_form`. A valid submit updates the movie and returns to the home page.

## What we gained

- Forms with Flask-WTF and WTForms, including CSRF protection.
- Validators: `NumberRange(0, 10)` for the rating, a length limit for the review. `InputRequired` is used instead of `DataRequired`, because a rating of 0 is valid.
- The GET shows the form filled with current values; the POST validates and stores.
- `db.get_or_404` answers an unknown movie with a 404 page.
- Redirect after POST, so a page reload does not submit twice.

## Try it

`/edit?id=1`

## Screenshot

![Edit form for Phone Booth](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r2-edit.png)

## Next step

[Step 3: Delete movies](Step-3-Delete-movies)
