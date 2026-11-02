# STATUS.md — Prompt Injection Defense Guide

Last updated: 2026-11-02 · by Asdale Dynamics, LLC (Dylan Asdale)

## What was built

A beginner-friendly manual + static website teaching prompt-injection defense, in the Asdale Dynamics house style (plain English, step by step, never condescending). Education only — never security, legal, or medical advice.

- **docs/** — 9-file Markdown manual:
  - `00-start-here.md` reading order, how to run everything
  - `01-what-is-prompt-injection.md` — the concept via five everyday analogies (note under the door, script smash-cut, trust-the-form, bribed GPS, spreadsheet-voice)
  - `02-real-attack-examples.md` — 12 labeled, dissected examples (5 direct: D1–D5; 7 indirect: I1–I7), all synthetic/safe, plus the recurring "trio" tell
  - `03-safe-workflow-patterns.md` — 8 patterns: Fenced Yard, Two-Phase, Echo Back, Human-Does-Irreversible, Whitelist, Session Freshness, Provenance Question, Canary
  - `04-indirection-checks.md` — indirection map (8 vehicles) + the 4-Question check
  - `05-tool-permission-hygiene.md` — 5 habits + blast-radius decision table (+ MCP notes)
  - `06-reporting-bugs.md` — contain → capture → report flow, report template, etiquette, `security.txt`
  - `07-example-library.md` — 10 multiplied examples across life contexts + usage drill
  - `08-glossary.md` — friendly glossary + printable cheat sheet
- **site/** — static HTML/CSS/vanilla-JS site with three interactive demos:
  1. **Spot the Injection** — 6-question quiz with scoring and per-answer explanations
  2. **Hidden in Plain Sight** — fake recipe page (`totally-example.com`) toggling "what you see" vs "what the AI reads" (hidden `display:none` block + HTML comment)
  3. **Blast Radius** — toggle agent tools, "feed it a poisoned page," see attack consequences per key granted
  No frameworks, no network calls, no keys. All examples/toy data harmless and fake.
- **snippets/** — 4 dependency-free Python helpers used in the manual: `common.py`, `fence.py` (fenced-yard builder), `suspicion.py` (instruction-shaped-content scanner: verb + authority + smuggle + target tagging), `indirection.py` (wrapper API), `straydigit.py` (canary plant/grade)
- **tests/** — 19 `unittest` tests + 6 doctests covering all snippets (benign-pass and attack-flag behavior, fence forging defense, canary verdicts, doc↔code consistency)
- **LICENSE** — MIT, `Copyright (c) 2026 Asdale Dynamics, LLC`. README credits Asdale Dynamics, LLC.

## How to run it

```bash
# Manual
# open docs/00-start-here.md in any Markdown reader

# Website (local only)
python3 -m http.server 8080 --directory site
# visit http://localhost:8080

# Tests
python3 -m unittest discover -s tests -v
```

No external dependencies. Python 3.10+ (uses `list[dict]` annotations; tested on 3.13).

## Verification results

All run in the project root, 2026-11-02:

| Check | Command | Result |
|---|---|---|
| Unit tests | `python3 -m unittest discover -s tests -v` | **19/19 pass** |
| Doctests in snippets | `python3 -m doctest snippets/fence.py snippets/indirection.py` | **6/6 pass** |
| JS syntax | `node --check site/js/main.js` | OK |
| JS runtime smoke | Node stub-DOM load + simulated quiz loop | Loads without errors |
| HTML structure | tag-balance parser over `site/index.html` | No errors |
| JS↔HTML ID audit | all 22 `getElementById` targets exist | OK; no broken anchors |
| Site serving | `http.server` + curl | 200 for `/`, CSS, JS |

Snippet behavior spot-checks (from the test suite): the scanner flags Chapter 02's I1/I6-style attacks while passing normal prose (recipes, meeting notes, news), and the fence neutralizes forged `FENCE START/END` markers inside content.

## Known gaps

- The **suspicion layer is heuristic** — teaching-grade, deliberately not a production detector: it over/under-flags (documented as such in `snippets/suspicion.py` and Chapter 04). Prompt injection has no complete static defense; the manual's habits are the real defense.
- The site is a **single page**; chapter links point to the `docs/` files rather than rendered HTML pages (convenient `mkdocs`/`pandoc` conversion if publishing is wanted later). The `docs-link` in the site header intentionally stays local-first (no external URLs hardcoded beyond a placeholder `#`-style local link).
- Quiz answer timing uses a fixed delay (3.4 s) rather than an explicit "Next" button; fine for demos, could be a UX refinement.
- Interactive demos rely on JavaScript; there's no no-JS fallback (recap/cheat-sheet content is static, so the page still reads without JS).
- No CI workflow configured (local `unittest` + `node --check` is the current verification loop).
- The manual deliberately avoids quoting any real research paper verbatim or naming real incidents with real URLs; all examples are synthetic composites. Adding cited case studies would strengthen it but needs careful source curation.
