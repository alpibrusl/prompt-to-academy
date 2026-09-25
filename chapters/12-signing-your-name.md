# Signing Your Name

Something you delegated has broken, in front of someone who was relying on it.

They are not interested in how it was built. They want to know what happened, whether it is fixed, and whether it will happen again.

What do you say?

## The thing that does not transfer

You can delegate the building. You can delegate the testing, the drafting, the checking, the writing-up.

You cannot delegate being answerable for it. That stays with whoever put their name on it, and it stays there completely — "the tool did it" has never been an answer and is not becoming one.

This is not a moral position. It is a description of how responsibility works, and it is about to be most of adult work: signing off on things you did not personally build. Doctors sign off on tests they did not run. Engineers sign off on calculations they did not perform. Editors publish articles they did not write. None of them can inspect every step, and all of them are answerable anyway.

What makes that possible is not a lower standard. It is a different one: they are answerable for **what they checked, what they did not, and whether that was a reasonable place to draw the line.**

## What a good account sounds like

When something has gone wrong, the account that actually helps has five parts, roughly in this order.

**What happened**, plainly, without softening. Not "there may have been some inconsistency" — the thing that happened.

**What was checked.** Specifically. "I tested it against three known cases and it handled all three."

**What was not checked.** Also specifically, and this is the part that separates an account from a defence. "I did not test what happens with no data at all. That is the case that broke."

**Why that line was drawn there.** There is always a reason — time, judgement, an assumption that seemed safe. Say it. "I assumed there would always be at least one entry, because there always had been."

**What changes now.** Concrete. "That case is in the test folder. It runs before anything ships."

Notice what is absent. No blaming the tool. No claiming it was checked when it was not. No claim that it was unforeseeable — it was foreseeable, you simply did not foresee it, which is ordinary and survivable and different from impossible.

## Why the record makes this possible

The account above is only available if you kept one.

Nobody remembers, six weeks later, what they checked. Memory reconstructs it in a flattering direction — you will sincerely recall having considered a case you never considered, because you can easily imagine having considered it.

The record is the defence against your own memory. What you asked. What came back. What you checked. What you did not. Written at the time, when there was nothing at stake and therefore no reason to shade it.

That record does three things. It makes an honest account possible after a failure. It makes your own pattern of omission visible before one. And it is the thing that lets someone else judge whether the work was done carefully — which is, in the end, what anyone is actually asking when they ask whether they can rely on you.

## Answering out loud

There is a particular kind of knowing that only shows up under questioning, and it is the reason this material is assessed by talking rather than by submitting.

You explain what you built. Someone asks why you did it that way. You answer. They ask what would have happened if the input had been empty. You answer, or you find that you cannot.

That moment — the one where you open your mouth and discover there is nothing behind a decision you made — is the most useful thing in this whole programme, and it cannot be produced by any amount of reading. It only happens live, in front of someone asking a question you did not anticipate.

It is also, not coincidentally, the only assessment that still means anything. Anything that can be produced unsupervised can be produced by something other than you, which makes it evidence about the work and not about the person. A defence is evidence about the person. So is teaching it to someone younger, which is the cheapest way ever discovered to find out whether you actually understood something.

## Some things are not yours to delegate

Everything so far has assumed the question is *how* to delegate well — what to specify, what to check, what account to give afterwards. There is a prior question, and it is easy to skip because the rest of this book has been so focused on technique: **should this be delegated at all, however carefully?**

Some things do not become acceptable to hand off just because you would check the result carefully afterwards.

Other people's private information going anywhere it does not need to go is one — a medical record, a home address, a grade, a password, fed to a system so that it can help draft something, is now somewhere it cannot be recalled from, and no amount of careful checking of the *output* undoes that.

A decision that cannot be undone if it is wrong is another — who gets an interview, who gets flagged, who gets removed, decided by a system whose reasoning you cannot fully inspect, acted on before anyone has a chance to say *that was wrong, undo it*.

Underneath both is the general case: anything where "I checked what I could, and here is what I did not" is not an acceptable answer to the person it affects. Most of this book has argued that a careful, honest account of partial checking is good enough, because it is what everyone competent actually gives. It is good enough for a shelf tracker. It is not good enough for a diagnosis, a sentence, or a decision about somebody's safety, because the cost of the part you did not check is no longer yours alone to bear.

None of this is a rule with a bright line, and this book will not pretend to give you one — it depends on what is at stake, who bears the cost of being wrong, and whether the person affected ever gets to ask you the question this whole book has been building toward. But the question itself has to be asked *before* the specifying and the checking begin, because by the time you are holding a careful, well-verified result, it is too late to ask whether you should have built it at all.

## What this was all for

Here is the whole book, compressed into one test.

Hand someone a confident result. A number, a conclusion, a finished piece of work, delivered with total assurance and no visible seams.

If they ask **how do you know?** — and then **what would have to be true for that to be wrong?** — and can tell whether the answers they get are any good —

then everything in these chapters has landed. Not because those two questions are magic. Because asking them, and meaning them, and being able to evaluate the response, requires all of it: knowing what a specification is, knowing what verification can and cannot reach, knowing what a fair comparison looks like, knowing that a chart is a claim, and having been wrong yourself often enough to expect that anyone might be.

The person who asks those questions is not sceptical of the tools. They use them constantly, for nearly everything, and they get far more done than someone who does not.

They simply know what they have checked. They know what they have not. They will tell you which is which.

And when it breaks — because eventually it breaks — they are standing there, with the record, ready to say what happened.
