---
ai_writable: false
area: null
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- veille-ia-build
- team
- task-coordination
- inboxes
id: 20260508100040-team-interne-task-list-pour-paralléliser-multi-fin
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-0844-session-e172a5dd.md
source_session: e172a5dd-5040-43b5-8a0e-4fec08f8f037
status: active
summary: Veille-ia-youtube utilise structure team (`veille-ia-build`) avec task-list
  et inboxes pour paralléliser analyses.
tags:
- permanent
- synthesized
- multi-agent
- coordination
- parallelization
- team-structure
tier: warm
title: Team interne + task-list pour paralléliser multi-findings
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-08'
---

Pattern de coordination multi-agents : chaque finding complexe (ex: Finding #1, Finding #2) = 1 session/agent isolé, coordonné via team central. Structure : `/root/.claude/teams/veille-ia-build/config.json` (membership), `/root/.claude/teams/veille-ia-build/inboxes/` (messages asynchrones), `/root/.claude/tasks/veille-ia-build/` (task list). Avantage : évite context-window saturation quand N findings en parallèle, permet progression indépendante, inbox capture outputs pour synthèse finale. Pattern réutilisable pour tout pipeline multi-findings (audit, refactoring, migration).