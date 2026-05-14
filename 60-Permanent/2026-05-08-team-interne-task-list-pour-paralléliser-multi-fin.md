---
ai_writable: false
area: null
backlinks:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
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
related:
- '2026-05-07'
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-10-questionsprompts-externalisées-par-jeu
- '2026-05-13'
- _MOC-claude-system
- deep-research
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

## Related

- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia
- [[2026-05-07]] — Veille IA — Jeudi 7 mai 2026
- [[_MOC-claude-system]] — MOC Claude System — système IA personnel
- [[deep-research]] — deep research
- [[2026-05-10-questionsprompts-externalisées-par-jeu]] — Questions/prompts externalisées par jeu
- [[2026-05-13]] — Veille IA — Mercredi 13 mai 2026