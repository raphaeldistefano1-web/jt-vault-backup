---
ai_writable: false
area: null
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- teams
- tasks
- session paralleling
id: 20260508040142-paralléliser-tâches-complexes-via-teams-sessions-i
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-07-1424-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1419-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1416-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1414-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1341-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1445-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1553-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1538-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1319-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1413-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1429-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1511-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1311-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1457-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1543-session-e172a5dd.md
source_session: e172a5dd-5040-43b5-8a0e-4fec08f8f037
status: active
summary: Décomposer tâche complexe en N findings indépendants → dispatcher chaque
  sur session séparée via teams. Isolement contexte + parallèle vrai.
tags:
- permanent
- synthesized
- workflow
- parallelization
- agent coordination
tier: warm
title: Paralléliser tâches complexes via teams + sessions indépendantes
topic_cluster: claude-system
type: permanent-note
updated: '2026-05-08'
---

**Pattern** : quand une session coupe au milieu d'une tâche multi-finding, ou quand findings sont indépendants (ex: findings #1 et #2 de veille-ia) :
1. Créer `team: veille-ia-build` avec tasks list.
2. Assigner finding #1 → agent1, finding #2 → agent2.
3. Chaque agent tourne en session séparée, contexte isolé.
4. Parallélisme vrai (pas séquentiel dans une session).

**Avantage** : 
- Pas de compétition contexte window entre findings.
- Si une session coupe, l'autre continue.
- Scaling linéaire : N findings = N sessions parallèles.
- Cada agent peut avoir ses skills/tools spécialisés.

**Setup** : `TeamCreate(team_name, description)` → crée team + task list. Puis `Agent(..., team_name=..., name=...)` pour dispatcher agents nommés à la team. Ils se coordonnent via task list (TaskUpdate pour claim + mark completed).