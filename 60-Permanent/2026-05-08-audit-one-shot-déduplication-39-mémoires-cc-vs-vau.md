---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- RUNBOOK-disaster-recovery
- note-schema
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- mémoires-CC
- vault
- 60-Permanent
id: 20260508095956-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
- 2026-05-10-decision-defensive-truncation-et-sync-check-vault-
- CANONICITY
- RUNBOOK-disaster-recovery
- note-schema
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-0903-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0950-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0942-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0920-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0935-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0901-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0921-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-0928-session-4d0a55cb.md
source_session: 4d0a55cb-ed1e-494e-9202-45857e2bd2b9
status: active
summary: Processus d'audit pour identifier et retirer 39 mémoires CC redondantes,
  migrer deltas vers vault.
tags:
- permanent
- synthesized
- audit
- dedup
- maintenance
- data-hygiene
tier: warm
title: Audit one-shot — déduplication 39 mémoires CC vs vault
topic_cluster: vault-maintenance
type: permanent-note
updated: '2026-05-08'
---

**Processus d'audit recommandé** :

1. **Inventorier** : extraire la liste complète des 39 mémoires CC suspects (filtre : contenu ≈ contenu vault)
2. **Analyser chaque paire** (CC-memo, vault-note) :
   - Comparer : intent, topic, entities, tier, body
   - Déterminer : laquelle est plus fraîche / plus compète
3. **Décider** pour chaque paire :
   - Vault > CC : archiver CC, créer wikilink CC→vault
   - CC > Vault : migrer delta dans vault, archiver CC
   - Divergent : merger manuellement (rare), puis archiver
4. **Tracer** : un commit git par mémoire archivée

**Sortie de l'audit** :
- Rapport JSON : 39 entrées (memo_path, vault_path, décision, ratio_similarité)
- Git history : commits atomiques, messages clairs
- Validation humaine : Raphaël approuve avant bulk-delete des mémoires CC

**Post-audit** :
- Mettre en place `vault-sync-memories` (script cron) pour éviter ré-divergence

## Related

- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo]] — Hiérarchie persistance : Mémoire vs Vault vs Todo
- [[note-schema]] — note schema
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault
- [[2026-05-10-decision-defensive-truncation-et-sync-check-vault-]] — Decision : Defensive truncation et sync-check vault RAG
- [[2026-05-10-analyse-métier-valider-source-de-données-réelle]] — Analyse métier — valider source de données réelle