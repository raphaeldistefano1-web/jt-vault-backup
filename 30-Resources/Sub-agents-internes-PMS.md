---
type: resource
status: active
tags: [pms, agents, ai, claude-code]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "6 sub-agents internes du projet PMS dans .claude/agents/ — priorité sur les plugins officiels Claude Code"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[Workflow-Collaboration-IA]]"
id: 202604252031-sub-agents-internes-pms
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: ".claude/agents/ à la racine du projet /var/www/pms-jardin-tropical/."
entities: [devops, infrastructure, pms]
topic_cluster: pms-architecture
intent: reference
tier: warm
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
