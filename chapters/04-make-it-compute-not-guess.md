# Make It Compute, Not Guess

Ask an agent, in ordinary prose, to work out a tip on a restaurant bill split between seven people, with one person not drinking.

Then ask it to write a small program that does the same thing, and run the program.

Compare.

## Two different machines in one box

Most of the time these agree, and when they disagree the prose version is the one that is wrong.

The reason is worth understanding, because it determines when you can trust an answer and when you must not.

When an agent answers in prose, it is producing text that continues plausibly from your question. It has seen an enormous number of worked arithmetic examples, so the text it produces is usually arithmetically correct — the same way a fluent speaker usually gets grammar right without consulting rules. But "usually correct because correctness is typical" is a different guarantee from "correct because it was computed", and the difference shows up exactly where you would least like it to: on the unusual cases, the ones with an awkward remainder, the ones that are not typical.

When it writes and runs a program, something categorically different happens. The program executes. The arithmetic is done by a machine that cannot be plausible at it — it can only be right or crash. And you can read the program, which is a claim you can inspect, instead of a number you have to take on faith.

## The rule

**Anything past retrieval gets code, and the output shown.**

Retrieval is fine in prose: what is the capital of Peru, what does this word mean, what is the usual name for this technique. If the answer is a fact that was in the training data, prose is the right shape for it.

Everything else — arithmetic, counting, sorting, dates, percentages, unit conversion, anything with a "how many" or a "how much" — should be computed, and you should see the computation and its output, not a sentence reporting what the output was.

Two things about this rule.

First, it is not a rule about distrust. It is a rule about *which mechanism you are using*. A calculator is not more trustworthy than a person because calculators are virtuous; it is more trustworthy at arithmetic because it computes instead of estimating. You are choosing a mechanism, not rendering a verdict.

Second, and this is the part people get wrong: **the output has to actually be shown.** An agent will sometimes write correct code, then tell you what the code "would" produce, in prose, without running it. That is the prose mechanism wearing the costume of the computational one, and it is the worst of both, because it looks like it was computed and it was not. If you did not see the output, it was not computed.

## The number that ends in a zero

There is a small habit that catches a surprising fraction of errors, and it costs nothing.

Before you look at the answer, guess it. Roughly. Out loud or on paper, and to the nearest power of ten if that is all you can manage.

The bill is about ninety, seven people, so about thirteen each, less for the one not drinking, so call it fourteen for the rest.

Now look. If the answer is 13.80, fine. If the answer is 138, something has gone wrong by a factor of ten, and you knew that in the half-second before you read it carefully — because you had already committed to an expectation, and the mismatch was jarring.

The order matters absolutely. An estimate made *after* seeing the answer is not an estimate; it is a rationalisation, and it will agree with whatever you saw. This is not a failure of character. It is how minds work, and it is why the guess has to be committed to first, preferably in writing where it cannot quietly revise itself.

Estimating first is the cheapest verification that exists. It catches nothing subtle. It catches everything catastrophic.

## What this generalises to

The specific rule is about arithmetic, but the shape recurs everywhere in this book.

There is usually a version of a task that *produces* an answer and a version that *reports* one. The produced version can be inspected, re-run, and checked against a case you already know. The reported version can only be believed.

Whenever you have the choice, take the version that produces. Not because the reporting version is usually wrong — it usually is not — but because when it is wrong you have no way to find out, and a method whose failures are undetectable is not a method you can build on.

And when you cannot have the produced version, say so. Out loud, in the record: *this part was not computed, it was asserted, and I did not check it.* An honest unverified claim is a perfectly respectable thing to hand someone. An unverified claim presented as a verified one is not, and the difference is entirely in whether you said which it was.
