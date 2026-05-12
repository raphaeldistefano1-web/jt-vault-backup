---
ai_writable: false
area: null
backlinks:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- Docker
- WordPress instances
- ollama
- chrome-headless
- syncthing
id: 20260512040046-services-pausable-durgence-docker-systemd-inventor
intent: config
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
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
summary: Liste des containers/services pouvant être arrêtés en cas d'urgence CPU.
tags:
- permanent
- synthesized
- cpu-intensive
- pausable-safely
- vps-operations
tier: warm
title: Services pausable d'urgence — Docker + systemd inventory
topic_cluster: vps-services-inventory
type: permanent-note
updated: '2026-05-12'
---

**Docker containers (WordPress instances)** :
- `jt-wp-a`, `jt-wp-b`, `jt-wp-c`, `jt-wp-d`, `jt-wp-e` (+ suffixes `-cli`, `-redis`, `-db`)
- Arrêt sûr via `docker stop` (0 data loss, redémarrage propre après)
- Impact : sites non-accessibles temporairement mais data intact

**Systemd services** :
- `chrome-headless.service` (Whisper transcription, ~15% CPU sous charge)
- `ollama.service` (modèles LLM locaux, jusqu'à 100% CPU)
- `syncthing@root.service` (sync vault, transfert I/O lourd)

**Stratégie d'arrêt** : En escalade → Chrome → Syncthing → Ollama → WordPress. Commande rapide : `systemctl stop chrome-headless.service ollama.service syncthing@root.service && docker stop jt-wp-*.`

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g]] — systemd override.conf pour Ollama : MemoryMax=2.5G
- [[2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd]] — Ollama démarrage manuel, pas auto-start systemd
- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod