# Proposal: four toy models, one per module

Status: **draft for review**. Nothing in `cohort/` has changed yet. Only
Chapter 1 has been edited, to state the new goal (see "What you are aiming
at", "Why anyone would bother" and "Where each part ends").

## The idea in one paragraph

The course currently starts from a small attempt made by hand, and that stays
as the entry move. What changes is the destination. Each module now ends in a
**toy model**: the smallest description of a problem that still behaves like
the problem, where every omission is deliberate and can be defended. The small
first attempt and the toy model are both small, but for opposite reasons. The
first is small because the student doesn't yet know what matters. The toy is
small because they do.

The goal is not to produce seniors. The goal is to change *why* a student goes
and learns something. Instead of asking the agent random questions and
believing the answers, the student writes down what their toy predicts, runs
the agent, and compares. A disagreement is a specific question, and a specific
question is worth learning the answer to. Knowledge is pulled in by the
collision instead of pushed in beforehand.

## The loop every toy runs through

1. **Hold a model**, naive at first. That's fine.
2. **Write the prediction down** before the agent runs, on paper.
3. **Run the agent, or open the fixture.** This is "reality".
4. **Compare.** A gap means the agent is wrong, or the model is missing a
   degree of freedom, or the model kept one that doesn't matter.
5. **Revise the model**, and go back to step 2.

Owning a toy, rather than having heard of it, is tested the same way every
time: **put back something the toy left out, and predict what changes.**

---

## Module 1 (The spec is the work): the open decisions

**The model.** A specification that leaves *n* decisions open, each with *k*
reasonable answers, is satisfied equally well by *kⁿ* different builds. The
builder picks one. An agent tends to pick the most common answer to each open
decision, so it matches what you wanted exactly as often as what you wanted is
typical.

**Degrees of freedom.** How many decisions are open (*n*); how many reasonable
answers each has (*k*); how unusual your wants are.

**Left out on purpose.**
- *Decisions interact, so some combinations are impossible.* That lowers the
  count but doesn't change how fast it grows.
- *The builder could ask.* In sessions 1–2 they may not, by rule, and agents
  mostly don't.
- *Some wrong guesses cost more than others.* True, and it matters. It's Module
  4's subject.

**Regimes.** If your wants are typical, a vague spec "usually works"
(Chapter 3's disconcerting result) because the agent's default is your answer.
If even one want is unusual, that decision has to be closed in writing, or it
will come back wrong. Nothing will flag it, because the result still meets the
spec.

**The prediction, on the existing fixture.** `brief-01-shelf.md` names five open
decisions itself: what "something" is, what "on the shelf" means for a book on
loan, who uses it, simultaneous updates, and whether "mostly bring them back"
is a problem to solve. Even at two answers each, that's 2⁵ = 32 builds that
all meet the brief. Before session 2, the student marks which of their own
answers are unusual and predicts which decisions the agent will get "wrong".
`agent-output-01.md` is the collision.

**What it pulls in.** You can only close a decision you know exists. The
student's questions change from "can you build this?" to "what decisions does
a lending shelf involve?" That's domain knowledge, sought for a reason.

**Ownership test.** "The builder may ask you exactly one question. Which one
do you want it to be?" The right answer is the decision where the student's
want is least typical.

---

## Module 2 (The known-answer test): loud rows

**The model.** An average shares every row's size equally among all rows.
One row that is wrong by *M*, in a list of *N*, moves the average by about
*M* ÷ *N*. The median barely moves until about half the rows are bad.

**Degrees of freedom.** List length (*N*); how many rows are wrong; how wrong
each one is (*M*).

**Left out on purpose.**
- *The shape of the distribution.* It doesn't change *M* ÷ *N*.
- *Which summary is "right".* That depends on the question, which is Module 1's
  business.

**Regimes.** When *M* ÷ *N* is large, the answer is visibly absurd, but only to
someone who expected something. When it's small, the error is invisible in the
result and can only be found by looking at the data (Chapter 7). The toy states
its own limit: *small errors can't be caught at the output, only at the
input.*

**The prediction, on the existing fixture** (instructor numbers, from
`cohort/fixture/README.md`, verified). `attendance.csv` holds the ages of
13–15-year-olds, so the prediction before running is "about 14". The naive
mean comes back as **40.38**. The toy recovers that number from the honest
one:

- the `999` pushes the mean up by (999 − 14) ÷ 37 ≈ 26.6;
- the blank, read as 0, pulls it down by 14 ÷ 37 ≈ 0.4;
- the duplicate is a normal age and moves it almost nothing;
- so 14.14 + 26.6 − 0.4 ≈ **40.4**.

A student who can derive 40.38 from 14.14 and the list of problems owns the
toy. A student who just found the 999 has fixed one file.

**What it pulls in.** Mean against median; what a blank becomes inside a
program; why the duplicate is the dangerous one here (it's invisible in the
result, and only visible in the data).

**Ownership test.** "Suppose ten of the 37 ages had been blanks read as 0.
Would you catch it from the average alone?" The average drops by about
10 × 14 ÷ 37 ≈ 3.8, to about 10.3. That's borderline: plausible for a
different class, absurd for this one. The honest answer depends on what you
expected, which is the point.

---

## Module 3 (Comparing fairly): how big luck is

**The model.** Across *n* yes/no trials, luck moves a percentage by roughly
50 ÷ √*n* points either way. Between two groups of *n* each, a gap smaller than
about **100 ÷ √*n* points** is the kind luck produces routinely. A real
difference keeps its size as *n* grows. Luck shrinks like 1 ÷ √*n*.

**Degrees of freedom.** Trials per group (*n*); the gap; **how many times you
looked**.

**Left out on purpose.**
- *Rates far from 50%.* At a 25% base rate the spread is about 87% as wide.
  The numbers shift, the shape doesn't.
- *Unequal group sizes, exact tests.* Also numbers, not shape.

**Regimes.** Below the threshold, the comparison says nothing. Above it, the
comparison might mean something, **if you decided *n* before you looked.**
Look repeatedly, and some look will eventually show a gap above the threshold
by luck alone.

**The prediction, on the existing fixture** (verified against
`ab_test_log.csv`, which has no real effect by construction). Before opening
it: 400 trials is about 200 per variant, so any final gap under 100 ÷ √200 ≈
**7 points** means nothing. Commit to that. Then peek, as sessions 7–8 already
intend:

| trials seen | A | B | gap | toy threshold |
|---|---|---|---|---|
| 80 | 12.2% | 33.3% | 21.1 | ~16 |
| 160 | 16.5% | 41.3% | 24.8 | ~11 |
| 240 | 23.8% | 35.5% | 11.7 | ~9 |
| 320 | 23.6% | 34.2% | 10.6 | ~8 |
| 400 | 27.1% | 32.4% | 5.3 | ~7 |

At 160 trials the gap clears the threshold easily. That's the collision, and
it's supposed to happen: the toy was missing its third degree of freedom, the
number of looks. The revised toy predicts that a real effect holds around 25
points while luck shrinks, and the table shows it shrinking. The final 5.3 is
under 7. Nothing, as constructed.

**What it pulls in.** Square roots, and why randomness adds up more slowly than
size; why the stopping rule has to be fixed in advance.

**Ownership test.** "You want to detect a 2-point difference. How many trials
per group?" 100 ÷ √*n* = 2 gives *n* = 2,500. Small effects are expensive, and
the toy says how expensive before anyone runs anything.

---

## Module 4 (Answering for it): the long chain

**The model.** A job of *k* steps, each right with probability *p*, comes out
entirely right with probability *pᵏ*. Twenty steps at 95% gives about **36%**;
at 99%, about 82%. A check that catches errors after a step starts the count
again from there.

**Degrees of freedom.** Chain length (*k*); per-step reliability (*p*); where
the checks sit.

**Left out on purpose.**
- *Steps aren't independent.* Correlated errors change the number, but not the
  lesson that length works against you.
- *Some errors are harmless.* Deciding which errors matter is the
  specification's job (Module 1) and exactly what Chapter 11 says checking
  can't see.
- *Checks aren't perfect.* A check that misses errors is modelled as a longer
  chain.

**Regimes.** Short chains: "usually right" is good enough. Long chains: even at
95% per step, the whole job is more likely wrong than right after 14 steps
(0.95¹⁴ ≈ 0.49). This is why an agent that is right ninety times in a row
(Chapter 1's last line) can still hand you a broken result.

**The prediction.** Before signing anything (Chapter 12): count the steps in
what was delegated, estimate *p*, write down the chance the whole thing is
right, and decide where the checks go. The orders fixture fits as the
collision. 200 orders became 169 deliveries, which is what a four-step delivery
chain at about 96% per step produces. And the analysis chain (read, join,
average) had a step that "succeeded" while silently dropping the 31 orders that
never arrived.

**What it pulls in.** Multiplying probabilities; independence; where
verification is worth its cost.

**Ownership test.** "You can afford two checks on a 20-step job. Where do they
go?" After the least reliable steps, or spread out to break the chain into
thirds. Either answer is defensible, and the defence is the test.

---

## Why these four

- Each can be worked by hand in minutes, by a 13-year-old, with no algebra
  beyond a square root.
- Each has a threshold where the situation changes kind. That's what makes
  them toys and not formulas.
- Three of the four predict a **verified number in a fixture the course
  already has**, so no new fixtures are needed. The fourth (open decisions)
  predicts qualitatively, against `agent-output-01.md`.
- Every one replaces "is this right?" with a question the student can go and
  answer.

## What adopting this would change (not done in this draft)

- **Vocabulary.** Chapters 5–7 and sessions 4–6 say "toy case" for the small
  known-answer case, which is the *entry* end. With "toy model" as the
  destination, one word would name both ends. Proposed rename: "small case"
  (e.g. Chapter 6 "Running It on the Small Case", Chapter 7 "When the Small Case
  Passes Anyway").
- **Sessions.** The last session of each module (3, 6, 9, 12) gets a toy block:
  work the toy by hand, write down the prediction, collide with the fixture.
- **Rubric.** A dimension for *predicts before running* and *can defend what
  the model leaves out*, or a reworking of an existing one.
- **Capstone.** "Defend it" becomes "reduce it and defend it": give the toy
  model of a problem, justify every omission, predict the full build before
  seeing it.
- **Cohort subtitle.** Currently "Do it by hand first, then delegate it, then
  find out what you forgot to ask for." It could gain a fourth clause about
  what the small version predicts.
- **Tooling.** If the toy block needs its own field in `sessions.yaml`, that
  change belongs upstream in cohort-kit, not here.
