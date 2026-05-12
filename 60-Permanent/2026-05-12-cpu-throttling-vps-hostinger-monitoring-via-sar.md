---
ai_writable: false
area: null
backlinks:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- VPS-Hostinger
- Whisper-VPS-Reference
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- VPS Hostinger
- sar
- performance
- '%steal'
id: 20260512040050-cpu-throttling-vps-hostinger-monitoring-via-sar
intent: lesson
last-accessed: '2026-05-12'
moc: null
project: null
related:
- Whisper-VPS-Reference
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- VPS-Hostinger
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
summary: Surveiller %steal (vol CPU) via `sar -u` pour détecter throttling Hostinger
  précocement.
tags:
- permanent
- synthesized
- cpu-throttling
- monitoring
- hostinger
tier: warm
title: CPU throttling VPS Hostinger — monitoring via sar
topic_cluster: vps-monitoring
type: permanent-note
updated: '2026-05-12'
---

**Observation** : Hostinger applique throttle très agressif (réduction CPU) dès que moyenne CPU dépasse 85% pendant >3h. Le signal clé est **%steal** dans `sar -u 1 10` (vol CPU = temps demandé par OS mais pas donné par hyperviseur).

**Détection** : `sar -u 1 10 | tail` → si %steal > 10-15%, c'est du throttling en action. Avant OOM/freeze, augmentation de %steal annonce restriction imminente.

**Réflexe opérationnel** : Si VPS rame (load élévée, services lents) → lancer `sar -u 1 10` avant d'ajouter ressources. Si %steal haut → c'est throttle Hostinger, pas manque RAM. Réponse : arrêter services non-essentiels, pas scaler horizontalement (impossible chez Hostinger).

**Tools** : `sysstat` package. Cron `sar -o /var/log/sa/sa$(date +%d)` toutes les 10 min pour historique (visualisation post-incident).

## Related

- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[VPS-Hostinger]] — VPS Hostinger