---
id: 70-data-README
type: index
title: "70-Data — métriques Claude Code persistées"
project: claude-system
tier: warm
created: 2026-05-10
updated: 2026-05-10
tags: [data, metrics, claude-code, sqlite]
ai_writable: false
---

# 70-Data

Couche de **données quantitatives** sur l'usage Claude Code, séparée des notes de connaissance (qui restent dans `00-Inbox/` → `10-Projects/` → `60-Permanent/`).

## Pourquoi un dossier séparé

Le reste du vault est en Markdown, conçu pour être lu / lié sémantiquement (RAG, MOC, wikilinks). Cette couche-ci est **structurée, requêtable, agrégeable** — pas adaptée au format note. SQLite est le bon outil pour ça.

## Contenu

| Fichier | Quoi |
|---|---|
| `metrics.db` | SQLite — toutes les sessions Claude Code (tokens, modèle, tools, coût estimé) |
| `metrics.db-wal`, `metrics.db-shm` | Sidecar WAL SQLite — **exclus du sync Syncthing** (volatile, propre à chaque host) |
| `schema.sql` | Schéma versionné (re-jouable pour migration) |
| `queries.md` | Bibliothèque de requêtes utiles |

## Comment lire la DB

### Depuis VPS
```bash
sqlite3 /srv/vault/70-Data/metrics.db "SELECT * FROM v_tokens_by_project_30d;"
```

### Depuis Mac (via Obsidian)
La DB est syncée sur le Mac via Syncthing (sauf les WAL). Ouvrable avec **DB Browser for SQLite** (gratuit, brew install). Plus tard : plugin Obsidian Bases (1.9+) pourra exposer des vues directement dans Obsidian.

## Pipeline

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│ Claude Code     │      │ Hook Stop        │      │ /srv/vault/     │
│ session         │─────▶│ extract_memory   │─────▶│ 00-Inbox/       │
│ (génère JSONL)  │      │ + lib/metrics.py │      │ <session>.md    │
└─────────────────┘      │                  │      │ (frontmatter    │
                         │                  │      │  enrichi)       │
                         │                  │      └─────────────────┘
                         │                  │      ┌─────────────────┐
                         │                  │─────▶│ 70-Data/        │
                         │                  │      │ metrics.db      │
                         └──────────────────┘      │ (insert row)    │
                                                   └─────────────────┘
```

## Schéma (résumé)

- `sessions` : 1 ligne par session capturée. Clé naturelle (session_id, transcript_path)
- `tool_calls` : breakdown par tool (Bash, Edit, mcp__*…)
- `agents_dispatched` : breakdown par sub-agent type (code-explorer, …)
- `mcp_calls` : breakdown par serveur MCP (codex, vault, context7…)
- 3 vues pré-construites : `v_tokens_by_project_30d`, `v_top_sessions_7d`, `v_agents_30d`

Détail complet : `schema.sql`.

## Pricing utilisé pour `cost_usd_est`

Prix Anthropic publics (à ajuster dans `lib/metrics.py` si Anthropic les modifie) :

| Modèle | Input $/M | Output $/M | Cache write $/M | Cache read $/M |
|---|---:|---:|---:|---:|
| Opus 4.7 | 15.00 | 75.00 | 18.75 | 1.50 |
| Sonnet 4.6 | 3.00 | 15.00 | 3.75 | 0.30 |
| Haiku 4.5 | 1.00 | 5.00 | 1.25 | 0.10 |

Sur Plan Max 5x sans API, ces dollars ne sont **pas dépensés** — c'est un proxy d'usage, utile pour comparer projets et identifier les sessions coûteuses du quota.

## Backfill rétroactif

Tous les transcripts JSONL existants dans `~/.claude/projects/` sont rejouables :
```bash
claude-metrics-backfill --dry-run        # estime le volume
claude-metrics-backfill                  # insère réellement
claude-metrics-backfill --since 2026-04-01  # limite à une fenêtre
```

Idempotent (UNIQUE sur `session_id, transcript_path`).
