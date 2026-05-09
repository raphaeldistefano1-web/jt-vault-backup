---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- Mémoire Claude
- Vault Obsidian
- todo_raphael.md
id: 20260509040209-hiérarchie-persistance-mémoire-vs-vault-vs-todo
intent: decision
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
summary: 'Trois systèmes parallèles avec source de vérité explicite : Mémoire = identité/règles
  éternelles, Vault = décisions archi, Todo = actions atomiques.'
tags:
- permanent
- synthesized
- architecture
- knowledge-structure
- multi-system
tier: hot
title: 'Hiérarchie persistance : Mémoire vs Vault vs Todo'
topic_cluster: knowledge-management
type: permanent-note
updated: '2026-05-09'
---

## Trois sources de vérité

| Système | Contenu | Exemples |
|---|---|---|
| **Mémoire Claude** | Identité utilisateur, préférences collab, "rules" transversales, pointeurs projets | Qui est l'utilisateur, comment il veut qu'on bosse, conventions de code, équipe |
| **Vault Obsidian** | Décisions techniques/archi (ADR), apprentissages métier, contexte projet riche | Pourquoi tel choix tech, archi système, audits, ADR, états détaillés |
| **todo_raphael.md** | Actions atomiques en attente, vivant, change quotidiennement | Ce qu'il doit faire manuellement (site, PMS, infra, hôtel) |

## Ordre de recherche imposé avant toute question

1. Contexte hooks injecté (système)
2. MEMORY.md (index mémoire Claude)
3. Fichiers mémoire individuels (Read ciblé)
4. Vault via vault_search (décisions archi/contexte)
5. todo_raphael.md (actions en attente)
6. Code source (grep, glob, agents Explore)
7. Demander à l'utilisateur (dernier recours)

## Où écrire quoi

- Nouveau fait identitaire durable → Mémoire Claude
- Nouvelle décision archi/contexte projet → Vault (format ADR si décision)
- Nouvelle action manuelle → todo_raphael.md

Cette hiérarchie élimine les redémarrages mémoire et structure la recherche avant d'importuner l'utilisateur.