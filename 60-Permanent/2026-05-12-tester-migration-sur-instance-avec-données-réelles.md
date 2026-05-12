---
ai_writable: false
area: null
backlinks:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- jt-migrate
- Instance B
- Instance D
- WordPress
id: 20260512040623-tester-migration-sur-instance-avec-données-réelles
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-1747-session-f978e4ee.md
source_session: f978e4ee-8378-4961-a70b-ecc2e9ede8d3
status: active
summary: 'Valider l''import sur copie de prod plutôt que instance vierge : révèle
  edge cases et incompatibilités cachées.'
tags:
- permanent
- synthesized
- testing
- migration
- real-data
- pre-prod
- edge-cases
tier: warm
title: Tester migration sur instance avec données réelles, pas vierge
topic_cluster: testing-strategy
type: permanent-note
updated: '2026-05-12'
---

Avant cutover prod (Instance A), créer une Instance D = copie de Instance B (déjà en production). Tester la migration sur cette copie plutôt que sur une instance vierge.

**Pourquoi** : une instance vierge ne détecte pas les edge cases (données orphelines, plugins en conflit, caches stale). Une copie de prod reproduit l'environnement réel et révèle problèmes cachés : la session a détecté un issue HBook (placeholder names) uniquement sur le test réel, qui n'aurait jamais émergé sur vierge. Pattern : utiliser Instance C/D comme copies de B ou A selon la phase de test.

## Related

- [[2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor]] — HBook placeholder names corrupted lors export/import entre instances
- [[2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi]] — Valider systèmes de dispatch via test instances vierges
- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps
- [[2026-05-09-instance-d-wordpress-en-rotation-test]] — Instance D WordPress en rotation test
- [[2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl]] — Scripts pre-cutover cleanup et post-import reenable