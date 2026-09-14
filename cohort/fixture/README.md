# Fixtures

Shared material the exercises run on. Every file here is deliberate: the
errors in it are planted, they are of a specific kind, and they are the
point.

Do not clean these files up.

| File | Carries | Used by |
|---|---|---|
| `brief-01-shelf.md` | An ordinary request with ordinary ambiguity | Sessions 1–2 |
| `agent-output-01.md` | Output that satisfies the spec and is unusable | Session 2 |
| `bill.md` | Arithmetic with an awkward remainder | Session 3 |
| `attendance.csv` | A blank, a `999`, a duplicate row, two date formats | Sessions 4–6 |
| `ab_test_log.csv` | A fair coin that looks significant if you peek | Sessions 7–8 |
| `chart-brief.md` | Real numbers, drawn three ways | Session 9 |
| `orders.csv` + `deliveries.csv` | Rows that do not exist for things that did not happen | Session 10 |
| `trace-sheet.md` | The delegation record, one page | Every session from 2 on |
| `scoring-sheet.md` | The pilot's own instrument | Sessions 1 and 12 |

## The verified numbers

Instructors should know these before running the sessions. Students should not.

**`attendance.csv`** — 37 rows, one of which is a duplicate submission. Taking
the mean of the `age` column as it stands gives **40.38**. The honest mean,
after dropping the blank and the `999` and the duplicate, is **14.14**. A
child who reports 40.38 has not done anything incorrectly; they have computed
exactly what they asked for.

**`ab_test_log.csv`** — 400 trials. Both variants were generated from the
*same* 25% chance. There is no effect, by construction.

- Stopping at trial 160: A converts at 16.5%, B at 41.3%. z ≈ 3.49.
- Running all 400: A at 27.1%, B at 32.4%. z ≈ 1.15. Nothing.

This is the file that teaches session 8, and it only teaches it if the
children peek first and believe it. Let them.

**`orders.csv` / `deliveries.csv`** — 200 orders placed, 169 delivered, 31
never arrived. Mean delivery time computed from `deliveries.csv` is **3.28
days**, and is the mean of the deliveries that happened. There is no row in
any file for an order that never arrived. Nothing announces their absence.
