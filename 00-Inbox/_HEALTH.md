---
id: 20260525-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-05-25T04:00:01+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-05-25 04:00:01 UTC

## Synthèse
- **srv1524600** — 8 checks OK / 1 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 18.3 MB |
| Curator log | ✅ | dernier run 2026-05-25 03:00 (il y a 1.0h) |
| Synthesizer log | ✅ | dernier run 2026-05-24 04:00 (il y a 24.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ✅ | 33/797 notes non consolidated |
| Index sync (FS vs DB) | ❌ | disk=1083, db=1023, drift=+60 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 1127 files, 0 errors |
| Disk free / | ✅ | 51.8 GB libre / 96 GB (46% used) |

## Actions recommandées

- **Index sync (FS vs DB)** — disk=1083, db=1023, drift=+60 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
