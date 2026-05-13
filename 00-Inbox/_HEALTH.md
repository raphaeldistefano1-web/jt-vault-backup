---
id: 20260513-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-05-13T04:00:01+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-05-13 04:00:01 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 2 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 13.0 MB |
| Curator log | ✅ | dernier run 2026-05-13 03:05 (il y a 0.9h) |
| Synthesizer log | ✅ | dernier run 2026-05-12 04:07 (il y a 23.9h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ❌ | 56/526 notes non consolidated (> 50) |
| Index sync (FS vs DB) | ❌ | disk=788, db=730, drift=+58 (>5 → reindex incomplet) |
| Syncthing folder | ✅ | idle, 799 files, 0 errors |
| Disk free / | ✅ | 53.3 GB libre / 96 GB (44% used) |

## Actions recommandées

- **Notes non consolidées** — 56/526 notes non consolidated (> 50)
- **Index sync (FS vs DB)** — disk=788, db=730, drift=+58 (>5 → reindex incomplet)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
