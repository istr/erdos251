# item-0028 landing note -- the three pintz10 planning inputs

Landed by item-0028 from the steering workpaper set of 2026-07-26,
byte-exact as authored; sha256 booked in payloads/HASHES.txt by the same
apply. Authored by steering (Claude Opus 5) on operator instruction,
2026-07-26; held untracked in the executor working tree under
dossier/item-0022-workpapers/ from 2026-07-26 until this landing
(extract-grades-r3.md Section 0; ANN-20260731-87), and landed here
because item-0028 is their consuming item. The set is a findings record
plus a deterministic reproduction pair; it is not an extract and does
not carry extract standing.

Verification standing at landing. The header of
pintz10-source-defects.md declares "awaiting executor confirmation under
the item-0022 repair dispatch r1, Task D; awaiting operator ratification
thereafter". That path was superseded by a stronger instrument before
any Task D ran: the graded extract
dossier/item-0022-workpapers/extract/pintz10-patterns.md, transcribed
from the anchored 1004.1072v1 bytes, graded CLEAN by a fresh executor
session and hashed (ANN-20260728-83; extract-grades-r3.md). The
item-0028 session re-verified every source-facing claim of the workpaper
against that graded extract and against
dossier/item-0017-workpapers/extract/pintz10-singser.md, and re-executed
pintz10-2-16-recheck.py with output identical to
pintz10-2-16-recheck.txt up to the tool-version line; the verification
record is item-0028-final-report.md Section V-A. The operator apply that
lands these files is the ratification the header awaits.

Clauses superseded at landing, left byte-exact in the files per the
leave-and-document convention (ANN-20260728-82/83 header disposition;
runs/README rule 27 by analogy):
- header: "NOT COMMITTED" and the Task D verification-status sentence
  (discharged as above);
- Section 1, instrument I2 row: "This is the gap that r1 Task D closes"
  (closed by the graded extract instead);
- Section 2, support class: "pending confirmation against the anchored
  bytes" (confirmed via the graded extract, ANN-20260728-83);
- Section 2 consequence and Section 6 first bullet: the item-0022
  verdict register they address was withdrawn as an instrument
  (ANN-20260727-77); the general-r reading survives via the graded
  extract, register rows do not;
- Section 6: "item-0031 is proposed and unscheduled" (item-0031 was
  withdrawn, ANN-20260727-77);
- Section 8 item 1 (discharged as above).

Label collision, binding on every consumer: Section 4 of
pintz10-source-defects.md uses "S1" as its own observation label. The
project-level S1 is the separator carrier of separator-repricing.md
W4.S1. No item-0028 artifact uses the bare label "S1" for the Section 4
observation; it is cited as "the (2.16) sharpening" throughout, and any
later consumer should do the same.
