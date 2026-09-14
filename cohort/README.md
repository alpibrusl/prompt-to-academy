# The Builders cohort

Twelve weeks, four modules, ages 13–15, 8–12 per cohort.

Source is three files plus fixtures. Everything else is built.

```
cohort.yaml    identity and format
sessions.yaml  the twelve sessions
rubric.yaml    the five dimensions the capstone is judged on
fixture/       the material the exercises run on, errors included
```

## The module shape

Every session runs the same arc, and the order is not negotiable:

**fail by hand → name the concept → learn the question → delegate and verify**

The failure comes first so the question is a memory rather than a ritual. A
checklist handed to someone who has never been burned gets run, passes, and
teaches the performance of diligence without any of it.

This is enforced rather than trusted. `cohortkit check` refuses to build a
non-capstone session with no `by_hand`, and refuses `ai_mode: answer` on any
session that has no hand-done phase to unlock. It is a build failure because
it is the first thing dropped by a facilitator running forty minutes behind,
and a session that dropped it looks exactly like one that never had it.

## Modules

| # | Module | Sessions | Ends on |
|---|---|---|---|
| 1 | The spec is the work | 1–3 | prose against program |
| 2 | The known-answer test | 4–6 | the five questions, on your own work |
| 3 | Comparing fairly | 7–9 | three honest charts |
| 4 | Answering for it | 10–12 | the capstone defence |

## AI mode by session

| Session | Mode | Why |
|---|---|---|
| 1 | `none` | the spec fails against a person first, visibly |
| 2–3 | `answer` | unlocked; the hand-done phase is behind them |
| 4 | `none` | the toy case must be built by someone who knows the answer |
| 5–6 | `answer` | |
| 7 | `none` | forty coin flips, by hand, no substitutes |
| 8 | `tutor` | an agent in answer mode explains optional stopping and the experience is lost |
| 9–10 | `answer` | |
| 11 | `tutor` | no agent during the accounts |
| 12 | `answer` | full delegation, every delegation audited |

## The three choice sessions

Sessions 3, 7 and 10 offer the exercise in two forms — hand-done first, or
agent unlocked from the start. The choice is the child's, made privately,
with no adult reaction either way.

This is the pilot's fourth measure, and it is the one the proposal expects
to be hardest: whether a fourteen-year-old takes the unaided path when the
shortcut is in their pocket. Record the count. Do not record who, and do not
react.

## Running it without a room

`--home` renders the same twelve sessions for one adult and one child. It is
not the self-paced build with a second person: a pair is a real room and can
run a scaled-down version of most live segments, so each session carries an
`at_home` restatement and — more importantly — `parent_notes`, the follow-up
question for an adult who cannot judge whether the answer is correct.

See [`../home/`](../home/).
