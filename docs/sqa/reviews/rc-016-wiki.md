# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [66b728d] |

---

## Artifact Under Review

- Instance reviewed: `docs/wiki` (the wiki folder, published 2026-11-10; it has no artifact ID)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none (the reviewer reads English and the IT domain as stand-in for S01)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`; the author is the same AI, so this review is a stand-in, to be challenged in the run summary)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Starts with the bold title, then one English page list with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 7 English pages are linked; a script found 0 broken links. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last, one line per language, written in that language. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is hand-maintained text produced once; no generator is used. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has a language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia; the PO language is English. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 7 pages per language: 21 page files plus the sidebar. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line, current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Home-da.md and Home-ms.md style names; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names and code identifiers are in English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge all 22 wiki pages and the 7 screenshots returned HTTP 200 on the host, and the published sidebar lists the Home-da and Home-ms links. Pages were fetched, not clicked through in a browser. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no layout rule changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | docs/wiki is flat; languages are told apart by file name. |

## Overall Verdict

Go - The wiki meets all mandatory criteria and was checked on the host. Autonomous stand-in review, not independent: the Danish and Bahasa Malaysia texts were written by the same AI and have not been read by a native speaker.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Have a native reader check the Danish and Bahasa Malaysia pages | S01 | 2026-11-30 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[66b728d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/commit/66b728de665308828f3282ba39d076f54ecf15a9
