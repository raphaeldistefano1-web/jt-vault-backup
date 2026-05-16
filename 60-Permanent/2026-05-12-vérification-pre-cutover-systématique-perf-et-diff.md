---
ai_writable: false
area: null
backlinks:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- 2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- jt-migrate
- WordPress
- performance
id: 20260512040626-vérification-pre-cutover-systématique-perf-et-diff
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- 2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- 2026-05-15-qa-hygiene-serveur-next-local
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-1747-session-f978e4ee.md
source_session: f978e4ee-8378-4961-a70b-ecc2e9ede8d3
status: active
summary: Avant prod, comparer perf (speed, memory, queries) + différences fonctionnelles
  (plugins, data intégrité) source vs cible.
tags:
- permanent
- synthesized
- migration
- verification
- performance
- checklist
- quality-gate
tier: warm
title: 'Vérification pre-cutover systématique : perf et différences'
topic_cluster: cutover-process
type: permanent-note
updated: '2026-05-12'
---

Avant le cutover final, exécuter une vérification complète : (1) comparaison de performance (time, memory, query count), (2) différences applicatives (tous plugins chargés ? données intactes ? placeholders résolus ?). Cette checklist prévient les surprises en prod.

**Pourquoi** : une migration peut réussir techniquement mais dégrader la perf ou introduire des inconsistances subtiles (détectables seulement sous charge réelle ou usage). Le pattern observé (Raphaël demande "refais un test de perf", puis "vérifie les différences") montre que cette vérification doit être **explicite et décidée à chaque étape**, pas assumée.

## Related

- [[2026-05-10-analyse-métier-valider-source-de-données-réelle]] — Analyse métier — valider source de données réelle
- [[2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph]] — Validation syntax gate avant commit sur plugins PHP
- [[2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl]] — Scripts pre-cutover cleanup et post-import reenable
- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod
- [[2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl]] — Utiliser /ultrareview avant merge de changements plugin
- [[2026-05-15-qa-hygiene-serveur-next-local]] — 2026-05-15-qa-hygiene-serveur-next-local