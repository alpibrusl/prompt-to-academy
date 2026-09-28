# Doing Became Optional

There is a particular kind of knowing that only arrives by the long way round.

Someone who has run a statistical test by hand — really by hand, with a pencil, on twelve numbers — knows something that the formula does not contain. They know which step is fragile. They know the feeling of a number coming out too clean. They have been wrong at least once in a way that stung, and the sting left a mark shaped like a question: *is this actually right?*

That knowledge was never taught on purpose. It was a by-product. It came free with the only available route to producing the result, because the route was long and you had to walk it.

The route is now optional.

## What changed

Every artifact a school grades can be produced without the student. An essay, a program, a chart, a translation, a problem set, a lab write-up. Not badly, either — often better than the student would have managed, and in less time than it takes to read the assignment.

This is not a complaint about cheating. Cheating is a much smaller problem and a much older one. The problem is that the thing which used to form judgement has become separable from the thing which used to prove it, and almost every institution is still measuring the second one.

Three consequences follow, and they are worth naming separately because people tend to collapse them.

**Doing became optional.** Learning by doing still works exactly as well as it ever did. It just no longer happens as a side effect of producing. If you want the doing, you now have to want it specifically, and arrange for it, and defend it against the obvious shortcut sitting in everyone's pocket.

**Certification broke.** Homework proves nothing about the person who handed it in. A portfolio proves nothing. A take-home essay proves nothing. None of these were ever *meant* to be proof — they were proxies that happened to work, because producing the artifact required the person. The proxy has come apart from the thing it was proxying for, and most assessment has not adjusted.

**The bundle came apart.** This is the subtle one. Anyone who could write a working program had, necessarily, climbed the hill that teaches you where programs fail. Anyone who could produce a persuasive argument had climbed the hill that teaches you how arguments mislead. Competence and caution arrived together because they came from the same climb. Now a machine will hand you the competence, in seconds, and the caution does not come with it. It has to be taught separately, deliberately, as its own subject.

## The failure mode

Picture someone sixteen years old who can get a correct-looking answer to almost any question they can phrase. They are, by any test their school administers, doing extremely well.

Hand them a result that is confidently, plausibly wrong — the kind that is wrong in the third step of five, where the first two steps were fine and the conclusion is stated with total assurance. What happens?

If nothing happens — if it reads as true because it reads as fluent — then what has been built is a person who is fluent and ignorant. Able to ask for anything. Unable to tell whether what came back is right. And, because they did not build it, not especially inclined to feel responsible for it either way.

That combination is the thing this book exists to prevent. Not AI use. Not shortcuts. That specific combination.

## What is actually scarce

It helps to be precise about what is now rare, because the honest answer is not "the ability to produce things".

It is also not the ability to phrase a request well. Wording a prompt so that a system understands it is a real skill, and it is not what this book is about, and it is not what turns out to be scarce — a query that is technically well-formed can still be pointed at the wrong target, and being fluent in asking is no protection against being wrong about what you asked. Put it a different way: whatever this book's title suggests, it will not teach you to write better prompts. It exists to teach the parts on either side of the prompt — the wanting, precisely enough to state it, and the checking, precisely enough to trust it.

What is rare is the ability to say what you actually want, in enough detail that a competent stranger could build it and you would recognise whether they had.

What is rare is knowing what "correct" would look like *before* you see the answer — because after you see it, it is almost impossible to un-see, and everything the answer says starts to sound like what you meant.

What is rare is the reflex to ask what was left out. Not what is wrong with the answer — what is missing from the question.

What is rare is being willing to put your name on something you did not build, understand what you are taking on by doing that, and still do it, because that is what taking responsibility means and it is going to be most of adult work.

None of those are AI skills. They are older than that, and they were always the valuable part. They were simply bundled with production, and the bundle has come apart.

## The shape of the fix

Everything that follows starts with one move, repeated.

**Do the thing yourself first, small, and get it wrong.**

Not the whole thing. A tiny version — five rows of data, twenty lines of code, one paragraph. Small enough to finish in ten minutes. Real enough to fail.

Call that tiny version a **dummy**: small enough to do by hand, and built before you understand the problem well enough to know what it leaves out.

Then, and only then, delegate it. And because you have felt where it goes wrong, you now have a question to ask the result, and the question is a memory rather than an item on a checklist.

That ordering is not a preference. It is where the method starts. A checklist of verification questions handed to someone who has never been burned is a ritual — they will run it, it will pass, and they will have learned to perform diligence without acquiring any. The failure has to come first, and it has to be theirs.

The chapters after this one each take one such failure and walk it: what to do by hand, what goes wrong, what the concept is called, what question that failure leaves you with, and what happens when you hand the same work to a machine.

## What you are aiming at

The dummy is not the goal. It is small because you do not yet know what matters, and most of what it leaves out, it leaves out by accident.

The goal is a different small thing, and it comes last. Call it a **toy model**: the smallest description of a problem that still behaves like the problem. Three or four quantities, a rule connecting them, and nothing else — and everything that was left out, left out on purpose, for a reason you can say aloud.

The two are easy to confuse, because both fit in your head. They are small for opposite reasons. A dummy leaves things out because you have not noticed them yet. A toy model leaves things out because you have checked that they do not matter. Each part of this book starts with a dummy and ends with a toy model, and in between sits the real, full-sized thing — usually built by an agent — whose disagreements with what you expected are what turn the one into the other.

Here is one. A class of thirty takes a test marked out of ten, and the scores are mostly around six. One score was typed as 100 instead of 10. What is the average now?

You do not need the list. An average shares every row's size equally among all the rows, so one row that is 90 too big, among thirty, pushes the average up by 90 ÷ 30, which is 3. The average will come out near 9 instead of near 6. That is the whole model: a mistake of size M in a list of N moves the average by about M ÷ N. It already tells you something the list never would — that a big mistake in a short list is loud, and a small mistake in a long list is nearly silent, which is the kind worth worrying about.

This is what an experienced person is using when they glance at an agent's answer and say "that can't be right". They are not redoing the work. They are running a much smaller version of it in their head and noticing that the answer does not fit. Much of what gets called judgement is a handful of these, held firmly.

## Why anyone would bother

A student with an agent and no model asks questions more or less at random and believes what comes back, because there is nothing to hold it against. Telling them to be sceptical does not help. Scepticism with nothing behind it is either a pose or a paralysis.

A toy model changes the order of events. Before the agent runs, you write down what your model predicts. Then the agent runs. Then you compare.

When the two agree, you have learned a little. When they disagree, one of two things is true: the agent is wrong, or your model is missing something. Either way you now hold a specific question — not "is this right?", which nobody can answer, but "why does my model say 9 when the agent says 6?" — and a specific question is one you can go and find the answer to, including by asking the agent.

That is what this book relies on to make the knowledge worth having. Nobody is asked to learn about averages, or luck, or percentages in advance and in the abstract. They meet a disagreement between their own prediction and a confident answer, and the knowledge becomes the thing they need to settle it. The agent stops being an oracle and becomes the thing their model collides with, and each collision leaves the model a little better than it was.

**Write the prediction down before the agent runs.** On paper, not in your head. Once you have seen an answer, whatever you meant to predict will quietly drift towards it, and you will not notice it happening.

## Where each part ends

Each of the four parts of this book ends in one toy model, in its last chapter, small enough to work by hand and specific enough to predict with:

- how many different things could be built that all match what you wrote;
- how a few bad rows move a summary, and which ones you would never see;
- how big a difference luck produces, and how that shrinks as you collect more;
- how often a long chain of usually-right steps comes out right at the end.

Four is not a lifetime's worth. It is enough to own a few properly — to say what each one leaves out and what would change if you put it back — and to leave with the habit of asking, whenever something large comes back from an agent, what the small version predicts.

You will notice that the machine is usually right. That is the point. A machine that was usually wrong would be easy to stay sceptical of. The difficulty of this subject is that the answers are good, they are good most of the time, and the discipline you need is the one that survives being right ninety times in a row.
