---
id: 20260607-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-06-07T04:00:01+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-06-07 04:00:01 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 2 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 22.3 MB |
| Curator log | ✅ | dernier run 2026-06-07 03:00 (il y a 1.0h) |
| Synthesizer log | ✅ | dernier run 2026-06-07 00:00 (il y a 4.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ❌ | 60/1006 notes non consolidated (> 50) |
| Index sync (FS vs DB) | ❌ | disk=1349, db=1290, drift=+59 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 1393 files, 0 errors |
| Disk free / | ✅ | 48.1 GB libre / 96 GB (50% used) |

## Actions recommandées

- **Notes non consolidées** — 60/1006 notes non consolidated (> 50)
- **Index sync (FS vs DB)** — disk=1349, db=1290, drift=+59 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
