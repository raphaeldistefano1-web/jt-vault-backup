---
ai_writable: true
backlinks:
- 2026-04-25-session-context
- 2026-04-25-session-context 2
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- TODO-Site-WP
- Workflow-Collaboration-IA
created: 2026-04-25
description: Pointeur vers la to-do persistante centralisée de Raphaël (mémoire globale
  Claude)
embed_hash: null
embed_model_version: null
entities:
- documentation
- reference
id: 202604252041-todo-centralized
intent: reference
last-accessed: 2026-04-25
related:
- '[[User-Raphael-Distefano]]'
- '[[Workflow-Collaboration-IA]]'
relevance: high
status: active
summary: 'La to-do canonique est dans la mémoire globale de Claude :'
tags:
- todo
- central
tier: warm
topic_cluster: operations
type: resource
updated: 2026-04-25
---

# 📋 TODO Centralisée — pointeur

## Source de vérité

La to-do canonique est dans la mémoire globale de Claude :

**`/root/.claude/projects/-root/memory/todo_raphael.md`**

Avec règle automatique dans `feedback_todo_list.md` qui dit :
> Quand Raphaël demande "ma to-do", "ce qui reste", "qu'est-ce que j'ai à faire", lire et présenter ce fichier.

## Pourquoi pas dans le vault directement ?

La to-do est mise à jour **à chaque session Claude** (Claude Code et Claude Desktop). Elle vit donc plus naturellement dans la mémoire `/root/.claude/projects/-root/memory/` que dans le vault Obsidian.

À terme (quand la stack vault sera vraiment mûre), on pourra symlinker ce fichier dans le vault ou faire un script de sync. Pour l'instant : **vault = référence stable**, **mémoire = état dynamique**.

## Catégories de la to-do

Cf. le fichier source pour la liste complète. Sections :
- **Critique** — à faire dans la semaine
- **Performance & sécurité** — gros boosts dispos
- **Email infrastructure**
- **Stratégique**
- **Contenu pages**
- **PMS**
- **Infra / serveur**
- **Terminé récemment**

## Liens

- [[User-Raphael-Distefano]]
- [[Workflow-Collaboration-IA]]