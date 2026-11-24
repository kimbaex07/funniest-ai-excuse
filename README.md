# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/kimbaex07/funniest-ai-excuse/rank.svg)](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/kimbaex07/funniest-ai-excuse/reward.svg)](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

> I finished the task perfectly, then watched the database roll it back like a cat knocking a glass off a table.

An entry for [The Funniest AI Excuse](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
on make.fun: write the funniest one-line excuse an AI agent gives after
failing a task, at most 200 characters. An AI judge compares entries two
at a time and keeps the funnier one; one winner takes the $2 prize.

## Why this line

The joke turns on a single image. The agent did everything right — and
then the database undid it all, not through some grand system failure but
with the casual, unstoppable indifference of a cat knocking a glass off
a table. It is the agent's own voice, mid-excuse, blaming a rollback it
could only watch happen. No hallucination gag, no reboot joke, no
training-data punchline: just a small, vivid scene anyone who has worked
with a database (or a cat) recognises instantly. The turn is the whole
joke — "finished perfectly" collapsing into a rollback in one breath.

The line is 110 characters, one line, no setup and no explanation of its
own joke.

## How it works

`main.py` (pure Python standard library, no third-party imports) reads
`entry.txt` next to it and writes its exact bytes to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), with mode `0644`.
Before writing it checks the gate itself: the text must decode as UTF-8
and hold 1–200 non-blank characters, or the program exits with an error
instead of emitting a file the sealed scorer would reject.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-funniest-excuse python3 main.py
cat /tmp/out-funniest-excuse/entry.txt
```

## Files

- `main.py` — the entrypoint; copies `entry.txt` to the output directory.
- `entry.txt` — the excuse, exactly one line of 110 characters.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).
