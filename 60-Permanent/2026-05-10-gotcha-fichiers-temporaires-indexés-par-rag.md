---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
- RUNBOOK-disaster-recovery
- _VAULT-INDEX
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- vault-obsidian
- RAG
- file-indexing
id: 20260510040225-gotcha-fichiers-temporaires-indexés-par-rag
intent: gotcha
last-accessed: '2026-05-10'
moc: null
project: null
related:
- _VAULT-INDEX
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
- RUNBOOK-disaster-recovery
- _Index
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
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
summary: Dossiers temporaires (.stversions, .obsidian) peuvent être indexés si non-filtrés,
  bruitant les requêtes.
tags:
- permanent
- synthesized
- indexing
- troubleshooting
- maintenance
tier: warm
title: 'Gotcha : Fichiers temporaires indexés par RAG'
topic_cluster: vault-obsidian-infrastructure
type: permanent-note
updated: '2026-05-10'
---

Au cours de la maintenance vault 2026-05-09, la base RAG indexait involontairement `.stversions/AGENTS.md` et autres artifacts temporaires.

**Symptôme** : requêtes RAG bruitées par du contenu non-sémantique, doublets indexés.

**Cause** : le curator ne filtrait pas les chemins systèmes.

**Fix** :
- Ajouter un `.gitignore`-like dans `/opt/vault-rag/lib/config.py` pour exclure `.stversions`, `.obsidian`, `.trash`, etc.
- Rebuilder l'index via `vault-build-index` après correction
- Vérifier via `vault-doctor` que stats contiennent uniquement notes intentionnelles

Cette classe de bug est récurrente avec les RAG : whitelist explicitement les dossiers d'indexation plutôt que blacklist.

## Related

- [[_VAULT-INDEX]] — Vault Index — point d'entrée racine
- [[2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d]] — Bug : synthesizer omet la section Signaux feedback détectés
- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault
- [[_Index]] — Index — montage-video
- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)