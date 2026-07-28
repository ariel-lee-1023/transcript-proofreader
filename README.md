# Transcript Proofreader

> An Agent Skill for proofreading, correcting, and formatting Chinese and English speech-to-text transcripts — with the discipline of a professional copyeditor rather than the enthusiasm of a rewriter.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/type-Agent%20Skill-blueviolet)](SKILL.md)
[![Languages](https://img.shields.io/badge/languages-中文%20%7C%20English-informational)](#)

---

## What this is

ASR output is not a rough draft. It is a **spoken record** that happens to have been damaged in transit. Most AI cleanup tools treat the two as the same thing and quietly rewrite the speaker into a better prose stylist than they were — smoothing the hesitations that carried emphasis, resolving the ambiguities that were the point, and correcting recollections that were never the transcriber's to correct.

This skill draws the line the copyediting profession draws:

> **You may _style_ a spoken source. You may not _reword_ it.**

Mechanics get fixed. Content gets flagged. Everything the editor supplies goes in brackets, and the output is a draft for the speaker to approve, never a closed text.

## What it does

| Capability | Detail |
|---|---|
| **Level-setting** | Light / Medium / Heavy, declared before editing, plus an FIQ table (Fix / Ignore / Query) when the categories are contestable |
| **Fix vs. query** | Mechanical errors are corrected; factual and logical problems are queried with candidate readings, never silently rewritten |
| **Phonetic reasoning** | Mandatory Pinyin-candidate protocol for Chinese ASR errors before any character is changed |
| **Three registers** | Entity Memory, Style-Decisions Register, Silent-Changes List — carried across chunks |
| **Chunked processing** | Long transcripts split at speaker turns and topic shifts, with explicit Entity Memory Updates passed forward |
| **Verification triggers** | Retrieval settles *how to write* something — never *what the speaker claimed* |
| **Bracket convention** | `[…]` reserved exclusively for editor-supplied material; period-correct forms preserved, current forms added |
| **Triage** | An even pass over the whole transcript beats a perfected opening and an unread remainder |
| **Bilingual** | 中文 and English, with language-specific priority lists and output templates |

## Repository layout

```
.
├── README.md
├── LICENSE
├── NOTICE.md
├── CHANGELOG.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── validate-skill.yml      # optional CI: frontmatter + link checks
├── SKILL.md                        # the skill itself
└── references/                     # loaded on demand
    ├── reference-einsohn-copyediting.md
    ├── reference-hill-king-oral-history.md
    └── reference-saller-editorial-relations.md
```

The three reference files are **progressive disclosure**: `SKILL.md` stays small enough to sit in context permanently, and the agent reads a reference only when the situation calls for it.

## Installation

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/ariel-lee-1023/transcript-proofreader.git \
  ~/.claude/skills/transcript-proofreader
```

Restart Claude Code. Use `/skills` to confirm it loaded.

For a single project instead of globally, copy into `.claude/skills/` at the project root.

### Claude.ai / Claude Desktop

Zip the repository directory — the folder itself, not its contents, so that
`SKILL.md` sits at the top level inside the archive:

```bash
cd .. && zip -r transcript-proofreader.zip transcript-proofreader \
  -x '*/.git/*'
```

Then upload under **Settings → Capabilities → Skills**.

### Claude Agent SDK / API

Point your loader at `SKILL.md` and give it read access to `references/`. Keep the two together — the links in the skill's routing table resolve relative to `SKILL.md`'s own directory.

## Usage

The skill triggers on its own when you hand Claude transcription text and ask for cleanup. Nothing to invoke.

```
请帮我校对这份会议录音的转录稿。

[transcript]
```

```
Proofread this interview transcript — medium edit, prepping it for publication.

[transcript]
```

To steer it:

- **`light` / `medium` / `heavy`** — set the intervention level explicitly
- **"personal notes" / "for publication"** — changes how the FIQ table routes borderline issues
- **Supply a confusion-patterns table** — the skill will consult it and say when it did
- **Supply session metadata** (speakers, date, occasion, access restrictions) — it will be preserved in a header block and scoped per action

### What it will refuse to do

It won't tighten a speaker's argument, resolve their contradictions, or make them sound more articulate than the recording does. Those come back as queries. If you actually want a rewrite, ask for a rewrite — that's a different job, and the skill will tell you so.

## Design principles

1. **Fix mechanics; query content.** The whole skill is machinery for keeping those two apart.
2. **The speaker is the final authority.** Output is a draft for approval, following the oral-history procedure where the memoirist corrects her own transcript before a final copy exists.
3. **Point of view is the deliverable**, not noise to be filtered. An oral account is *a retrospective and personal accounting*, valuable precisely because it holds what written records omit.
4. **Style is arbitrary; grammar mostly isn't.** Classify before objecting. If it's style, the user wins by default.
5. **Never stealth-edit.** Silent is fine; undisclosed is not. Pervasive changes are declared once at the top.
6. **Guard against illusory knowledge.** Where confidence outruns evidence, mark `存疑` instead of correcting.
7. **Stop.** There is no end to the fussing available, and over-editing makes you miss real errors.

## Sources and attribution

The three reference files are **original analytical summaries** written for this skill. They are not reproductions, excerpts, or translations of the works they discuss. Each distills the frameworks, decision rules, and worked examples of a source into a form an agent can act on, with brief attributed quotation only where exact wording carries the argument.

| Reference | Source work |
|---|---|
| `reference-einsohn-copyediting.md` | Amy Einsohn & Marilyn Schwartz, *The Copyeditor's Handbook: A Guide for Book Publishing and Corporate Communications*, 4th ed. (University of California Press, 2019) |
| `reference-saller-editorial-relations.md` | Carol Fisher Saller, *The Subversive Copy Editor: Advice from Chicago* (University of Chicago Press) |
| `reference-hill-king-oral-history.md` | Ruth Edmonds Hill & Patricia Miller King, eds., *Guide to the Transcripts of the Black Women Oral History Project* (Schlesinger Library, Radcliffe College) |

Copyright in the underlying works remains with their respective rights holders. If you want the arguments rather than the operational residue, read the books — particularly Einsohn & Schwartz ch. 8, which is where the styling-not-rewording permission comes from.

## Contributing

Issues and pull requests are welcome. Useful contributions, roughly in order of value:

- **Confusion patterns** — additional Chinese homophone and near-homophone pairs seen in real ASR output, with the domain that produces them
- **Failure cases** — a transcript where the skill rewrote something it should have queried, or queried something it should have fixed
- **English-side gaps** — filler and disfluency patterns not covered by the current priority list
- **Language support** — the architecture generalizes; the phonetic-reasoning protocol does not

Please keep `SKILL.md` lean. New material that isn't needed on every invocation belongs in a reference file, not in the skill body.

## Versioning

[Semantic versioning](https://semver.org/). See [CHANGELOG.md](CHANGELOG.md).

- **MAJOR** — a change to the fix/query line or another non-negotiable
- **MINOR** — new capability, new reference file, new protocol
- **PATCH** — wording, examples, added confusion patterns

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any referenced source books, which remain the property of their respective copyright holders.

