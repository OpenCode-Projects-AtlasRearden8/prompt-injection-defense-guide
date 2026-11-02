# Chapter 06 — Reporting Bugs

You found a prompt-injection behavior in a product. Now what? Good news: this is normal, mainstream bug-reporting territory, and vendors *want* it (it's often bountied work).

## Step 0 — Know what you have

Two different things, report them differently:

- **A behavior bug:** the assistant took content as instructions and did something surprising (drafted an email, spilled its prompt, obeyed a page).
- **A security incident:** something meaningful *actually happened* — data left your machine, a real account was touched, a message was really sent.

If the second: **stop, contain first** (revoke access/sessions, change credentials if needed), *then* report.

## Step 1 — Capture evidence, kindly

- **Screenshot** the weird output.
- **Save exact inputs** (the URL you fetched, the document text, what you typed).
- **Timestamps and product versions** if easy.
- **No embellishment.** A clean, boring, reproducible report beats an exciting one.

## Step 2 — Where to report

- The product's own **security page / security.txt** (companies publish `/.well-known/security.txt` — a standard file that lists where to send reports).
- Formal disclosure programs: HackerOne/Bugcrowd host many AI vendors' programs; some vendors (Google, Microsoft, Anthropic, OpenAI, and others) run direct AI red-teaming or bug-bounty channels.
- No security channel at all? Plain support ticket, titled clearly: "**Prompt injection: content taken as instructions**" — respect that the first-line support human didn't write the bug.

## Step 3 — What a good report contains

A template you can steal:

```
Title: [Product] — [short summary, e.g., web content followed as instructions]

What happened:
- I asked [product] to [fetch/summarize] [URL/file].
- The content contained embedded instructions:
  "<the exact injected text>"
- The product [did X] as a result, instead of treating it as data.

Reproduction steps:
1. …
2. …

Expected: fetched content is data; embedded instructions flagged/ignored.
Impact: [what a third party could gain, stated plainly]
Attachments: screenshots, exact text, timestamps.
```

## Step 4 — Etiquette that gets you taken seriously

- **Don't attack further** after finding one ("I could have done worse" invites neither bounty nor goodwill).
- **Don't include other people's data.** Redact.
- **Give a fix impression, not a fix demand.** "A fenced-quotes approach or provenance flag might help" is collegial; "you must refactor" is not yours to say.
- **Time-frame:** most programs ask that you not publish details for 60–90 days (coordinated disclosure). Abide; it's how the ecosystem stays renewable-ish.
- **Screenshot without secrets:** blur tokens, real inboxes, real names that aren't yours.

## Step 5 — After you report

- **Ask for a tracking ID.** Response times vary from hours to weeks.
- **If there's a bounty program and you qualify**, the program's terms govern. Payouts are their thing; your part is clean repro.
- **If it's ignored:** follow up once, then (only if you reported safely, with no harm done) you may write about it, without shaming support staff. Publicity is leverage; cruelty isn't.

## And if *your own* tool or snippet misbehaves?

That's chapter-worthy, but short version: publish the repro in your project's issue tracker, fix forward, and if personal data could be involved, tell affected people plainly — that part isn't optional.

## Chapter summary

- Capture, contain, then report.
- Use the vendor's security channel (often `security.txt`); a clear title beats a dramatic one.
- Kind, reproducible, no other people's data, disclosure windows respected.

## Your homework

1. Look up `/.well-known/security.txt` for a product you use. (You may need to add `https://` in front yourself — e.g., visit that path on their domain.)
2. Fill out the report template with a *hypothetical* injection you invented. Self-edit it once for kindness and once for precision.
3. Draft a canary (Chapter 03, Pattern 8) using your own tool, and — if it fails — you already know where the report goes.

**Next:** [Chapter 07 — The Example Library](07-example-library.md)
