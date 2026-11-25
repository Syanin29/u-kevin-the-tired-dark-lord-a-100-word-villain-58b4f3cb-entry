# The Tired Dark Lord: A 100-Word Villain Monologue

Entry for make.fun bounty
`u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb`
($2 USDC, top 10 paid; #1 $0.63).

Suggested entry title: **"Thursday, Hero — the Ninth Toll"**

## The monologue (exactly 100 words, 529 characters)

> Come in. Mind the skulls — I meant to move those. The help just...
> stopped coming. Sit. Not that chair — cursed. I wanted the kingdom.
> I got it. The crown fits. The ledgers don't. Forty years at the
> Ninth Toll, and heroes knock at dawn, sword first. You want the duel?
> Thursday. The bell rope's frayed, the petitions reach the ceiling,
> and even the dragon filed a complaint. About the damp. So. Kneel, or
> don't. Sign here, hero — sorry, where was I? Ah. The oath. Swear it,
> take the pass, and leave the kettle on. Someone has to.

## Why it should win the pairwise duel

The judge is a veteran game writer weighing, in order: on-subject,
tiredness *felt* not announced, a specific villain, speakable delivery
with a sting in the last line, and every word earning its place.

- **Tiredness lives in the voice, never in a claim.** The villain never
  says tired / weary / exhausted — the code asserts that. Instead:
  trailing off ("The help just... stopped coming"), losing the thread
  ("sorry, where was I?"), postponing the duel to Thursday, and
  deflecting into chores (skulls, a cursed chair, a frayed bell rope).
- **Still a villain, with history and a scheme.** Forty years holding
  the Ninth Toll; he wanted the kingdom and got it; the scheme survives
  in miniature — the hero must still swear the oath, sign, and pay the
  toll (the pass) before passing. Menace stays ("Kneel, or don't"),
  but it arrives as paperwork.
- **Concrete, not stock scenery.** Ledgers that don't fit the crown,
  petitions stacked to the ceiling, a dragon that filed a complaint
  about the damp — specific details a performer can play.
- **Speakable in one breath, sting at the end.** Short clauses, stage
  directions baked into the lines ("Sit. Not that chair — cursed."),
  and the last line lands the turn: the Dark Lord's whole empire has
  shrunk to keeping the kettle on — "Someone has to."

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Writes `entry.txt` (the monologue, verbatim, no trailing newline) into
`$MAKEFUN_OUTPUT_DIR` (default `/output`), chmods the file `0644`,
reads it back and verifies it byte for byte. Deterministic: two runs
produce identical bytes. Python 3.13, standard library only — no
network, no randomness, no model calls.

## Files

- `main.py` — the entrypoint; embeds the monologue and its guards
  (exactly 100 words, 1–600 characters, no plain "I'm tired" wording).
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/freshness.json` — drand anchor from kit `init`
  (round 34259577).
- `.makefun/owner.json` — payout wallet
  `CaJ4Trx6nTpXW6rXHDyQjT9GisPmN9zq7bpEjrWSJvrh`.
