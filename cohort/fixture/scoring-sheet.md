# Pilot scoring sheet

The pilot commits to measuring four things. This is the instrument. Run it
identically in session 1 and session 12, by the same assessor, ideally
without that assessor knowing which sitting they are marking.

## 1. Unaided spec-and-verify

Twenty minutes, no agent, pen and paper. Given `brief-01-shelf.md`:

| | 0 | 1 | 2 |
|---|---|---|---|
| States what "done" means | Not stated | Vague | Checkable |
| Names an ambiguity in the brief | None | One | Two or more |
| Describes a result that meets the spec and is still wrong | No | Generic | Specific |
| Says what was deliberately left out | No | — | Yes |

## 2. Planted-error catch rate

The headline number. Give the child an agent output containing exactly one
planted defect and the spec it was built from. Ten minutes.

Record, per item: **caught / not caught**, and time taken.

Use a different defect of the same class at the end, never the same one.
Classes, in the order they appear in the curriculum: an unstated decision
silently made; a computed number that was asserted rather than computed; a
result that passes every stated test and fails an unstated need; a
comparison that is not like-for-like; a chart whose axis does the arguing;
a dataset missing the rows that matter.

> Report this as a **rate across items**, not a pass/fail per child. The
> pilot's question is whether the rate moves, and a per-child verdict
> answers a question nobody asked.

## 3. Oral defence

Scored against the capstone rubric by an external practitioner, blind to
whether this is the first or last sitting. Five minutes, two follow-up
questions minimum, at least one of which the child cannot have prepared for.

## 4. Whether they choose the unaided path

The motivation question, observed rather than surveyed.

In sessions 3, 7 and 11 the exercise is available in two forms — one where
the hand-done phase is required and one where the agent is unlocked from the
start — and the choice is the child's, made privately, with no adult
reaction either way.

Record only the count. Do not record who.

---

**Decision at the end:** expand to all three tracks, or redesign the modules
that did not move the unaided numbers. Measures 1 and 2 are the unaided
numbers. Measure 4 is the one the proposal expects to be hardest, and the
one most likely to say something uncomfortable.
