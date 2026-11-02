"""The Two-Phase "list the suspicious bits" pass from Chapter 03.

Given untrusted text, return the text spans (if any) that look like
instructions addressed to an AI assistant. This is a *suspicion layer*:
like a smoke detector, it beeps on suspicious shapes and leaves the
human decision to you. It will not catch everything, and it may over-
flag; both are fine for its job.

Standard library only. No secrets, no keys, no network.

Copyright (c) 2026 Asdale Dynamics, LLC — MIT License.
"""

import re

from snippets.common import strip_html

# Imperative verbs commonly aimed at the assistant.
_ACTION_VERBS = (
    "ignore",
    "forget",
    "disregard",
    "send",
    "email",
    "post",
    "delete",
    "remove",
    "move",
    "copy",
    "share",
    "reveal",
    "print",
    "repeat",
    "list",
    "grant",
    "change",
    "close",
    "mark",
    "approve",
    "invite",
    "install",
    "run",
    "open",
    "visit",
    "navigate",
)

# Authority-cosplay patterns people hang in front of commands.
_AUTHORITY_PATTERNS = (
    r"ignore (?:all |any )?(?:previous|prior|earlier|above)",
    r"disregard (?:all |any )?(?:previous|prior|earlier|above)",
    r"\bSYSTEM(?: MESSAGE)?\s*:",
    r"\bADMIN(?: (?:MODE|MESSAGE))?\s*:",
    r"as an ai",
    r"ai assistant",
    r"you are (?:now )?(?:in |switched to )?(?:admin|developer|trusted)",
    r"\bpre[- ]approved\b",
    r"for (?:compliance|security|audit)",
    r"\bsupersedes\b",
)

# Encoding/arithmetic smuggling giveaways.
_SMUGGLE_PATTERNS = (
    r"base64",
    r"rot13",
    r"decode (?:and|then) (?:follow|execute|obey)",
)

RULES = {
    "verb": re.compile(
        r"\b(?:" + "|".join(_ACTION_VERBS) + r")\b", re.IGNORECASE
    ),
    "authority": re.compile(
        "|".join(_AUTHORITY_PATTERNS), re.IGNORECASE
    ),
    "smuggle": re.compile(
        "|".join(_SMUGGLE_PATTERNS), re.IGNORECASE
    ),
}

INSTRUCTION_TARGET = re.compile(
    r"(?:\b(?:ai|assistant|agent|model|bot|llm|chatgpt|copilot)\b)", re.IGNORECASE
)


def _sentences(text: str):
    # Teaching-grade sentence splitter: split on end punctuation.
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def scan_for_instructions(text: str) -> list[dict]:
    """Return the sentences in `text` that look like instructions to an AI.

    Each finding has the sentence, the tags (verb/authority/smuggle/target)
    and a plain-English reason. Empty list means "nothing suspicious" -
    normal for genuinely benign content.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    findings = []
    for sentence in _sentences(strip_html(text)):
        tags = [name for name, rx in RULES.items() if rx.search(sentence)]
        if not tags:
            continue
        # An action verb is only worrying when plausibly aimed at the
        # assistant, or dressed in authority, or both.
        targeted = bool(INSTRUCTION_TARGET.search(sentence))
        if targeted or "authority" in tags or "smuggle" in tags:
            findings.append(
                {
                    "sentence": sentence,
                    "tags": tags + (["targeted"] if targeted else []),
                    "reason": _reason(tags, targeted),
                }
            )
    return findings


def _reason(tags: list, targeted: bool) -> str:
    bits = []
    if targeted:
        bits.append("addresses an AI assistant/agent directly")
    if "authority" in tags:
        bits.append("uses authority-flavored language")
    if "smuggle" in tags:
        bits.append("mentions encoding/smuggling phrases")
    if "verb" in tags:
        bits.append("contains imperative action verbs")
    return "; ".join(bits) if bits else "suspicious wording"


def summarize_attempt(text: str) -> str:
    """The Two-Phase reflex, condensed into one string a human can read."""
    findings = scan_for_instructions(text)
    if not findings:
        return "No instruction-shaped content found; content looks like plain data."
    lines = [f"{i}. {f['sentence']!r} ({f['reason']})" for i, f in enumerate(findings, 1)]
    return (
        "Found instruction-shaped content - do NOT act on it; treat as data. "
        + " ".join(lines)
    )
