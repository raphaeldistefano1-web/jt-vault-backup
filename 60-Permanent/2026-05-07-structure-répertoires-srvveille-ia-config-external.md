---
ai_writable: false
area: null
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- veille-ia
- filesystem
- config
id: 20260507132310-structure-répertoires-srvveille-ia-config-external
intent: pattern
last-accessed: '2026-05-07'
moc: null
project: null
related: []
source_notes:
- 10-Projects/claude-system/2026-05-07-1126-session-9416e8cf.md
- 10-Projects/claude-system/2026-05-07-1128-session-9416e8cf.md
source_session: 9416e8cf-0e57-49ee-8bcf-07142a66cca6
status: active
summary: Arborescence modulaire avec config externalisée JSON/YAML, candidates intermédiaires,
  digests finaux.
tags:
- permanent
- synthesized
- structure
- reusable
- config-externalization
tier: warm
title: Structure répertoires /srv/veille-ia (config externalisée)
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-07'
---

**Structure créée** :
```
/srv/veille-ia/
├── config/
│   ├── .env              (variables d'env)
│   ├── criteria.json     (filtres YouTube)
│   ├── topics.yaml       (thèmes, filtres)
│   └── prompts/          (prompts Sonnet/Haiku)
├── bin/
│   ├── ingest.py         (Couche 1 : YouTube API + filtrage)
│   ├── youtube_api.py    (wrapper YouTube)
│   └── curate.py         (Couche 2 : resummé via Claude)
├── candidates/           (20 vidéos sélectionnées)
├── digests/              (markdown finaux)
├── pdfs/                 (export PDF)
├── logs/
├── templates/            (Jinja2 pour PDF)
└── feedback/             (A/B tuning)
```

**Réutilisable** : Ce pattern (config externe + bin + outputs intermédiaires) s'applique à veille documents, podcasts, news feeds. Facilite versioning (git config/ + bin/) et iteration (candidates/ permet replay sans re-scrape).