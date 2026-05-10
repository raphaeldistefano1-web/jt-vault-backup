---
ai_writable: false
area: null
backlinks:
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- nomic-embed-text-v2-moe
- Smart Connections
- Ollama
- embedding-model
id: 20260508040100-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
intent: gotcha
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g
- 2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-08-ollama-systemd-memorymax-guardrail-et-swap
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
summary: Modèle MoE annoncé 700 MB, consomme 1.4 GB RSS + surcharges Ollama + boucles
  non-contrôlées.
tags:
- permanent
- synthesized
- memory-overhead
- moe-architecture
- model-selection
tier: warm
title: nomic-embed-text-v2-moe consommation réelle vs annoncée
topic_cluster: vault-embeddings
type: permanent-note
updated: '2026-05-08'
---

Le modèle `nomic-embed-text-v2-moe` (305M params actifs, MoE multilingue) choisi pour recherche sémantique Smart Connections + Ollama. **Annoncé ~700 MB RAM** en doc Nomic, **réalité : 1.4 GB RSS + surcharges Ollama + boucles POST `/api/embed` non-contrôlées = 5.6 GB virtual total**.

**Leçon durable** : tester sur production réelle (104 notes + queries chaudes), pas juste théorie. **Si RAM limitée** (<4 GB), réduire à :
- `nomic-embed-text-v2` (non-MoE, 256M params, ~900 MB)
- `all-minilm-l6-v2` (35M params, ~100 MB)

Suivre `journalctl -u ollama -f` pendant indexation pour détecter boucles infinies.

## Related

- [[2026-05-07-vps-guardrails-4-gb-swap-ollama-memorymax25g]] — VPS guardrails : 4 GB swap + Ollama MemoryMax=2.5G
- [[2026-05-07-systemd-overrideconf-pour-ollama-memorymax25g]] — systemd override.conf pour Ollama : MemoryMax=2.5G
- [[2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod]] — Lesson : profiler services lourds avant scaling prod
- [[2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd]] — Ollama démarrage manuel, pas auto-start systemd
- [[2026-05-08-ollama-systemd-memorymax-guardrail-et-swap]] — Ollama systemd MemoryMax guardrail et swap