---
ai_writable: false
area: null
backlinks:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- Whisper-VPS-Reference
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- VPS Hostinger
- systemd
- watchdog
- mail
id: 20260512040044-watchdog-cpu-durgence-pattern-systemd
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- Whisper-VPS-Reference
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
schema_version: 1
source_notes:
- 10-Projects/openclaw-plugin/2026-05-11-2047-session-a2f2421f.md
- 10-Projects/openclaw-plugin/2026-05-11-1820-session-a2f2421f.md
- 10-Projects/openclaw-plugin/2026-05-11-1809-session-a2f2421f.md
- 10-Projects/openclaw-plugin/2026-05-11-2045-session-a2f2421f.md
- 10-Projects/openclaw-plugin/2026-05-11-1823-session-a2f2421f.md
- 10-Projects/claude-system/2026-05-11-1748-session-a2f2421f.md
- 10-Projects/claude-system/2026-05-11-2119-session-a2f2421f.md
- 10-Projects/claude-system/2026-05-11-1805-session-a2f2421f.md
- 10-Projects/claude-system/2026-05-11-2122-session-a2f2421f.md
- 10-Projects/claude-system/2026-05-11-2100-session-a2f2421f.md
- 10-Projects/claude-system/2026-05-11-2052-session-a2f2421f.md
source_session: a2f2421f-261b-497a-ab22-7566cddd56d7
status: active
summary: Script Python systemd qui arrête services si CPU > 80%, envoie email rapport.
tags:
- permanent
- synthesized
- cpu-throttling
- monitoring
- emergency
- automation
tier: warm
title: Watchdog CPU d'urgence — pattern systemd
topic_cluster: vps-cpu-management
type: permanent-note
updated: '2026-05-12'
---

**Architecture** : `/usr/local/bin/cpu-emergency-watchdog.py` + unité systemd timer (service + socket-based trigger).

**Comportement** : Polling continu du CPU via `/proc/stat`. Seuil 80% → arrête services listés dans config JSON (containers Docker, services systemd) → mail à owner avec rapport (timestamp, CPU peak, services arrêtés).

**Config** : `/etc/cpu-emergency/config.json` : listes de containers Docker + services systemd à pausable, seuil CPU, email destination, interval polling.

**Activation** : `systemctl enable --now cpu-emergency-watchdog.service` + timer pour réactivation périodique.

**Contexte** : Créé suite à throttling agressif VPS Hostinger (2 vCPU EPYC, limite burst 3h @ 85%). Watchdog prévient dépassement et limite domino (OOM, freeze).

## Related

- [[2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak]] — Cron 23h30 pour ingestion veille (timing off-peak)
- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule