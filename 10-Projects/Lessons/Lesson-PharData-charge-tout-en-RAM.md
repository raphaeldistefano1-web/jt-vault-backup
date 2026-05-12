---
ai_writable: true
backlinks:
- JT-Migrate-v1.0.0
- Migration-WP-com-vers-VPS-2026-04-25
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — PharData PHP charge l'intégralité de l'archive en mémoire, OOM
  sur fichiers > 100 MB
embed_hash: null
embed_model_version: null
entities:
- php
- phardata
- migration
id: 202605120007-lesson-phardata-charge-tout-en-ram
intent: log
last-accessed: 2026-05-12
project: Lessons
status: stub
summary: PharData::compress/extract chargent tout en RAM → fix par streaming gzopen/USTAR
  custom
tags:
- lesson
- php
- migration
tier: cold
type: lesson
updated: 2026-05-12
---

# Lesson PharData charge tout en RAM

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

Généralisation du [[Bug-PharData-RAM-OOM]] documenté sur le plugin jt-migrate v1.0.

## À documenter

- [ ] Limite réelle (taille mémoire / nb fichiers)
- [ ] Pattern de remplacement (streaming `gzopen` + USTAR custom)
- [ ] Alternative `ZipArchive` (mêmes limites ?)
- [ ] Recommandation : ne jamais utiliser PharData pour > 50 MB

## Related

- [[Bug-PharData-RAM-OOM]]
- [[Decision-Streaming-tar-gz-vs-PharData]]
- [[Lessons-Learned]]