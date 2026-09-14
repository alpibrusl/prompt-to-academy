# Right, and Still Wrong

Every chapter so far has circled the same fact from a different side. This one states it directly, because it is the centre of the subject.

**Verification only checks what you asked for.**

You wrote a specification. You wrote tests against it. The tests pass. Every requirement is met. And the result is unusable.

Nobody made a mistake. The agent built what was asked. The tests checked what was asked. The specification was simply incomplete in a direction that none of the checking looked, because checking compares a result to a stated expectation, and it is structurally blind to the distance between what you stated and what you wanted.

## What this looks like in practice

A booking system that correctly prevents double-booking, handles cancellations, sends confirmations — and lets anyone cancel anyone else's booking, because nothing in the spec said otherwise and nothing in the tests checked.

A tool that correctly summarises meeting notes, tested on a dozen examples, all good — and quietly drops anything said by the last person to speak, because of an off-by-one in the splitting that only shows up when the transcript ends without a trailing blank line. Every test transcript was copied from a file that had one.

A report that correctly calculates average delivery time and is completely wrong because the deliveries that never arrived are not in the data. There is no row for the thing that did not happen. Every number is right. The average is of the survivors.

That last shape is worth staring at. The most dangerous omissions are usually not wrong entries but *missing* ones, and nothing in a dataset announces what is absent from it.

## The question

You cannot check for everything. The space of things you did not specify is unbounded, and there is no procedure that enumerates it.

But the question that goes at it is short:

**What did I not ask for, that would have changed this?**

And there is a more tractable version, which is what you actually use:

**Where did my instructions run out, and what got chosen there?**

That one terminates. Go back to your own words. Find the places where a decision was necessary and you did not make one. Then find what got decided. The errors are there, almost always, because the parts you specified are the parts that got built correctly.

Four prompts help pull those places out of hiding:

*Who is this actually for, and what do they need that I did not say?*
*What happens when there is none of it — no rows, no data, nobody?*
*What happens when there is far too much?*
*What is missing from this data entirely, and would I be able to tell?*

## Why this cannot be automated away

It is reasonable to ask whether this is a temporary skill — whether better tools will eventually ask these questions for you.

Partly. Tools already catch a great deal, and will catch more. But the question "what did I forget to specify?" is a question about *what you wanted*, and the wanting is not in the system. It is in you, and it is frequently not fully in you either — much of what you want is discovered by seeing something that is not it.

This is why the record matters. Not compliance paperwork: a working tool. What you asked, what came back, what you checked, what you caught. After a dozen entries, your own pattern becomes visible, and it is stable and personal. Some people always forget the empty case. Some always forget who the output is for. Some always assume the input is clean.

Yours is yours. No one can tell you what it is, and once you know it, you check for it first, forever.

## Small, deliberate, repeatable

The practical form of this is a habit rather than a technique.

Before you delegate: write what done means, and one way the result could satisfy that and still be wrong.

After it comes back: find the decisions you left open. Look at what was chosen. Check the one thing you wrote down. Then ask, once more, what you still have not asked.

Write down what you checked and what you did not. Especially what you did not. An honest "I did not verify this part" is a perfectly respectable thing to hand someone; an unverified claim presented as verified is not, and the entire difference is whether you said which it was.

## The reason this is the last technique in the book

Because it is the one that does not resolve.

The others complete. A known-answer test passes or fails. A chart is honest or it is not. An experiment was planned in advance or it was not.

This one never finishes. There is always another thing you did not specify. You get better at it — you learn your own blind spots, you build the reflex, you start writing specs that anticipate more — and it never becomes complete, because completeness would require knowing everything you want in advance, and nobody does.

That is not a defect in the method. That is what judgement is: operating carefully in a situation you cannot fully specify, knowing you cannot fully specify it, and remaining answerable for the outcome anyway.

Which is the last chapter.
