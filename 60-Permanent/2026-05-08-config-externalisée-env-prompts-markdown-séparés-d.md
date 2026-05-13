---
ai_writable: false
area: null
backlinks:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-10-questionsprompts-externalisées-par-jeu
- 2026-05-12-approche-défensive-pour-cutover-jt-migrate
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- .env
- prompts/digest.md
- templates/digest.html.j2
id: 20260508100040-config-externalisée-env-prompts-markdown-séparés-d
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-10-questionsprompts-externalisées-par-jeu
- 2026-05-12-refactor-env-loader-veille-ia
- Workflow-API-Integrations
- impeccable
- n8n-Reference
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-0844-session-e172a5dd.md
source_session: e172a5dd-5040-43b5-8a0e-4fec08f8f037
status: active
summary: 'Séparation complète : env vars en `.env`, prompts AI en markdown, templates
  HTML en Jinja2 — tous hors code source.'
tags:
- permanent
- synthesized
- configuration
- separation-of-concerns
- templates
- versionability
tier: warm
title: 'Config externalisée : .env + prompts markdown séparés du code'
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-08'
---

Pattern configuration robuste : **1) `.env`** : variables sensibles (API keys masquées), chemins, flags runtime. **2) `config/prompts/digest.md`** : prompt Haiku pour digest generation (modifiable sans rebuild, audit trail git). **3) `templates/digest.html.j2`** : rendu final (flexibilité design indépendante de logic). Bénéfices : 1) Modifs config/prompts sans redéploiement code. 2) Secrets sécurisés (masqués en logs). 3) Historique git traceable (qui a changé quoi/quand/pourquoi). 4) Tests/AB : deux versions prompts en deux fichiers, basculer via flag .env. Applicable à tout pipeline multi-étape avec orchestration IA.

## Related

- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend]] — Pipeline veille-ia-youtube : ingest→analyze→render→send
- [[Workflow-API-Integrations]] — Workflow API Integrations
- [[impeccable]] — impeccable
- [[n8n-Reference]] — n8n self-hosted — URLs, paths, credentials, commandes
- [[2026-05-10-questionsprompts-externalisées-par-jeu]] — Questions/prompts externalisées par jeu
- [[2026-05-12-refactor-env-loader-veille-ia]] — 2026-05-12-refactor-env-loader-veille-ia