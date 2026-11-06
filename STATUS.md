# STATUS — Free Read-Aloud Directory

Last updated: 2026-11-06
Maintained by Asdale Dynamics, LLC

## What was built

A static, no-build HTML directory site cataloging **18 free text-to-speech and
read-aloud helpers** across 5 sections:

| Section | Entries | Examples |
|---|---|---|
| Browser read modes | 4 | Edge Read Aloud, Chrome Android "Listen to this page," Apple Spoken Content, Word Immersive Reader |
| Phone equivalents | 4 | Play Books "Listen," Android Select to Speak, @Voice Aloud Reader, NaturalReader free tier |
| Free TTS apps | 5 | Balabolka, Piper (local), TTSMaker, Windows Narrator, Audiobookshelf |
| E-readers | 3 | Kindle VoiceView/Assistive Reader, PocketBook TTS, Onyx Boox |
| Bonus listening (human narration) | 2 | Libby, hoopla |

Every entry carries four curated fields: **Platform**, **Offline** flag
(Yes / Partial / No), **What it checks** (practical verification steps), and a
one-line plain-English **Verdict**.

Files:

- `index.html` — the directory (responsive, print-friendly, accessible filters)
- `style.css` — styling; offline work-alike filter badges; print styles
- `app.js` — category filter buttons + "works offline only" toggle + live result count
- `docs/curation-notes.md` — selection criteria, exclusions, sibling-project disambiguation, review cadence
- `scripts/verify.py` — validation script (HTML structure, entry completeness, assets)
- `README.md`, `LICENSE` (MIT)

## How to run it

No build step, no dependencies:

- Open `index.html` directly in a browser, **or**
- `python3 -m http.server 8000` and visit http://localhost:8000

Optional check:

```bash
python3 scripts/verify.py
```

## Verification results (2026-11-06)

- `python3 scripts/verify.py` — PASS: 18 entries parsed (4 browser, 4 phone, 5 TTS, 3 reader, 2 listen); all entries have valid category/offline attributes and all four required fields; `style.css`, `app.js`, and `docs/curation-notes.md` present.
- Full-document HTML tag balance — PASS: no mismatched or unclosed tags.
- Local server smoke test (`python3 -m http.server 8123` + curl) — all four public files return HTTP 200.
- Secret scan (`grep` for keys/tokens/passwords) — clean; no secrets, API keys, or personal data in any file.

## Known gaps

- **Feature drift:** browser/device makers rename and move these features often (e.g., Chrome's "Listen to this page" and Kindle accessibility menus). "What it checks" fields are written so each tool can be re-verified in ~5 minutes; recommended re-check every 6 months.
- **Offline flags are best-effort:** "Partial" entries depend on downloaded voice packs, which users may need to fetch once while online.
- **Regional variance:** Kindle Assistive Reader availability and library app catalogs differ by country/model; entries note "check your model" instead of listing every SKU.
- **No screenshot/step-by-step visuals yet:** plain text only; screen-reader-friendly by construction but could add per-tool walkthrough pages later.
- **Sibling cross-links are name-only:** ai-narration-choices-guide and free-large-print-tech-kit are referenced by name; add URLs when those repos are published.
- Not affiliated with or endorsed by any listed provider; informational only, not medical or legal advice.
