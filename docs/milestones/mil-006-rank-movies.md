# Requirement 5: sort and rank by rating

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c015885] |

---

## Purpose

Decide whether the home page ranks movies by rating, best first, and keeps the ranking current.

## Deliverable

`home()` ordering by rating and assigning `ranking` 1..N, tests of the ranking cases from the assignment, a screenshot and README updates.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Highest rating is ranked 1 and shown first | Met | Not met |
| 2 | Editing a rating re-ranks the list on the next visit | Met | Not met |
| 3 | Adding a movie ranks it by its rating | Met | Not met |
| 4 | Movies with no rating are listed last | Met | Not met |
| 5 | Tests pass and `docs/screenshots/r5-ranking.png` exists | Met | Not met |
| 6 | Code review against `qc-programming-python` is `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | Ranking covers movies added through TMDB |

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

2026-11-16 - within the Business Case constraints (no fixed deadline; one pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Ranking in home | Change `home()` to order by rating descending (unrated last), convert the scalars to a list, assign `ranking` from the position and commit. | No | |
| 2 | Tests, screenshot and docs for R5 | Test the Matrix, Spirited Away and Parasite examples before and after an edit; capture `r5-ranking.png`; finish the README feature list. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
