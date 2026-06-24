---
id: 20260624-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-06-24T04:00:01+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-06-24 04:00:01 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 2 critical sur 9

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 28.0 MB |
| Curator log | ✅ | dernier run 2026-06-24 03:00 (il y a 1.0h) |
| Synthesizer log | ✅ | dernier run 2026-06-23 04:00 (il y a 24.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ✅ | 7/1099 notes non consolidated |
| Index sync (FS vs DB) | ❌ | disk=1512, db=1454, drift=+58 (>5 → reindex incomplet) |
| Syncthing folder | ❌ | URLError: timed out |
| Disk free / | ✅ | 64.9 GB libre / 96 GB (32% used) |

## Actions recommandées

- **Index sync (FS vs DB)** — disk=1512, db=1454, drift=+58 (>5 → reindex incomplet)
- **Syncthing folder** — URLError: timed out

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
