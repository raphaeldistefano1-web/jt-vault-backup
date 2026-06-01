---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-05-30
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202605301615-claudemem-65ceeb61
intent: log
last-accessed: 2026-05-30
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: 65ceeb61-382f-4174-a2ab-357b6d6e457e
source: claude-mem:session_summaries#39
status: draft
summary: Identified correct app bundle; rebuilt app from current sources; captured
  real onboarding screen with accurate content; confirmed catalog structure and gameplay
  card types; diagnosed version
tags:
- session
- log
- ai-generated
tier: cold
title: Diagnose why app screenshots show wrong version; capture onboarding, home,
  catalog, and
topic_cluster: session-log
type: meeting
updated: 2026-05-30
---

# Session (claude-mem) — Diagnose why app screenshots show wrong version; capture onboarding, home, catalog, and

> Capture semantique claude-mem (2026-05-30). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `65ceeb61-382f-4174-a2ab-357b6d6e457e`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #39)

## Demande

Diagnose why app screenshots show wrong version; capture onboarding, home, catalog, and gameplay screens from Cyclone iOS app

## Investigue

Examined which app bundle was being captured and tested (discovered `com.cyclone.app` was old May version vs. correct `com.cyclone.app.dev` built May 31 03:51); analyzed onboarding screen content; reviewed catalog cards; inspected app build output for placeholder text and cleanliness

## Appris

App had two versions in circulation with same name but different bundles; correct production-ready version is `com.cyclone.app.dev`; onboarding flow requires name entry; catalog contains PICOLO card with alcohol references ("une gorgée" = a sip) that may trigger Meta/TikTok moderation; older builds contained placeholder text, newer build is production-clean; AppleScript keystroke injection and coordinate-mapped clicks are unreliable for simulator automation

## Realise

Identified correct app bundle; rebuilt app from current sources; captured real onboarding screen with accurate content; confirmed catalog structure and gameplay card types; diagnosed version mismatch root cause

## Prochaines etapes

Resolve simulator automation blocker: either obtain manual screenshots (user captures onboarding→home, Jeux tab→catalog, Action ou Vérité→gameplay) or continue refining copy-paste and click-coordinate approach if pursuing automated flow. User decision pending on whether to provide manual screenshots or resume automation attempts

## Notes

Simulator interaction automation (AppleScript, coordinate mapping) proved unreliable; manual screenshot capture would be faster and more reliable. Content moderation flag identified: alcohol references in onboarding and card names may need review for platform policies. Work was halted mid-troubleshooting pending user direction on screenshot approach

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente