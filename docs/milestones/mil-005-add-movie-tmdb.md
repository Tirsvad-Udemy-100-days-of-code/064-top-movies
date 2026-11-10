# Requirement 4: add movies through TMDB

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether a user can search TMDB by title, pick a result, store it and then rate it.

## Deliverable

`FindMovieForm`, `add` and `select` views, a TMDB client behind a small interface, redirect to `edit` after adding, tests with a test double, screenshots and README updates.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Add page shows a one-field form for the title | Met | Not met |
| 2 | Search lists matching titles and years from the TMDB client | Met | Not met |
| 3 | Choosing a result stores title, year, description and img_url and redirects to the edit page | Met | Not met |
| 4 | Tests need no network and no API key | Met | Not met |
| 5 | Missing `TMDB_API_KEY` gives a clear error page, not a crash | Met | Not met |
| 6 | Screenshots `r4-add.png`, `r4-select.png`, `r4-edit-new.png` exist | Met | Not met |
| 7 | Code review against `qc-programming-python` is `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The new movie is sent to the edit page |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 3 in [BC-001]; CN-001, CN-004 in [SA-001] | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-15 - within the Business Case constraints (no fixed deadline; one pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | TMDB client | Create a client with `search_movies(title)` and `get_movie(id)` using `requests` against the TMDB v3 API, with the key read from `TMDB_API_KEY`, a timeout, and the endpoints and image base URL in `constants.py`. The app depends on a small interface so tests inject a fake. | No | |
| 2 | FindMovieForm and add view | Create `FindMovieForm` (title only) and `add()` that searches through the client and renders `select.html` with results. | No | |
| 3 | select view | Implement `select()` for `/select?id=N`: fetch details, store title, year, description and img_url, and redirect to `edit` for the new movie. A title already stored redirects to its edit page instead of failing. | No | |
| 4 | Tests, screenshots and docs for R4 | Test with a fake client and a faked `requests` layer; capture the add, select and edit-new screenshots in Docker using the fake client; document how to set `TMDB_API_KEY` in the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
