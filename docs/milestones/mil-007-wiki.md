# Wiki, screenshots and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c015885] |

---

## Purpose

Decide whether the documentation is complete in three languages and the project can be released.

## Deliverable

Wiki pages in English, Danish and Bahasa Malaysia that explain what was gained in each lecture step with its screenshot, a final README, a Doxygen build, and release v1.0.0.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Wiki has the same pages in en, da and ms | Met | Not met |
| 2 | Each of the five steps has a screenshot and a what-we-gained text in every language | Met | Not met |
| 3 | README links the wiki and every screenshot resolves | Met | Not met |
| 4 | `check-readme.sh`, `check-languages.sh` and the wiki checklist pass | Met | Not met |
| 5 | opengrep scan of `main` reports no open finding | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-006 | All steps and screenshots exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5 in [BC-001]; CN-005 in [SA-001] | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-17 - within the Business Case constraints (no fixed deadline; one pull request per milestone).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Wiki structure and English pages | Create the wiki following `framework/process/wiki.md`: home, one page per lecture step (R1 to R5) and run instructions, explaining what each step teaches, with its screenshot. | No | |
| 2 | Danish and Bahasa Malaysia pages | Translate the same pages into Danish (`da`) and Bahasa Malaysia (`ms`) with language links between them. | No | |
| 3 | Publish the wiki | Push the wiki to the Gitea wiki repository using `TOKEN_FOR_GITEA_WIKI` from the shell environment, and verify each page loads. | No | |
| 4 | Final README and Doxygen check | Make sure the README embeds the five screenshots, links the wiki, and that `doxygen` builds without warnings. | No | |
| 5 | Release v1.0.0 | Tag and create a Gitea release with notes, using `TOKEN_FOR_GITEA_RELEASE` from the shell environment. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
