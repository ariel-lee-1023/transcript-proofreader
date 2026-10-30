# Source and coverage ledger — 2026-10-30

## Scope and architecture

Continued distillation into the existing `transcript-proofreader` repository, based on local baseline commit `d703916`. This is a targeted maintenance pass, not three new books or a complete reread. Preserve the destination's canonical root skill, three `references/reference-*.md` files, root experience table, CI, NOTICE and changelog. Keep maintainer records here. New runtime content was built and checked in the designated staging area before integration into the existing final checkout; no second clone or history replacement.

The final checkout already had uncommitted AGENTS.md changes. Preserve these bytes and their local status; new authorship/source guidance is separable. Do not publish unrelated metatool changes.

## Corpus identity and extraction

Three supplied Markdown books were extracted through the metatool's standard-library text pipeline. Their paired PDFs were inventoried and hashed, not read independently. No usable PDF backend was available in the default interpreter; the existing Markdown was sufficient for this bounded expansion. The three original Markdown files total approximately 544,837 tokens by the extractor's script-density estimate. This is a corpus-size estimate, not actual tokens consumed. Extractor page estimates were rejected as printed pagination. The source manifest records file hashes, original line counts and scan labels; no raw books or full extractions are published.

Titles/editions: Einsohn and Schwartz, fourth edition (2019); Saller, supplied first edition (2009); Hill and King, Meckler publication (1991). The 1987/1989 dates near Hill's advisory committee are distinct from the publication copyright page. The printed-pages/scan-label distinction is explicit in each reference.

## Existing framework spine and disposition

| Source | Retained framework or principle | Expansion, qualification or deliberate exclusion |
|---|---|---|
| Einsohn ch.1 | 4 Cs/Cardinal C, four commandments, six tasks, editorial judgment, ILF/ISF, illusory knowledge | Existing synthesis retained; human accuracy figures removed as a misleading capability implication; no claim every inherited detail was re-audited |
| Einsohn ch.1 | Light/Medium/Heavy, FIQ, review stages, triage | Distinguish general publishing levels from narrower transcript levels; preserve complete-pass priority |
| Einsohn ch.2 | Queries, style sheets, author review | Expand actual returned-copy reconciliation, new-text checks, unanswered queries and numbering checks |
| Einsohn ch.3 | Reference tools, language corpora | Add register/genre/period/collocation comparison and sense/composition cautions; omit obsolete database size claims |
| Einsohn chs.4–6 | Punctuation, spelling, capitalization | Existing meaning-changing punctuation example and mechanical consistency retained; full inventories and exercises excluded from this transcript-focused pass |
| Einsohn ch.7 | Numbers and numerals | Add percent/percentage-point/basis-point distinction, bases and ambiguous comparisons; query content rather than repair a claim silently |
| Einsohn ch.8 | Spoken versus written quotations, brackets, minor cleanup | Verify conditional publisher practice and unchanged-meaning limit; paraphrase must be labeled separately |
| Einsohn chs.9–13 | Abbreviations, visual material, documentation, apparatus, markup | Existing acronym/style guidance retained; full production taxonomy, legal guidance and technical tables outside this expansion; no claim of exhaustive coverage |
| Einsohn chs.14–15 | Grammar/usage/diction, audience, EFL/ESL, bias-free language | Preserve scope overview; add deliberate-view versus inadvertent-bias distinction; no automatic sanitization of testimony |
| Saller chs.1–3 | Reader loyalty, Six Habits, carefulness/transparency/flexibility, stet | Preserve existing core; qualify style-versus-grammar shorthand by reader effect and actual record type |
| Saller ch.4 | Difficult-author restraint | Add firmness about consequential errors; source does not demand unconditional surrender |
| Saller ch.5 | Dear Writers | Add untracked replacement-file danger and visible review amendments |
| Saller ch.6 | Automate, delegate, reevaluate | Correct reevaluate to necessity/reader benefit; retain accept-your-fate fallback; describe delegation without authorizing external action |
| Saller ch.7 | Five collision-insurance practices | Labels and folders, trial runs, version control, transparency, backup; omit obsolete interface directions |
| Saller ch.8 | Lists, schedules, logs | Preserve their distinct temporal roles and handoff implications |
| Saller chs.9–10 | Play nicely/work through channels, reliability and overruns | Add bounded coordination and scope judgment; detailed pricing, tax, fee collection and career advice excluded |
| Saller ch.11 | Working to rule, sufficient quality, over-editing costs | Retain stopping judgment and one worked example; no promise of measured performance |
| Saller appendix | Entering the profession | Excluded: not needed to proofread supplied transcripts |
| Hill preface | Retrospective personal accounting, sampling limits, narrator review, signed agreements | Verify 72 interviewees, avoid equating that with number of entries audited; opportunity for review is not universal final authority |
| Hill guide note/abbreviations | Finding-aid limits, estimates in brackets, historical name expansion | Broader bracket policy explicitly identified as adaptation; source bracket provenance retained |
| Hill sampled entries | Identity variants, distinct objects, session fields, access actions | Sampled Margaret Walker Alexander, Kathleen Adams and Sadie Alexander access block; remove unverified claim of 70 identical entries and original chronological order |
| Hill index | Index-to-guide limit | No claim of full transcript index coverage or current permission |

## Attribution and synthesis boundaries

**Ariel Lee** confirmed on 2026-10-30 that the Liu Zhongjing confusion patterns come from Ariel Lee's experience. The table is neither Liu's authored instructions nor his endorsement and is not a fourth book. Retain all 45 numbered pairs for continuity; qualify inherited frequency and review labels because source recordings and per-case evidence are absent. In particular, rows 37, 38, 41 and 43 include semantic expansions or deletion risks and cannot be treated as homophones. Context does not automatically identify 保利 or 河南. Rows mapping a form to itself are spelling reminders.

Modern Mandarin candidate reasoning, chunk registers, strict-verbatim exceptions, speaker-label safeguards, source-bracket provenance and Word/PDF delivery are project adaptations. Some of these were already local user preferences and are now aligned with the core. They are not validated ASR methods taken from the English books.

The English books determine the default explanation language under the construction profile. Original transcript language remains unchanged; explicit user or project language preferences prevail. This revision's conversation with the user remains Chinese.

## Reading, budget and limits

Read bounded source-local slices, clean copies without changing source files, and retain actual ranges and estimated cleaned tokens in reading-ledger.json. Short metadata probes preceded the frozen acceptance suite; substantive source expansion followed it. Some tool outputs were truncated; emitted spans are reported conservatively as upper-bound coverage. No expenditure threshold was approached. Repeated lines and unique line coverage are separate in reading-report.json. PDF image fidelity and inherited claims outside inspected spans remain unverified.

All references stay below their computed planning budgets and hard caps; low length is not a defect to fill with padding. The Hill reference's table may trigger the validator's technical-text heuristic; manually this is a text-heavy finding aid. Its content is also below the stricter text cap. The core is trimmed against its own scaling budget. One worked example per book is retained.
