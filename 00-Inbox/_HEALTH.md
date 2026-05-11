---
id: 20260511-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-05-11T04:00:28+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-05-11 04:00:28 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 2 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 8.1 MB |
| Curator log | ✅ | dernier run 2026-05-11 03:59 (il y a 0.0h) |
| Synthesizer log | ✅ | dernier run 2026-05-10 04:07 (il y a 23.9h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ❌ | 99/417 notes non consolidated (> 50) |
| Index sync (FS vs DB) | ❌ | disk=609, db=426, drift=+183 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 620 files, 0 errors |
| Disk free / | ✅ | 44.4 GB libre / 96 GB (54% used) |

## Actions recommandées

- **Notes non consolidées** — 99/417 notes non consolidated (> 50)
- **Index sync (FS vs DB)** — disk=609, db=426, drift=+183 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
