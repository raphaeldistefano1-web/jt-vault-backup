---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-10
backlinks:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
confidence: medium
created: '2026-05-10'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- analytics
- data-sourcing
feedback_level: MEDIUM
id: 20260510040344-analyse-métier-valider-source-de-données-réelle
intent: feedback-rule
last-accessed: '2026-05-10'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: Avant analyse de données métier (taux, statistiques, financière), accéder
  directement aux sources (API, BDD) plutôt que mémoire. Déclarer explicitement si
  données partielles ou stale.
related:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- deep-research
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- queries
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
schema_version: 1
source_notes:
- 10-Projects/pms-jardin-tropical/2026-05-09-1524-session-b53ba567.md
- 10-Projects/pms-jardin-tropical/2026-05-09-1506-session-b53ba567.md
- 10-Projects/pms-jardin-tropical/2026-05-09-1522-session-b53ba567.md
- 10-Projects/pms-jardin-tropical/2026-05-09-1516-session-b53ba567.md
source_session: b53ba567-cec1-4390-a306-dc625e77c91e
status: auto-applied
summary: Avant analyse de données métier, accéder directement aux sources (API, BDD)
  plutôt que mémoire; déclarer explicitement limitations.
tags:
- permanent
- synthesized
- feedback
- pending-review
- methodology
- validation
tier: warm
title: Analyse métier — valider source de données réelle
topic_cluster: data-methodology
type: permanent-note
updated: '2026-05-10'
usage_count: 0
---

**Signal feedback** : Raphaël remet en question la fiabilité d'une analyse de taux d'occupation (« tu es sur de tout les chiffres ? »), ce qui indique que la méthodologie (synthèse à partir de mémoire) était insuffisante.

**Discipline à adopter** : 
1. Avant de produire une analyse de données métier, vérifier d'abord qu'on a accès aux vraies sources (API, BDD, exports).
2. Ne pas générer de chiffres / graphiques à partir de la seule mémoire Claude.
3. Si accès limité : déclarer explicitement les limitations (« données jusqu'au X date », « réservations confirmées uniquement », etc.).
4. Si impossibilité : demander au user où chercher plutôt que d'inventer.

**Pourquoi** : Les données métier (financière, opérationnelle) doivent être vérifiables et exactes. Une analyse fausse peut mener à de mauvaises décisions d'exploitation.

## Related

- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod
- [[deep-research]] — deep research
- [[2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau]] — Audit one-shot — déduplication 39 mémoires CC vs vault
- [[queries]] — 70-Data — requêtes SQL utiles
- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)