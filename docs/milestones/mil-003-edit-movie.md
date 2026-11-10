# Requirement 2: edit rating and review

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c015885] |

---

## Purpose

Decide whether a movie's rating and review can be changed through a WTForms form.

## Deliverable

`RateMovieForm`, an `edit` view using the existing `edit.html` through Bootstrap-Flask `render_form`, tests, a screenshot and README updates.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Form has a rating and a review field with validators | Met | Not met |
| 2 | Valid POST updates the stored movie and redirects to `/` | Met | Not met |
| 3 | Invalid rating is rejected and nothing is stored | Met | Not met |
| 4 | Tests pass and `docs/screenshots/r2-edit.png` exists | Met | Not met |
| 5 | Code review against `qc-programming-python` is `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Needs the model, templates and home view |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 in [BC-001]; CN-001 in [SA-001] | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-13 - within the Business Case constraints (no fixed deadline; one pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | RateMovieForm | Create `RateMovieForm` with a numeric rating (0 to 10) and a review text field, CSRF protected through Flask-WTF, with a `SECRET_KEY` from the environment and a development default kept in `constants.py`. | No | |
| 2 | edit view | Implement `edit()` for `/edit?id=N`: show the form filled with current values, validate, update the movie with SQLAlchemy and redirect to `home`. Unknown ids return 404. | No | |
| 3 | Tests, screenshot and docs for R2 | Test valid, invalid and unknown-id cases; capture `r2-edit.png`; add the step to the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
