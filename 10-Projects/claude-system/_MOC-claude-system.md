---
id: 20260507-1101-moc-claude-system
type: moc
title: "MOC Claude System — système IA personnel"
project: claude-system
area: null
status: active
confidence: high
summary: "Hub pour l'amélioration continue du système IA Claude de Raphaël (agents, skills, hooks, mémoire, vault)."
intent: reference
entities: [claude-code, agents, skills, hooks, memory, vault, mcp]
topic_cluster: ai-tooling
related: ["[[20260507-1530-vault-rebuild]]"]
moc: "[[INDEX]]"
source: null
tier: hot
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [claude, ai, system]
ai_writable: false
---

# 🧠 MOC — Claude System

> Hub pour l'amélioration continue du **système IA personnel** de Raphaël : agents, skills, hooks, mémoire, plugins, intégrations Obsidian.

## Sous-domaines

### Vault Obsidian
- Voir `vault/` du projet
- En cours : refonte multi-projets (Phases 0-3 mai 2026) — cf. [[20260507-1530-vault-rebuild]]

### Agents & skills
- Plugin officiels installés : feature-dev, code-review, frontend-design, claude-md-management, ralph-loop, superpowers
- Sub-agents projet (PMS) : pms-planner, pms-explorer, pms-implementer, etc.

### Hooks Claude Code
- Phase 3 (en cours) : hook `Stop` extract_memory (Haiku 4.5)
- Phases futures : `SessionStart`, `UserPromptSubmit`

### Mémoire & contexte
- Mémoire CC : `/root/.claude/projects/-root/memory/` (28 entrées)
- Vault Obsidian : `/srv/vault/` (cerveau multi-projets, ce système)
- Pont : Phase 3 hook Stop écrit dans Inbox vault

### MCP servers
- Phase 4 prévu : iansinnott/obsidian-claude-code-mcp, dan6684/smart-connections-mcp
- Existants : Context7, Canva, Drive, WordPress

### Semantic search (Phase 4+)
- Stack cible : Smart Connections + nomic-embed-text-v2-moe via Ollama + sqlite-vec
- Activation seuil : ~200-300 notes

## Notes (à venir)

Cette section se remplira au fur et à mesure que des notes atomiques seront créées sur :
- Patterns d'agents efficaces
- Choix de modèles par tâche (économie tokens)
- Pipeline auto-alimentation vault
- Mécanismes de retrieval token-efficient
