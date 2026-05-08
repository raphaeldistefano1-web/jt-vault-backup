---
ai_writable: false
area: null
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- vault
- CANONICITY.md
- 60-Permanent
- mémoires-CC
- /root/.claude/projects
id: 20260508095955-décision-canonicitymd-pour-déduplication-vaultmémo
intent: decision
last-accessed: '2026-05-08'
moc: null
project: null
related: []
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
summary: Doc `/srv/vault/90-Meta/CANONICITY.md` établit règles de canonicité pour
  déduplicer 39 mémoires CC redondantes avec vault.
tags:
- permanent
- synthesized
- governance
- memory-dedup
- architecture-decision
tier: warm
title: Décision — CANONICITY.md pour déduplication vault↔mémoires CC
topic_cluster: vault-architecture
type: permanent-note
updated: '2026-05-08'
---

**Décision architecturale** : créer une doc de gouvernance `/srv/vault/90-Meta/CANONICITY.md` qui établit la source de vérité unique entre :
- Notes vault (`/srv/vault/60-Permanent/`) — source primaire pour insights durables
- Mémoires Claude Code (`/root/.claude/projects/*/memory/`) — legacy, partiellement redondantes

**Problème identifié** :
- 39 mémoires CC sont déjà représentées dans le vault (contenu dupliqué ou équivalent)
- Risque de divergence si une source est mise à jour unilatéralement
- Pas de règle unique d'arbitration

**Livrable attendu** :
1. Doc `CANONICITY.md` : définit la stratégie (vault primaire vs mirror bidirectionnel)
2. Script de sync (`vault-sync-memories` ?) : matérialise la règle en production
3. Audit one-shot : migration des 39 mémoires + archivage

**Implémentation possible** (à valider) :
- Option A : vault est source ; mémoires CC archivées/supprimées
- Option B : vault et CC synchronisés, vault reste primaire pour résolution de conflits