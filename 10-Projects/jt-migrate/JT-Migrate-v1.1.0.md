---
type: project
status: superseded
tags: [jt-migrate, version]
created: 2026-04-25
updated: 2026-04-25
relevance: low
description: "v1.1.0 — fix export streaming tar.gz + shutdown handler pour capturer fatals"
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.0.0]]"
  - "[[JT-Migrate-v1.2.0]]"
supersedes: "[[JT-Migrate-v1.0.0]]"
superseded_by: "[[JT-Migrate-v1.2.0]]"
id: 202604252035-jt-migrate-v1-1-0
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "❌ Superseded par JT-Migrate-v1.2.0."
entities: [documentation, migration, reference]
topic_cluster: wp-migration
intent: reference
tier: warm
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
