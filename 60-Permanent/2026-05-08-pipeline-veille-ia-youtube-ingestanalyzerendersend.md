---
ai_writable: false
area: null
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- veille-ia-youtube
- ingest.py
- analyze.py
- render.py
- email_send.py
id: 20260508100039-pipeline-veille-ia-youtube-ingestanalyzerendersend
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-0844-session-e172a5dd.md
source_session: e172a5dd-5040-43b5-8a0e-4fec08f8f037
status: active
summary: 'Système 4-étapes pour analyse YouTube : ingest transcripts → AI selection/summarization
  → markdown render → email distribution.'
tags:
- permanent
- synthesized
- pipeline
- architecture
- multi-stage
- automation
- config-driven
tier: warm
title: 'Pipeline veille-ia-youtube : ingest→analyze→render→send'
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-08'
---

Architecture pipeline complète et réutilisable : **1) Ingest** : `ingest.py` télécharge transcripts YouTube bruts → `/srv/veille-ia/candidates/`. **2) Analyze** : `analyze.py` sélectionne 20 finalistes via Sonnet, génère résumés via Haiku, clustering thématique. **3) Render** : `render.py` convertit markdown → HTML via template Jinja2 (`digest.html.j2`). **4) Send+Cleanup** : `email_send.py --date YYYYMMDD` distribue digest, `cleanup.sh` nettoie temporaires. Config externalisée : `.env` pour variables, `/srv/veille-ia/config/prompts/digest.md` pour prompt Haiku (versionnable). Digests stockés en `/srv/veille-ia/digests/YYYY-MM-DD.md`.