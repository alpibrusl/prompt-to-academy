# When the Toy Passes Anyway

A method that passes its known-answer test can still be wrong about the real data, and the reasons are not exotic. They are the ordinary reasons, and they are worth having names for, because a thing with a name is a thing you can look for.

## The toy was clean and the world is not

You built five tidy rows. The real data has a blank where a number should be, a date written three different ways, a duplicate that arrived twice because someone pressed submit twice, and one row where a person typed their age as 999.

Your method handles none of this, and it will not crash. It will quietly produce an answer, because most methods are built to produce answers, and a blank will be read as zero, and 999 will be averaged in with everyone else.

The fix is not cleverness. It is to look at the real data before trusting any result computed from it. How many rows? How many blanks per column? What is the smallest value, the largest, the most common? Does anything in that list make no sense?

This takes two minutes and is skipped almost universally, because it feels like it is not the real work. It is the real work.

## The toy was small and size changes the answer

Some things behave differently at scale in ways a five-row case cannot show. A method that is correct but takes an hour per row. A rounding error that is invisible once and ruinous a million times. A rule that made sense when there were three categories and falls apart at three thousand.

Small cases test correctness. They do not test what happens when the thing meets its actual volume, and you should not let a passing toy case persuade you that they do.

## The answer leaked into the question

This one is worth watching for above all the others, because it produces the most convincing wrong results.

You are trying to predict something. Somewhere in the data you are predicting from, the answer is already present — not obviously, but in some form. A column that was filled in afterwards. An identifier that happens to be assigned in order of the outcome. A timestamp that only exists for the cases that succeeded.

The result is spectacular. Everything is predicted almost perfectly. And it means nothing at all, because you have built something that looks up the answer rather than working it out, and on genuinely new data it will fail completely.

The tell is the one from the last chapter: **the result is better than it has any right to be.** Hold on to that instinct. When something works far better than expected, the first hypothesis is always leakage, and it is right most of the time.

## You measured what you could, not what you meant

The most common and least dramatic failure.

You wanted to know whether people found the thing useful. You measured how long they spent on the page. Those are not the same, and one of them is easy to count.

This substitution happens silently and constantly, because measurable things get measured and unmeasurable things get quietly replaced by measurable neighbours. Then everyone talks about the neighbour as though it were the original. Time-on-page becomes engagement becomes value. Marks become learning. Lines of code become productivity.

Every one of those has a well-documented history of people optimising the proxy until it stopped tracking the thing it was proxying for — and the optimising is what breaks the link, which is why a measure that worked fine for years can fail precisely when you start trying hard to improve it.

The defence is a written sentence, before you start: *I want to know X. I am measuring Y. They differ in these ways.* Write the third part. It is the part that makes the first two honest.

## The world changed underneath you

The method was right. The data was clean. Nothing leaked. And it is wrong now, because it was built on how things were and things moved.

Anything learned from the past assumes the future resembles it. Usually true. Occasionally, expensively, not — and the moments when it stops being true are exactly the moments that matter, because that is what a change is.

Nothing in the method will tell you this has happened. There is no internal signal. The only defence is external: keep checking a known-answer case over time, and notice when an answer that used to be right stops being right.

## What to do with this list

This is not a checklist to run once and file. It is five questions to ask, each of which sometimes finds something:

Did I look at the actual data?
Would this behave differently at scale?
Is this result too good?
Am I measuring what I meant, or what I could count?
Has the situation changed since this was built?

None of them is clever. None requires expertise to ask. All of them are routinely skipped by people who do have expertise, under time pressure, which is the only condition under which real work is ever done.

And there is a sixth, which subsumes the rest and is the one this whole book keeps returning to: **what did I not ask, that would have changed the answer?**
