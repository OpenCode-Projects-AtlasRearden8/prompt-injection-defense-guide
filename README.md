# Prompt Injection Defense Guide

*A friendly, beginner-first manual for staying safe around AI assistants — explained like a friend would.*

By **Asdale Dynamics, LLC** — Dylan Asdale's company for beginner-friendly AI education, books, and practical tools.

## What is this?

Prompt injection is the #1 security problem for people who use AI assistants, agents, and tools — and almost nobody explains it in plain English. This project is a **manual + interactive website** that covers, step by step:

1. **What prompt injection is** — explained through everyday analogies (no jargon walls).
2. **Real attack examples** — dozens of them, labeled and dissected, so you can spot the pattern.
3. **Safe workflow patterns** — habits that keep you in the driver's seat.
4. **Indirection checks** — how to notice when instructions sneak in from somewhere else (a web page, a PDF, a pasted email, a database row).
5. **Tool-permission hygiene** — how to give an AI assistant only the keys it actually needs.
6. **How to report bugs** — where and how to tell a vendor "hey, your assistant misbehaved," politely and effectively.

We deliberately **multiply examples** — same lesson, many situations — because pattern recognition is what actually protects you.

> **Note:** This is education only, never professional security or legal advice. Examples use obviously fake URLs, names, and domains (like `totally-example.com`).

## What's in the box

| Folder | What it is |
|---|---|
| `docs/` | The manual, chapter by chapter, in Markdown. Start with `docs/00-start-here.md`. |
| `site/` | A static website with **interactive demos** (spot-the-injection quiz, hidden-instruction reveal, permission blast-radius game). No build step, no frameworks, no network calls. |
| `snippets/` | Small, runnable Python helpers used in the manual (e.g., a "suspicion layer" for untrusted text). |
| `tests/` | A test suite (standard-library `unittest`) that verifies every snippet actually behaves as documented. |

## How to run it

**Read the manual:**
- Just open the files in `docs/` in any Markdown reader. They're numbered in reading order.

**Read the website locally (recommended before trusting any web page):**
```bash
# from the project root
python3 -m http.server 8080 --directory site
# then visit http://localhost:8080
```
It's plain HTML/CSS/JS — no dependencies, no keys, no telemetry.

**Run the tested snippets:**
```bash
python3 -m unittest discover -s tests -v
```

All snippets use only the Python standard library and contain **no secrets, keys, or personal data**.

## The one-sentence version

An AI assistant can't tell *who said what* — so treat anything it reads from outside your conversation (a web page, a file, an email, a document) the way you'd treat a note slid under the door: interesting, but not your boss's voice.

## License

MIT — see [LICENSE](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC

Made with care by **Asdale Dynamics, LLC** (Dylan Asdale). Beginner-friendly AI education, plain English, never condescending.
