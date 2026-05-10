---
ai_writable: false
area: null
backlinks:
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-08-youtube-bloque-requêtes-datacenter-proxy-résidenti
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- veille-ia
- cron
- scheduler
id: 20260507132310-cron-23h30-pour-ingestion-veille-timing-off-peak
intent: config
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- Decision-Disable-WP-Cron-cron-Linux
- Vault-Setup
source_notes:
- 10-Projects/claude-system/2026-05-07-1126-session-9416e8cf.md
- 10-Projects/claude-system/2026-05-07-1128-session-9416e8cf.md
source_session: 9416e8cf-0e57-49ee-8bcf-07142a66cca6
status: active
summary: Lancement ingestion 23h30 pour éviter congestion réseau et optimiser bande
  passante VPS.
tags:
- permanent
- synthesized
- scheduling
- ops
tier: cold
title: Cron 23h30 pour ingestion veille (timing off-peak)
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-07'
---

**Timing** : cron 23h30 (probablement heure locale Guadeloupe UTC-4).

**Rationale** : éviter pic d'utilisation, réduire latence YouTube API, optimiser bande passante VPS partagée (n8n, PMS, vault en service). Ingestion offline se termine avant réveil journalier (notification 8h ou email matin).

**Lieu** : cron root ou systemd timer (à confirmer implémentation).

**Moins critique que Couche 1 logic**, mais important pour ops : si changement horaire futur, éditer crontab/systemd sans toucher Python.

## Related

- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[2026-05-08-automatiser-envoi-digest-via-email-avec-date]] — Automatiser envoi digest via email avec date
- [[Decision-Disable-WP-Cron-cron-Linux]] — Decision Disable WP Cron cron Linux
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia
- [[Vault-Setup]] — Vault Setup
- [[2026-05-10-config-cron-jobs-pour-curator-et-synthesizer]] — Config : Cron jobs pour curator et synthesizer