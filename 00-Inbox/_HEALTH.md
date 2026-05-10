---
id: 20260510-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-05-10T04:00:02+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-05-10 04:00:02 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 2 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 8.1 MB |
| Curator log | ✅ | dernier run 2026-05-10 03:04 (il y a 0.9h) |
| Synthesizer log | ✅ | dernier run 2026-05-10 00:00 (il y a 4.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ❌ | 88/320 notes non consolidated (> 50) |
| Index sync (FS vs DB) | ❌ | disk=485, db=426, drift=+59 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 496 files, 0 errors |
| Disk free / | ✅ | 47.5 GB libre / 96 GB (50% used) |

## Actions recommandées

- **Notes non consolidées** — 88/320 notes non consolidated (> 50)
- **Index sync (FS vs DB)** — disk=485, db=426, drift=+59 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
