---
ai_writable: false
area: null
backlinks:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- Bug-JT-Migrate-v1.1-Import-Extract-Fail
- _VAULT-INDEX
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- UpdraftPlus
- WordPress
- jt-migrate
id: 20260512040627-cleanup-post-cutover-supprimer-plugins-temporaires
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- Lesson-mu-plugins-WP-com-toxiques-sur-standalone
- _Index
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- Bug-JT-Migrate-v1.1-Import-Extract-Fail
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-1747-session-f978e4ee.md
source_session: f978e4ee-8378-4961-a70b-ecc2e9ede8d3
status: active
summary: Après cutover prod, désinstaller plugins de sauvegarde/migration sauf UpdraftPlus
  si usage continu prévu.
tags:
- permanent
- synthesized
- migration
- cleanup
- post-prod
- security
- maintainability
tier: warm
title: 'Cleanup post-cutover : supprimer plugins temporaires'
topic_cluster: cutover-process
type: permanent-note
updated: '2026-05-12'
---

Après cutover prod de jt-migrate vers Instance A, nettoyer les plugins temporaires utilisés uniquement pour la migration. Exemple : désinstaller 2 plugins backup, mais garder UpdraftPlus si une sauvegarde continue est prévue.

**Pourquoi** : chaque plugin actif = surface d'attaque, load supplémentaire, dette maintenabilité. Post-migration, ces plugins deviennent des bloatware sans utilité.

## Related

- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps
- [[Lesson-mu-plugins-WP-com-toxiques-sur-standalone]] — Lesson mu plugins WP com toxiques sur standalone
- [[_Index]] — Index — jt-migrate
- [[2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor]] — HBook placeholder names corrupted lors export/import entre instances
- [[Bug-JT-Migrate-v1.1-Import-Extract-Fail]] — Bug JT Migrate v1.1 Import Extract Fail