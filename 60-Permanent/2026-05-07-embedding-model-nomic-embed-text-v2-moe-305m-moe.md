---
ai_writable: false
area: null
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- nomic-v2-moe
- embedding
- Ollama
id: 20260507132132-embedding-model-nomic-embed-text-v2-moe-305m-moe
intent: pattern
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
summary: 'Remplace bge-m3 : MoE 305M params actifs, multilingue, 768-dim, ~700 MB
  réel'
tags:
- permanent
- synthesized
- rag
- vault-obsidian
- model-selection
tier: warm
title: 'Embedding model : nomic-embed-text-v2-moe (305M MoE)'
topic_cluster: vault-rag
type: permanent-note
updated: '2026-05-07'
---

Après OOM bge-m3, migration vers `nomic-embed-text-v2-moe`. **Caractéristiques** : - MoE (Mixture of Experts) : 305M params *actifs* seulement (vs dense large) - Multilingue natif (FR, EN, etc.) - 768 dimensions (indexable SQLite vec0) - Empreinte réelle : ~700 MB observé vs bge-m3 5.6 GB - Performance : MTEB benchmark au-dessus bge-m3 spécialement en French

**Usage** : `config.py` pointe `ollama:nomic-embed-text-v2-moe`, indexe 104 notes vault en 5m40s sans OOM. Déploiement : pull depuis Ollama registry, no special config needed.