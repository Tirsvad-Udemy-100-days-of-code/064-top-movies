# Requirement 1: view the movie list

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c015885] |

---

## Purpose

Decide whether the home page lists movies from the SQLite database as the assignment shows.

## Deliverable

Flask application factory, `Movie` model with a unique title in `instance/movies.db`, the Bootstrap templates, an idempotent seed with Phone Booth and Avatar The Way of Water, a `home` view that renders every movie card, tests, a screenshot and README and docs updates.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `Movie` has id, title (unique), year, description, rating, ranking, review, img_url | Met | Not met |
| 2 | Seeding twice leaves two rows and raises no integrity error | Met | Not met |
| 3 | `GET /` renders both seeded movies | Met | Not met |
| 4 | Tests pass and the screenshot `docs/screenshots/r1-home.png` exists | Met | Not met |
| 5 | Code review against `qc-programming-python` is `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Skeleton, tooling and screenshot tool |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3 in [BC-001]; CN-001, CN-004 in [SA-001] | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-12 - within the Business Case constraints (no fixed deadline; one pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | App factory, database and Movie model | Create `create_app()` with the instance folder, Flask-SQLAlchemy and the `Movie` model (fields id, title unique, year, description, rating, ranking, review, img_url). Table creation happens at start-up. | No | |
| 2 | Templates and static files | Re-create `base.html`, `index.html`, `edit.html`, `add.html`, `select.html` and the stylesheet with Bootstrap-Flask, so the front shows the ranking, title and year and the back shows rating, review, description and Update/Delete buttons. | No | |
| 3 | Seed command | Add an idempotent seed that inserts Phone Booth and Avatar The Way of Water with the assignment's values (rating 7.3, ranking 10 and 9), runnable twice without an integrity error. | No | |
| 4 | home view | Implement `home()` to query movies with `db.session.execute(...).scalars()` and render `index.html`. | No | |
| 5 | Tests, screenshot and docs for R1 | Write pytest tests for the model, the seed and the home page; capture `r1-home.png` through the Docker tool; add the step to the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
