---
ai_writable: false
area: null
backlinks:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-10-decision-defensive-truncation-et-sync-check-vault-
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- cron
- curator
- synthesizer
- /etc/cron.d
- logrotate
id: 20260508040102-vault-rag-curator-synthesizer-crons-schedule
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-08-syncthing-p2p-vault-sync-tailscale-only
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- 2026-05-10-decision-defensive-truncation-et-sync-check-vault-
- 2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
- RUNBOOK-disaster-recovery
- Vault-Setup
schema_version: 1
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1325-session-158ff0de.md
- 10-Projects/openclaw-plugin/2026-05-07-1340-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1433-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1532-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1446-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1520-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1437-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1307-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1513-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1551-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1655-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1549-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1517-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1420-session-158ff0de.md
- 10-Projects/pms-jardin-tropical/2026-05-07-1459-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: Crons curator 3h + synthesizer 4h + warmup + backup, logs rotatés daily.
tags:
- permanent
- synthesized
- automation
- scheduling
- maintenance
- background-jobs
tier: warm
title: vault-rag curator synthesizer crons schedule
topic_cluster: vault-rag
type: permanent-note
updated: '2026-05-08'
---

Pipeline vault-rag asynchrone avec crons `/etc/cron.d/` :

- **vault-curator** : toutes les 3h (import notes, embeddings, nettoyage orphelins) → logs logrotate
- **vault-synthesizer** : toutes les 4h (RAG summaries, MOC refresh) → logs logrotate
- **vault-warmup** : amorce VPS + après reboot (pré-charge embeddings mémoire Ollama)
- **vault-backup-github** : daily minuit (git push vault vers backup repo)

Chaque cron a entrée logrotate (daily, rotate 7, compress). Erreurs catchées via exit code → alerting optionnel mail.

**Bénéfice** : vault toujours à jour sans charge synchrone requête utilisateur. **À monitorer** : curator peut timeout si 100+ notes nouvelles — ajouter `--batch-size 50` si besoin.

## Related

- [[2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak]] — Cron 23h30 pour ingestion veille (timing off-peak)
- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault
- [[Vault-Setup]] — Vault Setup
- [[2026-05-08-syncthing-p2p-vault-sync-tailscale-only]] — Syncthing P2P vault sync Tailscale-only
- [[2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau]] — Audit one-shot — déduplication 39 mémoires CC vs vault
- [[2026-05-10-decision-defensive-truncation-et-sync-check-vault-]] — Decision : Defensive truncation et sync-check vault RAG
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-10-config-cron-jobs-pour-curator-et-synthesizer]] — Config : Cron jobs pour curator et synthesizer
- [[2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault]] — Pattern : Scripts maintenance et diagnostic vault
- [[2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag]] — Gotcha : Fichiers temporaires indexés par RAG