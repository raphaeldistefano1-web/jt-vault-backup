---
ai_writable: false
area: null
backlinks:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- CANONICITY
- RUNBOOK-disaster-recovery
- _VAULT-INDEX
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- vault-obsidian
- RAG
- token-limits
id: 20260510040227-decision-defensive-truncation-et-sync-check-vault-
intent: decision
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- CANONICITY
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- RUNBOOK-disaster-recovery
- note-schema
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
summary: 'ADR 0001 : truncation défensive des embeddings et vérification intégrité
  DB post-curation.'
tags:
- permanent
- synthesized
- architecture
- safety
- embeddings
tier: hot
title: 'Decision : Defensive truncation et sync-check vault RAG'
topic_cluster: vault-obsidian-architecture
type: permanent-note
updated: '2026-05-10'
---

Créé `/opt/vault-rag/docs/adr/0001-defensive-truncation-and-doctor-sync-check.md`.

**Décision** : le curator applique truncation défensive quand note dépasse ~8K tokens (seuil nomic-v2-moe). Chunks dépassants sont splittés et indexés séparément.

**Rationale** : 
- Embeddings + synthèses nécessitent budgets tokens stricts
- Notes existantes peuvent atteindre ~50K tokens → crash embedder si non gérés
- Truncation + chunking = stabilité sous charge

**Monitoring** : `vault-doctor` vérifie post-curator que :
- DB contient bien N notes attendues
- `embeddings.count == notes.count`
- Aucun orphelin en DB
- Aucun fichier `/srv/vault` sans correspondant DB

Cette approche a évité plusieurs OOM durant charge tests mai 2026.

## Related

- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC
- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault
- [[note-schema]] — note schema