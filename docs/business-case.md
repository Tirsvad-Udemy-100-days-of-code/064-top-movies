# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Day 64 of Udemy's "100 Days of Code" asks participants to build "Top Movies", a Flask website that lists a personal top-10 of films. The user adds a film by searching The Movie Database (TMDB), rates and reviews it, deletes it, and sees the list ranked by rating. This project delivers that assignment as a readable, tested, documented Python repository, with one screenshot and one wiki explanation (English, Danish, Bahasa Malaysia) for each lecture step, so other course participants can run it and compare solutions.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code. Artifacts are checked against the QC checklists of `framework/qc/`, tagged with ISO/IEC 25010:2023 characteristics. Code follows `qc-programming-python` and the `clean-architecture` skill.

## Problem Statement

A course participant who follows the lecture only sees fragments (gists, screenshots in a video). There is no single runnable, tested repository that walks the five requirements in order with the reasoning behind each step. Participants comparing solutions cannot tell which step a piece of code belongs to.

## Business Opportunity

A repository structured by lecture step gives S02 a reference to compare against, gives S03 a clean example of a small Flask application with tests, and gives S01 a finished, portfolio-quality assignment and practice with the framework.

## Objectives

1. Deliver the five requirements of the Day 64 assignment: list (R1), edit rating and review (R2), delete (R3), add via TMDB (R4), rank by rating (R5).
2. Keep the assignment's names (`home`, `edit`, `delete`, `add`, `select`, `RateMovieForm`, `FindMovieForm`, `Movie`).
3. Test every requirement with pytest, with the TMDB API replaced by a test double, so tests need no network and no API key.
4. Document how to create and use a local `.venv`, run the application and run the tests.
5. Provide a README and a wiki in English, Danish and Bahasa Malaysia that explain, for each lecture step, what was gained, each with a screenshot.
6. Publish the repository with a description and topics.

## Scope

### In Scope

- Python 3.13 or later Flask application under `src/`, tests under `tests/`, documents under `docs/`.
- SQLite through Flask-SQLAlchemy; forms through Flask-WTF and Bootstrap-Flask; TMDB access through `requests`.
- `pyproject.toml`, Python `.gitignore`, `constants.py`, Doxygen comments and a `Doxyfile`.
- README from the framework template; wiki in three languages; one screenshot per lecture step.
- A local opengrep scan before each push.

### Out of Scope

- User accounts, authentication, deployment to a server, or a production database.
- A copy of the Udemy starter files or completed project (the code is written for this repository).
- Any use of the personal tokens in `.env` inside the project.

## Expected Benefits

### Tangible Benefits

- A runnable repository with passing tests for all five requirements.
- A README and a wiki in three languages with one screenshot per lecture step.

### Intangible Benefits

- Practice with Flask, SQLAlchemy, WTForms and a third-party API.
- A reusable reference for other participants.

## Strategic Alignment

The project supports S01's goal of completing the bootcamp with traceable, reviewed work, and exercises the framework end to end on a small product.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Requirements delivered | 5 of 5 | each requirement has a merged milestone and passing tests |
| 2 | Automated tests | all pass | `python -m pytest` exit code 0 |
| 3 | Network-free tests | 0 live calls | tests run with no `TMDB_API_KEY` |
| 4 | Security scan | 0 open findings | opengrep run before each push |
| 5 | Documentation | README and 3 wiki languages | each lecture step has a screenshot and a "what we gained" text |
| 6 | Repository metadata | set | description and topics visible on the repository |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| No TMDB API key is available to the project | The add flow cannot be shown live | Tests use a test double; the key is read from the `TMDB_API_KEY` environment variable and documented; screenshots of the add flow use the test double |
| Secrets in `.env` leak into the repository | Credential exposure | `.env` is in `.gitignore`; the project never reads or imports it; tokens are used only from the shell for git host calls |
| Screenshots taken on the host desktop take over mouse and keyboard | Disturbs S01 | Screenshots are produced in a Docker container (`framework/process/gui-testing.md`) |
| Scope growth beyond the assignment | Delay | Out of Scope list; changes go through the Project Plan |
| Runtime dependencies conflict with S03's wish for none | Reader confusion | Only the packages the assignment names are used; the README states why |

## Assumptions

- S01 is Product Owner, developer and reviewer, and is reachable in chat.
- The git host `git.tirsystem.com` accepts the tokens in `.env` for repository, issue and wiki calls.
- Docker is available for GUI tests and screenshots.
- S02 and S03 are not contacted; their needs are taken from the prompt.

## Constraints

- Python 3.13 or later, `venv`, pytest, `pyproject.toml`, constants in `constants.py`, Doxygen comments, folders `src/`, `tests/`, `docs/`.
- English and IT are the Product Owner's language and domain; wiki in English, Danish and Bahasa Malaysia.
- One branch and one pull request per milestone; the plan-first gate applies.
- The Udemy starter archives are not downloaded; their templates are re-created.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: the project has no revenue, budget or licence cost, so a numeric ROI would add nothing to the decision.

| Costs | Benefits |
| --- | --- |
| S01's time and AI agent effort; no licence or hosting cost | Finished assignment, shareable reference, framework practice |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a finished, correct assignment |
| S02 | Udemy coursists; want readable, runnable code with the assignment's names and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README, and no extra runtime dependencies |

## Recommendation

Proceed - the scope is small, fully specified by the assignment, and testable without external services.

---

[SA-001]: ./stakeholder-analysis.md
