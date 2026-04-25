---
type: area
status: active
tags: [workflow, ia, collaboration]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Comment Raphaël collabore avec ses IA — préférences, mode auto, to-do persistante, conventions"
ai_writable: false
related:
  - "[[User-Raphael-Distefano]]"
  - "[[TODO-centralized]]"
  - "[[Mu-plugin-vs-Theme-Pattern]]"
---

# 🤝 Workflow Collaboration IA

## Mode auto

[[User-Raphael-Distefano|Raphaël]] utilise massivement le **mode auto** de Claude Code. Implications :

1. **Action > planification** : faire plutôt que demander confirmation
2. **Pas de blocage** sur des décisions de routine — assumer raisonnable et avancer
3. **Course corrections** acceptées en cours de route
4. **Pas d'actions destructives** sans validation : `rm -rf`, `force push`, drop tables
5. **Pas d'exfiltration** sans autorisation explicite

## Pile d'outils IA

- **Claude Code** (Opus 4.7) — daily driver, mode auto
- **Cursor** — usage occasionnel pour code
- **ChatGPT** — usage ponctuel
- **Gemini** — rare
- **Site Kit Google** — installé sur WP, à configurer

## Plugins officiels Claude Code installés

7 plugins, dispatch automatique sur déclencheurs :
- `code-explorer` — cartographie code inconnu
- `code-architect` — plan archi feature non-triviale
- `code-reviewer` — review post-implementation
- `code-simplifier` — simplification gros diff
- `frontend-design` — composants UI distinctifs
- `claude-md-improver` — audit/improve CLAUDE.md
- `superpowers:*` — ensemble de skills

## Sous-agents projet PMS

Quand on travaille dans `/var/www/pms-jardin-tropical`, **les sub-agents internes du projet ont priorité** sur les plugins officiels (cf. [[Sub-agents-internes-PMS]]).

## Conventions

- **Langue** : français
- **Commits** : conventional (`feat:`, `fix:`, `docs:`)
- **Branches** : feature courtes, merge sur `main`
- **Code review** : auto via `code-reviewer` avant merge majeur
- **Workflow refonte UI** : [[Workflow-Preview-Then-Apply]]
- **API integrations** : [[Workflow-API-Integrations]]
- **Deploy PMS** : [[Workflow-Deploy-PMS]]

## To-do persistante

[[User-Raphael-Distefano|Raphaël]] veut une **to-do centralisée** présentée à la demande (formulations : "ma to-do", "ce qui reste", "qu'est-ce qui me reste à faire"). Cf. [[TODO-centralized]] et la mémoire `feedback_todo_list.md`.

À chaque action manuelle qui ne peut être automatisée, **ajouter à la to-do**. Cocher `[x]` quand fait, garder l'historique 30 jours.

## Approche optim WP

[[Mu-plugin-vs-Theme-Pattern|Pattern]] : compléter le theme via mu-plugin plutôt que d'installer un plugin SEO/perf qui voudrait écraser. Le theme `jardintropical-child` est déjà ultra pro.
