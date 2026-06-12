---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-06-11
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202606110642-claudemem-a5f894bb
intent: log
last-accessed: 2026-06-11
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: a5f894bb-e4e1-47c1-8428-fd17ae18a05d
source: claude-mem:session_summaries#159
status: draft
summary: Successfully built Swapy for physical iOS device with proper code signing
  and provisioning profile generation (DEVELOPMENT_TEAM=FZ99ZN8WN5). Installed app
  on iPhone Raphael via devicectl. Launched app
tags:
- session
- log
- ai-generated
tier: cold
title: Enable real device testing by building, signing, and installing Swapy on physical
topic_cluster: session-log
type: meeting
updated: 2026-06-11
---

# Session (claude-mem) — Enable real device testing by building, signing, and installing Swapy on physical

> Capture semantique claude-mem (2026-06-11). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `a5f894bb-e4e1-47c1-8428-fd17ae18a05d`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #159)

## Demande

Enable real device testing by building, signing, and installing Swapy on physical iPhone hardware; validate that core features (group matching, Supabase backend integration) function on actual iOS device.

## Investigue

Examined development environment: device pairing status, available codesigning identities, cached provisioning profiles, device developer mode enablement, Xcode build schemes, build infrastructure readiness (xcodegen version, device tunnel state).

## Appris

Apple Developer team FZ99ZN8WN5 (RAPHAEL DI STEFANO) from prior Cyclone project is available with valid signing certificate and can sign Swapy builds. Xcode's automatic code signing (CODE_SIGN_STYLE=Automatic) auto-generates provisioning profiles on first real device build. iPhone Raphael (11 Pro Max) is fully prepared for development builds: developer mode enabled, booted, paired, tunneled, and developer disk image services active. Development builds signed with this team certificate remain valid for ~1 year (until 2027), bypassing the standard 7-day unsigned app limit.

## Realise

Successfully built Swapy for physical iOS device with proper code signing and provisioning profile generation (DEVELOPMENT_TEAM=FZ99ZN8WN5). Installed app on iPhone Raphael via devicectl. Launched app on physical device without errors. App is now running on real hardware and ready for functional testing. Group mode confirmed to communicate with real Supabase cloud backend. Catalogue displays 17 seeded test locations. Invitation code sharing functional (web landing page not yet hosted).

## Prochaines etapes

User to manually test Swapy on physical iPhone Raphael to validate group matching, multi-device features, backend connectivity, and overall app behavior on real hardware. Pending user feedback on any issues discovered during device testing. Optional: persist signing configuration (DEVELOPMENT_TEAM and CODE_SIGN_STYLE) to project.yml to enable one-click rebuilds from Xcode without command-line overrides; currently signing config is temporary (command-line parameters, not in project).

## Notes

Development build eliminates the 7-day expiration pressure, allowing iterative testing over weeks. Simulator tests remain unaffected by signing changes (command-line overrides only). Real device testing enables validation of features like group joining, matching logic, and backend communication that can behave differently on physical hardware. Two major blockers remain from prior session: #1 RLS security hardening (code written, not deployed) and #2 OSM open data ingestion (code validated, blocked by prod access). Both predate this device testing phase.

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente