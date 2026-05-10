---
ai_writable: false
backlinks:
- 2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a
- 2026-05-10-architecture-decision-records-template-structure
- 2026-05-10-service-worker-offline-pour-pwa-cul-sec
- Dev-PMS-Area
- PMS-Stack
- Workflow-Collaboration-IA
created: 2026-04-25
description: 6 sub-agents internes du projet PMS dans .claude/agents/ — priorité sur
  les plugins officiels Claude Code
embed_hash: null
embed_model_version: null
entities:
- devops
- infrastructure
- pms
id: 202604252031-sub-agents-internes-pms
intent: reference
last-accessed: 2026-04-25
related:
- 2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a
- 2026-05-10-architecture-decision-records-template-structure
- 2026-05-10-service-worker-offline-pour-pwa-cul-sec
- '[[Dev-PMS-Area]]'
- '[[Workflow-Collaboration-IA]]'
relevance: high
status: active
summary: .claude/agents/ à la racine du projet /var/www/pms-jardin-tropical/.
tags:
- pms
- agents
- ai
- claude-code
tier: warm
topic_cluster: pms-architecture
type: resource
updated: 2026-04-25
---

# 🧑‍💼 Sub-agents internes PMS

## Localisation

`.claude/agents/` à la racine du projet `/var/www/pms-jardin-tropical/`.

## Liste (6 agents)

Cf. mémoire `agents_workflow.md` (PMS) pour la matrice de décision exacte. Agents typiques :
- `pms-planner` — plan d'archi feature
- `pms-explorer` — cartographie code
- `pms-reviewer` — review post-implementation
- `pms-simplifier` — refactor / cleanup
- `pms-tester` — tests
- `pms-deployer` — deploy avec safety checks

## Règle de priorité

Quand on travaille dans `/var/www/pms-jardin-tropical/`, **les agents internes du projet ont priorité** sur les plugins officiels Claude Code (`code-explorer`, `code-architect`, `code-reviewer`, `code-simplifier`).

Ils sont plus spécialisés (connaissent les conventions PMS, le stack Next.js 15 + Prisma 6, les workflows preview-then-apply). Fallback sur les plugins officiels uniquement pour les autres projets.

## Quand spawn lequel

Cf. matrice de décision dans la mémoire `agents_workflow.md`.

## Liens

- [[Dev-PMS-Area]]
- [[Workflow-Collaboration-IA]]
- Mémoire référence : `agents_workflow.md` (mémoire projet PMS)

## Related

- [[2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a]] — Nouveaux skills doivent être auto-découverts par agents
- [[2026-05-10-service-worker-offline-pour-pwa-cul-sec]] — Service Worker offline pour PWA CUL SEC
- [[2026-05-10-architecture-decision-records-template-structure]] — Architecture Decision Records template structure