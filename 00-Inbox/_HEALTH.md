---
id: 20260508-vault-health
type: report
title: "🚨 Vault Health Check"
project: claude-system
status: active
summary: "Health check vault — généré 2026-05-08T04:00:02+0000"
intent: monitor
tier: hot
tags: [health, monitor, ai-generated, alert]
ai_writable: false
auto-generated: true
---

# 🏥 Vault Health — 2026-05-08 04:00:02 UTC

## Synthèse
- **srv1524600** — 7 checks OK / 1 critical sur 8

## Checks détaillés

| Check | État | Détail |
|---|---|---|
| Ollama | ✅ | version 0.23.1 |
| Vault.db | ✅ | integrity ok, 4.3 MB |
| Curator log | ✅ | dernier run 2026-05-08 03:00 (il y a 1.0h) |
| Synthesizer log | ✅ | dernier run 2026-05-07 13:24 (il y a 14.6h) |
| Inbox backlog | ✅ | 0 notes en backlog |
| Notes non consolidées | ✅ | 40/61 notes non consolidated |
| Syncthing folder | ❌ | URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1000) |
| Disk free / | ✅ | 50.0 GB libre / 96 GB (48% used) |

## Actions recommandées

- **Syncthing folder** — URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1000)

---

_Auto-régénéré toutes les heures par `/usr/local/bin/vault-doctor` (cron `/etc/cron.d/vault-doctor`)._
