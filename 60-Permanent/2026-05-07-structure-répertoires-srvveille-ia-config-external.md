---
ai_writable: false
area: null
backlinks:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
- 2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest
- 2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin
- 2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag
- 2026-05-10-questionsprompts-externalisées-par-jeu
- _VAULT-INDEX
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
related:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-08-config-externalisée-env-prompts-markdown-séparés-d
- 2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest
- 2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin
- 2026-05-10-questionsprompts-externalisées-par-jeu
- 2026-05-12-refactor-env-loader-veille-ia
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

## Related

- [[2026-05-08-config-externalisée-env-prompts-markdown-séparés-d]] — Config externalisée : .env + prompts markdown séparés du code
- [[2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin]] — Team interne + task-list pour paralléliser multi-findings
- [[2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest]] — Pipeline modulaire ingest→analyze→render→digest
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia
- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-10-questionsprompts-externalisées-par-jeu]] — Questions/prompts externalisées par jeu
- [[2026-05-12-refactor-env-loader-veille-ia]] — 2026-05-12-refactor-env-loader-veille-ia