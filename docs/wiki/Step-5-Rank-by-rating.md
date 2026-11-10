**English** · [Dansk](Step-5-Rank-by-rating-da) · [Bahasa Melayu](Step-5-Rank-by-rating-ms)

# Step 5: Rank by rating

## What was built

The home page ranks the movies by rating, best first, and stores the ranking. In the screenshot a new movie rated 9.2 becomes number 1 and the others move down. Editing a rating re-ranks the list on the next visit. Movies without a rating come last.

## What we gained

- A pure business rule in the `domain` layer (`rank_by_rating`) with no Flask or database code.
- A stable sort: ties keep their order; unrated movies come last.
- Turning query results into a Python list and writing the computed ranking back.
- Testing the rule alone with plain objects, and the page with the lecture examples (Matrix 9.3, Spirited Away 9.5, Parasite 9.9).
- The clean architecture idea in practice: rules in the middle, framework at the edge.

## Try it

`/`

## Screenshot

![Home page ranked by rating](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r5-ranking.png)
