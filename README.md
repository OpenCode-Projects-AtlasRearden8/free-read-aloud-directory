# Free Read-Aloud Directory

A static, no-build directory of **free text-to-speech and read-aloud helpers**
for readers who prefer listening: browser read modes, phone equivalents, free
TTS apps, and e-readers with synthetic narration. Each entry lists its
platform, an offline flag, practical "what to check" items, and a one-line
plain-English verdict.

This project is distinct from the sibling guides **ai-narration-choices-guide**
(audiobook narration choices for authors) and **free-large-print-tech-kit**
(print and large-print accessibility).

## Run it

No build step and no dependencies. Either:

- **Open it:** double-click `index.html`, or
- **Serve it locally:**

  ```bash
  python3 -m http.server 8000
  # then visit http://localhost:8000
  ```

## Contents

- `index.html` — the directory (5 sections, 18 curated entries)
- `style.css` — styling, print-friendly
- `app.js` — category filters and an "offline only" toggle
- `docs/curation-notes.md` — selection criteria, exclusions, review cadence

## Set up your own checks (optional)

```bash
python3 scripts/verify.py
```

This re-validates the HTML structure, entry fields, and asset references.

## Project notes

- Static HTML/CSS/JS only — no secrets, API keys, or personal data anywhere in this repo.
- Feature availability changes often; each entry's "what it checks" field tells you exactly what to re-verify on your own device.
- Informational only — not medical or legal advice. Not affiliated with any of the tools listed.

## License

MIT — see [LICENSE](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC. Curated with care by
**Asdale Dynamics, LLC** — beginner-friendly AI education, books, and practical
tools. Plain English, step by step, never condescending.
