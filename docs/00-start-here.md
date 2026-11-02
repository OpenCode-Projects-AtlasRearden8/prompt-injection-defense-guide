# Start Here

Welcome! This manual teaches you about **prompt injection** — the single most important safety idea for anyone who uses AI assistants, agents, or AI-powered tools — and it promises three things up front:

1. **Plain English.** No jargon without a friendly translation right next to it.
2. **Step by step.** Each chapter builds on the last one.
3. **Never condescending.** If something is confusing, that's on the explanation, not on you.

## How to use this manual

Read in order. Each chapter ends with **"Your homework"** — tiny, safe exercises (no attacking anything, just spotting patterns).

| Chapter | Title | In one line |
|---|---|---|
| 01 | [What Prompt Injection Is](01-what-is-prompt-injection.md) | The big idea, through everyday analogies. |
| 02 | [Real Attack Examples](02-real-attack-examples.md) | Dozens of attacks, labeled and dissected. |
| 03 | [Safe Workflow Patterns](03-safe-workflow-patterns.md) | Habits that keep you in the driver's seat. |
| 04 | [Indirection Checks](04-indirection-checks.md) | Spotting instructions that sneak in sideways. |
| 05 | [Tool-Permission Hygiene](05-tool-permission-hygiene.md) | Give the assistant only the keys it needs. |
| 06 | [Reporting Bugs](06-reporting-bugs.md) | Telling vendors about misbehavior, the kind way. |
| 07 | [The Example Library](07-example-library.md) | The same lesson, multiplied across many situations. |
| 08 | [Glossary & Cheat Sheet](08-glossary.md) | The words, and what to do when it's Tuesday and you're tired. |

## The companion website

The `site/` folder has **interactive demos**: a spot-the-injection quiz, a hidden-instructions reveal, and a permission blast-radius game. Run it locally:

```bash
python3 -m http.server 8080 --directory site
# visit http://localhost:8080
```

## The tested snippets

Small Python helpers mentioned in the manual live in `snippets/`, and every one is covered by the test suite in `tests/`. Verify them yourself:

```bash
python3 -m unittest discover -s tests -v
```

No API keys, no accounts, no network. Everything runs on your machine.

---

Ready? Head to [Chapter 01 — What Prompt Injection Is](01-what-is-prompt-injection.md).
