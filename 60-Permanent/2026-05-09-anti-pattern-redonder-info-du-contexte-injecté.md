---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- contexte injecté
- Mémoire Claude
- MEMORY.md
id: 20260509040209-anti-pattern-redonder-info-du-contexte-injecté
intent: gotcha
last-accessed: '2026-05-09'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1726-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1811-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1821-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1832-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1753-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1823-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1755-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1732-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1758-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1736-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1743-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1809-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1825-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1750-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1827-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1802-session-96ce7c71.md
- 10-Projects/claude-system/2026-05-08-1740-session-96ce7c71.md
source_session: 96ce7c71-9b8d-45c1-a608-8a8a0cffb777
status: active
summary: Demander à l'utilisateur une info présente dans contexte injecté = perte
  sèche quota + frustration. Vérifier 7 sources avant de poser une question.
tags:
- permanent
- synthesized
- anti-pattern
- efficacité
- perte-quota
tier: warm
title: 'Anti-pattern : redonder info du contexte injecté'
topic_cluster: knowledge-management
type: permanent-note
updated: '2026-05-09'
---

Quand on se prend à demander "tu peux me redire X ?", c'est symptôme : on n'a pas cherché assez fort dans les sources disponibles.

## Manifestations type
- Demander une préférence déjà documentée en MEMORY.md
- Ignorer l'ordre de recherche 7 étapes et sauter directement au user
- Redémarrer conversation sans relire MEMORY.md ou CLAUDE.md injecté

## Coûts
- Perte sèche de tokens (redonde information présente)
- Frustration utilisateur ("tu oublies déjà ?")
- Signal d'inattention

## Prévention
Toujours vérifier MEMORY.md + contexte injecté AVANT de poser une question. Si pas de réponse dans les 7 sources, seul là demander.