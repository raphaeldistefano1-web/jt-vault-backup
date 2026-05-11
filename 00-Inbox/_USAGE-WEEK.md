---
title: Vault RAG — usage week report
type: meeting
created: '2026-05-10'
updated: '2026-05-10'
id: usage-week-20260510
schema_version: 1
tier: warm
status: report
intent: log
topic_cluster: vault-usage
project: claude-system
tags: [usage, telemetry, weekly, ai-generated]
ai_writable: false
---

# 📊 Vault RAG — usage report (2026-05-03 → 2026-05-10)

> Total **5 appels MCP** sur 7 jours. Source : `/var/log/vault-rag-usage.jsonl`.

## 🚨 Phase 6 — alerte simplification

**5 queries** cette semaine, en dessous du seuil 10. Si ça persiste 2 semaines → désactiver MCP + synthesizer (cron commenté), garder vault en lecture humaine + Syncthing.

## Queries par jour

- `2026-05-10` :   5 ▇▇▇▇▇

## Répartition des tools

- `vault_get_note` : 3 (60%)
- `vault_search` : 2 (40%)

## Latence

- p50 : **66ms**
- p95 : **622ms**
- moyenne : **238ms**

## 🏆 Top-10 notes retournées (dans top-3)

- `20260507-index-montage-video` : 2 fois
- `20260507-1107-moc-montage-video` : 2 fois
- `202605100114-session-19e3ce30-alors-j-ai-un-petit-projet-dif` : 2 fois
- `202605071400-session-e7718f3c-ok-alors-nous-deux-on-va-bosse` : 1 fois
- `color-expert` : 1 fois

## Projets ciblés (filtre `project:`)

- `montage-video` : 1

---
_Rapport généré par `vault-usage-report` le 2026-05-10 21:00 UTC._