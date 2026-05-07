---
ai_writable: false
area: null
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
related: []
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