---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-06-03
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202606031341-claudemem-62ee60cb
intent: log
last-accessed: 2026-06-03
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: 62ee60cb-ab49-472f-aae5-f9295cc059e4
source: claude-mem:session_summaries#89
status: draft
summary: Built Cyclone app with CYCLONE_FORCE_PREMIUM flag enabled for Debug configuration;
  successfully installed custom build (bundle ID com.cyclone.app.dev) to user's physical
  iPhone (UUID C8F851DD-7B3D-58E9-8B7F-F52496DB71C7); confirmed repository
tags:
- session
- log
- ai-generated
tier: cold
title: Deploy premium version of Cyclone app to user's personal iPhone
topic_cluster: session-log
type: meeting
updated: 2026-06-03
---

# Session (claude-mem) — Deploy premium version of Cyclone app to user's personal iPhone

> Capture semantique claude-mem (2026-06-03). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `62ee60cb-ab49-472f-aae5-f9295cc059e4`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #89)

## Demande

Deploy premium version of Cyclone app to user's personal iPhone

## Investigue

AppModel.swift premium entitlement system; discovered CYCLONE_FORCE_PREMIUM compile flag that bypasses StoreKit validation and forces isPremium=true in test builds; examined how premium state is cached and persisted

## Appris

Cyclone uses StoreKit for production premium entitlements, but supports a test build flag (CYCLONE_FORCE_PREMIUM) that completely bypasses subscription checks and locks premium features in place; this flag is guarded by preprocessor conditionals and never reaches production builds

## Realise

Built Cyclone app with CYCLONE_FORCE_PREMIUM flag enabled for Debug configuration; successfully installed custom build (bundle ID com.cyclone.app.dev) to user's physical iPhone (UUID C8F851DD-7B3D-58E9-8B7F-F52496DB71C7); confirmed repository working tree remains clean with no uncommitted changes

## Prochaines etapes

Session complete; user now has premium features immediately accessible on their device (Imposteur, C'est un 10, unlimited corsé questions, retour arrow without paywall); no further action required unless user wants to test paywall behavior again

## Notes

Premium forced-unlock exists only in the deployed device build; all committed code remains unchanged with normal premium gating intact. User can revert to standard build anytime by requesting reinstall without the test flag. This approach uses test infrastructure properly and does not compromise production code.

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente