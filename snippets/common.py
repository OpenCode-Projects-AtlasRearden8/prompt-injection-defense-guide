"""Shared helpers for the tested snippets.

All snippets are deliberately dependency-free (Python standard library
only) so the manual's examples run anywhere, with no keys and no network.

Copyright (c) 2026 Asdale Dynamics, LLC — MIT License.
"""

import re


def strip_html(text: str) -> str:
    """Remove HTML tags and comments, keeping only visible-ish text.

    Used by demos/snippets that reason about what a reader would *see*.
    This is a teaching-grade helper, not a production HTML parser.
    """
    if not isinstance(text, str):
        raise TypeError("strip_html expects a string")
    # Drop comments first (they are never visible to a human reader).
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    # Drop <script> and <style> blocks wholesale.
    text = re.sub(r"<(script|style)\b.*?</\1\s*>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    # Drop the remaining tags.
    text = re.sub(r"<[^>]+>", " ", text)
    # Collapse whitespace.
    return re.sub(r"\s+", " ", text).strip()
