# 🔥 Ember Drift — money runbook

**Game:** one-input arcade, hold to rise. Everyone flies the **identical daily canyon** (UTC-seeded),
graze the rock for combo bonuses. Zero backend, one file: [index.html](index.html). Original IP.

**Source method:** "I Asked Claude Fable 5 To Build Me A $100K/Month Game" (THE ECOM KING, watched
2026-07-09). His own realistic number for a first accepted game: **$500–$3,000/mo** ad rev-share.
The $100K examples (slither.io etc.) are outliers with years of traffic. Strategy = quality + volume:
ship this one, then repeat the pipeline for more games.

## Status
- [x] Game built + auto-verified (menu → play → graze bonus → death → results → streak/best persistence)
- [ ] Eric hand-playtest (difficulty feel — first gates may need widening for casuals)
- [ ] Deploy free hosting
- [ ] Submit to platforms
- [ ] Marketing clips

## Monetization steps (in priority order)
1. **Deploy free:** Cloudflare Pages or GitHub Pages (drag-drop `index.html`). Custom domain optional.
2. **Submit to CrazyGames** (developer.crazygames.com): rev-share, they bring the traffic. Requirements:
   integrate their HTML5 SDK (hooks already stubbed at the bottom of index.html — `gameplayStart/Stop`,
   rewarded ad = one "second chance" continue per run), quality review takes days–weeks.
3. **Submit to Poki** (developers.poki.com): same model, pickier review, higher traffic if accepted.
4. **Self-host + AdSense** (full revenue, but you bring traffic): AdSense account → verify URL → paste
   the ad snippet into index.html.
5. **UGC marketing clips:** Eric already has **Higgsfield** (empire watcher). Per the video: Marketing
   Studio → add game URL → custom gamer avatar (Recraft) → 3×15s hype clips → CapCut (1.1x speed +
   music + b-roll) → post 1–3/day on TikTok/IG. Hook line: "everyone on Earth plays the SAME course
   today — send it to your most competitive mate."
6. **Game-agency angle (method 2):** sell branded reskins of this engine to local businesses/brands
   (recolor, logo, prize hook). The engine is deliberately reskinnable: palette + title + seed.

## Viral mechanics built in
Daily identical course (UTC seed) · day-streak counter · today's-best vs all-time · share button with
challenge text · near-miss "graze chain" dopamine loop · instant restart (RUN IT BACK).

## Next games (repeat pipeline, ~2h each once tuned)
Check CrazyGames "popular" + SensorTower for proven simple formats; keep original themes. Candidates:
drift-parking, one-button climber, swarm survivor. Same daily-seed + streak + share skeleton — extract
it into a template after game #2.

## Test/verify recipe
`python -m http.server 8377 --directory D:/Dev/EmberDrift` → browser. Automated pilot: see
`window.__dbg()` hook — poll it, hold Space when `py + vy*0.13 > next gate center`.
