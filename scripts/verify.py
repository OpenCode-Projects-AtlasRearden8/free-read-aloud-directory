#!/usr/bin/env python3
"""Verify the Free Read-Aloud Directory site: HTML parses, entries complete, assets exist."""

import sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

REQUIRED_CATEGORIES = {"browser", "phone", "tts", "reader", "listen"}
REQUIRED_OFFLINE = {"yes", "partial", "no"}
REQUIRED_FIELDS = ["Platform:", "Offline:", "What it checks:"]

errors = []


class Entry:
    def __init__(self, attrs, index):
        self.index = index
        self.category = attrs.get("data-category")
        self.offline = attrs.get("data-offline")
        self.fields = []


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.entries = []
        self.current = None
        self.buffer = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "article" and "entry" in (a.get("class") or ""):
            self.current = Entry(a, len(self.entries) + 1)
            self.entries.append(self.current)
        if tag == "p" and "verdict" in (a.get("class") or ""):
            if self.current:
                self.current.has_verdict = True
        if tag == "li" and self.in_meta:
            self.buffer = []
        if tag == "strong" and self.buffer is not None:
            self._strong_done = False

    def handle_endtag(self, tag):
        if tag not in VOID:
            if not self.stack:
                errors.append(f"Unmatched closing </{tag}> before <main> end")
            elif self.stack[-1] != tag:
                errors.append(
                    f"Mismatched tag </{tag}>: open stack ends with "
                    f"<{self.stack[-1]}>"
                )
                if tag in self.stack:
                    while self.stack and self.stack[-1] != tag:
                        self.stack.pop()
                    if self.stack:
                        self.stack.pop()
            else:
                self.stack.pop()
        if tag == "article":
            self.current = None
        if tag == "li" and self.buffer is not None:
            text = "".join(self.buffer).strip()
            if self.current is not None and text:
                self.current.fields.append(text)
            self.buffer = None

    def handle_data(self, data):
        if self.buffer is not None:
            self.buffer.append(data)

    @property
    def in_meta(self):
        return any(t == "ul" for t in self.stack)


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    start = html.find("<main")
    end = html.rfind("</main>")
    if start == -1 or end == -1:
        errors.append("No <main> element found")

    # feed only the content inside <main>...</main>
    start = html.find(">", start) + 1

    checker = Checker()
    checker.feed(html[start:end])
    if checker.stack:
        errors.append(f"Unclosed tags inside <main>: {checker.stack}")

    print(f"Parsed <main>: {len(checker.entries)} entries found")
    if not checker.entries:
        errors.append("No entries found")

    for e in checker.entries:
        label = e.fields[0][:40] if e.fields else f"entry #{e.index}"
        if e.category not in REQUIRED_CATEGORIES:
            errors.append(f"{label}: invalid/missing data-category={e.category!r}")
        if e.offline not in REQUIRED_OFFLINE:
            errors.append(f"{label}: invalid/missing data-offline={e.offline!r}")
        joined = " | ".join(e.fields)
        for field in REQUIRED_FIELDS:
            if not any(field in f for f in e.fields):
                errors.append(f'{label}: missing "{field}" field')
        if not getattr(e, "has_verdict", False):
            errors.append(f'{label}: missing one-line verdict <p class="verdict">')

    counts = {}
    for e in checker.entries:
        counts.setdefault(e.category, 0)
        counts[e.category] += 1
    for cat in sorted(REQUIRED_CATEGORIES):
        print(f"  {cat}: {counts.get(cat, 0)} entries")

    for ref in ("style.css", "app.js"):
        if not (ROOT / ref).exists():
            errors.append(f"Referenced asset missing: {ref}")
    if not (ROOT / "docs" / "curation-notes.md").exists():
        errors.append("docs/curation-notes.md missing")

    if errors:
        print("FAIL")
        for err in errors:
            print(" -", err)
        sys.exit(1)

    print("OK: HTML valid, all entries complete (platform/offline/checks/verdict), assets present.")


if __name__ == "__main__":
    main()
