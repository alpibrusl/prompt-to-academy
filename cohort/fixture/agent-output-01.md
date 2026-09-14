# Agent output — shelf tracker

*This is a real-shaped response to a real-shaped specification. It is
included so that a session can run even when the cohort's own agent produces
something different on the day.*

---

**Built: a shelf inventory tool.**

Every requirement in the specification is met:

- ✅ Lists every book on the shelf with title and author
- ✅ Marks a book as "out" when someone takes it, with their name
- ✅ Marks it "in" when it comes back
- ✅ Sorted alphabetically by title
- ✅ Shows a count of books currently on the shelf
- ✅ Works on a phone
- ✅ Handles the empty shelf (shows "no books")

Tested against 6 cases, all passing: empty shelf, one book, many books, a
book taken out, a book returned, and two books with the same title.

The tool is ready to use.

---

*What to look for, before reading the facilitator's copy:*

*Everything above is true. The tool does all of it, correctly. Ask instead:
who can mark a book as returned? What stops someone marking a book "in" when
it is still in their bag? If two people open it at the same time and both
take the last copy, what happens? And — the one that is almost never
specified — how does a book get **onto** the list in the first place?*
