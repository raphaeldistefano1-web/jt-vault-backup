---
ai_writable: false
area: null
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
related: []
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