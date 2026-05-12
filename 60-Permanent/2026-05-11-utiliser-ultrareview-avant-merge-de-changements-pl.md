---
ai_writable: false
area: null
backlinks:
- 2026-05-11-audit-migration-wp-phase-0-7-décisions-en-attente
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
- Plugin-jt-migrate
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- /ultrareview
- Claude Code
- peer-review
id: 20260511212048-utiliser-ultrareview-avant-merge-de-changements-pl
intent: lesson
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-11-audit-migration-wp-phase-0-7-décisions-en-attente
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
- Decisions-Log
- Plugin-jt-migrate
- _MOC-jt-migrate
- devils-advocate
- research-companion
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-10-0817-session-4fd4bfe4.md
source_session: 4fd4bfe4-3f6f-4405-ae32-6d3603b75c92
status: active
summary: Déclencher `/ultrareview` sur branche feature avant merge pour catch erreurs
  que la relecture manuelle pourrait rater.
tags:
- permanent
- synthesized
- qa-gate
- automation
- plugin-audit
tier: warm
title: Utiliser /ultrareview avant merge de changements plugin
topic_cluster: code-review-workflow
type: permanent-note
updated: '2026-05-11'
---

La commande `/ultrareview` (Claude Code) lance un audit automatisé cloudé (multi-agent) qui inspecte :
- Sécurité (injections, perms)
- Performance (N+1 queries, bundle)
- Compatibilité (régression features existantes)
- Accessibilité, UX

Pour plugins WordPress complexes (export/import de données, manipulation DOM/AJAX) où les défauts peuvent être subtils (timing issues, charset bugs, state leaks), `/ultrareview` coûte peu (free 3x par session) et rattrape les trucs qu'une relecture humaine rapide oublie.

Workflow recommandé : implémentation → syntax gate → git commit → `/ultrareview` → fix findings → merge.

## Related

- [[devils-advocate]] — devils advocate
- [[_MOC-jt-migrate]] — MOC JT-Migrate Plugin
- [[Plugin-jt-migrate]] — Plugin jt migrate
- [[research-companion]] — research companion
- [[Decisions-Log]] — Decisions Log
- [[2026-05-11-testing-vérification-obligatoires-après-chaque-éta]] — Testing + vérification obligatoires après chaque étape migration
- [[2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos]] — Git init empty baseline pour ultrareview sur repos existants
- [[2026-05-11-audit-migration-wp-phase-0-7-décisions-en-attente]] — Audit migration WP Phase 0 — 7 décisions en attente
- [[2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph]] — Validation syntax gate avant commit sur plugins PHP
- [[2026-05-12-vérification-pre-cutover-systématique-perf-et-diff]] — Vérification pre-cutover systématique : perf et différences