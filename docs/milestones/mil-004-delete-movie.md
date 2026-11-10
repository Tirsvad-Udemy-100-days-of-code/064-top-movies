# Requirement 3: delete movies

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether a movie can be removed from the database from its card.

## Deliverable

A `delete` view wired to the card's Delete button, tests, a screenshot and README updates.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Delete removes exactly the movie with the given id | Met | Not met |
| 2 | Unknown id returns 404 and removes nothing | Met | Not met |
| 3 | Tests pass and `docs/screenshots/r3-delete.png` exists | Met | Not met |
| 4 | Code review against `qc-programming-python` is `Go` | Met | Not met |

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
| 1 | delete view | Implement `delete()` for `/delete?id=N`: fetch the movie (404 if absent), delete it, commit and redirect to `home`. | No | |
| 2 | Tests, screenshot and docs for R3 | Test deleting an existing and an unknown movie; capture `r3-delete.png`; add the step to the README. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
