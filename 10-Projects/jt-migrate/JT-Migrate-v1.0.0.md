---
type: project
status: superseded
tags: [jt-migrate, version, bug]
created: 2026-04-25
updated: 2026-04-25
relevance: low
description: "Première version JT Migrate — bloque sur sites > 100 MB à cause de PharData::compress qui charge tout en RAM"
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.1.0]]"
  - "[[Bug-PharData-RAM-OOM]]"
supersedes: []
superseded_by: "[[JT-Migrate-v1.1.0]]"
id: 202604252034-jt-migrate-v1-0-0
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "❌ Superseded par JT-Migrate-v1.1.0."
entities: [debugging, migration, site-wordpress]
topic_cluster: wp-migration
intent: reference
tier: warm
---

# 📦 JT Migrate v1.0.0

## Status

❌ **Superseded** par [[JT-Migrate-v1.1.0]].

## Bug

`JT_Migrate_Archive::create()` utilisait `PharData::compress(Phar::GZ)` qui charge le `.tar` complet en mémoire avant compression GZ.

Sur le site dealmfr (305 MB d'uploads JPG/PNG quasi-incompressibles), ça :
- Dépassait `memory_limit = 512M` (combiné à WP overhead + interne PharData)
- Provoquait un fatal PHP "Allowed memory size exhausted"
- Le frontend voyait juste "❌ Étape échouée" sans message (le frontend ne lisait pas xhr.responseText)

## Diagnostic

Phase 1 systematic-debugging révélée :
- Logs Apache 5xx absents (PHP fatal court-circuite l'output)
- `state.json` du job restait au stage `files_done` — l'erreur arrivait ENSUITE pendant l'archive

## Solutions essayées

- Augmenter memory_limit → impossible sur WP.com Business
- Augmenter Apache Timeout → pas le problème (memory, pas timing)

## Fix

[[JT-Migrate-v1.1.0]] : réécriture en **streaming tar.gz** custom (gzopen + USTAR headers à la main), 0.6 MB peak memory sur archive 239 MB.

## Apprentissage clé

[[Lesson-PharData-charge-tout-en-RAM]] — `PharData` n'est PAS scalable, à éviter pour fichiers > 100 MB.

## Liens

- [[Plugin-jt-migrate]]
- [[Migration-WP-com-vers-VPS-2026-04-25]]
