---
ai_writable: false
aliases:
- JT Migrate
backlinks:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- Bug-Apache-Timeout-300-vs-Uploads
- Bug-JT-Migrate-Auth-Loss-After-DB-Restore
- Bug-PharData-RAM-OOM
- Decision-Streaming-tar-gz-vs-PharData
- JT-Migrate-v1.0.0
- JT-Migrate-v1.1.0
- JT-Migrate-v1.2.0
- JT-Migrate-v1.2.1
- Migration-WP-com-vers-VPS-2026-04-25
- Site-Plugins-Stack-2026-04-25
- Site-WordPress
- Workflow-File-Share-Uploads
- _Index
- _MOC-jt-migrate
- _VAULT-INDEX
created: 2026-04-25
description: Plugin WP custom de migration full-fidelity v1.2.1 — similaire All-in-One
  WP Migration mais pure PHP, streaming
embed_hash: null
embed_model_version: null
entities:
- debugging
- migration
- site-wordpress
- wordpress
id: 202604252034-plugin-jt-migrate
intent: reference
last-accessed: 2026-04-25
project: jt-migrate
related:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- '[[JT-Migrate-v1.0.0]]'
- '[[JT-Migrate-v1.1.0]]'
- '[[JT-Migrate-v1.2.0]]'
- '[[JT-Migrate-v1.2.1]]'
- '[[Migration-WP-com-vers-VPS-2026-04-25]]'
- '[[Site-WordPress]]'
relevance: high
status: active
summary: 'Plugin WordPress custom de migration full-fidelity entre instances WP. Similaire
  à All-in-One WP Migration mais :'
tags:
- wordpress
- plugin
- migration
- custom
tier: warm
topic_cluster: wp-migration
type: project
updated: 2026-04-25
---

# 🚚 Plugin jt-migrate v1.2.1

## Nature

Plugin WordPress **custom** de migration full-fidelity entre instances WP. Similaire à **All-in-One WP Migration** mais :
- **Pure PHP** (pas besoin de shell, marche sur WP.com Business)
- **Streaming** (pas de chargement RAM, marche sur sites > 100 MB)
- Auto-détection multilingue / forms / cache
- Compatible WP 6.0+ / PHP 7.4+

## Versions

- [[JT-Migrate-v1.0.0]] — initiale, **bug streaming inversé** (PharData charge tout en RAM → fail sur > 100 MB)
- [[JT-Migrate-v1.1.0]] — fix streaming **export** (gzopen + USTAR custom), shutdown handler
- [[JT-Migrate-v1.2.0]] — mode **import-from-server-path** (bypass upload HTTP), conflit auth résolu
- [[JT-Migrate-v1.2.1]] — fix streaming **import** (parser USTAR custom en lecture, miroir du fix v1.1)

## Architecture (8 classes)

- `JT_Migrate_Utils` — workspace, preflight, feature detection, exclusions
- `JT_Migrate_Database` — dump/restore gzip-aware
- `JT_Migrate_Replace` — recursive_replace serialize-safe
- `JT_Migrate_Archive` — **streaming tar.gz** (gzopen + USTAR à la main, lecture par chunks 64 KB)
- `JT_Migrate_Export` — pipeline AJAX (init → db → files → archive → done)
- `JT_Migrate_Import` — pipeline AJAX (upload OR from-path → extract → db → replace → files → cleanup)
- `JT_Migrate_Admin` — UI 3 onglets (Export / Import / Diagnostic)

## Distribution

- **Source dev** : `/var/www/jt-migrate/`
- **ZIP** : `/var/www/pms-jardin-tropical/public/downloads/jt-migrate-v1.2.1.zip` (~35 KB)
- **URL** : https://pms-46-202-171-204.nip.io/downloads/jt-migrate-v1.2.1.zip

## Performance

- v1.0.0 : crashait > 100 MB (PharData OOM)
- v1.2.1 : **archive 239 MB** créée avec **memory_limit forcé à 64M**, peak mem **0.6 MB**, débit ~38 MB/s
- Test réel : archive 306 MB / 1795 entrées extraite en **1 s** à **300 MB/s**

## Bug de design (v1.3.0 todo)

[[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] :

Le pipeline d'import écrase la table `wp_users` AVANT search-replace + files copy → cookie de session admin invalidé → `current_user_can('manage_options')` échoue → steps `replace` et `files` retournent 403 silencieusement.

Workaround actuel : finir l'import via wp-cli (bypass auth web). Fix v1.3.0 : ordonner `extract → files → replace → db (en dernier)` ou mode CLI-only.

## Use case réussi

[[Migration-WP-com-vers-VPS-2026-04-25]] — migration site dealmfr.wpcomstaging.com → VPS Hostinger, 321 MB d'archive, succès après séquence v1.0 → v1.1 → v1.2 → v1.2.1.

## Liens

- [[Site-WordPress]]
- [[Migration-WP-com-vers-VPS-2026-04-25]]

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[2026-05-09-instance-d-wordpress-en-rotation-test]] — Instance D WordPress en rotation test