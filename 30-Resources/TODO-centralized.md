---
type: resource
status: active
tags: [todo, central]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Pointeur vers la to-do persistante centralisée de Raphaël (mémoire globale Claude)"
ai_writable: true
related:
  - "[[User-Raphael-Distefano]]"
  - "[[Workflow-Collaboration-IA]]"
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
