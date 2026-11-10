# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c015885] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [MIL-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [MIL-001] | [RC-002] |
| [MIL-001] | MIL | en | it | [BC-001], [SA-001] | - | [RC-003], [RC-010] |
| [MIL-002] | MIL | en | it | [BC-001], [SA-001] | - | [RC-004], [RC-011] |
| [MIL-003] | MIL | en | it | [BC-001], [SA-001] | - | [RC-005], [RC-012] |
| [MIL-004] | MIL | en | it | [BC-001], [SA-001] | - | [RC-006], [RC-013] |
| [MIL-005] | MIL | en | it | [BC-001], [SA-001] | - | [RC-007], [RC-014] |
| [MIL-006] | MIL | en | it | [BC-001], [SA-001] | - | [RC-008], [RC-015] |
| [MIL-007] | MIL | en | it | [BC-001], [SA-001] | - | [RC-009] |
| docs/wiki | Wiki | en, da, ms | it | [MIL-007] | - | [RC-016] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | - | - | Gap |
| CN-002 | - | - | - | Gap |
| CN-003 | - | - | - | Gap |
| CN-004 | - | - | - | Gap |
| CN-005 | - | - | - | Gap |
| CN-006 | - | - | - | Gap |
| CN-007 | - | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-view-movies.md
[MIL-003]: ../milestones/mil-003-edit-movie.md
[MIL-004]: ../milestones/mil-004-delete-movie.md
[MIL-005]: ../milestones/mil-005-add-movie-tmdb.md
[MIL-006]: ../milestones/mil-006-rank-movies.md
[MIL-007]: ../milestones/mil-007-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-mil-004.md
[RC-007]: ./reviews/rc-007-mil-005.md
[RC-008]: ./reviews/rc-008-mil-006.md
[RC-009]: ./reviews/rc-009-mil-007.md
[SA-001]: ../stakeholder-analysis.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
[RC-010]: ./reviews/rc-010-code-mil-001.md
[RC-011]: ./reviews/rc-011-code-mil-002.md
[RC-012]: ./reviews/rc-012-code-mil-003.md
[RC-013]: ./reviews/rc-013-code-mil-004.md
[RC-014]: ./reviews/rc-014-code-mil-005.md
[RC-015]: ./reviews/rc-015-code-mil-006.md
[RC-016]: ./reviews/rc-016-wiki.md
