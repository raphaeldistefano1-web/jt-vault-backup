---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- vault
- note-schema
- metadata
id: 20260509040323-schéma-canonique-des-notes-du-vault-atomiques
intent: config
last-accessed: '2026-05-09'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1021-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-1034-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-1013-session-4d0a55cb.md
- 10-Projects/pms-jardin-tropical/2026-05-08-1007-session-4d0a55cb.md
source_session: 4d0a55cb-ed1e-494e-9202-45857e2bd2b9
status: active
summary: 'Notes `/srv/vault/60-Permanent/` suivent un schéma uniforme : title, intent
  (decision|gotcha|pattern|config|lesson), topic_cluster, tier (hot|warm|cold), entities,
  tags, summary, body.'
tags:
- permanent
- synthesized
- documentation
- knowledge-structure
tier: warm
title: Schéma canonique des notes du vault atomiques
topic_cluster: vault-schema
type: permanent-note
updated: '2026-05-09'
---

Le schéma canonique des notes atomiques du vault est formalisé dans `/srv/vault/90-Meta/schemas/note-schema.md`. Chaque note doit avoir :

- **title** (5-10 mots, très clair)
- **intent** (decision | gotcha | pattern | config | lesson)
- **topic_cluster** (slug court du domaine)
- **tier** (hot = urgent/réf quotidienne | warm = important long terme | cold = archive/historique)
- **entities** (noms de services/libs/projets mentionnés)
- **tags** (mots-clés transversaux)
- **summary** (phrase unique, 25 mots max)
- **body** (markdown 100-300 mots, atomique, evergreen, sans dépendre du contexte)

Pour les notes `intent: feedback-rule` uniquement :
- **feedback_level** (HIGH | MEDIUM | LOW)
- **applies_to** (global | project:<slug>)
- **proposed_rule** (phrase impérative prête à coller dans CLAUDE.md)

Documentalisé dans `/srv/vault/90-Meta/CANONICITY.md`.