---
id: 20260614-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-06-14T04:00:02+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-06-14 04:00:02 UTC

## Synthèse
- **srv1524600** — 8 checks OK / 1 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 23.2 MB |
| Curator log | ✅ | dernier run 2026-06-14 03:01 (il y a 1.0h) |
| Synthesizer log | ✅ | dernier run 2026-06-14 00:00 (il y a 4.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ✅ | 28/1041 notes non consolidated |
| Index sync (FS vs DB) | ❌ | disk=1417, db=1359, drift=+58 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 1461 files, 0 errors |
| Disk free / | ✅ | 48.1 GB libre / 96 GB (50% used) |

## Actions recommandées

- **Index sync (FS vs DB)** — disk=1417, db=1359, drift=+58 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
