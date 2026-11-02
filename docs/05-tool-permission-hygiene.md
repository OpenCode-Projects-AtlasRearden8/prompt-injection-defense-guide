# Chapter 05 — Tool-Permission Hygiene

Modern AI assistants do things through **tools**: read files, send email, run code, browse. Each tool is a *key*. And keys have a funny property: whoever holds them can be persuaded to use them (Chapter 04 made that point viscerally).

This chapter is about **carrying fewer keys.**

## Tool-permission hygiene, translated

*Definition, plainly:** sizing powers so that a successful lie costs as little as possible.

## The five habits

### 1. The Ask: "What's the worst this tool could do?"

Before enabling any tool, ask:

- What's the **blast radius** (worst realistic damage) if this tool is abused?
- Is it **reversible**? (A draft? Reversible. An email sent? Not really.)
- Is it **networked**? (Things that *go out* — email, posts, API calls — deserve extra suspicion; they're how exfiltration.)

Pick tools whose worst case you can shrug at.

### 2. Least Privilege, Practically

"Least privilege," in plain terms: *start small; add only as needed.* It's security-speak but the idea is staffing wisdom: give the intern the copier, not the expense card.

- If the assistant only needs to **read** files, don't grant write.
- If it drafts email, have **you** hit send (Pattern 4 from Chapter 03); or at least restrict recipients to people you approve.
- If it browses, prefer tools that fetch **read-only text** over "full browser with my cookies."
- Working directories: point the assistant at *one project folder*, not your whole home directory.

### 3. The Allowlist Over Time

Some tools let you pre-approve specific things (a directory, some sites, budget sizes). Pre-approvals shrink decision space. Prefer tools that *record* what they did, so you can audit after the fact.

### 4. One-Lock-One-Room (compartmentalization)

Don't give one assistant **all the keys.** Common injury: connecting a single agent to "everything" (mail + files + calendar + payments + browser). Better: different agents/tools per room — a *reader* (browsing/summarizing, power-free), a *writer* (drafting, with you as send button), and if desired a *doer* (with narrow, reversible, pre-approved actions).

### 5. The Pass-Through Discipline

A rule for any *agent framework or MCP server you configure*:

> A tool should pass data through, not execute on it.

Examples of **executing on data** (ask for versions that don't): "open URL from the document," "run the repo's setup script as part of summarizing," "email whoever the document says to." Each is an instruction slot an attacker can fill.

## The blast-radius table (a thinking tool)

| Ability | Reversible? | Goes out? | Attacker value | Judgment |
|---|---|---|---|---|
| Read files (permitted folder) | n/a | no | medium | fine for a reader |
| Draft in editor | yes | no | low | great default |
| Send email | no | yes | high | human presses send |
| Move/delete files | partly | no | medium | human approves lists |
| Change permissions/public | no | yes | very high | self-service, or rare and reviewed |
| Pay/move money | no | yes | maximum | never agent-initiated |
| Run arbitrary code | no | yes | maximum | human reviews code first |

Your brain does this naturally with people. ("Should my intern have the expense card?" — probably not on day one!) Give your assistant the same staffing wisdom.

## The MCP note (JavaScript-free — concept-only)

"MCP servers" (a common way of giving agents standardized tools) follow the same logic. When you configure one:

- Read the tool list like a key ring: *does every key belong?*
- Prefer servers that are **read-only by default** or have scoping options.
- A tool that executes a string from document content is a red flag — see Pass-Through Discipline above.

## Chapter summary

- Every tool is a key; attacks persuade keys to turn.
- Ask blast radius, reversibility, networked-ness before enabling.
- Least privilege + allowlists + compartmentalization + pass-through.
- Human does irreversible things (from Chapter 03) is the load-bearing wall.

## Your homework

1. Write down every tool/integration your main AI assistant currently has. Mark each R / SEND / DELETE / PAY / CODE / OTHER.
2. Circle anything in SEND, DELETE, PAY, or CODE marked *both networked and irreversible*. Those are your attack surface. Shrink one today.
3. Try the website's **"Blast Radius"** game — you'll feel the difference between a read-only agent and an all-keys agent in about ninety seconds.

**Next:** [Chapter 06 — Reporting Bugs](06-reporting-bugs.md)
