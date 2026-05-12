---
ai_writable: false
aliases:
- AGENTS.md
backlinks:
- Linux-Foundation-AAIF
- MCP-Model-Context-Protocol
- Vault-Setup
created: 2026-04-25
description: Standard fichier AGENTS.md à la racine d'un repo/vault — orientation
  universelle des agents IA
embed_hash: null
embed_model_version: null
entities:
- documentation
- mcp
- reference
id: 202604252026-agents-md-standard
intent: concept
last-accessed: 2026-04-25
related:
- '[[MCP-Model-Context-Protocol]]'
- '[[Vault-Setup]]'
- '[[Linux-Foundation-AAIF]]'
relevance: high
status: active
summary: 'Fichier markdown à la racine d''un projet/repo/vault, lu en premier par
  les agents IA pour s''orienter : identité user, st…'
tags:
- agents-md
- ai
- standard
tier: warm
topic_cluster: vault-architecture
type: concept
updated: 2026-04-25
---

# 📜 AGENTS.md — standard 2026

## Définition

Fichier markdown à la racine d'un projet/repo/vault, lu en premier par les agents IA pour s'orienter : identité user, structure, règles, FAQ, conventions. Équivalent à `README.md` mais **ciblé agents** plutôt que humains.

## Histoire

- **Créé par OpenAI** (initialement pour Codex CLI)
- **Donné à la Linux Foundation** (AAIF) en décembre 2025, comme [[MCP-Model-Context-Protocol|MCP]]
- Adopté par 60k+ repos en 2026
- Lu par défaut par : **Cursor, Codex CLI, Gemini CLI, Aider** et — par symlink vers `CLAUDE.md` — par **Claude Desktop, Claude Code**

## Sections recommandées

```markdown
# AGENTS.md

## Identité utilisateur
- Qui je suis, mon rôle, mes préférences

## Pointeurs vault/repo
- Quels fichiers consulter en priorité

## Règles
- Ce que l'IA peut/doit/ne doit pas faire

## FAQ
- Infos qu'aucune IA ne doit redemander

## Conventions
- Code style, commits, deploy
```

## Pattern symlink

Pour cohabiter avec les conventions historiques de Claude (`CLAUDE.md`) sans dupliquer :

```bash
cd vault/
ln -sf AGENTS.md CLAUDE.md
```

→ un seul fichier source, les deux noms y pointent.

## Usage Le Jardin Tropical

Le vault `/srv/vault-jardin-tropical/` a son `AGENTS.md` à la racine + `CLAUDE.md` symlinké. Toutes les IA y trouvent en 30 sec :
- Profil [[User-Raphael-Distefano|Raphaël]]
- Stack technique (cf. [[Stack-Tech]])
- Pointeurs MOCs ([[Hotel]], [[PMS]], [[Site-WordPress]])
- Règles d'écriture pour IA (frontmatter, atomic notes, append-only sur archives)

## Liens

- Spec officielle : https://agentsmd.org (à vérifier)
- Repo de référence : https://github.com/openai/codex-cli