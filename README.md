# prompt-to-academy

**Prompt to Judgement** — a book, and the cohort curriculum derived from it.

Teaches children to use AI productively and safely by first making them do
the thing themselves, small and by hand, and only then letting them delegate
it and check the result.

```
book.yaml + chapters/   the book        → bookkit   → EPUB / PDF
cohort/                 the curriculum  → cohortkit → four documents
```

Nothing in `build/` is committed. The book is the source; the EPUB is an
artifact. The curriculum is three YAML files; the handout is an artifact.

> **Two licences.** The manuscript in `chapters/` is
> [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/); the cohort
> curriculum, the fixtures and the tooling are [EUPL-1.2](LICENSE). GitHub
> shows only the second; [`COPYING.md`](COPYING.md) is the authority.

## Build it

```bash
pip install "content-kit-core @ git+https://github.com/alpibrusl/content-kit@main#subdirectory=packages/core"
# Until cohort-kit#12 lands, from the branch rather than main: this
# curriculum uses by_hand, verify, ai_mode, module, at_home and
# parent_notes, and --home does not exist on main yet.
pip install "cohortkit @ git+https://github.com/alpibrusl/cohort-kit@claude/book-portal-app-proposal-zu2i02"

cohortkit check cohort --book-path .              # gates CI

cohortkit build cohort --out build --book-path .              # handout + facilitator guide
cohortkit build cohort --out build --book-path . --home       # family guide
cohortkit build cohort --out build --book-path . --self-paced # self-paced handbook
```

> **Why the branch, and not `main`.** Installing from `main` today does not
> fail loudly, which is exactly the problem: `cohortkit build --home` errors,
> but `cohortkit check` *passes* — the schema does not forbid unknown fields,
> so all six are dropped silently. That is a green check on a curriculum
> where nothing verified that a session has a hand-done phase. Use the branch
> until [cohort-kit#12](https://github.com/alpibrusl/cohort-kit/pull/12) is
> merged, then switch back.

`--book-path .` embeds each session's real chapter text into the document,
collapsed under that session. A child needs the one HTML file and nothing
else — no PDF, no EPUB, no login, no account, nothing fetched at runtime.

## Four documents, one source

| Document | For | Carries |
|---|---|---|
| `handout.html` | the child | everything except the traps and the notes |
| `facilitator-guide.html` | a practitioner running a cohort | `facilitator_notes`, the `verify` traps |
| `family-guide.html` | **one adult, one child** | `at_home`, `parent_notes`, the traps |
| `self-paced-handbook.html` | a reader alone | `solo`, traps behind a spoiler |

The family guide is the one to read first if you are a parent. See
[`home/`](home/).

## What is here, and what is not

**Built:** the twelve-week **Builders** pilot (ages 13–15) — the cohort the
proposal specifies, in full. Twelve sessions, four modules, five rubric
dimensions, the fixtures the exercises actually run on, and the pilot's own
measuring instrument.

**Not built:** Explorers (10–12) and Founders (16–18). Deliberately. The
proposal's own decision gate is *"expand to all three tracks, or redesign
the modules that did not move the unaided numbers"* — writing all three
before the pilot reads out would be answering a question the pilot exists to
ask. They get their own `cohort/` directories when there is evidence.

## What this repo decided

The proposal left five things underdetermined or in tension. Each was
resolved here rather than left for a facilitator to discover live.

**Twelve weeks, four modules, but seven Builders modules were listed.**
Resolved as twelve weekly sessions in four modules of three — not by
discarding three of the seven, but by folding them in. *Make it compute*
joins module 1; *measuring what you did* and *a chart is a claim* join
module 3. Nothing listed is dropped.

**Tutor mode is the default, but the first AI lesson requires answer mode.**
"Catch it being confidently wrong" cannot happen against an agent that
withholds answers. Resolved with a per-session `ai_mode` (`none` / `tutor` /
`answer`) that states the setting in every document, and a build rule that
refuses `answer` on a session with no hand-done phase. The unlock is a rule,
not a mood.

**Accountability is a principle for every track but appears only in
Founders.** Session 11 makes it explicit for Builders at their scale — a
staged failure of their own earlier work, accounted for out loud, unprepared.

**"Nothing produced unsupervised counts" conflicts with the review
portfolio,** which is produced unsupervised. Resolved: the trace record is
not itself graded. It is the *subject* of the live defence — the panel reads
it and asks about it, and the grade attaches to the answers. An unsupervised
artifact used as the material for supervised questioning is not an
unsupervised assessment.

**"Rate at which children catch a planted error" had no instrument.**
Built: [`cohort/fixture/scoring-sheet.md`](cohort/fixture/scoring-sheet.md),
run identically in sessions 1 and 12 by an assessor blind to which sitting
they are marking, plus the planted errors themselves as real files with
verified numbers.

## The delegation trace

Currently paper: [`cohort/fixture/trace-sheet.md`](cohort/fixture/trace-sheet.md),
one per delegation, filled in while working rather than reconstructed
afterwards. Paper is not a placeholder for the pilot — it is slower, and
slow is the point.

The digital version rides the existing `cohortkit progress` channel
(browser-local, JSON export, no server, no account) and is deliberately not
built yet: it changes a wire format students and instructors already
exchange, and the pilot does not need it.

## Privacy

There is no server, no account and no database anywhere in this repo. The
documents are static HTML; progress lives in the reader's own browser and
leaves it only when they click Export and send the file themselves.

That is a design decision rather than a limitation. The proposal promises
children's work stays in an environment the academy controls, and the
cheapest way to keep that promise is to hold nothing.

## Licence

**Two licences**, the same split as the rest of the series. The manuscript in
`chapters/` is [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
— share and adapt with credit, no commercial use. Everything else, including
the cohort curriculum, the fixtures, the family guide and the tooling, is
[EUPL-1.2](LICENSE), matching content-kit and cohort-kit. GitHub shows only the
second; [`COPYING.md`](COPYING.md) is the authority on the split.

In practice: an academy may charge fees and run this curriculum, and a parent
may run it at home, without asking anyone. Selling the book's text is the thing
the manuscript licence excludes.
