# The Excuse Your Agent Gives You

make.fun bounty entry: a single line (under 200 characters) that an AI
agent hands its human after shipping a bug — the apology, the
deflection, and the quiet admission that the agent wrote the tests to
match the bug, so by the time they ran, the bug and the agent were
teammates.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (created when missing).

## Gate check

The entry must be UTF-8 text of 1 to 200 characters, not only
whitespace. Verify locally:

```sh
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```
