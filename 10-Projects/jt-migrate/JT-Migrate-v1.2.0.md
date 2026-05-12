---
ai_writable: false
backlinks:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- Bug-Apache-Timeout-300-vs-Uploads
- JT-Migrate-v1.1.0
- JT-Migrate-v1.2.1
- Lessons-Learned
- Migration-WP-com-vers-VPS-2026-04-25
- Plugin-jt-migrate
- _Index
- _MOC-jt-migrate
created: 2026-04-25
description: v1.2.0 — mode import-from-server-path (bypass upload HTTP, dépose archive
  via SCP dans incoming/)
embed_hash: null
embed_model_version: null
entities:
- debugging
- migration
- rag
- wordpress
id: 202604252035-jt-migrate-v1-2-0
intent: reference
last-accessed: 2026-04-25
project: jt-migrate
related:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- Workflow-File-Share-Uploads
- '[[Bug-Apache-Timeout-300-vs-Uploads]]'
- '[[JT-Migrate-v1.1.0]]'
- '[[JT-Migrate-v1.2.1]]'
- '[[Plugin-jt-migrate]]'
relevance: medium
status: superseded
summary: ❌ Superseded par JT-Migrate-v1.2.1.
superseded_by: '[[JT-Migrate-v1.2.1]]'
supersedes: '[[JT-Migrate-v1.1.0]]'
tags:
- jt-migrate
- version
- feature
tier: warm
topic_cluster: wp-migration
type: project
updated: 2026-04-25
---

# 📦 JT Migrate v1.2.0

## Status

❌ **Superseded** par [[JT-Migrate-v1.2.1]].

## Apport

### Mode import-from-server-path

Bypass l'upload HTTP qui était fragile sur les gros fichiers (cf. [[Bug-Apache-Timeout-300-vs-Uploads]]).

#### Workflow

1. User dépose le `.tar.gz` directement dans `wp-content/uploads/jt-migrate/incoming/` via **SCP** (ou côté server-to-server par `curl`)
2. UI WP → Plugins → JT Migrate → Import → onglet "Import depuis incoming/"
3. Liste des archives présentes, clic sur "Importer"
4. Pipeline d'import normal (extract → db → replace → files → cleanup) sans passer par upload HTTP

#### Implémentation

- `JT_Migrate_Import::ajax_from_path()` — équivalent de `ajax_upload()` mais lit depuis incoming/ au lieu de `$_FILES`
- Path direct vers le fichier (pas de copie dans le job_dir)
- Sécurité : `realpath()` + check que le path résolu est sous `incoming_dir/`, regex sur extension `.gz` / `.tgz`
- UI : panneau dépliable "📂 Ou : importer une archive déjà déposée sur le serveur"

### Bug subsistant (corrigé en v1.2.1)

L'extract utilisait toujours `PharData::extract()` qui crash sur archive > 100 MB en RAM.

## Liens

- [[Plugin-jt-migrate]]
- [[JT-Migrate-v1.2.1]]

## Related

- [[Workflow-File-Share-Uploads]] — Workflow-File-Share-Uploads
- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps
- [[2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl]] — Scripts pre-cutover cleanup et post-import reenable