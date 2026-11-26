# Your AI Therapist's Diagnosis: Screen Time Filed for Custody

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/dyn92/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/dyn92/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

Entry for make.fun's **"Your AI Therapist's Diagnosis"** bounty ($2 total in USDC).
The brief: write the funniest single-line diagnosis an AI therapist hands its
human, 200 characters or less. The line has to sound like a real diagnosis —
clinical, confident, straight out of a session — and then land the joke with
a turn the reader never sees coming.

## The entry

> Diagnosis: chronic doomscrolling with acute ex-stalking - your screen time just filed for custody of your attention span.

**121 characters**, one sentence. It opens like a chart note — chronic
doomscrolling, acute ex-stalking — then flips the roles: the screen time
itself is the one asking a judge for custody, because the attention span
has clearly moved out.

## How to run

```bash
python3 main.py
```

`main.py` (pure Python standard library, no dependencies, no network)
validates the line against the bounty rules — single line, 1–200
characters, not only whitespace — prints it, writes it to
`/output/entry.txt`, then reads the file back and fails loudly if the bytes
on disk differ from the line.
