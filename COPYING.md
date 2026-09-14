# Licensing

This repository holds two different kinds of work, under two different licences.

## The manuscript — CC BY-NC 4.0

`chapters/` is licensed under the Creative Commons Attribution-NonCommercial
4.0 International Licence.

You may share and adapt the text, provided you give appropriate credit and do
not use it commercially. An adaptation is not required to carry the same
licence.

Full text: <https://creativecommons.org/licenses/by-nc/4.0/legalcode>

## Everything else — EUPL-1.2

The cohort curriculum source (`cohort/`, including `sessions.yaml`,
`rubric.yaml` and the fixtures), the family guide in `home/`, the
`skills/` directory, `book.yaml` and the CI configuration are licensed under
the **European Union Public Licence v1.2** — the same licence as
[content-kit](https://github.com/alpibrusl/content-kit) and
[cohort-kit](https://github.com/alpibrusl/cohort-kit), the toolchains this book
and its curriculum are built with. The full text is in [`LICENSE`](LICENSE).

The EUPL is an OSI-approved licence: use, study, modify and redistribute freely,
including commercially, provided that derivative works you distribute are shared
under the EUPL or a compatible licence.

Matching cohort-kit's licence is deliberate. The fields this curriculum depends
on — `by_hand`, `verify`, `ai_mode`, `module`, `at_home` and `parent_notes` —
were filed against that project
([cohort-kit#12](https://github.com/alpibrusl/cohort-kit/pull/12)), and matching
licences means the curriculum and the renderer can move against each other
without a relicensing question.

## The fixtures are deliberately broken

`cohort/fixture/` contains data with planted errors: an attendance file that
averages to an impossible age, an A/B log generated from a single fair coin
that looks decisive if you stop early, and an orders/deliveries pair that
disagree by the rows that were never written. They are teaching material and
the errors are the point. Do not reuse them as sample data, and do not "fix"
them.

## Why the split

The two bodies of work want different things. The manuscript is a book: sharing
it is welcome, selling it is not. The curriculum and the tooling are meant to be
reused — including by a school or a company running this commercially — with the
copyleft that keeps improvements available.

A practical consequence worth stating plainly: an academy may charge fees and
run this curriculum, and a parent may run it at home, without asking anyone.
Selling the book's text is the thing the manuscript licence excludes.
