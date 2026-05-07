---
type: workflow
status: active
tags: [workflow, ui, pms]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Workflow obligatoire pour toute refonte UI du PMS — passer par route _v2 prévisualisable"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[PMS-Dashboard-v2]]"
  - "[[PMS-Calendar-v2]]"
id: 202604252029-workflow-preview-then-apply
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Toute refonte UI d'envergure du Dev-PMS-Area|PMS passe par une route v2 prévisualisable, jamais de modif directe sur le …"
entities: [calendar, dashboard, pms]
topic_cluster: pms-patterns
intent: how-to
tier: warm
---

# 🎨 Workflow Preview-Then-Apply

## Règle

Toute refonte UI d'envergure du [[Dev-PMS-Area|PMS]] passe par une **route `_v2` prévisualisable**, **jamais** de modif directe sur le shell prod.

## Why ?

Le PMS est utilisé en prod par [[User-Raphael-Distefano|Raphaël]] au quotidien pour piloter l'hôtel. Une UI cassée = blocage opérationnel.

## How

1. Créer une route ou route group `_v2` (ex: `/dashboard-v2`, `/calendar-v2`)
2. Implémenter la nouvelle UI dans cette route
3. Le user prévisualise et valide via cette route
4. Quand validé : "appliquer en prod" = swap les composants/routes pour que `/dashboard` serve la v2
5. La v1 reste accessible quelques jours en `_v1` pour rollback

## Exemples passés

- [[PMS-Dashboard-v2]] — appliqué prod 2026
- [[PMS-Calendar-v2]] — appliqué prod 2026
- [[PMS-Settings-Hub]] — consolidation paramètres en hub

## Liens

- [[Dev-PMS-Area]]
- [[Workflow-Deploy-PMS]]
