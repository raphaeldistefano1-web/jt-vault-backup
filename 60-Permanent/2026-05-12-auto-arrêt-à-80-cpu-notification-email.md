---
ai_writable: false
applies_to: global
area: null
auto_applied_at: 2026-05-12
backlinks:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- _VAULT-INDEX
confidence: medium
created: '2026-05-12'
created_by: vault-synthesizer
embed_hash: null
embed_model_version: null
entities:
- VPS
- monitoring
- automation
feedback_level: HIGH
id: 20260512040048-auto-arrêt-à-80-cpu-notification-email
intent: feedback-rule
last-accessed: '2026-05-12'
last_used: null
moc: null
pinned: false
project: null
proposed_rule: Tout VPS en production doit avoir un watchdog CPU qui arrête services
  préemptivement à 80% et envoie email rapport.
related:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-12-monitor-launchd-veille-ia
- Whisper-VPS-Reference
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
status: auto-applied
summary: Déployer watchdog qui arrête services à 80% CPU et envoie email rapport.
tags:
- permanent
- synthesized
- feedback
- pending-review
- cpu-throttling
- emergency-automation
tier: warm
title: Auto-arrêt à 80% CPU + notification email
topic_cluster: vps-operations
type: permanent-note
updated: '2026-05-12'
usage_count: 0
---

**Signal détecté** : User demande explicitement « quand CPU atteint 80%, arrête ou met en pause toutes les applications + mail rapport ».

**Rationale** : VPS Hostinger throttle agressif au-delà de 85% CPU pendant >3h. Sans watchdog, risque OOM/freeze qui paralysent l'infra entière. Arrêt préventif à 80% + notification donne 5% de buffer avant throttle, évite catastrophe.

**Implémentation** : Watchdog systemd (voir note « Watchdog CPU pattern ») maintenant en place. À valider : fréquence polling, liste services, adresse mail destinataire, format rapport.

**Permanent** : Cette règle s'applique à tout déploiement futur VPS (pattern réutilisable multi-projets).

## Related

- [[2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak]] — Cron 23h30 pour ingestion veille (timing off-peak)
- [[2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g]] — systemd override.conf pour Ollama : MemoryMax=2.5G
- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[2026-05-12-monitor-launchd-veille-ia]] — 2026-05-12-monitor-launchd-veille-ia