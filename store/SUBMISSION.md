# 📦 Skull Drift — store submission pack (copy-paste ready)

## Files
- CrazyGames upload: `dist/skulldrift-crazygames.zip` (CG SDK v3 integrated)
- Poki upload: `dist/skulldrift-poki.zip` (Poki SDK integrated)
- Art: `store/cover_16x9.png` (1920×1080) · `cover_4x3.png` (800×600) · `icon_512.png` · `thumb_720.png`

## Name
Skull Drift

## Tagline (short)
Ride a flaming skull through the world's daily catacomb.

## Description
Hold to rise. Let go to drop. That's it — now survive the ossuary.

You are a flaming skull hurtling through catacombs stacked from bones. Thread the gaps, and shave
past the bone pillars for GRAZE bonuses — the closer you fly, the bigger your combo chain.

The twist: everyone on Earth rides the IDENTICAL catacomb today. Same bones, same gaps, same speed.
No excuses — just you, your nerve, and the leaderboard bragging rights. A brand-new course drops
every midnight (UTC). Keep your daily streak alive.

- One-button controls: hold = rise, release = fall (works with mouse, spacebar, or touch)
- Daily seeded course — identical for every player, resets at midnight UTC
- Graze system: near-misses pay escalating combo bonuses
- Day streaks, today's-best and all-time records
- 60-second runs. "One more ride" guaranteed.

## Category / tags
Casual · Arcade · One Button · Skill · Flying
Tags: skull, one-button, daily-challenge, arcade, hypercasual, flappy, dodge, highscore, streak, halloween

## Controls text
Hold (mouse / spacebar / touch) to rise — release to drop. Graze bones for bonus points.

## Technical answers (both platforms ask these)
- Engine: custom HTML5 Canvas (vanilla JS), single file, no backend
- Loads offline after first load: yes · Save data: localStorage only
- Orientation: landscape or portrait (responsive) · Mobile-friendly: yes (touch controls)
- SDK: CrazyGames SDK v3 (init + gameplayStart/Stop + midgame ad on restart) in the CG build;
  Poki SDK (init + gameLoadingFinished + gameplayStart/Stop + commercialBreak on restart) in the Poki build
- External links: none in Poki build context (share uses native share/clipboard, no navigation)
- Age rating: all ages (stylized cartoon skulls, no gore/violence/text chat)

## Review-pass checklist (do before hitting Submit)
- [ ] Test the CG zip in CrazyGames' QA tool (dev portal → your game → QA) — verify ad break fires on restart
- [ ] Poki Inspector (dev portal preview) — same checks
- [ ] Upload art, paste description, pick tags
- [ ] Submit for review (CG: days; Poki: pickier, may take weeks / request changes)

## After acceptance
- Post the game link + 1–3 UGC clips/day (Higgsfield Marketing Studio per README runbook)
- Next: game #2 from the same daily-seed template.
