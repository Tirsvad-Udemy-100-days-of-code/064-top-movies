# Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c015885] |

---

## Purpose

Decide whether the project skeleton, tooling and repository metadata are ready for feature work.

## Deliverable

Python project skeleton under `src/` and `tests/`, `pyproject.toml`, `.gitignore`, `constants.py`, Doxyfile, README from the framework template with venv, run and test instructions, a local opengrep scan script, a Docker screenshot tool, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` runs and passes in a fresh `.venv` | Met | Not met |
| 2 | `pyproject.toml` requires Python 3.13 or later | Met | Not met |
| 3 | README follows the framework template and passes `check-readme.sh` | Met | Not met |
| 4 | Repository description and topics are set on the git host | Met | Not met |
| 5 | opengrep scan of the branch reports no open finding | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone after the baseline |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 6 in [BC-001]; concerns CN-003, CN-006, CN-007 in [SA-001] | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-11 - within the Business Case constraints (no fixed deadline; one pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Project configuration and skeleton | Create `pyproject.toml` (Python 3.13 or later, runtime dependencies Flask, Flask-SQLAlchemy, Flask-WTF, Bootstrap-Flask and requests; pytest as a dev extra), a Python `.gitignore` that also ignores `.env`, `instance/` and `.venv/`, the `src/top_movies/` package with `constants.py`, and an empty `tests/` package with a smoke test. | No | |
| 2 | Local venv and README | Write the README from `framework/templates/README-template.md`: create and use a local `.venv`, run `python -m pip install --upgrade pip`, install the project, run the app and run pytest, on Windows and POSIX. State why each runtime dependency is needed. | No | |
| 3 | Doxygen configuration | Add a `Doxyfile` for `src/` and the rule that every module, class and function carries a Doxygen comment (`@brief`, `@param`, `@return`). Verify with `doxygen` that it builds without warnings. | No | |
| 4 | Local opengrep scan | Add `scripts/scan.ps1` and `scripts/scan.sh` that run `~/.opengrep/cli/latest/opengrep.exe` over `src/` and `tests/`, and document in the README that it runs before every push. | No | |
| 5 | Repository description and topics | Set the description and topics of the Gitea repository through its API, reading the token from the shell environment (`.env` is read by the shell only, never by the project). | No | |
| 6 | Docker screenshot tool | Add `tools/screenshots/` with a Dockerfile and a script that starts the app in a container and captures a named page with a headless browser, as `framework/process/gui-testing.md` requires, so screenshots never use the host desktop. | No | |
| 7 | Git hooks | Run `framework/scripts/install-git-hooks.sh --enable-plan-gate` so commits are checked against accepted milestones. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
