# The Spec Is the Work

Here is an experiment worth running before reading further.

Think of something simple. A sandwich. A paper aeroplane. A way of sorting a shelf of books. Write instructions for it — on paper, no talking — and hand them to someone who will follow them exactly, without asking you anything.

Then watch.

## What always happens

Something always goes wrong, and it is almost never the thing you were worried about.

The instructions said "put the filling on the bread". They did not say which side. They did not say that the bread comes in two slices and that both are involved. They said "spread the butter" and did not say how much, and now there is a centimetre of butter, technically spread.

The person following your instructions is not being difficult. They are being *exact*. Every ambiguity you left is a decision you handed to them, and they had to make it somehow.

This is the first and most durable lesson in the book, and it has nothing to do with machines: **the gap between what you said and what you meant is invisible to you, and obvious to whoever has to act on it.**

You cannot find that gap by re-reading your own instructions. You wrote them. When you read "put the filling on the bread", your own intention is still attached to the words, and you read your intention rather than your sentence. The gap only becomes visible when it is executed by someone who does not share your head.

## Why this is the graded work

In most schools, the thing that gets marked is the artifact. The essay, the program, the model.

Here the thing that gets marked is the specification and the review — what you asked for, how you defined "correct", what you tested, and what you caught. The artifact is a by-product.

This is not a gimmick to make assessment harder to fake, although it does that. It is because the specification is genuinely where the work now lives. When production was expensive, the spec was a quick sketch before the real effort began, and it could be vague because you were going to build the thing yourself and resolve the ambiguities as you went, unconsciously, a hundred times an hour.

When production is nearly free, all of that unconscious resolving stops happening. Every ambiguity gets resolved by someone — or something — that is not you, and you find out what it chose when you look at the result. If you look at the result.

The spec is not the preliminary to the work. The spec is the work.

## What a usable spec has in it

After a few rounds of watching your instructions come back wrong, a pattern emerges. Good specifications tend to answer four questions, and the first two are the ones people skip.

**What does "done" mean?** Not "a program that sorts the list" — what makes a sorted list correct? What about an empty list? A list with two identical items? If you cannot say what done means, you cannot tell whether you are done, and neither can anyone else.

**What does "wrong" look like?** This is separate from the first question and harder. Describe a result that would satisfy everything you just said and still be unusable. If you cannot think of one, you have not thought about it long enough — there is always one.

**What is fixed and what is free?** Which parts are requirements and which are your first guess at a solution? People routinely over-specify the parts they happen to have imagined and under-specify the parts that actually matter.

**What did you leave out on purpose?** Writing this down is what stops "we never discussed that" from becoming an argument later.

## The rewrite is where it lands

The first spec is not meant to be good. The first spec exists so that the second one can be written by someone who has now watched their own words be taken literally.

That second version is noticeably different. It is more specific in some places, but — and this surprises people — it is often *less* specific in others, because the first attempt was full of incidental detail that was never a requirement at all. It contains edge cases. It says what done means. It usually contains a sentence that starts "if it is ambiguous, do this rather than that", which is a sentence nobody writes before their first failure and nearly everybody writes after it.

Keep both versions. The difference between them is the thing being learned, and it is much easier to see in the diff than in either document alone.

## A note on the machine

Everything in this chapter is true about people. That is why the exercise uses a person first.

There is a temptation, once you know the chapter is heading towards AI, to skip the human round — it seems like a slower version of the same demonstration. It is not. When a person follows your instructions badly, you can see them do it. You can watch the moment of hesitation where they decide something you should have decided. You can ask them afterwards what was unclear, and they will tell you, in words, with irritation.

None of that is available from a machine. A machine resolves your ambiguities silently, instantly, and plausibly, and hands you something that looks finished. The hesitation is invisible. The decision is invisible. If you have never watched a person do it visibly, you will not know to look.

So: a person first, and only then the same spec, unchanged, to an agent. Which is the next chapter.
