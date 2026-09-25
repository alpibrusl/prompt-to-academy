# The Same Spec, to a Machine

Take the specification that a person just misread. Do not improve it. Hand it, word for word, to an agent.

Something disconcerting happens. It usually works.

## Why that is the difficult part

If agents were unreliable, none of this would need teaching. Unreliable tools train their own scepticism — anyone who has used a flaky printer checks the printer. You learn caution from being burned, and a tool that burns you weekly is a tool you never fully trust.

An agent is not like that. It is right most of the time, across an enormous range of things, at a speed that makes checking feel like an insult. And the failures, when they come, do not look like failures. They look like the successes. Same tone, same structure, same confidence, same plausible detail.

This is the hardest fact in the subject: **you cannot tell a good answer from a bad one by how it reads.** Fluency carries no information about correctness. It never did — a confident person can be wrong too — but with people you had other signals. You knew whether they were an expert. You could see them hesitate. You could hear them say "I think" or "probably" or "you'd want to check that". Those signals have been stripped out, and nothing has replaced them.

## The three ways a machine differs from your classmate

Having watched a person and a machine work from the same instructions, three differences are worth naming.

**It never asks.** Your classmate stopped and said "which side of the bread?" — perhaps with a sigh. That sigh was information. It told you exactly where your spec was thin. An agent asks nothing. It resolves the ambiguity, silently, and moves on, and the resolution is usually reasonable, which is worse than if it were unreasonable, because a bad guess would have been visible.

**It fills gaps with the average.** Where your instructions ran out, the agent supplies the most typical continuation. Not a random one — a *plausible* one, drawn from the enormous middle of everything similar it has seen. This is why the output so often feels almost right. It is the average of a thousand versions of your request, which is a good answer to a question nobody asked, and might not be an answer to yours.

**It is confident in exactly the same way whether it is right or wrong.** There is no tell. There is no equivalent of the hesitation. This is not a flaw that will be fixed next year; the confidence is a property of how the text is produced, not a report on how sure anything is.

## The reflex this should install

You asked for X. Something arrived. It appears to be X.

The question is not *is this right?* — you often cannot answer that by looking, and if you could, you would not have needed to delegate it.

The question is: **what did I not specify, and what did it choose?**

That is a question you can actually answer. Go back to your own words. Find the places where a decision was required and you did not make one. Then look at the output and find what it decided there. Those places are where the errors live, essentially always, because the parts you did specify are the parts it got right.

This reframe is most of the skill. "Check the answer" is advice nobody can act on. "Find the decisions you left open, and go look at what was chosen" is a procedure, and it terminates.

## A worked case: the shelf

Concrete beats abstract, so here is the whole thing once, start to finish, on something small enough to hold in your head.

The brief: *"We have one shelf of books in the room. People take them and mostly bring them back. Right now nobody can tell what is on it without walking over. Make something that fixes that."*

A first spec, written after ten minutes of thought, might say: list every book with title and author; mark a book "out" when someone takes it, with their name; mark it "in" when it comes back; sort alphabetically; show a count; work on a phone; handle the empty shelf.

Hand that to an agent. What comes back is, by every measure the spec supplies, correct. Every line checked off. Six test cases passing — empty shelf, one book, many books, a book taken out, a book returned, two books sharing a title. The tool works. It is ready to use.

Now run the reflex. *What did I not specify, and what did it choose?*

Go back to the spec. It never said who is allowed to mark a book "in" — so the tool let anyone do it, including someone who never had the book, and including someone marking it back before actually returning it. It never said what happens if two people try to take the last copy at the same moment — so the tool does not handle that at all, because nothing asked it to. And it never said how a book gets *onto* the list in the first place, which is not an edge case — it is the ordinary first day of using the thing, and the spec walked straight past it.

None of that is the agent's fault, and none of it shows up by re-reading the output. It shows up by re-reading the *spec*, and asking, for every decision the finished tool is now visibly making, whether that decision was ever actually yours to make.

The second spec adds four sentences the first one did not have: who may change a book's status; what happens on a simultaneous claim; how new books get added, and by whom; and what "the count" means while a claim is being contested. None of those sentences would have occurred to the person who wrote the first version — they only became visible by watching a correct-looking answer and asking what it had quietly decided.

That is the whole method, run once on something small, so that it is recognisable later on something that is not.

## When the thing is not small

The shelf is six requirements and a handful of gaps. A five-hundred-line program or a ten-page report has hundreds of places where the spec ran out, and reading the whole output line by line looking for each one does not scale — worth admitting plainly, because the method above can sound tidier than it actually is at that size.

The partial fix is to stop relying on your own re-reading and ask for the list directly. Before accepting anything built at that scale, ask the agent to state, separately from the result, every place it made a judgement call the specification did not settle — every default it picked, every case it assumed would not occur, every ambiguity it resolved one way rather than another. That list is not guaranteed to be complete; an agent does not always know which of its choices were choices. But it is a much shorter document than the output, it is aimed at exactly the right question, and reading forty stated assumptions is a task you can actually do in a way that re-deriving forty unstated ones from the output alone is not.

This does not make the problem small. It turns it into a list instead of a search, which is the difference between a task you can finish and one you only feel bad about not finishing.

## Verification only checks what you asked for

There is a specific trap that this chapter is really about, and it recurs in every chapter after it.

You write a spec. You write tests against the spec. The tests pass. Everything you asked for is present and correct.

And the result is still wrong.

It is wrong because of something you never thought to ask for. The tests could not catch it — tests check what you asked. The agent could not catch it — it built what you asked. Nobody made a mistake, in the sense of doing something incorrectly. The specification was simply incomplete in a direction none of the checking looked.

A sorting program that handles empty lists, single items, duplicates, and a million entries, all correctly — and puts them in ascending order, when the thing being sorted was a leaderboard.

Every verification step you will ever run has this shape. It is not a weakness in a particular technique; it is what verification *is*. A check compares a result against a stated expectation, so a check can only ever find the gap between the result and what you stated. It is structurally blind to the gap between what you stated and what you wanted.

So the discipline is not "check more". It is "keep asking what you forgot to specify", and that question has no automated form, which is precisely why it is worth a person knowing how to ask it.

## What to do with this

Keep a record. What you asked for, what came back, what you checked, what you caught.

Not because anyone needs the paperwork, but because the pattern in your own record is the fastest available teacher. After ten entries you will notice you make the same kind of omission repeatedly — that you always forget the empty case, or always forget who the output is for, or always assume the data is clean. That pattern is personal, it is stable, and nobody else can tell you what yours is.

Reading a delegation record is a skill in the way that reading a bibliography once was. It is how you tell, about work you did not watch being done, whether anybody was actually paying attention.
