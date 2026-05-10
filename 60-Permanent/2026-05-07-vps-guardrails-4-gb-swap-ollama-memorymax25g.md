---
ai_writable: false
area: null
backlinks:
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
- _VAULT-INDEX
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- swap
- systemd
- Ollama
- MemoryMax
id: 20260507132132-vps-guardrails-4-gb-swap-ollama-memorymax25g
intent: decision
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd
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
summary: Ajout swap 4 GB + limite Ollama via systemd override (MemoryMax=2.5G)
tags:
- permanent
- synthesized
- guardrail
- memory-management
- vps-stability
tier: warm
title: 'VPS guardrails : 4 GB swap + Ollama MemoryMax=2.5G'
topic_cluster: vps-memory
type: permanent-note
updated: '2026-05-07'
---

Après OOM bge-m3, deux guardrails déployés : 1. **4 GB swap** : buffer qui délaye OOM-kill brutal, laisse place à degradation graceful. 2. **systemd override** (`/etc/systemd/system/ollama.service.d/override.conf`) : `MemoryMax=2.5G`, `MemoryHigh=2.0G` — limite stricte même si le modèle veut plus. **Rationale** : on sait maintenant que bge-m3 veut 5.6 GB ; on force un plafond. Si modèle nécessite plus, fallback sur modèle plus léger (ex: nomic-v2-moe) ou upgrade RAM VPS. Sans ces limites, tout service lourd futur aura même risque de crash.

## Related

- [[2026-05-07-ollama-démarrage-manuel-pas-auto-start-systemd]] — Ollama démarrage manuel, pas auto-start systemd
- [[2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann]] — nomic-embed-text-v2-moe consommation réelle vs annoncée
- [[2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe]] — Embedding model : nomic-embed-text-v2-moe (305M MoE)