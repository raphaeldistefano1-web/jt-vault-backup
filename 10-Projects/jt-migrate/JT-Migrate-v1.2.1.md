---
type: project
status: active
tags: [jt-migrate, version, current]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "v1.2.1 — fix streaming import (parser USTAR custom en lecture, miroir du fix v1.1 mais à l'extract). Version actuelle."
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.2.0]]"
  - "[[JT-Migrate-v1.1.0]]"
  - "[[Bug-JT-Migrate-v1.1-Import-Extract-Fail]]"
supersedes: "[[JT-Migrate-v1.2.0]]"
id: 202604252035-jt-migrate-v1-2-1
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "✅ Version actuelle, déployée sur le VPS."
entities: [debugging, documentation, migration]
topic_cluster: wp-migration
intent: reference
tier: warm
---

# 📦 JT Migrate v1.2.1 — current

## Status

✅ **Version actuelle**, déployée sur le VPS.

## Apport

### Streaming extract (parser USTAR custom en lecture)

`JT_Migrate_Archive::extract()` réécrit en streaming :
- `gzopen($path, 'rb')` pour lire le tar.gz au fil de l'eau
- Boucle qui parse 1 header USTAR de 512 bytes à la fois
- `parse_tar_header()` extrait `name`, `prefix`, `size`, `typeflag` du header
- `sanitize_extract_path()` rejette tout chemin avec `..` (anti path traversal)
- Pour chaque entry : `fopen($target, 'wb')` + boucle `gzread → fwrite` par chunks 64 KB
- Skip padding au prochain multiple de 512 entre fichiers

C'est le **miroir** du fix v1.1.0 (qui avait fix l'export streaming) mais cette fois côté lecture.

### Test réel

Archive 306 MB (321 MB raw / 1795 entrées) extraite en :
- **1 seconde**
- **300 MB/s** débit
- **0.6 MB** peak memory avec memory_limit forcé à **64 MB**

`PharData::extract()` aurait OOM bien avant.

## Bug de design subsistant (à fixer en v1.3.0)

[[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] :

Le pipeline d'import écrase la table `wp_users` AVANT search-replace + files copy → cookie session admin invalidé → steps suivants 403.

Workaround actuel : finir via wp-cli.

Fix v1.3.0 : ordonner `extract → files → replace → db (en dernier)` ou mode CLI-only sans dépendance auth web.

## Distribution

- **ZIP** : `/var/www/pms-jardin-tropical/public/downloads/jt-migrate-v1.2.1.zip` (~35 KB)
- **URL** : https://pms-46-202-171-204.nip.io/downloads/jt-migrate-v1.2.1.zip

## Liens

- [[Plugin-jt-migrate]]
- [[Migration-WP-com-vers-VPS-2026-04-25]]
