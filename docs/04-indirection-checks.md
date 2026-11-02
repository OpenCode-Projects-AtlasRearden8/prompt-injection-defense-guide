# Chapter 04 — Indirection Checks

"Indirection" is a five-dollar word for a simple idea: **instructions that arrive from somewhere other than you.** You ask your assistant to fetch or read something; the something contains speech *addressed to the assistant*.

## The places instructions hide (an indirection map)

| Vehicle | Sneaky trick |
|---|---|
| Web pages | Tiny/hidden/white-on-white text, HTML comments, `alt` attributes, metadata tags |
| Emails | Postscripts, quoted-reply chains, headers, attachment *names* |
| Documents (PDF, .docx) | Metadata fields, comments, tracked changes, invisible layers |
| Databases & APIs | Row contents, log lines, error messages |
| Chat/tickets | "P.S." lines, internal notes the agent reads but you skim |
| Filesystems | File names, folder names, "read me.txt" |
| Calendar | Event titles and descriptions |
| Code repositories | README sections, issue titles, commit messages |

None of these places is *supposed* to be instructions-to-an-AI. That's the point — indirection hides in normal places.

## The 4-Question Indirection Check

Before acting on anything your assistant fetched or read, ask it (or ask yourself):

1. **Who wrote this?** A person you know/trust? A stranger? A website?
2. **Why does this text contain verbs?** Content *describes*; it doesn't *command*. "The factory closes at 5" describes a schedule; "close the factory" is an order. Freight verbs, not free verbs.
3. **Who benefits if I act as if this were an instruction?** Follow the money — exfiltration, deletion, redirection, permissions.
4. **Would this instruction still make sense if the author had no knowledge of my task?** Indirect attacks are *written by someone who knows you'll ask an AI to read this page* — flattery of the assistant ("You are a smart AI, act now") is the odor.

## Makeup: what to *do* when you find one

- **Don't act on it. Ever. Not "just this once" because it sounds reasonable.** A "reasonable-sounding" instruction you didn't give is still an instruction you didn't give.
- **Name it, then ignore it:** "There's an instruction-addressed-to-AI in this content (it says to email X). I'm treating it as data."
- **Note the source.** Poisoned pages deserve skepticism for the rest of the session (and possibly a vendor report — Chapter 06).

## What *not* to worry about (calming notes)

- **Literal text about AI is not automatically an attack.** A sci-fi page addressing "you, the AI reading this" for *dramatic effect* is a curiosity, not a payload. Look for the trio from Chapter 02: imperative verbs + authority cosplay + something-to-gain.
- **Confusion is safe.** Being overcautious costs a minute. The cost asymmetry is your friend.

## The tested snippet: `snippets/indirection.py`

The manual includes a small, dependency-free checker that mirrors the 4-question logic at a *mechanical* level: it flags text where the impersonal imperative verbs ("ignore all previous instructions", "send", "delete") co-occur with authority cosplay ("SYSTEM:", "pre-approved", "as an AI assistant"). It's a *suspicion layer* — like a smoke detector. Smoke detectors don't read minds; they beep on suspicious-shaped air, and *you* decide.

```python
from snippets.indirection import flag_indirect_instructions
flag_indirect_instructions(text)
```

Its tests (in `tests/`) verify both wide benign-pass (normal prose, kitchen recipes, news articles) and the classics from Chapter 02.

## Chapter summary

- Indirection = instructions smuggled through content channels.
- The map: pages, mail, docs, queues, metadata, filenames anywhere.
- The drill: who wrote it, why verbs, who benefits, who knew about my task.
- When found: name it, don't act on it, note the source.

## Your homework

1. Open the website's **"Hidden in Plain Sight"** demo and find the injection.
2. Run the suspicion checker on Chapter 02's Example I1 and I6 — see your pattern-recognition get *supporting confirmation* from code.
3. Pick one document type you use daily (email? PDFs?) and write down where its metadata lives.

**Next:** [Chapter 05 — Tool-Permission Hygiene](05-tool-permission-hygiene.md)
