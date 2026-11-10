# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [c015885] |

---

## Purpose

Identify who the project serves and what each needs, using the Power/Interest grid, so that the Business Case objectives and the README and wiki content answer real concerns.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer, reviewer | Self | HIGH | HIGH | Manage Closely | A finished, correct, well documented assignment |
| S02 | Udemy coursists | Fellow course participants | Udemy | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and clear run instructions |
| S03 | GitHub viewers | Repository browsers | Public | LOW | LOW | Monitor | Clear description, topics and README; no unnecessary runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact.
- **Keep Informed (S02):** cannot change the project but depends on the quality of the README and wiki.
- **Monitor (S03):** casual readers, served by the repository front page.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | All five lecture requirements work as the assignment describes | Functionality |
| CN-002 | S01 | Changes are reviewed and traceable per step | Supportability |
| CN-003 | S02 | Code can be run from the README without guessing | Usability |
| CN-004 | S02 | Function names match the lecture so solutions can be compared | Functionality |
| CN-005 | S02 | Each lecture step is explained with a screenshot | Usability |
| CN-006 | S03 | The repository states what it is through description and topics | Usability |
| CN-007 | S03 | Dependencies are limited to what the assignment needs | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat | Per run | Plan and run summary to S01 | All milestones |
| CM-002 | README | Per milestone | Run instructions and screenshots | MIL-001 to MIL-006 |
| CM-003 | Wiki (en, da, ms) | Once | What we gained per lecture step | MIL-007 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies; the assignment requires Flask and related packages | S02, S03 | Only the assignment's packages are used and the README says why |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | Objectives 1 and 3 in [BC-001] |
| S02 | CN-003, CN-004, CN-005 | Objectives 2, 4 and 5 in [BC-001] |
| S03 | CN-006, CN-007 | Objective 6 in [BC-001] |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted (AI as stand-in) | 2026-11-10 |

---

[BC-001]: ./business-case.md
[c015885]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/c015885544ba82f59729d068bc55c5d2a1f2bb7c
