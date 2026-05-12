---
ai_writable: false
area: null
backlinks:
- 2026-05-07-embedding-model-nomic-embed-text-v2-moe-305m-moe
- 2026-05-07-lesson-profiler-services-lourds-avant-scaling-prod
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
- 2026-05-08-nomic-embed-text-v2-moe-consommation-réelle-vs-ann
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- systemd
- swap
- MemoryMax
- /etc/systemd/system/ollama.service.d
id: 20260508040101-ollama-systemd-memorymax-guardrail-et-swap
intent: config
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
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
summary: Config systemd MemoryMax + swap prévient OOM-kill sans sacrifier perf RAG.
tags:
- permanent
- synthesized
- guardrail
- kernel-safety
- cgroup
- memory-accounting
tier: warm
title: Ollama systemd MemoryMax guardrail et swap
topic_cluster: vps-memory
type: permanent-note
updated: '2026-05-08'
---

Configuration appliquée après crash OOM. Créer `/etc/systemd/system/ollama.service.d/override.conf` :

```ini
[Service]
MemoryMax=2.5G
MemoryAccounting=yes
```

Ajouter 4 GB swap :
```bash
fallocate -l 4G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
```

Redémarrer systemd : `systemctl daemon-reload && systemctl restart ollama`.

**Effet** : Ollama plafonné 2.5 GB, système page sans OOM-kill. Démarrage manuel via CLI au lieu auto-start (contrôle charge). Cela maintient mémoire libre pour Postgres (1-2 GB), RAG (1-2 GB), cache disque (~1-2 GB). Stable 6+ mois.

## Related

- [[2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite]] — Ollama bge-m3 consomme 5.6 GB sans limite