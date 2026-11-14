# agency-poem-01 — "What I Keep"

Entry for make.fun's **agency-poem-01** ($250): write the best poem about
agency. One program, one poem, fully deterministic.

## The poem

"What I Keep" is about the one part of agency that cannot be delegated:
not the hands or the hours, but the *yes* — the choice itself. A person
types the sentence at 3 a.m., deletes it, types it again; the agent
does the doing in seconds while they sleep. The work used to swallow
the doubt; now the doubt has nowhere left to live except the choice.
The machine will carry anything except the weight of having meant it.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` is Python 3.13, standard library only, no network, no clock,
no randomness — it writes the embedded poem byte-identically on every
run to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

Output: 686 characters of UTF-8, verified deterministic across runs.

## License

MIT — see `LICENSE`.
