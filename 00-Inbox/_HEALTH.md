---
id: 20260603-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-06-03T04:00:01+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-06-03 04:00:01 UTC

## Synthèse
- **srv1524600** — 8 checks OK / 1 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 21.3 MB |
| Curator log | ✅ | dernier run 2026-06-03 03:01 (il y a 1.0h) |
| Synthesizer log | ✅ | dernier run 2026-06-02 04:00 (il y a 24.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ✅ | 47/948 notes non consolidated |
| Index sync (FS vs DB) | ❌ | disk=1257, db=1198, drift=+59 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 1301 files, 0 errors |
| Disk free / | ✅ | 50.8 GB libre / 96 GB (47% used) |

## Actions recommandées

- **Index sync (FS vs DB)** — disk=1257, db=1198, drift=+59 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
