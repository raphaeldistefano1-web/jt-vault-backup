---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-12
backlinks:
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
confidence: medium
created: '2026-05-12'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- Raphaël
feedback_level: MEDIUM
id: 20260512040629-workflow-itératif-valider-par-phase-plutôt-que-bat
intent: feedback-rule
last-accessed: '2026-05-12'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: Pour les migrations et features multi-phase, valider chaque étape avant
  de planifier la suivante. Ne pas assumer un grand plan ; laisser le feedback utilisateur
  décider la trajectoire.
related:
- 2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- _RULES-APPLIED
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-1747-session-f978e4ee.md
source_session: f978e4ee-8378-4961-a70b-ecc2e9ede8d3
status: auto-applied
summary: Raphaël valide chaque étape majeure ("OK parfait") puis demande l'action
  suivante, pas une grosse implémentation pré-plannifiée.
tags:
- permanent
- synthesized
- feedback
- pending-review
- methodology
- iteration
- collaboration
- agile
tier: warm
title: 'Workflow itératif : valider par phase plutôt que batch'
topic_cluster: workflow-methodology
type: permanent-note
updated: '2026-05-12'
usage_count: 0
---

Pattern observé dans la session : Raphaël approuve chaque étape ("OK c'est bon c'est fait"), puis immédiatement demande l'étape suivante ("Maintenant tu vas me reset l'instance D...", "Et maintenant on fait un test de perf"). Cela indique une préférence pour les **boucles tight de feedback** plutôt qu'une plannification monolithique en début de tâche.

**Pourquoi** : permet d'ajuster en temps réel, de déterminer le prochain move en fonction des résultats concrets, évite de coder une feature entière qui ne sera pas utilisée telle que conçue. Sur un cutover critique (données prod), c'est aussi une tactique de de-risking : valider chaque phase avant d'avancer.

## Related

- [[2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi]] — Valider systèmes de dispatch via test instances vierges
- [[2026-05-10-analyse-métier-valider-source-de-données-réelle]] — Analyse métier — valider source de données réelle
- [[_RULES-APPLIED]] — 📋 Rules apprises cette semaine — 6 appliquées, 0 archivées
- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)
- [[2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i]] — Paralléliser tâches complexes via teams + sessions indépendantes