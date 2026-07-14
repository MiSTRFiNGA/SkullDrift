# Skull Drift — v0.50 baseline

**Baseline frozen:** 2026-07-11 (America/New_York)

## What is included

- Single-input flaming-skull arcade flight game with touch support, sound, mute, local persistence, daily seeded course, combo scoring, streaks, sharing, and first-run tutorial.
- Gentle difficulty ramp has been tuned and automated gameplay testing previously cleared seven or more gates.
- CrazyGames and Poki SDK adapters, portal build artifacts, submission metadata, cover art, and preview videos are present.

## Release position

- This is the protected pre-continuation baseline. Portal submission still requires manual human QA/upload; CrazyGames requires the extracted `index.html` upload rather than the generated archive.
- No gameplay or source changes are authorized in this baseline note. Later work must be recorded separately and remain rollback-safe against the v0.50 backup.

## Primary files

- `index.html` — game source
- `build.py` — portal package builder
- `store/SUBMISSION.md` — portal submission copy and checklist
- `dist/` and `store/` — generated portal assets
