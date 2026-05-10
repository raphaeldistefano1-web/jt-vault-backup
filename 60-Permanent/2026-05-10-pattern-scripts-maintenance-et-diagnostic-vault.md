---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- RUNBOOK-disaster-recovery
- _VAULT-INDEX
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- vault-obsidian
- vault-rag
- curator
- synthesizer
id: 20260510040217-pattern-scripts-maintenance-et-diagnostic-vault
intent: pattern
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- _Index
- _Index
- _VAULT-INDEX
- 2026-05-08-vault-para-multi-projets-chemin-canonique
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-09-0856-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0841-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0825-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0835-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0855-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0809-session-7ba133d2.md
- 10-Projects/pms-jardin-tropical/2026-05-09-0822-session-7ba133d2.md
source_session: 7ba133d2-b9f1-4723-9e12-61b69f771a1b
status: active
summary: Suite d'outils CLI pour maintenir et diagnostiquer la santé de la vault RAG.
tags:
- permanent
- synthesized
- maintenance
- automation
- scripting
- RAG
tier: warm
title: 'Pattern : Scripts maintenance et diagnostic vault'
topic_cluster: vault-obsidian-infrastructure
type: permanent-note
updated: '2026-05-10'
---

Créés durant la refonte vault mai 2026 :

- **`/opt/vault-rag/bin/vault-build-index`** : (re)construction de l'index RAG depuis zéro
- **`/opt/vault-rag/bin/vault-rag-curator`** : cron job qui traite l'inbox et peuple les embeddings; run ~3h
- **`/opt/vault-rag/bin/vault-synthesizer`** : génère les notes synthétiques cross-références; run ~4h  
- **`/opt/vault-rag/bin/vault-rag-backfill-incoming`** : indexation batch de l'inbox
- **`/opt/vault-rag/bin/vault-rag-backlinks`** : peuplage des wikilinks
- **`/usr/local/bin/vault-doctor`** : diagnostic CLI de la santé (DB integrity, embeddings, logs)
- **`/usr/local/bin/vault-link-jobs`** : wrapper de gestion des jobs cron

Chaque script est idempotent. Les logs se trouvent dans `/var/log/vault-{curator,synthesizer}.log`. À consulter avant d'exécuter des commandes de rebuild manuel.

## Related

- [[2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs]] — Vault synthesizer — synthèse auto des session-logs
- [[_Index]] — Index — claude-system
- [[_Index]] — Index — openclaw-plugin
- [[_VAULT-INDEX]] — Vault Index — point d'entrée racine
- [[2026-05-08-vault-para-multi-projets-chemin-canonique]] — Vault PARA multi-projets chemin canonique