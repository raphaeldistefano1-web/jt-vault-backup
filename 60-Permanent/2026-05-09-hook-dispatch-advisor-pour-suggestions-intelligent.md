---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- dispatch_advisor.py
- hooks
- claude-system
id: 20260509040129-hook-dispatch-advisor-pour-suggestions-intelligent
intent: decision
last-accessed: '2026-05-09'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1442-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1802-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1721-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1459-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1649-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1605-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1613-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1452-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1444-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1433-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1604-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1828-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1449-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1651-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1440-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1616-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1822-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1454-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1622-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1619-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1437-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1656-session-21c4cfc3.md
- 10-Projects/pms-jardin-tropical/2026-05-08-1625-session-21c4cfc3.md
source_session: 21c4cfc3-93d1-4d4d-9bab-ab7b63ed0c6a
status: active
summary: Hook UserPromptSubmit dispatch_advisor.py suggère agents/skills/plugins/MCP
  pertinents en début de chaque prompt, basé sur task_type détecté.
tags:
- permanent
- synthesized
- agent-suggestion
- UX-automation
- dispatch
tier: warm
title: Hook dispatch_advisor pour suggestions intelligentes
topic_cluster: automation
type: permanent-note
updated: '2026-05-09'
---

Hook `dispatch_advisor.py` inspecte chaque prompt entrant et suggère :
- Agents recommandés (Explore, Architect, Reviewer, Simplifier)
- Skills éligibles (Impeccable, emil-design-eng, elements-of-style, deep-research, etc.)
- MCP servers pertinents (Context7, Canva, Vault)
- Coût estimé token (warning si > moyen)

**Décision** : au lieu de laisser user naviguer manuellement le catalogue 40+ outils, automatiser la suggestion basée sur type de tâche (design, prose, research, code-review).

**Mécanisme** : regex sur mots-clés prompt + catalogue `.claude/dispatch_catalog.py` (YAML éditable).

**Bénéfice** : réduit surcharge cognitive, évite oublis systématiques (pre-mortem avant prod, code-review avant merge).