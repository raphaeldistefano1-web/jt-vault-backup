---
ai_writable: false
area: null
backlinks:
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
- 2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- Ollama
- systemd
- startup-policy
id: 20260507132132-ollama-démarrage-manuel-pas-auto-start-systemd
intent: decision
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
- 2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1254-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1240-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1215-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1257-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1225-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: Ollama ne démarre plus au boot — démarrage manuel `systemctl start ollama`
tags:
- permanent
- synthesized
- memory-management
- vps-ops
tier: warm
title: Ollama démarrage manuel, pas auto-start systemd
topic_cluster: vps-services
type: permanent-note
updated: '2026-05-07'
---

Ollama est lourd (2.5G+ RAM sous limite). Configuré sans auto-start au boot (`Type=simple`, pas `WantedBy=multi-user.target`). **Rationale** : c'est une ressource qu'on contrôle manuellement. Réduit surface d'OOM-cascade si d'autres services montent en charge. **Usage** : `systemctl start ollama` quand indexation Obsidian nécessaire. Peut rester arrêté en periods basse-charge. Applique philosophie "services lourds = démarrage explicite".

## Related

- [[2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite]] — Ollama bge-m3 consomme 5.6 GB sans limite
- [[2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g]] — VPS guardrails : 4 GB swap + Ollama MemoryMax=2.5G
- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod
- [[2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann]] — nomic-embed-text-v2-moe consommation réelle vs annoncée
- [[2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe]] — Embedding model : nomic-embed-text-v2-moe (305M MoE)