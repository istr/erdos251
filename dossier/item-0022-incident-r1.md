# item-0022 incident report r1 -- a verdict register built on an object no session can read

**r1 (2026-07-27), authored after the operator resolved the open
decision.** The three reports are DROPPED AS OBJECTS. Section 9's first
question is therefore closed, Section 5a records what survives the drop
and why, and Sections 7 and 9 are revised accordingly. Nothing else
changed from r0, which never landed.

Analysis role, web sandbox. Read-only clone of public `main` at
`19495d7283042f74ba892d1d9b85771126494635`; history reviewed back to
`8cb50860c15491dbc6a982cb179ef7cba6416b3f` (the item-0017 v2 branch tip
that the three reports were generated from), 81 commits. One out-of-tree
network read was performed and is declared in Section 5. No commit, no
push. The roadmap half of the response ships as a `git am` patch; the
operator apply is the ratifying commit.

This document is a process finding, not a verdict on any mathematical
claim. It contains no erratum: no frozen or landed artifact is asserted
here to carry a wrong mathematical statement.

---

## 1. What the tree shows

The chain, in the order the tree records it.

**2026-07-18, 15:27.** `8cb5086` lands item-0017 v2 on its branch. Its
V4 section already names the three inputs the successor work needs: a
class lower bound for one matched-flank family, an extension upper bound
whose constant is $`o(\log{} x)`$ at $`k \sim \log{}\log{} x`$, and a
tail-intersection statement in the filters-first order. This is a
repository artifact, adjudicated through two adversarial reviews.

**2026-07-18, same day.** Three reports are generated outside the tree.
Report 1 is a ChatGPT literature survey on the S-weighted repair.
Report 2 is an Opus consolidation whose declared inputs are report 1 and
the item-0017 branch. Report 3 (2026-07-19) proposes eight alternative
routes. None of the three passes the project's own review protocol:
stateless run, one hash-verified payload, anchor-stripped object,
committed strip script, web off, wrapper verbatim in the config. They
are free-form outputs, and the project had no rule saying what standing
such an output has.

**2026-07-18, 21:43.** `a0e317e` closes item-0017 and creates the
successor package item-0018 through item-0022. item-0018's goal restates
the V4 triple. Report 2's Section 6 states the same triple as Satz A to
Satz D. **The triple is repository-originated**, so items 0018 to 0021
do not inherit their substance from report 2; this is the one place the
contamination could have been structural and is not. item-0022 is
created as the absorption item for the two 2026-07-18 reports.

**2026-07-24.** item-0026 lands `literature-consolidation.md`. Its
recommendation 5 refers to item-0023 as "the Dispersion Arm". That name
exists only inside report 3, which at that point is neither anchored nor
absorbed nor referenced anywhere in the tree. Report content reached a
landed artifact through model context rather than through the evidence
path.

**2026-07-26, 13:05.** `63742ff` (ANN-74) books ten hashes, resolves
item-0022's identification layer, records the finding that
`arXiv:1004.1072` was never on the shelf, re-executes report 1's k=2
numbers independently, and records ERRATUM-5 as booked-and-not-repaired,
because the workpaper carrying the false referent is itself anchored.
ANN-74 states the governing principle in one line: anchoring is not
absorption.

**2026-07-26, 13:10 and 13:11.** `ba05b39` and `9dee369` (ANN-75) split
report 3, amend item-0022, propose item-0031.

**2026-07-26, 13:30.** `3c40e6e` moves item-0022 to position 1 and books
its execution profile. **This is the last commit any ledger entry
covers.**

**2026-07-26, 20:10.** `d3966a3` lands 3308 lines under
`dossier/item-0022-workpapers/`: the absorption checklist, seven source
extracts, a numerical re-execution, the item-0022 final report, the
repair-r1 report, and the repair log. Its own message defers the ledger
entry, the handover refresh and the roadmap bookkeeping to steering.
That follow-up has not happened.

**After that.** `9cd43a3` proposes item-0032 and `19495d7` adds the
MathJax lint. Neither is booked either.

---

## 2. Root cause

The operator's three-part diagnosis is confirmed by the tree, and each
part sharpens into something a rule can catch.

### 2.1 The citation apparatus of report 1

Report 1 binds footnote *groups* to eight bare URLs, with no per-claim
page or theorem locator, and it names a Bloom-Kuperberg result that its
own bibliography carries no URL for. Two consequences follow
mechanically. A verifier cannot check a row without first re-deriving
which source a footnote belongs to, which is work the report was
supposed to have done. And a report whose citation apparatus has to be
reconstructed is not a survey of the literature; it is a list of leads.
The corpus can use leads. It cannot verdict them.

### 2.2 Report 2 is a derivative, and the item treated it as a second object

Report 2's literature-facing content is a recap of report 1. The
checklist's own consolidated table says so: its first row is annotated
as a recap. Its repo-facing content is a reading of the item-0017
branch. So item-0022's title, "primary verification of the two
2026-07-18 reports", promised two objects and had one and a half. The
half that is genuinely report 2's own -- its reading of the repository
-- is precisely the half the item declared unverifiable.

### 2.3 The firewall pointed the wrong way

Section 1 of the checklist bars the tree from serving as evidence, so
every claim report 2 makes about the repository is registered
`TREE-FIREWALLED` and verdicted against nothing. The firewall is sound
as a rule against circularity. Applied to this object it produced the
exact inversion of what was needed: **the claims that had already
influenced the roadmap were the ones the item was structurally unable to
check**, while the claims that had influenced nothing absorbed the
entire verification budget.

### 2.4 Operator-held is the load-bearing defect

All three reports are held outside the tree. The checklist quotes them
row by row as `Claim (verbatim)`. No session that reads only the tree
can confirm a single one of those quotations, now or ever. The artifact
is unfalsifiable in the repository, which is the exact opposite of the
single-source-of-truth charter, and the asymmetry is permanent rather
than temporary. Held outside the tree is the worst of the two available
states: enough standing to drive a ratified item, not enough to be
audited by anyone but the holder.

### 2.5 The instrument was a category error

Underneath all of the above: a per-claim verdict register over the prose
of a model-generated report manufactures the appearance of evidentiary
standing where none exists. Thirteen rows reading `CONFIRMED` look like
corpus knowledge. What they actually record is that a sentence in an
unratified PDF matched a sentence in an anchored PDF. The useful object
was never the report's claim; it was the anchored source behind it. The
correct instrument is a pointer harvest -- identifiers out, anchors and
extracts in, report discarded -- and ANN-74 had already written the
principle down one apply earlier.

---

## 3. Damage, itemized

**D1. Bookkeeping void, and a live re-run hazard.** Four commits since
the last ledger entry, including the 3308-line artifact drop. No hash
lines for any item-0022 workpaper. HANDOVER still presents item-0022 as
upcoming with its kickoff on request, the item is still `ratified`, and
until the attached patch it was position 1 of the execution order. A
cold start would have re-run an item whose acceptance artifact already
exists, over its own output. This is the one defect that was live and it
is the one this response closes first.

**D2. The object is not in the tree.** See 2.4. Everything downstream of
this is unauditable by construction.

**D3. Seventh verdict-promotion recurrence.** Five claim locations moved
from `STOP 7.5` -- an honest cannot-verify-under-this-gate -- to
`CONFIRMED` inside the repair pass, by widening the anchor gate from the
item's own ten named anchors to the whole shelf and then reading in-tree
extracts rather than the anchored sources. The two sources concerned are
booked on the shelf, so the class is legitimate in kind; the evidence
actually consulted was a derived transcription, and the widening
contradicts the checklist's own firewall sentence in Section 1. The
rule-16 strengthening B6, which targets exactly verdict promotion, has
been carried open since the third recurrence and was carried open again
by ANN-64. It has now produced the seventh.

**D4. A verdict oscillated three times in one day and landed unreviewed.**
Row R1-015 went `CORRECTED`, then was checked against the anchor and
upheld, then was reversed to `CONFIRMED` after the operator supplied two
further AI-generated PDFs mid-session. The executor handled those two
documents correctly under rule 19 -- they directed attention, the anchor
supplied the evidence -- and flagged in its own report that steering had
not reviewed the addendum. The apply ratified it anyway. **The content
is right** (Section 5); the path had no review in it.

**D5. Scope collapse the gates could not see.** The register carries 33
claims against a 60 to 140 envelope, 45 per cent below the low end, and
the envelope stop fires only on overshoot. Report 2's decisive sections
were registered at subsection granularity and verdicted against nothing.
The completion policy then declared the outcome complete.

**D6. ERRATUM-5 is frozen.** Report-3 content reached a landed workpaper
before report 3 was anchored, and because that workpaper is itself
hash-anchored it is booked and deliberately not repaired. A cold start
reading its recommendation 5 searches for an item that does not exist.
This is the specific trap that governs the extract handling in Section
7: **anchoring freezes what it books, so a defective artifact must never
be hashed.**

---

## 4. What the run actually bought

Recorded so the trade is visible rather than asserted.

- Seven extracts of anchored primary sources. These stand on their own
  anchors, not on report prose, and they are reusable. They are the
  run's real output.
- An independent re-execution of $`\mu_k(2)`$ and of the even-class
  ratio $`1.1504807723\ldots`$ over primes below $`2\times 10^6`$. Sound,
  and a duplicate: ANN-74 had already done it in the steering sandbox.
- The general-$`r`$ reading of Pintz's Lemma 2 (Section 5). Genuinely
  new and correct.
- The finding that `arXiv:1004.1072` was a shelf gap carrying an
  averaged relative one-position extension bound, routed to item-0028.
  This came from ANN-74, before the session ran.

So the literature value sits in the extracts and in two findings, of
which one predates the session. The verdict register -- the largest and
most expensive artifact -- is the part that is both costly and unusable.
That split is what makes the disposition in Section 6 straightforward.

---

## 5. Independent check of the one contested mathematical point

Because the repair-versus-rollback decision turns on whether the final
content state is right, the one row that oscillated was checked here
against the primary source directly. This is a fifth independent read of
the same object, from a different sandbox and a different fetch path.
Declared: `https://arxiv.org/abs/1004.1072` was fetched over the network
in this session, text layer, 2026-07-27.

The paper is Pintz, *Patterns of primes*, arXiv:1004.1072v1. What it
shows:

- Lemma 1 bounds the second moment over tuples of a fixed size, with
  the size restriction printed under the summation sign.
- The bridge sentence before Lemma 2 offers a more general form of the
  same lemma at the same cost.
- Lemma 2's display prints exponent 2 and shows no size restriction
  under the summation sign, exactly as the original item-0022 extract
  transcribed it. The transcription was accurate at all three passes.
- The lemma's own name, its threshold and its constant all carry $`r`$.
- The remark immediately after announces an asymptotic in the case
  $`r=1`$ that recovers Gallagher's theorem.
- The proof establishes the ratio bound over a single added element
  with exponent $`r`$, and the local-average computation that closes it
  carries $`r`$ throughout, not 2. Iterating over the size gives the
  general statement.

Two internal facts settle it independently of any glyph question. A sum
over *all* subsets of $`[1,H]`$ with no size restriction cannot be
bounded by $`c_8(\nu,r)H^\nu`$, so the restriction is required and is a
display omission. And a case $`r=1`$ has no content if the exponent
never depended on $`r`$. The coherent reading of the lemma is

$$
\sum_{\substack{D\subset[1,H]\cr \lvert D\rvert=\nu}}
\mathfrak{S}(D^+)^r \le c_8(\nu,r)\,H^\nu ,
$$

of which Lemma 1 is the case $`r=2`$ and the remark is the case $`r=1`$.
The printed 2 and the missing size restriction are typesetting defects
in the v1 preprint.

**Conclusion.** The reversal to `CONFIRMED` is substantively correct,
and report 1's claim about this lemma is accurate, including its own
observation that the rank stays fixed and the constant is unpriced in
$`\nu`$ and $`r`$. What was wrong was the path: an unreviewed addendum
rode into a ratifying apply. Nothing here needs to be un-done for
mathematical reasons; the row needs a review it never got.

---

## 5a. What survives the reports being dropped as objects

The operator's decision removes all three reports from the corpus as
objects. Nothing in this section is a re-verdict; it is an inventory of
what stands on its own anchor and therefore does not move.

**Survives, because it was re-anchored to a primary source before the
drop:**

- The seven primary-source anchors booked by ANN-74 and their
  identification layer. Each names a source with a stable identifier and
  a hash; none of them depends on a report for its standing.
- The seven extracts. Each transcribes an anchored source. Their grade
  is still open (Section 7, Phase 2), but the drop does not touch it.
- The `arXiv:1004.1072` shelf-gap finding and its routing to item-0028.
  Web-checked and hash-anchored in ANN-74, independent of the report
  that pointed at it.
- The k=2 numerics. Re-executed twice against the anchored Kowalski
  note, once in the steering sandbox and once in the session.
- The general-$`r`$ reading of Pintz's Lemma 2. Holds against the
  primary anchor (Section 5); the review it never got is still owed.

**Dies with the drop:**

- Every `Claim (verbatim)` row in the absorption checklist. The
  quotation now has no retrievable source, so the register is
  unauditable permanently and in principle, not merely inconveniently.
  This turns the withdrawal in Phase 2 from a judgement call into a
  consequence.
- item-0031. Its object is report 3. As written it is void; re-founding
  it would mean restating eight routes from tree-internal material that
  does not exist. It is `proposed` and unscheduled, so nothing is
  running on it, but it cannot be ratified as it stands.
- The two citation-policy questions carried since ANN-74 -- precedent
  anchors for the repository-shaped precedent and for the five carrying
  none of the project's mathematics, and the verdict class for
  citations that cannot be anchored. Both existed to classify citations
  belonging to dropped objects. They close as moot. The residual
  question, whether the two precedent extracts stay in the corpus at
  all, moves to the disposition item.
- ERRATUM-5's referent. The Dispersion Arm now has no object anywhere,
  in the tree or outside it. The erratum stays booked and unrepaired --
  the workpaper carrying it is anchored -- but its reason line changes
  from "exists only inside an operator-held report" to "has no object".

**Cannot be undone by the drop.** The three report hashes are already
booked in the append-only hash file. They stay as history. What the
ledger records is that those three lines name objects with no standing,
not that the lines are removed; an append-only file is not edited to
make a decision look tidier.

**The test this inventory exposes.** Everything that survives survives
for one reason: at some point somebody re-anchored it to a primary
source instead of citing the report. Everything that dies, dies because
nobody did. That is the whole rule of Phase 3 clause 1, stated as an
outcome rather than as a policy.

---

## 6. Repair or rollback: the decision

**Neither a revert nor a straight repair. Withdraw the instrument, keep
the evidence, repair the record.** The cut runs through the artifact,
not through the commit.

A `git revert` of `d3966a3` is wrong on three counts. It deletes the
seven extracts, which are the run's only output standing on primary
anchors. It deletes the evidence of the incident, which rule 5 keeps --
failed runs are data, and this run is now the project's best-documented
process failure. And it would delete the correct general-$`r`$ finding
along with everything else.

Leaving the checklist standing as a verdicted acceptance artifact is
equally wrong. It keeps thirteen `CONFIRMED` rows in the corpus whose
object no session can open, plus five promotions the item's own firewall
forbids.

What has to change is standing, not existence. The file stays; it stops
being an acceptance artifact and becomes the record of a withdrawn
instrument. That is a rollback of the verdict layer and a repair of the
record, and it is why the disposition item is scoped the way it is.

---

## 7. The strategy

### Phase 0 -- stop the re-run hazard (attached, one apply)

De-schedule item-0022 so no cold start is pointed at an item whose
acceptance artifact already exists; propose the disposition item and the
process item. One line reverts it if the operator disagrees. Shipped as
`erdos251-roadmap-item-0022-incident.patch`.

### Phase 1 -- book the void and the drop (one apply)

One ledger entry books the four unbooked commits, this incident, the
operator's decision to drop the reports as objects, and the disposition.
This report lands in the same apply, because Phase 3 clause 6 says an
artifact and the entry that books it travel together and this is the
first chance to honour it. HANDOVER gains a superseding bullet;
**historical lines that name item-0022 as upcoming are superseded, not
edited**, per the project's own convention that a stale claim stays and
a later sentence overrides it. **No hash line is added for anything** --
see the trap in Section 8. Draft entry in Section 10; the dispatch is
separate.

### Phase 2 -- withdraw the verdict layer (item-0033)

1. A withdrawal banner at the head of the absorption checklist, stating
   that its object is not in the tree and that its rows are not corpus
   knowledge. No row is deleted.
2. The five promoted locations are re-verified with their own anchored
   sources open -- both are already booked on the shelf, so this is
   cheap -- or returned to their pre-repair class. Whichever way each
   goes, it is listed as a promotion in the pass's own header.
3. R1-015 gets the steering review its addendum never had. Section 5 of
   this report is an independent input to that review, not a substitute
   for it.
4. The seven extracts are re-graded against their own anchored sources.
   Only after that are they hashed.
5. The item is named as an acceptance artifact nowhere in the store.

### Phase 3 -- close the rules (item-0034)

Six clauses, all falling directly out of this run.

1. **Report standing.** A model-generated report that no primary anchor
   backs enters the corpus as a pointer list only. Identifiers are
   booked, sources are extracted, the report's prose is never a unit of
   verification. This writes ANN-74's own sentence into the rule set.
2. **No unreadable object.** An object no session can read cannot be the
   object of a ratified item. If something genuinely cannot be
   committed, the rule names the substitute rather than leaving it to be
   improvised per item.
3. **Promotion gate (closes B6).** A verdict that moves toward a
   stronger class inside a repair, amendment or addendum pass needs its
   own pass with the primary anchor open, and appears as a promotion in
   that pass's header. The existing clause diffs a verdict before a
   review gate, which does not reach a pass that runs after it.
4. **Symmetric envelope.** The scope stop fires on undershoot as well as
   overshoot.
5. **No addenda.** An instruction that changes a run's task after its
   final report is issued opens a new run against a new pin.
6. **One apply.** An artifact drop and the ledger entry that books it
   land together. CI currently runs a Lean axiom gate and a MathJax
   lint; a check that every content commit is covered by a ledger entry
   is cheap and would have caught D1 the same evening.

---

## 8. Traps

- **Do not hash the item-0022 workpapers yet.** Anchoring freezes what
  it books; ERRATUM-5 is what that costs when the booked artifact is
  defective. Hash the extracts after the re-grade, and never hash the
  checklist as an anchor.
- **Do not revert `d3966a3`.** Rule 5, and the extracts.
- **Do not repair `literature-consolidation.md`.** It is anchored.
  ERRATUM-5 stays booked and unrepaired; the pointer belongs in the
  errata log, which is where it already is.
- **Do not re-run item-0022 as written.** The instrument is the defect.
  Re-running it produces the same artifact against the same unreadable
  object.
- **Do not let this report become the evidence for anything.** Under
  rule 19 it may direct attention and may not be the source of a
  wording or the evidence for a state. Section 5 in particular is a
  pointer to a primary anchor, not a substitute for opening it.
- **Do not read this report as a back door for the dropped objects.**
  It describes the three reports' *form* -- their citation apparatus,
  their derivation chain, their holding status -- and nowhere their
  claims. A dropped object stays dropped, and a process finding about
  it does not re-admit its content.

---

## 9. Decisions

**RESOLVED (2026-07-27): the three reports are dropped as objects.**
The middle state was the root cause and could not be kept. Consequences
inventoried in Section 5a; the drop is booked in Phase 1 and is not
re-opened by any later item.

Still open, and each is now smaller than it was:

1. Whether item-0022 closes as superseded with this report as its
   outcome. With its object gone it cannot be re-scoped into the pointer
   harvest it should have been, because there is nothing left to harvest
   from. Closing it as superseded is the only remaining shape; the
   disposition item carries the residue either way.
2. item-0031, void as written. Withdraw it, or re-found it on
   tree-internal material -- which would first require somebody to
   restate the routes from something that exists.
3. Whether the two precedent extracts stay in the corpus. They
   transcribe anchored sources, so they are legitimate; they were also
   made only because a dropped report cited those precedents, so nothing
   in the project now needs them.

---

## 10. Draft ledger entry

To be authored by steering against the tree rather than copied from
here; supplied as a shape, not as wording.

```yaml
  - id: ANN-20260727-76
    refs: [ANN-20260726-74, ANN-20260726-75, ERRATUM-5]
    date: 2026-07-27
    note: >-
      THE THREE REPORTS ARE DROPPED AS OBJECTS; THE item-0022 ARTIFACT
      DROP IS BOOKED FOUR APPLIES LATE AND THE INSTRUMENT THAT PRODUCED
      IT IS WITHDRAWN. Books the four commits since ANN-75 plus the
      roadmap apply, records the incident and its report, and carries
      the operator decision.
      NOTHING MATHEMATICAL MOVES. No Lean file, frozen block, anchor
      line or existing verdict changes; no bet is resolved or re-priced.
      No hash line is added, deliberately: anchoring freezes what it
      books, and the grade of the item-0022 artifact set is what the
      disposition item is for. The three report hash lines already in
      the append-only file STAY as history and now name objects with no
      standing.
      THE FINDING, in one line: a per-claim verdict register was built
      over the prose of three reports that no session can open, and the
      half of the material that had already influenced the roadmap was
      the half the item's own firewall made uncheckable.
      WHAT SURVIVES THE DROP survives for one reason -- somebody
      re-anchored it to a primary source instead of citing the report:
      the seven anchors and the identification layer, the seven
      extracts, the 1004.1072 shelf-gap finding and its routing to
      item-0028, the k=2 numerics, and the general-r reading of Pintz
      Lemma 2. WHAT DIES: every verbatim-claim row, item-0031 as
      written, and the two citation-policy decisions, which close as
      moot. ERRATUM-5 stays booked and unrepaired, with its referent now
      having no object anywhere.
      THE SEVENTH VERDICT-PROMOTION RECURRENCE. Five claim locations
      moved from STOP to CONFIRMED inside the repair pass by widening
      the anchor gate mid-item. B6 has been carried open since the
      third; item-0034 settles it.
      ONE ROW IS SUBSTANTIVELY RIGHT AND PROCEDURALLY UNREVIEWED. The
      general-r reading of Pintz Lemma 2 holds against the primary
      anchor; the addendum that landed it had no steering review and
      rode into a ratifying apply.
```

---

## 11. What this incident is worth

The experiment's charter says negative results are first-class and that
a documented failure map is a contribution. This is the cleanest failure
the project has recorded, because the mechanism is fully visible in the
tree: an artifact acquires standing from the process that touches it,
not from the evidence behind it, and a verification ritual applied to an
unreadable object manufactures standing rather than testing it. Four
sessions, two adversarial passes and a hash gate all ran correctly and
none of them could catch it, because every one of them was checking
fidelity to an object rather than the object's right to be there.

That is a finding about auditable LLM-assisted research, not about
Erdos 251, and it is worth writing up as such.
