# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **Flattened to the repository root.** `SKILL.md` and `references/` now sit at the
  top level instead of under `skills/transcript-proofreader/`, matching the layout
  used across the other skill repositories: the repository root *is* the skill root,
  so it can be cloned straight into a skills directory. The README's install, zip
  and SDK sections were rewritten to match.
- Moved the three reference files into `references/`, per the Agent Skills
  convention. The routing table in `SKILL.md` and the layout block in `README.md`
  follow the new paths; no file contents changed.

### Fixed

- `validate-skill.yml` sat at the repository root, where GitHub Actions never runs
  it, while `README.md` already documented it at `.github/workflows/`. Moved there.
- The `git clone` command in the README used a `<your-username>` placeholder and
  failed on copy-paste; it and the changelog links now point at the real repository.
- Added the `.gitignore` the layout block already listed.
- The layout block omitted `NOTICE.md`.

### Planned

- A companion confusion-patterns table as a fourth reference file, keyed by domain
- Worked before/after examples for each edit level
- Coverage for speaker-diarization errors (turns attributed to the wrong speaker)

## [1.0.0] — 2026-07-23

Initial public release.

### Added

- `SKILL.md` — the transcript-proofreading skill, bilingual (中文 / English)
  - The edited-verbatim warrant and its limit: style a spoken source, do not reword it
  - Six non-negotiables, including commission-over-omission and the guard against illusory knowledge
  - Step 1 — level-setting (Light / Medium / Heavy) with an FIQ fallback for contestable categories
  - Step 2 — three separate registers: Entity Memory, Style-Decisions Register, Silent-Changes List
  - Step 3 — chunking with explicit Entity Memory Update carry-over
  - Step 4 — the fix / query decision, with escalation when a mechanical change could alter meaning
  - Chinese Phonetic Reasoning Protocol — mandatory Pinyin-candidate enumeration before character changes
  - Verification triggers and a stopping rule: retrieval settles orthography, never factual claims
  - Bracket convention for all editor-supplied material, plus session and access metadata handling
  - Triage priority order for long, truncated, or budget-constrained jobs
  - Query craft — narrow, reversible, non-condescending, categories settled once
  - Output templates for both languages, and a closing quality checklist
- `reference-einsohn-copyediting.md` — levels of edit, FIQ, triage, querying, style sheets, quoting spoken sources
- `reference-saller-editorial-relations.md` — style vs. grammar, deference, stet, knowing when to stop
- `reference-hill-king-oral-history.md` — bracket conventions, speaker authority, session metadata, topic ordering
- `README.md`, `LICENSE` (MIT), `.gitignore`, and an optional skill-validation workflow

[Unreleased]: https://github.com/ariel-lee-1023/transcript-proofreader/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ariel-lee-1023/transcript-proofreader/releases/tag/v1.0.0
