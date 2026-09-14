# A Case You Already Know

Here is a question with a trick in it. Suppose you are handed a method — a formula, a program, a procedure — that is supposed to answer some question about a pile of data. How do you find out whether it works?

The obvious answer is: run it on the data and see whether the answer looks right.

That answer is worthless, and it is worth being precise about why. You do not know what the right answer is. That is why you are running the method. "Looks right" can only mean "agrees with what I already assumed", which means the method can only ever confirm you, and a method that can only confirm you has told you nothing.

## The move

Build a tiny case where you already know the answer. Run the method on that.

Five rows. Numbers you chose. An answer you worked out by hand, on paper, before running anything.

If the method gets your toy case right, it has earned a small amount of trust. If it gets your toy case wrong, you have found a bug in ten seconds that you would otherwise have shipped, and possibly never discovered.

This is called a known-answer test, and it is the single most transferable thing in this book.

## Why it survives everything

Most techniques for checking work are being quietly automated. Spotting a typo, catching a type error, noticing an unhandled case, flagging a suspicious pattern — machines do all of these, increasingly well, and there is not much point building a person's identity around doing them by hand.

The known-answer test does not automate away, and the reason is structural rather than temporary.

Constructing the toy case requires knowing what the answer *should* be. Not computing it — knowing it, from understanding the situation. And to know that, you have to understand what the method is for, what it assumes, and what question it is actually answering. That understanding is the thing being tested, and the toy case is how it gets tested.

An agent can write you a toy case. It will be a reasonable one. It will test what is typical. It will not test the thing you are specifically worried about, because it does not know what you are worried about — that is yours.

So the test tests the method, and building the test tests you. You cannot delegate the second half without losing the point.

## Making one that is worth anything

A good known-answer case has three properties, and the third is the one people skip.

**Small enough to do by hand.** If you cannot work out the expected answer with a pencil in a couple of minutes, the case is too big. Five rows. Three rows. Two, sometimes. The temptation is to make it realistic; realistic is the enemy here, because realistic means you cannot compute the answer yourself, and then you are back to "looks right".

**Chosen, not found.** Do not grab the first five rows of your real data. You do not know what is in them. Make up numbers that produce an answer you can predict — and make them awkward on purpose. Round numbers hide errors. If every value is 10, a method that multiplies when it should divide looks fine.

**Containing the case you are afraid of.** This is the part that separates a real test from a ritual one. Before you build it, ask: what would have to be true for this method to be wrong in a way that matters? A missing value. A duplicate. A negative number where you assumed positive. Two things arriving in the same second. Then put that in the toy case.

A test that only contains the easy situation confirms that the easy situation works, which was never in doubt.

## Both directions

A test that passes tells you less than you think. It tells you the method handles the case you thought of.

So build one that should fail. Feed the method a case where you know the right answer is "no", or "error", or "not enough information" — and check that it says so. A method that returns a confident answer for a question it cannot possibly answer is worse than one that crashes, because the crash is honest.

This is the same lesson as the previous chapters wearing different clothes. The spec that passes its own tests can still be wrong, because the tests check what you asked. The method that passes your toy case can still be wrong, because the toy case contains what you thought of. What you did not think of is where everything lives, and the only way at it is to keep deliberately asking.

## The order, again

Toy case first. Before the real data. Before the real run. Before you have any expectations formed by looking at output.

Once you have seen the method's answer on the real data, you cannot un-see it. Any toy case you build afterwards will be, without you intending it, one that the method passes — because your sense of what the answer should be has quietly been calibrated to what it said.

This is not weakness. It is the most reliable effect in the study of human judgement, and it operates on people who know about it. The only defence is procedural: build the test before you look, write down the expected answer before you run it, and then you are comparing two things instead of one thing and its own shadow.
