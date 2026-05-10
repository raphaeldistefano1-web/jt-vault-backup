---
ai_writable: false
area: null
backlinks:
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-08-ollama-systemd-memorymax-guardrail-et-swap
- _VAULT-INDEX
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- Ollama
- bge-m3
- systemd
id: 20260507132132-ollama-bge-m3-consomme-56-gb-sans-limite
intent: gotcha
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-08-ollama-systemd-memorymax-guardrail-et-swap
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
- Bug-PharData-RAM-OOM
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1254-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1240-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1215-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1257-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1225-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: bge-m3 annonce ~700 MB mais consomme 5.6 GB virtual → OOM-kill cascade
tags:
- permanent
- synthesized
- oom
- memory-leak
- vps-crash
tier: warm
title: Ollama bge-m3 consomme 5.6 GB sans limite
topic_cluster: vps-memory
type: permanent-note
updated: '2026-05-07'
---

Ollama avec `bge-m3` a déclenché un OOM-kill et reboot watchdog. **Annoncé** : ~700 MB. **Observé** : 5.6 GB virtual memory, 1.4 GB RSS. Sans swap ni limite systemd, le kernel a tué Ollama + tout le reste. **Piège détecté** : ne PAS supposer qu'un modèle "700 MB" sera limité à ça en practice — overhead Ollama, allocation context, padding inférence, caching intermédiaires gonflent la conso réelle. **Symptôme clé** : loop `POST /api/embed` sans fin, puis kernel freeze, puis reboot watchdog.

## Related

- [[2026-05-08-ollama-systemd-memorymax-guardrail-et-swap]] — Ollama systemd MemoryMax guardrail et swap
- [[2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd]] — Ollama démarrage manuel, pas auto-start systemd
- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod
- [[2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe]] — Embedding model : nomic-embed-text-v2-moe (305M MoE)
- [[Bug-PharData-RAM-OOM]] — Bug PharData RAM OOM