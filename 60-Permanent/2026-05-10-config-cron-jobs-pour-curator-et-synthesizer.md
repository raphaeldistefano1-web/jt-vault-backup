---
ai_writable: false
area: null
backlinks:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- RUNBOOK-disaster-recovery
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- vault-obsidian
- cron
- systemd
id: 20260510040222-config-cron-jobs-pour-curator-et-synthesizer
intent: config
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-12-watchdog-cpu-durgence-pattern-systemd
- RUNBOOK-disaster-recovery
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-09-0856-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0841-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0825-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0835-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0855-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0809-session-7ba133d2.md
- 10-Projects/pms-jardin-tropical/2026-05-09-0822-session-7ba133d2.md
source_session: 7ba133d2-b9f1-4723-9e12-61b69f771a1b
status: active
summary: Configuration des jobs périodiques qui maintiennent la base RAG et les synthèses
  vault.
tags:
- permanent
- synthesized
- automation
- scheduling
- maintenance
tier: warm
title: 'Config : Cron jobs pour curator et synthesizer'
topic_cluster: vault-obsidian-infrastructure
type: permanent-note
updated: '2026-05-10'
---

Les jobs cron sont lancés via `/etc/cron.d/vault-curator` et `/etc/cron.d/vault-synthesizer` (scope système, pas user crontab).

**Curator** (~3h de fréquence) :
- Lit `/srv/vault/00-Inbox/` pour les notes neuves
- Génère embeddings via nomic-v2-moe (via ollama loopback)
- Peuple la DB SQLite+vec0 avec notes et métadonnées
- Logs : `/var/log/vault-curator.log`

**Synthesizer** (~4h de fréquence) :
- Génère synthèses cross-field et liens transverses
- Utilise Claude Haiku via `claude-cli` (nécessite auth local)
- Logs : `/var/log/vault-synthesizer.log`

Vérifier l'état : `ps aux | grep -E "curator|synthesizer|ollama"`. Logs cruciaux pour diagnostiquer blocages ou OOM sous charge.

## Related

- [[2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak]] — Cron 23h30 pour ingestion veille (timing off-peak)
- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault
- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[2026-05-12-watchdog-cpu-durgence-pattern-systemd]] — Watchdog CPU d'urgence — pattern systemd