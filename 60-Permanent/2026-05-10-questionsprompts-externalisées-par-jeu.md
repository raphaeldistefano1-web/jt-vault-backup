---
ai_writable: false
area: null
backlinks:
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-08-config-externalisée-env-prompts-markdown-séparés-d
- 2026-05-08-paralléliser-tâches-complexes-via-teams-sessions-i
- 2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- data/questions/picolo.ts
- data/questions/paranoia.ts
id: 20260510040513-questionsprompts-externalisées-par-jeu
intent: pattern
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-08-config-externalisée-env-prompts-markdown-séparés-d
- note-schema
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-0114-session-19e3ce30.md
source_session: 19e3ce30-2ef0-48d6-ac76-36da992b94fe
status: active
summary: Chaque jeu a son fichier `/data/questions/*.ts` (picolo.ts, paranoia.ts,
  etc.) pour isoler contenu de logique.
tags:
- permanent
- synthesized
- content-structure
- separation-of-concerns
- maintainability
tier: warm
title: Questions/prompts externalisées par jeu
topic_cluster: culsec-data
type: permanent-note
updated: '2026-05-10'
---

**Structure** : `/var/www/culsec/data/questions/` contient 1 fichier TS par jeu ou par catégorie. Ex : picolo.ts exporte array de prompts typées.

**Avantages** : 
- Facile ajouter/éditer contenu sans toucher composants
- Contenu séparé de logique de rendu
- Réutilisation facile entre variantes

**Pattern** : exporter const array + type Question pour type-safety.

## Related

- [[2026-05-08-config-externalisée-env-prompts-markdown-séparés-d]] — Config externalisée : .env + prompts markdown séparés du code
- [[note-schema]] — note schema
- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)
- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté