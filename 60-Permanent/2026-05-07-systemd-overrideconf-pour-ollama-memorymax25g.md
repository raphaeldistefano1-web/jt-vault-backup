---
ai_writable: false
area: null
backlinks:
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
- _VAULT-INDEX
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- Ollama
- systemd
- override.conf
id: 20260507132132-systemd-overrideconf-pour-ollama-memorymax25g
intent: config
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
source_notes:
- 10-Projects/openclaw-plugin/2026-05-07-1254-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1240-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1215-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1257-session-158ff0de.md
- 10-Projects/claude-system/2026-05-07-1225-session-158ff0de.md
source_session: 158ff0de-03dd-41ec-927d-9cb29780c3d1
status: active
summary: 'Path: `/etc/systemd/system/ollama.service.d/override.conf` — MemoryMax=2.5G,
  MemoryHigh=2.0G'
tags:
- permanent
- synthesized
- memory-limit
- systemd-config
tier: warm
title: 'systemd override.conf pour Ollama : MemoryMax=2.5G'
topic_cluster: vps-services
type: permanent-note
updated: '2026-05-07'
---

**Chemin** : `/etc/systemd/system/ollama.service.d/override.conf`

```ini
[Service]
MemoryMax=2.5G
MemoryHigh=2.0G
```

**Application** : `systemctl daemon-reload && systemctl restart ollama`

Force systemd à terminer Ollama *gracefully* si RSS > 2.5G. `MemoryHigh=2.0G` déclenche reclaim agressif avant la limite hard. Nécessaire après incident bge-m3 OOM. Peut être ajusté si nouveau modèle nécessite plus, ou baissé si VPS monte en charge.

## Related

- [[2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann]] — nomic-embed-text-v2-moe consommation réelle vs annoncée