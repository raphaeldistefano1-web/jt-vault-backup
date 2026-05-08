---
title: Vault RAG — usage week report
type: meeting
created: '2026-05-08'
updated: '2026-05-08'
id: usage-week-20260508
schema_version: 1
tier: warm
status: report
intent: log
topic_cluster: vault-usage
project: claude-system
tags: [usage, telemetry, weekly, ai-generated]
ai_writable: false
---

# 📊 Vault RAG — usage report (2026-05-01 → 2026-05-08)

> Total **2 appels MCP** sur 7 jours. Source : `/var/log/vault-rag-usage.jsonl`.

## 🚨 Phase 6 — alerte simplification

**2 queries** cette semaine, en dessous du seuil 10. Si ça persiste 2 semaines → désactiver MCP + synthesizer (cron commenté), garder vault en lecture humaine + Syncthing.

## Queries par jour

- `2026-05-08` :   2 ▇▇

## Répartition des tools

- `vault_search` : 1 (50%)
- `vault_get_note` : 1 (50%)

## Latence

- p50 : **123ms**
- p95 : **123ms**
- moyenne : **66ms**

## 🏆 Top-10 notes retournées (dans top-3)

- `test-id-1` : 1 fois
- `test-id` : 1 fois

## Projets ciblés (filtre `project:`)

- `claude-system` : 1

---
_Rapport généré par `vault-usage-report` le 2026-05-08 10:05 UTC._