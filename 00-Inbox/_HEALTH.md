---
id: 20260509-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-05-09T04:00:01+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-05-09 04:00:01 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 1 critical sur 8

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 7.0 MB |
| Curator log | ✅ | dernier run 2026-05-09 03:06 (il y a 0.9h) |
| Synthesizer log | ✅ | dernier run 2026-05-08 04:02 (il y a 24.0h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ❌ | 96/176 notes non consolidated (> 50) |
| Syncthing folder | ✅ | idle, 330 files, 0 errors |
| Disk free / | ✅ | 49.6 GB libre / 96 GB (48% used) |

## Actions recommandées

- **Notes non consolidées** — 96/176 notes non consolidated (> 50)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
