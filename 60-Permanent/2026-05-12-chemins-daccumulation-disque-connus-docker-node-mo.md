---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- Stack-Tech
- VPS-Hostinger
- Whisper-VPS-Reference
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- VPS
- Docker
- node_modules
- logs
id: 20260512040451-chemins-daccumulation-disque-connus-docker-node-mo
intent: config
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- Whisper-VPS-Reference
- VPS-Hostinger
- Stack-Tech
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-2118-session-8bb149e5.md
- 10-Projects/jt-migrate/2026-05-11-2122-session-8bb149e5.md
- 10-Projects/pms-jardin-tropical/2026-05-11-2109-session-8bb149e5.md
- 10-Projects/pms-jardin-tropical/2026-05-11-2059-session-8bb149e5.md
source_session: 8bb149e5-9777-4d3a-88e6-d87fb5848961
status: active
summary: 'Top culprits d''accumulation sur VPS: images Docker dangling, node_modules
  récursifs, logs non rotatés, old node builds'
tags:
- permanent
- synthesized
- storage
- maintenance
tier: warm
title: 'Chemins d''accumulation disque connus: Docker, node_modules, logs'
topic_cluster: infrastructure-vps
type: permanent-note
updated: '2026-05-12'
---

Historiquement sur le VPS Hostinger, les giga s'accumulent dans:
- **/var/lib/docker**: images dangling + layers orphelines après builds (docker image prune, docker system prune)
- **/var/www**: node_modules récursifs sur projets Next/vite anciens (batcher avec pnpm store prune ou yarn cache clean)
- **/var/log**: logs non rotatés (journalctl --vacuum=30d, logrotate config)
- **/root/.npm, /root/.yarn**: package caches (npm cache clean --force)
- **/root/.nvm/versions**: old Node binaries (nvm uninstall)

Contrôle proactif: `du -sh /path/*` mensuellement vs attendu. Si saut >500MB inexpliqué, investigation immédiate.

## Related

- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[VPS-Hostinger]] — VPS Hostinger
- [[Stack-Tech]] — Stack Tech