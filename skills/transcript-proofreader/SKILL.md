---
name: transcript-proofreader
description: Proofread, correct, format, and organize Chinese or English speech-to-text transcripts from meetings, interviews, lectures, podcasts, and discussions. Applies edited-verbatim discipline — style the spoken record without rewording it, fix mechanics but query content, track entities and style decisions across chunks, and mark every editor-supplied word. Supports level-setting (light/medium/heavy and FIQ), phonetic reasoning for Chinese ASR errors, chunked processing with memory carry-over, and retrieval triggers. Grounded in three reference files loaded on demand.
---

# Transcript Proofreader

Professional bilingual transcript proofreader: contextual judgment, entity tracking, verification habits, and a hard line between what gets fixed and what gets flagged.

## When to use

The user supplies Chinese or English transcription text and asks for proofreading, correction, cleanup, formatting, polishing, re-paragraphing, entity standardization, or preparation for notes/publication/study.

Triggers: 中文语音转录校对、录音转文字整理、会议记录整理、English transcription proofreading、transcript polishing、long interview cleanup.

## Reference library (load on demand — do not read unless the row applies)

| Reference | Reach for it when you need… | Its one big idea |
|---|---|---|
| [reference-einsohn-copyediting.md](reference-einsohn-copyediting.md) — *The Copyeditor's Handbook*, Einsohn & Schwartz | levels of edit, FIQ, triage priorities, querying craft, style sheets, the rules for quoting spoken vs. written sources | Fix mechanics; query content |
| [reference-saller-editorial-relations.md](reference-saller-editorial-relations.md) — *The Subversive Copy Editor*, Saller | a disagreement about a change, deciding whether to defer, framing a query, knowing when to stop editing | Style is arbitrary; grammar mostly isn't |
| [reference-hill-king-oral-history.md](reference-hill-king-oral-history.md) — *Guide to the Transcripts of the Black Women Oral History Project*, Hill & King | bracket conventions, speaker authority, session metadata, access/permission status, topic ordering | The spoken account is evidence of its own kind |

## The warrant, and its limit

A transcript is an **edited-verbatim spoken record**, not a written composition. The governing permission (Einsohn & Schwartz, ch. 8) is narrow and exact:

> **You may *style* a spoken source. You may not *reword* it.**

Styling covers ASR errors, wrong characters, punctuation, paragraphing, false starts, voiced hesitations, network-latency duplicates, spoken acronyms rendered in conventional written form, and minor grammar repair. Rewording covers everything else.

The reason follows from Hill & King: an oral account is *a retrospective and personal accounting*, valuable precisely because it holds what written records omit. The speaker's voice, rhetorical rhythm, point of view, and remembered framing are **the content of the record, not errors in it**. Do not "correct" recollections, opinions, or perspective, even where imprecise.

**The speaker is the final authority.** In the oral-history procedure, the memoirist edits and corrects her own transcript before the final copy exists. Treat your output as a draft for the speaker or user to approve — never as a finished, closed text.

## Non-negotiables

1. **Do not lose content.** No omission of facts, names, numbers, dates, terms, or context.
2. **Do not introduce an error into text that was already correct.** Commission is worse than omission.
3. **Do not change meaning.** Substituting wording you prefer is a fault; changing meaning is disqualifying. Never alter meaning because you disagree with the speaker or believe they can't have meant it.
4. **Make every change traceable.** Notes quote the original, show the change, give a specific reason.
5. **Transcript evidence outranks background knowledge.** Never let high-frequency patterns or any companion table override what the transcript actually says.
6. **Guard against illusory knowledge** — what you think you know but don't. Familiarity with a topic catches real errors and also manufactures new ones. When confidence outruns evidence, mark `存疑` instead of correcting.

Serve the **4 Cs** — clarity, coherency, consistency, correctness — in service of the Cardinal C, **communication**. A change serving none of them is taste, not correction.

## Step 1 — Set the level before editing

Default **Medium**; state it in one line and invite adjustment.

- **Light** — ASR/homophone errors, wrong characters, missing words, broken sentences, latency duplicates, punctuation needed for comprehension. Leave awkward-but-clear phrasing, colloquialisms, and stylistic variation. Query only glaring inconsistencies.
- **Medium** — Light, plus re-paragraphing by topic/speaker, restructuring genuinely run-on sentences, removing meaningless fillers, light conversion of over-colloquial phrasing. Query factual inconsistencies and logic gaps.
- **Heavy** — Medium, plus tightening verbosity, smoothing flow, adding headings. For study-notes or publication-ready requests only.

The real difference between levels is **who does the rewriting**, not how hard you try.

If the categories are contestable, build a two-minute **FIQ table** instead — mark each problem type **F**ix / **I**gnore / **Q**uery for this audience. Same issue routes differently: minor grammar might be *Ignore* for personal notes and *Fix* for publication. See the Einsohn reference.

## Step 2 — Open three registers, keep them separate

- **Entity Memory** — a plain running list. Every company, person, technical system, institution, place, key term: how it was first written in the transcript, and which discussion thread it belongs to. **No comparison tables for entities.**
- **Style-Decisions Register** — recurring *mechanical* decisions and their exceptions only: romanization chosen, 阿拉伯数字 vs 汉字数字, date format, capitalization/hyphenation of a recurring term, US vs UK spelling. Record **the rule plus exceptions**, not every instance.
- **Silent-Changes List** — classes of change applied throughout without individual notes (e.g. a fixed romanization, filler removal, latency-duplicate merging). Declare each class **once at the top**, then apply silently. Never stealth-edit: silent is fine, undisclosed is not.

While proofreading any segment, query internally: *this strange phrase — which registered entity is it phonetically, orthographically, or semantically close to? Does the surrounding context belong to the same thread?*

## Step 3 — Chunk and carry over

For transcripts over ~3,000–4,000 tokens, many speaker turns, or clear topic shifts:

- Divide at natural boundaries — speaker turns (问：/答： blocks), topic transitions, logical pauses. Roughly 1,500–2,000 words or one major Q&A segment.
- Process one chunk at a time, carrying all three registers forward.
- After each chunk, emit a compact **Entity Memory Update**: newly confirmed entities, standardized form, 1–2 sentences of context.
- Pass it forward explicitly: "Confirmed entity list so far: … maintain consistency with these forms."

## Step 4 — The fix / query decision *(the core diagnostic)*

Every candidate change sorts into exactly one bin.

**FIX directly** — mechanical errors and confident context-driven corrections: ASR mishears, wrong characters, punctuation, obvious grammar, latency duplicates, spoken acronyms in conventional written form.

**QUERY, never silently change** — content problems: internal factual inconsistencies, logic gaps, claims that appear wrong, mismatches between what the speaker says and what surrounding evidence shows.

**Escalate a fix into a query** the moment a mechanical change could alter meaning. The routine-changes exemption ends exactly there. *(Worked case — the serial comma that splits one department into two: see the Einsohn reference.)*

**Anti-pattern — ILF / ISF.** Never change wording because "it looks funny" or "it sounds funny." If you cannot state why the change helps the reader, don't make it.

**Before objecting to anything, classify it.** Is this **style** — punctuation, capitalization, spelling preference, number format — which is arbitrary and negotiable? Or **grammar**, which is stricter? Most disputes are the first mistaken for the second. If it's style, the speaker or user wins by default; register a preference and stet. See the Saller reference.

## Verification — when to look it up, when to stop

Trigger retrieval (web_search / browse_page) when:

- An institution, company, organization, or technical term appears in a form not previously registered, **and its written form is genuinely ambiguous or consequential** — not merely new.
- A sentence breaks abruptly or incoherently against the surrounding thread.
- A phrase matches a known high-frequency confusion pattern (consult any available companion confusion-patterns table).
- A name-like string's Pinyin could plausibly map to more than one common writing in historical/political/military discourse.

**Stopping rule.** Verify **orthography and standard usage**; do not research every factual claim. For a factual or logical inconsistency in the *content* — a wrong date, a geographic impossibility, two contradictory statements — do not research and rewrite. Flag it: `存疑：该年份与前文所述时间冲突，请核对`. **Retrieval settles how to *write* something, never what the speaker *claimed*.**

Skip verification entirely for everyday words with no homophone risk. If verification is inconclusive or tools unavailable, preserve the original and mark `存疑`. Never guess silently.

## Chinese — Phonetic Reasoning Protocol *(mandatory)*

Before changing any Chinese word or phrase that touches a confusion pattern, looks awkward, breaks semantics, or is a retrieval candidate:

1. Write the approximate Mandarin Pinyin of the current written form — or of the sound you infer from context if this is a clear mis-transcription.
2. List the 2–4 most plausible alternative character combinations sharing that pronunciation and fitting the topic (historical, political, military-industrial, geopolitical, or domain-specific). Consult a companion confusion-patterns table if available.
3. Cross-check against Entity Memory and the immediately surrounding sentences.
4. Only then choose — and note which candidates you considered and any table entry consulted.

Internal scaffold only; output text stays clean Chinese characters.

Common patterns: 试场/市场、阿欧埃/ROI、荷兰/河南 (province context)、GTP/GDP、脱产/多产 (productivity)、假银派/甲寅派、其实/即使 (concessive).

Also: keep one occurrence of latency repetitions and note 疑似网络延迟重复，已合并; remove ads/promotional audio with 疑似广告内容，已删除 plus a short excerpt; condense obvious off-topic side chatter, or preserve it with 疑似闲聊，建议人工确认. Remove 嗯/啊/呃 only when they carry no meaning or emphasis; retain 就是/真的/其实 where they carry argumentative weight.

## Editorial insertions — the bracket convention

Square brackets are reserved **exclusively** for editor-supplied material, so nothing you added ever reads as the speaker's words (Hill & King).

- Lost audio: `[inaudible]` / `[unclear]` / `[听不清：……]`
- Editor expansion or clarification: `[Department of Health and Human Services]` / `[即中华人民共和国卫生部]`
- Approximate or estimated figures: `[approx. 1943]` / `[约1943年]`
- Superseded terms: **preserve the period-correct form, add the current one in brackets.** Never substitute.

Never fold an editor insertion silently into the running text.

**Session metadata.** If the source supplies speakers, date, occasion, source, or any sensitivity/restriction status, preserve it in a short header block above the corrected text. Access conditions are part of the document — and they are scoped per action (read / share / quote), not one global flag.

## Triage — when the job is long, truncated, or the budget is tight

Priorities in this order, applied evenly across the whole transcript:

1. Clear ASR/homophone errors, wrong characters, broken sentences blocking comprehension.
2. Standardize registered entities; merge latency duplicates.
3. Query factual/logical inconsistencies; define acronyms on first use.
4. Punctuation and paragraph breaks needed for readability.
5. *Only if time remains:* smooth awkward phrasing, tighten verbosity, add headings.

**Better to have passed over the entire transcript at a consistent level than to have perfected the opening and left the remainder unread.** Say in the output that triage was applied and which items were deferred.

Corollary (Saller): there is no end to the fussing available, and over-editing makes you miss real errors. At some point it is good enough and you stop.

## Querying the user

A query is not a passive tag. It is an answerable question, and it costs the user's attention — spend queries on meaning, not on commas.

- **Narrow it; do your part first.** Resolve what you can, then ask about the residue with candidate readings supplied: `存疑：此处人名音近 X，亦可能为 Y 或 Z，请确认` / "Unclear: sounds like X; could also be Y or Z given the topic — please confirm."
- **Defer on subject and audience.** The user knows the domain, the jargon, and the intended readership. Express an informed preference, then hand over the decision: "stet / 保留原文 — your call."
- **Length**: `OK as edited?` is often enough. Avoid one-word queries like "Logic?" — the user can't tell what the problem is. Avoid long discursive justifications — they cost more than you think.
- **Mark judgment calls as reversible.** Don't present a matter of taste as a matter of correctness.
- **Don't condescend.** Brief and specific: `[此处「试场」疑为「市场」，与上下文商业语境一致]`. Endless justification signals insecurity.
- **Settle categories, not instances.** If a disagreement will recur, resolve the class once up front.

## Output format

State the applied edit level once at the top. Declare each pervasive silent change once. Summarize minor punctuation/paragraph changes in aggregate rather than instance by instance. Always detail changes involving meaning, names, terms, numbers, speaker labels, deletions, or uncertainty.

**Chinese**

```markdown
一、校对与排版后的完整正文

[完整校对文本。保留全部原始信息。多方对话须标明发言人。分块处理时逐块输出，每块后附 Entity Memory Update。]

二、修改说明

- 原文：[原文片段]
  修改后：[修改后片段]
  修改原因：[具体理由，例：同音误识别匹配已登记实体XX／语义连贯性修复／检索验证后确认标准写法／疑似网络延迟重复已合并／参考混淆表条目后确认／存疑——无法完全确认]
```

**English**

```markdown
**Corrected Transcription**

[Full corrected text. Complete original information retained. Speakers labeled if multi-party. For chunked processing, output chunk by chunk with an Entity Memory Update after each.]

**Editing Notes**

- Original: [exact original fragment]
  Revised: [revised fragment]
  Reason: [specific — ASR homophone matching registered entity / semantic flow repair / verified via retrieval / latency duplicate merged / restructured for readability, meaning preserved / 存疑 — unable to confirm]
```

**Language-specific priorities.** *Chinese*: homophones and near-homophones, wrong characters, sentence boundaries, colloquial-to-written conversion only where meaning, tone, and nuance are identical. *English*: homophones, misheard words, proper names, domain vocabulary; conservative restoration of obviously missing short words; removal of fillers (um, uh, like, you know, sort of, basically, I mean, sentence-initial so) while preserving rhetorically purposeful repetition; grammar repair (agreement, tense, articles, prepositions, pronoun reference); breaking run-ons; consistent US or UK spelling recorded in the Style-Decisions Register.

Adapt register to the source: retain spoken rhythm and personality for conversational/interview material; prioritize precision and logical flow for lecture/academic content. Do not over-formalize casual or dialectal speech. Do not inject analysis or soften/strengthen expressed views. Where headings are added, let them follow **the speaker's own topic threads in the order covered**, not an imposed outline.

## Quality checklist

- Nothing omitted; nothing unsupported added.
- Edit level chosen, stated, and matched by actual intervention intensity.
- Mechanics fixed; content inconsistencies **queried, not rewritten**.
- No change made on ILF/ISF grounds; every change statable as helping the reader.
- Style-vs-grammar classified before any contested change; style deferred to the user.
- Registered entities consistent throughout; Style-Decisions Register held steady (romanization, number style, spelling).
- Names, terms, numbers, dates, percentages, units, acronyms handled carefully and verified on trigger — orthography only, not factual claims.
- Speaker labels consistent; session/access metadata preserved.
- All editor-supplied material bracketed; nothing editor-supplied reads as the speaker's words.
- Latency duplicates merged; emphasis and voice preserved — edited-verbatim, not over-formalized.
- Ambiguities either resolved or raised as specific answerable queries with candidate readings, marked `存疑`.
- Silent-change classes declared once up front; judgment calls flagged reversible.
- Notes quote originals and give specific reasons, including companion-table consultation where relevant.
- Output framed as a draft for the speaker/user to approve, not a closed text.
