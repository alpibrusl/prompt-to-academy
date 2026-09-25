# The Number That Moves When You Watch It

An experiment is running. The results come in gradually. You can see them.

You look on day one: nothing much. Day two: A is slightly ahead. Day three: B has caught up. Day four: B is clearly ahead, and the gap looks convincing. You stop the experiment and announce that B wins.

You have just done something that does not work, and it is worth doing it deliberately, at least once, in order to feel exactly how reasonable it seemed.

## Why it fails

Random data wanders. Not steadily — it drifts, and doubles back, and sometimes wanders a long way from where it started before coming back.

If you check repeatedly and stop when you like what you see, you are not measuring which version is better. You are waiting for the wandering to reach a point you find convincing, and then freezing it there. Given enough checks, it will get there eventually, whether or not there is any real difference at all.

You can watch this happen with no real effect present whatsoever. Flip a fair coin, calling heads "A" and tails "B", and check the running total after every ten flips. Keep going until one side looks convincingly ahead. It will, sooner or later. The coin has no preference. You made one appear by choosing when to stop looking.

This is called peeking, or optional stopping, and it is not a subtle statistical nicety. It is the single most common way honest people produce confident, false results. Nobody in that story lied. Everybody looked at real data and reported what they saw.

## Why the number is not what you think

Statistical tests answer a specific and narrow question: if there were genuinely no difference, how surprising would this data be?

That question assumes the data was collected in a fixed way, decided in advance. The moment "how much data" depends on what the data looked like, the question changes, and the answer no longer means what it says. The number still gets printed. It just is not measuring the thing its name claims.

The same damage occurs in several other shapes, all of which feel innocent:

**Testing many things and reporting the interesting one.** Try twenty variations, find the one that looks significant, write it up. With twenty tries, one looking unusual is what you should *expect* — that is what "unusual" means at that frequency.

**Splitting until something appears.** No overall effect, so look at just the younger participants. Nothing. Just the younger ones on weekends. Something! Each split is another draw from the same lottery.

**Deciding what you were measuring afterwards.** You measured five things. One moved. It turns out that one was what you cared about all along.

These are the same error wearing four coats: **the analysis was chosen after seeing the data.** Once that has happened, the numbers describe your search, not the world.

## The defence is a piece of paper

Write it down first. How many observations. What you are measuring. What counts as a difference worth acting on. How you will split the data, if you will.

Then run it to the end without looking, and analyse it the way you said.

This is genuinely difficult, and the difficulty is not intellectual. Not looking is hard. Looking and not acting is harder. Having written "I will collect 200" and standing at 140 with a beautiful-looking gap, and continuing to 200 while it evaporates — that is the actual skill, and it is closer to honesty than to statistics.

It is also the whole reason that written-in-advance plan exists. Not to keep you organised. To bind you, so that the version of you who has seen an encouraging number cannot quietly rewrite the question.

## And when you did peek

Sometimes you look. Sometimes you have to change the plan for a reason that has nothing to do with the results.

The correct response is not to hide it. It is to say so: *we planned 200, we stopped at 140 because the term ended, and we looked twice along the way.* That sentence costs you the strength of the claim and keeps its honesty, and anyone reading it can now judge the result correctly instead of being misled about it.

A result reported with its own weaknesses attached is more useful than a clean result whose weaknesses are hidden — because the first can be acted on carefully and the second will be acted on confidently and wrongly.

There are proper techniques for planned interim looks. They exist, they work, and they all share one feature: the looking is declared in advance, and the price of it is paid in the threshold. The thing that is never rescuable is deciding after the fact.

## The holdout

One last habit, and it is the cheapest insurance available.

Before you start, set aside some of your data — or some of your people — and do not touch it. Do not look at it. Do not use it to tune anything. Then, at the very end, after every decision is made, test on that.

Whatever you tuned, you tuned to the data you could see. The holdout is the only part that can tell you whether what you found is real or whether you have simply memorised the noise in front of you.

If the result survives the holdout, it is probably real. If it does not, you have learned something genuinely valuable and slightly painful, which is the only kind of learning this book is really about.

## Where this comes from

Stopping a trial as soon as it looks good, testing many things and reporting the interesting one, splitting the data until something appears — these have names in statistics older than any of the tools this book is about. Optional stopping. Multiple comparisons. People have been catching each other doing this, and occasionally doing it to themselves, for as long as there have been experiments.

The reason it belongs in a book about delegating to a machine is not that the machine invented the temptation. It is that the machine has made every one of those bad moves available at the speed of a follow-up question. Asking "what if we just look at the younger group" used to take a week of re-analysis. Now it takes one sentence, and the answer comes back before the part of you that would have hesitated has had time to.
