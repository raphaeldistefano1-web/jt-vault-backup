---
title: Canonicité vault ↔ mémoire Claude Code
type: index
created: '2026-05-08'
updated: '2026-05-08'
id: canonicity-vault-cc-memory
schema_version: 1
tier: hot
status: active
intent: decision
topic_cluster: vault-architecture
project: claude-system
tags: [canonicity, source-of-truth, memory, decision]
ai_writable: false
---

# Canonicité — vault vs mémoire Claude Code

> Décision actée 2026-05-08 (Phase 3 du plan d'amélioration vault). Cette doc est **prescriptive** : toute future contribution au vault ou à la mémoire CC doit la respecter.

## Règle

**Le vault `/srv/vault/` est la source de vérité unique.**

La mémoire Claude Code (`/root/.claude/projects/-root/memory/*.md`) est un **cache hot strict**, limitée aux faits qui doivent être chargés au tout démarrage de chaque session sans recours au RAG.

Tout doublon entre les deux doit être résolu en faveur du vault.

## Pourquoi cette règle

- **Une seule source de vérité** : pas de conflits, pas de mise à jour à deux endroits
- **Token-efficient** : la mémoire CC charge ~5k tokens à chaque session ; le vault n'est consulté que quand pertinent (via MCP)
- **Hermès convergera mieux** avec une frontière claire : il extrait les rules vers `~/.claude/CLAUDE.md`, le synthesizer alimente le vault, sans se chevaucher
- **Évolutif** : le vault est cross-IA (Mac, web, autres assistants), la mémoire CC est captive

## Ce qui RESTE dans la mémoire CC (whitelist hot)

Cap dur : ~15 fichiers maximum. Critères d'éligibilité cumulatifs :

1. **Hot par essence** : information consultée au démarrage de chaque session (identité, préférences workflow durables)
2. **Stable** : ne change pas quotidiennement
3. **Sans contexte** : se comprend isolément, pas besoin du graphe vault

### Liste autorisée

- `user_role.md` — identité Raphaël, role owner-operator
- `feedback_*.md` — préférences workflow durables (preview-then-apply, terminal, todo, etc.)
- `todo_raphael.md` — to-do centralisée (action live, change quotidiennement)
- `reference_claude_subscription.md` — quotas Plan Max, contraintes API
- `reference_vps_access.md` — comment accéder au VPS (Tailscale, ssh)
- 1-2 facts d'état projet brûlant si vraiment dans le sprint courant

### Tout le reste va au vault

Les `project_*.md`, `reference_*.md` qui décrivent un projet, un état long-terme, une infra → migrer dans `/srv/vault/` (10-Projects, 30-Resources, ou 60-Permanent selon nature).

## Mécanismes

### Audit one-shot (Phase 3.B)

Le script `vault-cc-dedup-audit` (cf. `/usr/local/bin/`) compare chaque mémoire CC contre le vault via `vault-rag-search`. Si match score > 0.78 (top-1), c'est un candidat doublon. Le rapport `00-Inbox/_CC-DEDUP-AUDIT.md` liste les candidats pour validation humaine.

### Promotion CC → vault

Quand on identifie qu'une mémoire CC est devenue trop riche/long-terme :
1. Créer la note correspondante dans le vault (10-Projects ou 30-Resources)
2. Indexer : `vault-rag-index --notes <path>`
3. Retirer le fichier de la mémoire CC
4. Mettre à jour `MEMORY.md` (retirer la ligne)

### Promotion vault → mémoire CC (rare)

Cas : une rule Hermès devient si critique qu'elle doit être au démarrage. Le pipeline `vault-sync-rules` la copie déjà dans `~/.claude/CLAUDE.md`, **pas** dans `/root/.claude/projects/-root/memory/`. Donc en pratique on ne fait jamais cette promotion manuellement.

## Auto-retrieval (Phase 3.5)

Le hook `UserPromptSubmit` `auto_retrieve.py` compense l'absence de notes en mémoire CC : à chaque prompt, il interroge le vault et injecte les notes pertinentes. C'est le bon mécanisme pour que **la canonicité vault ne se traduise pas par une perte de contexte**.

## Métriques de succès

À 2 semaines du déploiement :
- Mémoire CC : ≤ 15 fichiers (vs 39 actuellement)
- Doublons CC ↔ vault : 0 (vérifiable via audit)
- `vault-rag-usage.jsonl` : ≥ 10 queries utiles/semaine (sinon Phase 6 simplification)
- Aucune session avec dégradation perçue (à valider par feedback Raphaël)

## Anti-règles

- ❌ Ne PAS dupliquer une note dans les deux systèmes pour "redondance"
- ❌ Ne PAS retirer une mémoire CC sans la promouvoir d'abord vers le vault si non-doublon
- ❌ Ne PAS mettre des notes auto-générées par Hermès dans la mémoire CC (elles vont dans `~/.claude/CLAUDE.md` via `vault-sync-rules`)
- ❌ Ne PAS référencer un fichier mémoire CC depuis une note vault (les chemins peuvent changer)

## Liens

- Plan d'amélioration : voir mémoire CC `project_vault_rebuild.md`
- Hermès : `vault-sync-rules` + `/reflect-vault` skill
- Hook auto-retrieve : `/root/.claude/hooks/auto_retrieve.py`
