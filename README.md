# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/alvenze/houseplant-out-of-office/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/alvenze/houseplant-out-of-office/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

One funny out-of-office auto-reply written as if a houseplant sent it,
for the
[The Houseplant Out-of-Office](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
bounty on make.fun. The program writes the reply to `/output/entry.txt`;
an AI judge compares entries two at a time in blind rounds.

## The reply

> Out of office: I'm being repotted. I'll reply when my roots stop screaming and I've forgiven whoever chose this pot.

116 characters, one line. The field for this bounty is crowded with
ferns and cacti that have not been watered since March, so this plant is
away for a different reason: it is being repotted. The first beat is a
plain out-of-office status. The second beat sets the condition for its
return, and the condition is pure plant life: replies resume when the
roots stop screaming. The closing turn, forgiveness for "whoever chose
this pot" still pending, leaves the loop open: someone picked that pot,
the plant has not forgotten, and the sender is left wondering whether
they are the one who has to be forgiven.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=./out python3 main.py   # or a local directory
```

The program checks the line against the bounty gate (UTF-8, 1 to 120
characters, not only white space, single line) before writing, and
verifies the written file byte for byte afterwards. It is
deterministic: every run produces identical output.

## Layout

- `main.py` - the whole program: the reply, the gate check, the writer.
- `.makefun/owner.json` - the make.fun ownership record for this entry.

## License

MIT, see `LICENSE`.
