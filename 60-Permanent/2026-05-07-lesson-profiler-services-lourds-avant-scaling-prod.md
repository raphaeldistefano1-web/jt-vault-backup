---
ai_writable: false
area: null
backlinks:
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar
- 2026-05-12-services-pausable-durgence-docker-systemd-inventor
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- profiling
- memory
- deployment
id: 20260507132132-lesson-profiler-services-lourds-avant-scaling-prod
intent: lesson
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
- 2026-05-08-ollama-systemd-memorymax-guardrail-et-swap
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-12-auto-arrêt-à-80-cpu-notification-email
- 2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar
- 2026-05-12-services-pausable-durgence-docker-systemd-inventor
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1254-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1240-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1215-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1257-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1225-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: Annonces RAM ≠ réalité sous charge. Toujours profiler workload complet isolé
tags:
- permanent
- synthesized
- methodology
- devops
- vps-operations
tier: warm
title: 'Lesson : profiler services lourds avant scaling prod'
topic_cluster: vps-operations
type: permanent-note
updated: '2026-05-07'
---

Documentations donnent chiffres optimistes ("700 MB") qui ignores : overhead runtime (Ollama), allocation GPU/CPU context, padding inférence, caching intermédiaires, concurrent requests. **Protocole avant scaling** : 1. Isoler service sur machine test 2. Charger workload *complète* (104+ notes vault = 100+ embeddings) 3. Observer `top`, `free -h`, `ps aux` pendant 5+ min sous charge réelle 4. Ajouter 50% marge sécurité 5. Configurer systemd limits (MemoryMax) AVANT prod

**Monitoring continu en prod** : swap usage, OOM-kill counts (`journalctl -b | grep OOM`), systemd kill signals (`memory cgroup.events`).

## Related

- [[2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite]] — Ollama bge-m3 consomme 5.6 GB sans limite
- [[2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd]] — Ollama démarrage manuel, pas auto-start systemd
- [[2026-05-08-ollama-systemd-memorymax-guardrail-et-swap]] — Ollama systemd MemoryMax guardrail et swap
- [[2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann]] — nomic-embed-text-v2-moe consommation réelle vs annoncée
- [[2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g]] — systemd override.conf pour Ollama : MemoryMax=2.5G
- [[2026-05-10-analyse-métier-valider-source-de-données-réelle]] — Analyse métier — valider source de données réelle
- [[2026-05-12-auto-arrêt-à-80-cpu-notification-email]] — Auto-arrêt à 80% CPU + notification email
- [[2026-05-12-services-pausable-durgence-docker-systemd-inventor]] — Services pausable d'urgence — Docker + systemd inventory
- [[2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar]] — CPU throttling VPS Hostinger — monitoring via sar
- [[2026-05-12-vérification-pre-cutover-systématique-perf-et-diff]] — Vérification pre-cutover systématique : perf et différences