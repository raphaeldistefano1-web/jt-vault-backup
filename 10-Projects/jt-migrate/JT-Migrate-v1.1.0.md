---
ai_writable: false
backlinks:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- Bug-PharData-RAM-OOM
- Decision-Streaming-tar-gz-vs-PharData
- JT-Migrate-v1.0.0
- JT-Migrate-v1.2.0
- JT-Migrate-v1.2.1
- Lessons-Learned
- Migration-WP-com-vers-VPS-2026-04-25
- Plugin-jt-migrate
- _Index
- _MOC-jt-migrate
created: 2026-04-25
description: v1.1.0 — fix export streaming tar.gz + shutdown handler pour capturer
  fatals
embed_hash: null
embed_model_version: null
entities:
- documentation
- migration
- reference
id: 202604252035-jt-migrate-v1-1-0
intent: reference
last-accessed: 2026-04-25
project: jt-migrate
related:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- '[[JT-Migrate-v1.0.0]]'
- '[[JT-Migrate-v1.2.0]]'
- '[[Plugin-jt-migrate]]'
relevance: low
status: superseded
summary: ❌ Superseded par JT-Migrate-v1.2.0.
superseded_by: '[[JT-Migrate-v1.2.0]]'
supersedes: '[[JT-Migrate-v1.0.0]]'
tags:
- jt-migrate
- version
tier: warm
topic_cluster: wp-migration
type: project
updated: 2026-04-25
---

# 📦 JT Migrate v1.1.0

## Status

❌ **Superseded** par [[JT-Migrate-v1.2.0]].

## Apport

### 1. Streaming tar.gz custom (export)

`JT_Migrate_Archive::create()` réécrit en streaming :
- `gzopen()` + `gzwrite()` pour le flux gzip
- Headers USTAR de 512 bytes écrits à la main (`pack()` format `a100a8a8a8a12a12A8a1a100a6a2a32a32a8a8a155a12`)
- Lecture des fichiers par chunks de 64 KB
- 2 blocs de 512 zéros à la fin = EOF tar

**Résultat** : archive 239 MB avec memory_limit forcé à 64 MB, peak mem **0.6 MB**, débit ~38 MB/s.

Vérifié : archive lisible par GNU `tar -tzvf` ET par `PharData::extract()`.

### 2. Shutdown handler

`register_shutdown_function` qui capture les fatals PHP (memory, timeout, parse) et les persiste dans `state.json` avant que le process meure.

→ Sur le bug suivant ([[Bug-JT-Migrate-v1.1-Import-Extract-Fail]]), c'est ce shutdown handler qui a permis de voir le vrai message d'erreur.

### 3. Frontend amélioré

JS `runExportStep` poll `ajax_status` après `.fail()` pour récupérer le state et afficher l'erreur persistée par le shutdown handler. Plus de "❌ Étape échouée" muet.

## Bug subsistant

L'**import** utilise toujours `PharData::extract()` qui charge l'index complet en RAM → crash sur archive > 100 MB.

→ Fix dans v1.2.1 : streaming extract custom (parser USTAR à la main).

## Liens

- [[Plugin-jt-migrate]]
- [[JT-Migrate-v1.0.0]]
- [[JT-Migrate-v1.2.1]]

## Related

- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps
- [[2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl]] — Scripts pre-cutover cleanup et post-import reenable
- [[2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor]] — HBook placeholder names corrupted lors export/import entre instances