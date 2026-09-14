# Running It on the Toy

The toy case is built. The expected answer is written down, on paper, where it cannot revise itself. Now run the method.

Four things can happen, and each one means something different.

## It agrees

The method produces what you predicted. This is the boring outcome and the most commonly misread one.

What you have learned: the method handles this case. Not "the method works". Not "the method is correct". One case, the one you thought of, behaves as expected.

That is worth having. It is also a much smaller claim than the relief of a passing test makes it feel like, and the gap between the size of the claim and the size of the relief is where a lot of bad work gets through.

The right response to a passing test is to build a second one, harder than the first.

## It disagrees, and the method is wrong

You predicted 42. It said 137. You check your arithmetic; your arithmetic is fine.

This is the best possible outcome, and it is worth saying so plainly, because it will not feel like it. You have found a real defect in a minute, using five rows, before it reached anything that mattered. Every alternative route to this discovery was worse: shipping it, or never finding out.

## It disagrees, and you are wrong

You predicted 42. It said 137. You check your arithmetic and your arithmetic is wrong.

This is the outcome that teaches the most and is the most tempting to skip past quietly. Do not skip past it. Find out *why* you expected 42 — there was a reason, and the reason is a belief you hold about how this works, and it is incorrect. Fixing the arithmetic without fixing the belief means you will make the same prediction again next month.

Write down what you believed and what is actually true. That note is worth more than the test.

## It agrees, and you are both wrong

This is the dangerous one, and it is why the previous chapter insisted the toy case contain something awkward.

You expected 42 because you misunderstood what the method does. The method returned 42 because it does the thing you misunderstood it to do. Everything agrees. Everything is wrong. The test passes and certifies a shared misconception.

Nothing inside the test can catch this. The only defences are external: build a case whose answer you know from the *situation* rather than from your model of the method, and have someone else predict the answer independently before you show them yours.

The second one is remarkably effective, and it is the real argument for doing this work in a room with other people rather than alone. Two people who have not yet spoken will disagree about the expected answer surprisingly often, and every one of those disagreements is a misunderstanding that would otherwise have passed silently through a test.

## Then, and only then, the real data

Once the toy case behaves, run the real thing. And the moment you have a real answer, you have a new obligation: the real answer has to be sanity-checked against something outside the method.

Is it the right order of magnitude? Does the number of rows that came out make sense given the number that went in? Is anything suspiciously round? Is anything suspiciously perfect?

That last one deserves its own warning. When a result comes back far better than you expected — an accuracy of 99%, a perfect correlation, a model that gets everything right — the overwhelmingly likely explanation is not that you have done something brilliant. It is that the answer has leaked into the question somehow: the thing you are trying to predict is sitting in the data you are predicting from, in some form you did not notice.

A suspicious result is a signal to look harder, not to celebrate. This is a strange instinct to build and it goes against everything else in life, where good news is good. Here, good news that you did not expect is the single most reliable indicator that something is broken.

## Keeping the record

Every toy case you build is reusable. Keep them.

A folder of small cases with known answers is the most valuable thing you accumulate doing this work. It grows every time something surprises you — and a case built from a real surprise is worth ten cases built from imagination, because it encodes a specific way the world turned out to be more complicated than you assumed.

Over a year, that folder becomes a record of everything you have been wrong about. It is also, not incidentally, the fastest way to check whether a change broke something: run the whole folder and see what moved.
