---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- interface-design
- adr
- claude-system
id: 20260509040127-3-régimes-dintégration-plugin-distincts
intent: pattern
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
summary: 'Trois contextes d''intégration plugin nécessitent trois niveaux de persistance
  : décisions visuelles → .interface-design/system.md, décisions archi → docs/adr/,
  décisions comportement → CLAUDE.md.'
tags:
- permanent
- synthesized
- plugin-integration
- architecture
- persistence
tier: warm
title: 3 régimes d'intégration plugin distincts
topic_cluster: plugin-architecture
type: permanent-note
updated: '2026-05-09'
---

Régimes corrects :

1. **Décisions visuelles** (palette, spacing, motion, composants) → `.interface-design/system.md` (skill interface-design officiel, relectures cross-session)

2. **Décisions archi** (technologies, patterns, trade-offs) → `docs/adr/NNNN-slug.md` (ADR RFC 5242 standard, horodatage)

3. **Décisions comportement agent** (rules de dispatch, permissions, hooks) → `CLAUDE.md` global ou project-level

Chaque régime a son outil, sa fréquence d'audit, ses relecteurs. Pas de shortcut "tout dans CLAUDE.md".