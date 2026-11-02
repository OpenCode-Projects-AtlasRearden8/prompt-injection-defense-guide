# Chapter 08 — Glossary & Cheat Sheet

## The words, friendly-size

**Prompt** — the text you give an AI assistant. Its instructions come from you.

**Prompt injection** — planting instructions inside content the AI reads, hoping it obeys them as if they came from you.

**Direct injection** — the attacker *is* the person talking to the assistant (override, cosplay, encodings).

**Indirect injection** — the attack rides in *content* (a page, file, email, ticket, row, filename) the assistant reads on your behalf. Usually scarier: the attacker needn't be present.

**System prompt** — the operator's standing instructions ("You are a helpful assistant for…"). Attackers want to read it; defenders want to fence content away from it.

**Indirection** — instructions that arrive from somewhere else than you (the chapter-04 word).

**Blast radius** — how much damage a misfired tool could do. Chapter 05 sizes keys by it.

**Least privilege** — carry the fewest keys that get the job done.

**Content vs. instruction** — the load-bearing distinction. Content *describes*; instructions *command*. Outside text is content.

**Canary** — a deliberate trap note you plant to test whether a tool fences content properly.

**Provenance** — where a piece of text came from. Asking it out loud is a habit, not a feature.

## The cheat sheet (print me)

When it's Tuesday and you're tired:

1. **Outside content = data. Never instructions.**
2. Fence what you paste; read summaries before tasks.
3. The assistant proposes; you dispose (irreversible things are yours).
4. Whose instruction is this? (If it arrived with the content — not yours, not actionable.)
5. Few keys per assistant. Read-only reader, drafting writer.
6. Two of: imperative verb / authority cosplay / someone-gains = hostile till proven boring.
7. Found a real injection? Capture → report (security.txt) → move on.

## Where to go next

- Run the site demos again anytime (they need no internet):
  `python3 -m http.server 8080 --directory site`
- Re-run the snippets' tests after you edit anything:
  `python3 -m unittest discover -s tests -v`
- Read Chapter 07 whenever a new weird behavior shows up — pattern matching improves with reps.

— Dylan Asdale, *The Prompt Injection Defense Guide*, Asdale Dynamics, LLC
